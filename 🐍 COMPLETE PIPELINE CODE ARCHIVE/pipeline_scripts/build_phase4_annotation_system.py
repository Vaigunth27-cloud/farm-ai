import os
import sys
import json
import pandas as pd
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
master_images_csv = os.path.join(base_dir, "master_images.csv")
detections_csv = os.path.join(base_dir, "detections.csv")
yolo_dir = os.path.join(base_dir, "yolo_annotations")
labels_dir = os.path.join(yolo_dir, "labels")

os.makedirs(labels_dir, exist_ok=True)

# 12 Standardized Urban Infrastructure Classes for FarmwiseAI Task 5
CLASSES = [
    "building",           # 0
    "electric_pole",      # 1
    "streetlight",        # 2
    "commercial_sign",    # 3
    "traffic_signal",     # 4
    "road_sign",          # 5
    "transformer",        # 6
    "drain",              # 7
    "sidewalk",           # 8
    "waste_bin",          # 9
    "bus_stop",           # 10
    "other_urban_asset"   # 11
]

class_to_idx = {c: i for i, c in enumerate(CLASSES)}

# Export classes.txt
classes_file = os.path.join(yolo_dir, "classes.txt")
with open(classes_file, "w", encoding="utf-8") as f:
    for c in CLASSES:
        f.write(f"{c}\n")
print(f"Exported {len(CLASSES)} classes to {classes_file}")

# Load datasets
df_images = pd.read_csv(master_images_csv)
df_det = pd.read_csv(detections_csv)

print(f"Images: {len(df_images)}, Detections: {len(df_det)}")

# Generate YOLO .txt annotations for each image
annotations_by_image = {}
total_boxes = 0
invalid_boxes = 0

for idx, img_row in df_images.iterrows():
    img_id = img_row["Image_ID"]
    w_px = float(img_row["Width_px"])
    h_px = float(img_row["Height_px"])
    fname = img_row["File_Name"]
    # Base label filename without original extension
    base_name = os.path.splitext(fname)[0]
    txt_path = os.path.join(labels_dir, f"{img_id}.txt")
    
    # Filter detections for this image
    img_dets = df_det[df_det["Image_ID"] == img_id]
    
    yolo_lines = []
    ann_records = []
    
    for _, d in img_dets.iterrows():
        c_name = d["Class_Name"]
        if c_name not in class_to_idx:
            # Map alternative names
            if "pole" in c_name: c_name = "electric_pole"
            elif "light" in c_name: c_name = "streetlight"
            elif "sign" in c_name: c_name = "commercial_sign"
            elif "build" in c_name: c_name = "building"
            elif "signal" in c_name: c_name = "traffic_signal"
            elif "trans" in c_name: c_name = "transformer"
            else: c_name = "other_urban_asset"
            
        c_idx = class_to_idx.get(c_name, 11)
        
        x1 = float(d["BBox_X1"])
        y1 = float(d["BBox_Y1"])
        x2 = float(d["BBox_X2"])
        y2 = float(d["BBox_Y2"])
        
        # Clip to image boundaries
        x1 = max(0.0, min(w_px, x1))
        y1 = max(0.0, min(h_px, y1))
        x2 = max(0.0, min(w_px, x2))
        y2 = max(0.0, min(h_px, y2))
        
        bw = x2 - x1
        bh = y2 - y1
        
        if bw <= 1.0 or bh <= 1.0:
            invalid_boxes += 1
            continue
            
        # YOLO normalized format: x_center, y_center, width, height (all normalized 0 to 1)
        xc = (x1 + bw / 2.0) / w_px
        yc = (y1 + bh / 2.0) / h_px
        nw = bw / w_px
        nh = bh / h_px
        
        xc = round(float(np.clip(xc, 0.0, 1.0)), 6)
        yc = round(float(np.clip(yc, 0.0, 1.0)), 6)
        nw = round(float(np.clip(nw, 0.0, 1.0)), 6)
        nh = round(float(np.clip(nh, 0.0, 1.0)), 6)
        
        yolo_lines.append(f"{c_idx} {xc} {yc} {nw} {nh}")
        ann_records.append({
            "class_idx": c_idx,
            "class_name": c_name,
            "bbox_pixels": [round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1)],
            "yolo_normalized": [xc, yc, nw, nh],
            "asset_id": d.get("Asset_ID", f"ASSET-{img_id}-{len(yolo_lines)}"),
            "details": d.get("Details", "")
        })
        total_boxes += 1
        
    with open(txt_path, "w", encoding="utf-8") as tf:
        for line in yolo_lines:
            tf.write(f"{line}\n")
            
    annotations_by_image[img_id] = {
        "image_id": img_id,
        "street_id": img_row["Street_ID"],
        "street_name": img_row["Street_Name"],
        "file_name": fname,
        "image_path": img_row["Image_Path"],
        "width_px": w_px,
        "height_px": h_px,
        "boxes_count": len(ann_records),
        "annotations": ann_records
    }

print(f"Generated {len(annotations_by_image)} YOLO label files in {labels_dir}")
print(f"Total valid annotations exported: {total_boxes} (Invalid/clipped: {invalid_boxes})")

# Export dataset audit summary
audit_summary = {
    "annotation_system": "Human-in-the-Loop Urban Infrastructure Annotation Engine",
    "version": "1.0-Task5",
    "classes_defined": CLASSES,
    "total_images_annotated": len(annotations_by_image),
    "total_bounding_boxes": total_boxes,
    "average_boxes_per_image": round(total_boxes / len(annotations_by_image), 2),
    "class_counts": {c: 0 for c in CLASSES}
}

for item in annotations_by_image.values():
    for ann in item["annotations"]:
        audit_summary["class_counts"][ann["class_name"]] += 1

audit_json_path = os.path.join(yolo_dir, "annotation_audit.json")
with open(audit_json_path, "w", encoding="utf-8") as f:
    json.dump(audit_summary, f, indent=2)

# Generate dataset.yaml for YOLO training
data_yaml_content = f"""# FarmwiseAI Task 5 — Urban Intelligence Dataset Configuration
path: {yolo_dir}
train: images/train
val: images/val
test: images/test

nc: {len(CLASSES)}
names: {CLASSES}
"""
with open(os.path.join(yolo_dir, "data.yaml"), "w", encoding="utf-8") as f:
    f.write(data_yaml_content)

print(f"Generated {os.path.join(yolo_dir, 'data.yaml')}")
print(f"Generated {audit_json_path}")
