import os
import pandas as pd

p_images = r"D:\farm ai\master_images.csv"
p_streets = r"D:\farm ai\master_streets.csv"
p_meta = r"D:\farm ai\master_metadata.csv"

base_dir = r"D:\farm ai"

print("=== VALIDATING PHASE 2 CANONICAL DATASETS ===")

# 1. master_images.csv
df_img = pd.read_csv(p_images)
required_img_cols = [
    "Street_ID", "Street_Name", "Image_ID", "Latitude", "Longitude",
    "Image_Path", "Capture_Order", "Source", "Zone_Type"
]
missing_img_cols = [c for c in required_img_cols if c not in df_img.columns]
print(f"master_images.csv shape: {df_img.shape}")
print(f"Missing required columns in master_images.csv: {missing_img_cols}")
print(f"Image_ID unique count: {df_img['Image_ID'].nunique()} / {len(df_img)}")
print(f"Street_ID unique count: {df_img['Street_ID'].nunique()} ({sorted(df_img['Street_ID'].unique())})")

# Check all paths exist on disk
all_paths_exist = True
missing_paths = []
for p in df_img["Image_Path"]:
    full_p = os.path.join(base_dir, p)
    if not os.path.exists(full_p):
        all_paths_exist = False
        missing_paths.append(p)
print(f"All {len(df_img)} Image_Paths exist on disk: {all_paths_exist}")
if missing_paths:
    print(f"Missing paths: {missing_paths}")

# Check coordinates
lat_min, lat_max = df_img["Latitude"].min(), df_img["Latitude"].max()
lon_min, lon_max = df_img["Longitude"].min(), df_img["Longitude"].max()
print(f"Latitude range: {lat_min:.6f} to {lat_max:.6f}")
print(f"Longitude range: {lon_min:.6f} to {lon_max:.6f}")
print(f"Null values in master_images: {df_img[required_img_cols].isna().sum().to_dict()}")

# 2. master_streets.csv
df_str = pd.read_csv(p_streets)
required_str_cols = [
    "Street_ID", "Street_Name", "Folder_Name", "Zone_Type", "Road_Type",
    "Traffic_Level", "Total_Images", "Estimated_Length_m", "Start_Latitude",
    "Start_Longitude", "End_Latitude", "End_Longitude", "Study_Area_Ward",
    "Corporation", "State", "Boundary_Status", "Source"
]
missing_str_cols = [c for c in required_str_cols if c not in df_str.columns]
print(f"\nmaster_streets.csv shape: {df_str.shape}")
print(f"Missing required columns in master_streets.csv: {missing_str_cols}")
print(f"Total road network length: {df_str['Estimated_Length_m'].sum():.1f} meters ({df_str['Estimated_Length_m'].sum()/1000:.2f} km)")
print(f"Null values in master_streets: {df_str[required_str_cols].isna().sum().to_dict()}")

# 3. master_metadata.csv
df_met = pd.read_csv(p_meta)
print(f"\nmaster_metadata.csv shape: {df_met.shape}")
print(f"Columns in master_metadata.csv: {list(df_met.columns)}")
print(f"Quality flags: {df_met['Quality_Status'].value_counts().to_dict()}")
print(f"Boundary compliance: {df_met['In_Study_Boundary'].value_counts().to_dict()}")

print("\n--- SAMPLE ROWS FROM master_images.csv ---")
print(df_img[["Street_ID", "Image_ID", "Capture_Order", "Latitude", "Longitude", "Zone_Type", "Image_Path"]].head(6).to_string())

print("\n--- MASTER STREETS TABLE ---")
print(df_str[["Street_ID", "Street_Name", "Zone_Type", "Total_Images", "Estimated_Length_m", "Boundary_Status"]].to_string())
