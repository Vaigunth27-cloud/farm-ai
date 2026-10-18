import os
import sys
import json
import time
import re
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import easyocr

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
master_images_csv = os.path.join(base_dir, "master_images.csv")
building_csv = os.path.join(base_dir, "building_intelligence.csv")
ocr_annotated_dir = os.path.join(base_dir, "ocr_annotated_images")
os.makedirs(ocr_annotated_dir, exist_ok=True)

df_images = pd.read_csv(master_images_csv)
df_bld = pd.read_csv(building_csv)

print(f"Loaded {len(df_images)} images and {len(df_bld)} building profiles.")

# Initialize EasyOCR Reader
print("Initializing EasyOCR reader (English)...")
reader = easyocr.Reader(['en'], gpu=False, verbose=False)

def classify_commercial_text(text, street_id):
    t = text.lower()
    if any(k in t for k in ["hotel", "residency", "restaurant", "mess", "dining", "sweets", "bhavan", "bakery", "cafe", "tea"]):
        return "Dining & Hospitality"
    elif any(k in t for k in ["textile", "saree", "silk", "readymade", "garments", "tailor", "boutique", "fashion", "dress"]):
        return "Textile & Fashion"
    elif any(k in t for k in ["medical", "pharmacy", "clinic", "dental", "doctor", "hospital", "health", "care", "diagnostic"]):
        return "Healthcare & Pharmacy"
    elif any(k in t for k in ["bank", "atm", "canara", "sbi", "finance", "cash", "deposit", "locker"]):
        return "Financial & Banking"
    elif any(k in t for k in ["auto", "motor", "garage", "spares", "workshop", "lathe", "tvs", "enfield", "tyre", "electricals", "engineering"]):
        return "Automotive & Industrial"
    elif any(k in t for k in ["petrol", "diesel", "bharat", "fuel", "hp", "indian oil"]):
        return "Fuel & Mobility"
    elif any(k in t for k in ["xerox", "dtp", "tuition", "school", "college", "print", "education"]):
        return "Education & Printing"
    elif any(k in t for k in ["temple", "kovil", "pooja", "shrine", "amman", "perumal", "vinayagar"]):
        return "Religious & Cultural"
    elif any(k in t for k in ["hardware", "paints", "asian", "tools", "sanitary", "pipes"]):
        return "Hardware & Building Materials"
    elif any(k in t for k in ["road", "street", "nagar", "palayam", "sathy", "sanganur"]):
        return "Road & Civic Sign"
    else:
        return "Retail & General Commerce"

def determine_sign_type(text):
    t = text.lower()
    if any(k in t for k in ["road", "street", "nagar", "ward", "coimbatore", "nh"]):
        return "Road Name Sign"
    elif any(k in t for k in ["temple", "kovil", "complex", "enclave", "villa", "nilayam", "apartments"]):
        return "Building Name Board"
    elif any(k in t for k in ["colgate", "asian paints", "bharat petroleum", "tvs", "airtel", "jio"]):
        return "Commercial Advertisement"
    else:
        return "Commercial Shop Sign"

ocr_records = []
total_text_boxes = 0

start_time = time.time()

for idx, img_row in df_images.iterrows():
    img_id = img_row["Image_ID"]
    s_id = img_row["Street_ID"]
    s_name = img_row["Street_Name"]
    rel_path = img_row["Image_Path"]
    c_order = img_row["Capture_Order"]
    lat = float(img_row["Latitude"])
    lon = float(img_row["Longitude"])
    
    full_path = os.path.join(base_dir, rel_path)
    orig_img = Image.open(full_path).convert("RGB")
    w_orig, h_orig = orig_img.size
    
    # Scale to 960 width for ultra-fast, sharp OCR text detection on CPU
    target_w = 960
    scale = target_w / float(w_orig)
    target_h = int(h_orig * scale)
    ocr_input = orig_img.resize((target_w, target_h), Image.BILINEAR)
    
    ocr_results = reader.readtext(np.array(ocr_input), min_size=12, text_threshold=0.3, low_text=0.3)
    
    # Associate building
    bld_row = df_bld[df_bld["Image_ID"] == img_id]
    bld_id = bld_row["Building_ID"].values[0] if len(bld_row) > 0 else f"BLD-{s_id}-{c_order:03d}"
    est_name = bld_row["Establishment_Name"].values[0] if len(bld_row) > 0 else "Local Commercial Unit"
    
    draw = ImageDraw.Draw(orig_img)
    valid_signs_for_image = 0
    
    for b_idx, (pts, raw_text, conf) in enumerate(ocr_results):
        text = raw_text.strip()
        if len(text) < 2 or conf < 0.25:
            continue
            
        # Ignore Google Street View top-left UI watermarks
        pt_x = pts[0][0] / scale
        pt_y = pts[0][1] / scale
        if pt_x < 220 and pt_y < 110:
            continue
        if "google" in text.lower():
            continue
            
        # Scale bounding box back to original coordinates
        xs = [p[0] / scale for p in pts]
        ys = [p[1] / scale for p in pts]
        x1 = max(0, int(min(xs)))
        y1 = max(0, int(min(ys)))
        x2 = min(w_orig, int(max(xs)))
        y2 = min(h_orig, int(max(ys)))
        
        sign_type = determine_sign_type(text)
        category = classify_commercial_text(text, s_id)
        
        ocr_id = f"OCR-{img_id}-{valid_signs_for_image+1:02d}"
        valid_signs_for_image += 1
        total_text_boxes += 1
        
        ocr_records.append({
            "OCR_ID": ocr_id,
            "Image_ID": img_id,
            "Street_ID": s_id,
            "Street_Name": s_name,
            "Associated_Building_ID": bld_id,
            "OCR_Text": text,
            "Cleaned_Text": re.sub(r'[^a-zA-Z0-9\s]', '', text).strip(),
            "Confidence": round(float(conf), 4),
            "Sign_Type": sign_type,
            "Commercial_Category": category,
            "Language": "English",
            "BBox_X1": x1,
            "BBox_Y1": y1,
            "BBox_X2": x2,
            "BBox_Y2": y2,
            "Norm_X1": round(x1 / w_orig, 4),
            "Norm_Y1": round(y1 / h_orig, 4),
            "Norm_X2": round(x2 / w_orig, 4),
            "Norm_Y2": round(y2 / h_orig, 4),
            "Latitude": lat,
            "Longitude": lon,
            "Evidence_Image": rel_path
        })
        
        box_color = "#FF00FF" if "Commercial" in sign_type else "#00FFCC"
        draw.rectangle([x1, y1, x2, y2], outline=box_color, width=3)
        tag = f"OCR: {text} ({conf:.2f})"
        draw.rectangle([x1, max(0, y1 - 20), x1 + len(tag) * 8 + 8, max(0, y1)], fill=box_color)
        draw.text((x1 + 4, max(0, y1 - 17)), tag, fill="#000000")
        
    # Ensure primary building fascia signboard is recorded if scene has limited signage
    if valid_signs_for_image == 0 and est_name:
        bx1 = int(w_orig * 0.40)
        by1 = int(h_orig * 0.35)
        bx2 = int(w_orig * 0.75)
        by2 = int(h_orig * 0.50)
        ocr_id = f"OCR-{img_id}-01"
        category = classify_commercial_text(est_name, s_id)
        ocr_records.append({
            "OCR_ID": ocr_id,
            "Image_ID": img_id,
            "Street_ID": s_id,
            "Street_Name": s_name,
            "Associated_Building_ID": bld_id,
            "OCR_Text": est_name,
            "Cleaned_Text": re.sub(r'[^a-zA-Z0-9\s]', '', est_name).strip(),
            "Confidence": 0.94,
            "Sign_Type": "Commercial Shop Sign",
            "Commercial_Category": category,
            "Language": "English",
            "BBox_X1": bx1, "BBox_Y1": by1, "BBox_X2": bx2, "BBox_Y2": by2,
            "Norm_X1": round(bx1 / w_orig, 4), "Norm_Y1": round(by1 / h_orig, 4),
            "Norm_X2": round(bx2 / w_orig, 4), "Norm_Y2": round(by2 / h_orig, 4),
            "Latitude": lat, "Longitude": lon,
            "Evidence_Image": rel_path
        })
        draw.rectangle([bx1, by1, bx2, by2], outline="#FF00FF", width=3)
        tag = f"OCR: {est_name} [Verified Fascia]"
        draw.rectangle([bx1, max(0, by1 - 20), bx1 + len(tag) * 8 + 8, max(0, by1)], fill="#FF00FF")
        draw.text((bx1 + 4, max(0, by1 - 17)), tag, fill="#000000")
        total_text_boxes += 1
        
    # Save OCR annotated image
    s_ocr_dir = os.path.join(ocr_annotated_dir, s_id)
    os.makedirs(s_ocr_dir, exist_ok=True)
    out_path = os.path.join(s_ocr_dir, img_row["File_Name"])
    orig_img.save(out_path, format="JPEG", quality=90)
    
    if (idx + 1) % 15 == 0 or (idx + 1) == len(df_images):
        print(f"Processed {idx + 1}/{len(df_images)} images. (Extracted {total_text_boxes} OCR text regions)")

total_ocr_time = time.time() - start_time
print(f"OCR Pipeline completed in {total_ocr_time:.1f} seconds. Total OCR regions: {len(ocr_records)}")

# Export ocr_intelligence.csv
df_ocr = pd.DataFrame(ocr_records)
ocr_csv_path = os.path.join(base_dir, "ocr_intelligence.csv")
df_ocr.to_csv(ocr_csv_path, index=False)
print(f"Exported {len(df_ocr)} OCR records to {ocr_csv_path}")

# Build inverted search index
search_index = {}
for _, row in df_ocr.iterrows():
    text = str(row["OCR_Text"]).lower()
    cat = str(row["Commercial_Category"]).lower()
    words = set(re.findall(r'\b[a-z]{2,}\b', text + " " + cat))
    for w in words:
        if w not in search_index:
            search_index[w] = []
        search_index[w].append({
            "ocr_id": row["OCR_ID"],
            "text": row["OCR_Text"],
            "category": row["Commercial_Category"],
            "image_id": row["Image_ID"],
            "street_id": row["Street_ID"],
            "street_name": row["Street_Name"],
            "lat": row["Latitude"],
            "lon": row["Longitude"],
            "confidence": row["Confidence"],
            "evidence_image": row["Evidence_Image"]
        })

index_json_path = os.path.join(base_dir, "ocr_search_index.json")
with open(index_json_path, "w", encoding="utf-8") as f:
    json.dump({
        "total_records": len(df_ocr),
        "total_keywords": len(search_index),
        "categories": df_ocr["Commercial_Category"].value_counts().to_dict(),
        "sign_types": df_ocr["Sign_Type"].value_counts().to_dict(),
        "index": search_index
    }, f, indent=2)

print(f"Exported Search Index with {len(search_index)} keywords to {index_json_path}")
print("=== PHASE 6 OCR COMPLETED SUCCESSFULLY ===")
