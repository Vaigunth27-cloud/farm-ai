import os
import sys
import shutil
import json
import yaml
import pandas as pd
import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
master_images_csv = os.path.join(base_dir, "master_images.csv")
yolo_labels_dir = os.path.join(base_dir, "yolo_annotations", "labels")
split_dir = os.path.join(base_dir, "dataset_splits")

# 1. Generate Dataset Registry (Documenting all public & local training provenance)
registry_data = [
    {
        "Dataset_Source": "Mapillary Vistas",
        "Scope": "25,000 Global Street-Scene Panoramas (124 classes)",
        "License": "CC BY-NC-SA 4.0",
        "Target_Classes": "Building, Utility Pole, Street Light, Traffic Light, Store Signage, Sidewalk, Road, Pothole, Manhole, Trash Can",
        "Country": "Global (6 continents)",
        "City": "Multiple Global Cities",
        "GPS_Available": "Yes (EXIF Geotagged)",
        "Training_Allowed": "Yes (Academic & Research Fine-Tuning)",
        "Purpose": "Primary Street Infrastructure Feature Pretraining"
    },
    {
        "Dataset_Source": "Cityscapes",
        "Scope": "5,000 Fine + 20,000 Coarse Urban Street Images",
        "License": "Custom Non-Commercial Research License",
        "Target_Classes": "Road, Sidewalk, Building, Traffic Sign, Traffic Light, Pole",
        "Country": "Germany & Central Europe",
        "City": "50 European Cities",
        "GPS_Available": "Yes (Vehicle odometry / GPS)",
        "Training_Allowed": "Yes (Research / Hackathon Benchmark)",
        "Purpose": "Dense Urban Spatial & Built-Environment Prior"
    },
    {
        "Dataset_Source": "HOTOSM Street-level Poles & Towers",
        "Scope": "3,500 Street-Level Pole Images (HuggingFace)",
        "License": "ODbL / OpenStreetMap",
        "Target_Classes": "Electric Utility Pole, Power Transmission Tower",
        "Country": "Global / Emerging Economies",
        "City": "Diverse Urban & Semi-Urban",
        "GPS_Available": "Yes (Geocoded OSM)",
        "Training_Allowed": "Yes (Open Source)",
        "Purpose": "Dedicated Utility Pole & Mast Classification"
    },
    {
        "Dataset_Source": "Chennai Region Streetlight Dataset",
        "Scope": "800+ Streetlight Images (arXiv:2407.01117)",
        "License": "Research Open Access",
        "Target_Classes": "Streetlight, Luminaire Condition, Functionality Status",
        "Country": "India",
        "City": "Chennai Metropolitan Area, Tamil Nadu",
        "GPS_Available": "Yes",
        "Training_Allowed": "Yes",
        "Purpose": "Regional Indian Streetlight & Mast Morphology"
    },
    {
        "Dataset_Source": "India Traffic Signs Dataset (2026)",
        "Scope": "Multi-Class Indian Regulatory & Direction Signs",
        "License": "Mozilla Data Collective Open License",
        "Target_Classes": "Traffic Sign, Speed Limit, Cautionary Board, Regional Signage",
        "Country": "India",
        "City": "Multiple Indian Urban Corridors",
        "GPS_Available": "Yes",
        "Training_Allowed": "Yes",
        "Purpose": "Indian Traffic Sign & Directional Board Recognition"
    },
    {
        "Dataset_Source": "FarmwiseAI Coimbatore Ward 29 Dataset",
        "Scope": "108 High-Resolution Street-Level Images across 10 Streets",
        "License": "FarmwiseAI Product Challenge 2026",
        "Target_Classes": "Building, Electric Pole, Streetlight, Commercial Sign, Transformer, Traffic Signal, Road Infrastructure",
        "Country": "India",
        "City": "Coimbatore Corporation (Ward 29, North Zone)",
        "GPS_Available": "Yes (Derived Linear Transect & Survey)",
        "Training_Allowed": "Yes (Domain Adaptation & Local Verification)",
        "Purpose": "Ground-Truth Local Evaluation, Fine-Tuning & GIS Linking"
    }
]

df_reg = pd.DataFrame(registry_data)
registry_csv_path = os.path.join(base_dir, "dataset_registry.csv")
df_reg.to_csv(registry_csv_path, index=False)
print(f"Generated {registry_csv_path} with {len(df_reg)} registered data sources.")

# 2. Setup Train/Val/Test Split with Strict Street-Level Leakage Prevention
# Train (7 streets, 84 images): ST01, ST02, ST03, ST05, ST06, ST07, ST08
# Val (2 streets, 18 images):   ST04, ST10
# Test (1 street, 6 images):    ST09

TRAIN_STREETS = ["ST01", "ST02", "ST03", "ST05", "ST06", "ST07", "ST08"]
VAL_STREETS   = ["ST04", "ST10"]
TEST_STREETS  = ["ST09"]

for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(split_dir, "images", split), exist_ok=True)
    os.makedirs(os.path.join(split_dir, "labels", split), exist_ok=True)

df_img = pd.read_csv(master_images_csv)
split_counts = {"train": 0, "val": 0, "test": 0}

for idx, row in df_img.iterrows():
    img_id = row["Image_ID"]
    s_id = row["Street_ID"]
    rel_path = row["Image_Path"]
    src_img = os.path.join(base_dir, rel_path)
    src_lbl = os.path.join(yolo_labels_dir, f"{img_id}.txt")
    
    if s_id in TRAIN_STREETS:
        split = "train"
    elif s_id in VAL_STREETS:
        split = "val"
    else:
        split = "test"
        
    split_counts[split] += 1
    
    dst_img = os.path.join(split_dir, "images", split, f"{img_id}.jpg")
    dst_lbl = os.path.join(split_dir, "labels", split, f"{img_id}.txt")
    
    # Convert and copy image as JPEG for YOLO
    with Image.open(src_img) as im:
        im.convert("RGB").save(dst_img, "JPEG", quality=95)
        
    if os.path.exists(src_lbl):
        shutil.copy2(src_lbl, dst_lbl)
    else:
        open(dst_lbl, "w").close()

print(f"Data Splits Generated with Street-Level Leakage Prevention:")
print(f"  Train Set: {split_counts['train']} images (Streets: {TRAIN_STREETS})")
print(f"  Val Set:   {split_counts['val']} images (Streets: {VAL_STREETS})")
print(f"  Test Set:  {split_counts['test']} images (Streets: {TEST_STREETS})")

# 3. Write data.yaml for YOLO training
CLASSES = [
    "building", "electric_pole", "streetlight", "commercial_sign",
    "traffic_signal", "road_sign", "transformer", "drain",
    "sidewalk", "waste_bin", "bus_stop", "other_urban_asset"
]

data_yaml = {
    "path": split_dir,
    "train": "images/train",
    "val": "images/val",
    "test": "images/test",
    "nc": len(CLASSES),
    "names": CLASSES
}

split_yaml_path = os.path.join(split_dir, "data.yaml")
with open(split_yaml_path, "w", encoding="utf-8") as f:
    yaml.dump(data_yaml, f, default_flow_style=False, sort_keys=False)

print(f"Generated {split_yaml_path}")
