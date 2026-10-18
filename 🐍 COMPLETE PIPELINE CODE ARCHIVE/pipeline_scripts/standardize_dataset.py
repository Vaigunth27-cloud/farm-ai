import os
import hashlib
import json
import re
import numpy as np
import pandas as pd
from PIL import Image
from shapely.geometry import shape, Point, LineString

# Load Study Area
with open(r"D:\Study_area.geojson", "r", encoding="utf-8") as f:
    study_data = json.load(f)
study_poly = shape(study_data["features"][0]["geometry"])
study_poly_buff15 = study_poly.buffer(0.00015)

base_dir = r"D:\farm ai"

street_definitions = [
    {
        "Street_ID": "ST01",
        "Street_Name": "Sathy Road (NH 948)",
        "Folder_Name": "Sathy Road",
        "Zone_Type": "Commercial Highway Corridor",
        "Road_Type": "4-Lane Divided Asphalt Highway",
        "Traffic_Level": "High Commercial Traffic",
        "Start_Latitude": 11.035355,
        "Start_Longitude": 76.973424,
        "End_Latitude": 11.032812,
        "End_Longitude": 76.974161,
        "Source": "Google Street View",
        "Study_Area_Ward": "Ward 29",
        "Corporation": "Coimbatore",
        "State": "Tamil Nadu"
    },
    {
        "Street_ID": "ST02",
        "Street_Name": "4th Street, Sridevi Nagar",
        "Folder_Name": "Sridevi Nagar 4th Street",
        "Zone_Type": "Residential Colony",
        "Road_Type": "Paved Concrete Colony Road",
        "Traffic_Level": "Low Local Residential",
        "Start_Latitude": 11.036796,
        "Start_Longitude": 76.973404,
        "End_Latitude": 11.034500,
        "End_Longitude": 76.974801,
        "Source": "Google Street View",
        "Study_Area_Ward": "Ward 29",
        "Corporation": "Coimbatore",
        "State": "Tamil Nadu"
    },
    {
        "Street_ID": "ST03",
        "Street_Name": "Ganapathy Pudur 3rd Street",
        "Folder_Name": "Ganapathy Pudur 3rd Street",
        "Zone_Type": "Mixed (Commercial Ground Floor + Residential)",
        "Road_Type": "2-Lane Bitumen Road",
        "Traffic_Level": "Medium Mixed Traffic",
        "Start_Latitude": 11.033632,
        "Start_Longitude": 76.974801,
        "End_Latitude": 11.032400,
        "End_Longitude": 76.976212,
        "Source": "Google Street View",
        "Study_Area_Ward": "Ward 29",
        "Corporation": "Coimbatore",
        "State": "Tamil Nadu"
    },
    {
        "Street_ID": "ST04",
        "Street_Name": "Gandhi Nagar Street",
        "Folder_Name": "Gandhi Nagar",
        "Zone_Type": "Mixed Commercial & Institutional",
        "Road_Type": "2-Lane Bitumen Road",
        "Traffic_Level": "Moderate Traffic",
        "Start_Latitude": 11.038200,
        "Start_Longitude": 76.974500,
        "End_Latitude": 11.039600,
        "End_Longitude": 76.975600,
        "Source": "Google Street View",
        "Study_Area_Ward": "Ward 29 (Extended North Corridor)",
        "Corporation": "Coimbatore",
        "State": "Tamil Nadu"
    },
    {
        "Street_ID": "ST05",
        "Street_Name": "Gopalasamy Kovil Street",
        "Folder_Name": "Gopalasamy Kovil Street",
        "Zone_Type": "Traditional Residential & Temple Zone",
        "Road_Type": "Narrow Bitumen Street",
        "Traffic_Level": "Low Residential / Pedestrian",
        "Start_Latitude": 11.034497,
        "Start_Longitude": 76.971928,
        "End_Latitude": 11.035279,
        "End_Longitude": 76.973046,
        "Source": "Google Street View",
        "Study_Area_Ward": "Ward 29",
        "Corporation": "Coimbatore",
        "State": "Tamil Nadu"
    },
    {
        "Street_ID": "ST06",
        "Street_Name": "KRG Nagar - Kattabomman Street",
        "Folder_Name": "KRG Nagar - Kattabomman Street",
        "Zone_Type": "Dense Residential & Small Workshops",
        "Road_Type": "Paved Concrete & Bitumen",
        "Traffic_Level": "Moderate Residential & Auto",
        "Start_Latitude": 11.037542,
        "Start_Longitude": 76.980593,
        "End_Latitude": 11.037795,
        "End_Longitude": 76.982755,
        "Source": "Google Street View",
        "Study_Area_Ward": "Ward 29",
        "Corporation": "Coimbatore",
        "State": "Tamil Nadu"
    },
    {
        "Street_ID": "ST07",
        "Street_Name": "PN Palayam Street",
        "Folder_Name": "PN palayam street",
        "Zone_Type": "Mixed Residential & Textile Retail",
        "Road_Type": "2-Lane Bitumen Road",
        "Traffic_Level": "Moderate Mixed Traffic",
        "Start_Latitude": 11.028301,
        "Start_Longitude": 76.972502,
        "End_Latitude": 11.027349,
        "End_Longitude": 76.974835,
        "Source": "Google Street View",
        "Study_Area_Ward": "Ward 29",
        "Corporation": "Coimbatore",
        "State": "Tamil Nadu"
    },
    {
        "Street_ID": "ST08",
        "Street_Name": "Raja Street - Sanganur Road",
        "Folder_Name": "Raja Street - Sanganur Road",
        "Zone_Type": "Primary Commercial Collector Road",
        "Road_Type": "2-Lane High Capacity Bitumen",
        "Traffic_Level": "Heavy Commercial & Transit",
        "Start_Latitude": 11.035397,
        "Start_Longitude": 76.974161,
        "End_Latitude": 11.032241,
        "End_Longitude": 76.975105,
        "Source": "Google Street View",
        "Study_Area_Ward": "Ward 29",
        "Corporation": "Coimbatore",
        "State": "Tamil Nadu"
    },
    {
        "Street_ID": "ST09",
        "Street_Name": "Sri Ganapathy Gardens 3rd Street",
        "Folder_Name": "Sri Ganapathy Gardens 3rd Street",
        "Zone_Type": "Planned Residential Layout",
        "Road_Type": "Paved Concrete Residential Way",
        "Traffic_Level": "Very Low Local Traffic",
        "Start_Latitude": 11.039200,
        "Start_Longitude": 76.972200,
        "End_Latitude": 11.040300,
        "End_Longitude": 76.973100,
        "Source": "Google Street View",
        "Study_Area_Ward": "Ward 29 (Extended North Corridor)",
        "Corporation": "Coimbatore",
        "State": "Tamil Nadu"
    },
    {
        "Street_ID": "ST10",
        "Street_Name": "Ganapathy - Avarampalayam Road",
        "Folder_Name": "Avaram Palayam Street",
        "Zone_Type": "Commercial & Industrial Fringe",
        "Road_Type": "2-Lane Bitumen Road",
        "Traffic_Level": "Medium Commercial & Goods",
        "Start_Latitude": 11.031061,
        "Start_Longitude": 76.978492,
        "End_Latitude": 11.033774,
        "End_Longitude": 76.979375,
        "Source": "Google Street View",
        "Study_Area_Ward": "Ward 29",
        "Corporation": "Coimbatore",
        "State": "Tamil Nadu"
    }
]

# Helper to sort filenames naturally and chronologically
def natural_sort_key(s):
    # If it's a screenshot with date/time: Screenshot YYYY-MM-DD HHMMSS.png
    m = re.search(r"(\d{4}-\d{2}-\d{2}\s+\d{6})", s)
    if m:
        return (0, m.group(1))
    # If it's a number like 5.png, 10.png
    m_num = re.match(r"^(\d+)\.", s)
    if m_num:
        return (1, int(m_num.group(1)))
    return (2, s)

images_rows = []
streets_rows = []
metadata_rows = []

for s_def in street_definitions:
    s_folder = s_def["Folder_Name"]
    s_id = s_def["Street_ID"]
    s_name = s_def["Street_Name"]
    z_type = s_def["Zone_Type"]
    
    dir_path = os.path.join(base_dir, s_folder)
    if not os.path.exists(dir_path):
        print(f"Warning: Directory {dir_path} not found!")
        continue
        
    all_files = [f for f in os.listdir(dir_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    all_files.sort(key=natural_sort_key)
    
    img_count = len(all_files)
    
    # Calculate street length
    lat1, lon1 = s_def["Start_Latitude"], s_def["Start_Longitude"]
    lat2, lon2 = s_def["End_Latitude"], s_def["End_Longitude"]
    line = LineString([(lon1, lat1), (lon2, lat2)])
    mid_lat = (lat1 + lat2) / 2.0
    dlat = (lat2 - lat1) * 110574.0
    dlon = (lon2 - lon1) * 111320.0 * np.cos(np.radians(mid_lat))
    length_m = round(float(np.hypot(dlat, dlon)), 1)
    
    # Boundary check
    inter_buff = study_poly_buff15.intersection(line)
    pct_buff = round((inter_buff.length / line.length * 100), 1) if line.length > 0 else 0
    if pct_buff >= 95.0:
        boundary_status = "Fully Within Ward 29"
    elif pct_buff > 0.0:
        boundary_status = f"Borderline / Partial ({pct_buff}% in road buffer)"
    else:
        dist_m = round(float(study_poly.distance(Point(lon1, lat1))) * 111000, 1)
        boundary_status = f"Extended Corridor ({dist_m}m Outside Ward 29)"
        
    streets_rows.append({
        "Street_ID": s_id,
        "Street_Name": s_name,
        "Folder_Name": s_folder,
        "Zone_Type": z_type,
        "Road_Type": s_def["Road_Type"],
        "Traffic_Level": s_def["Traffic_Level"],
        "Total_Images": img_count,
        "Estimated_Length_m": length_m,
        "Start_Latitude": lat1,
        "Start_Longitude": lon1,
        "End_Latitude": lat2,
        "End_Longitude": lon2,
        "Study_Area_Ward": s_def["Study_Area_Ward"],
        "Corporation": s_def["Corporation"],
        "State": s_def["State"],
        "Boundary_Status": boundary_status,
        "Source": s_def["Source"]
    })
    
    # Process each image
    for idx, f in enumerate(all_files):
        capture_order = idx + 1
        img_id = f"IMG-{s_id}-{capture_order:03d}"
        f_path = os.path.join(dir_path, f)
        rel_path = f"{s_folder}/{f}"
        f_size = os.path.getsize(f_path)
        
        # MD5
        hasher = hashlib.md5()
        with open(f_path, "rb") as fp:
            while chunk := fp.read(65536):
                hasher.update(chunk)
        f_md5 = hasher.hexdigest()
        
        # PIL stats
        with Image.open(f_path) as im:
            w, h = im.size
            fmt = im.format
            mode = im.mode
            gray = im.convert('L')
            arr = np.array(gray, dtype=np.float32)
            mean_b = float(np.mean(arr))
            std_b = float(np.std(arr))
            gy, gx = np.gradient(arr)
            blur = float(np.var(np.hypot(gx, gy)))
            
        # Interpolated coordinate along street line
        if img_count > 1:
            alpha = idx / (img_count - 1)
            img_lat = round(lat1 + alpha * (lat2 - lat1), 6)
            img_lon = round(lon1 + alpha * (lon2 - lon1), 6)
        else:
            img_lat = lat1
            img_lon = lon1
            
        img_pt = Point(img_lon, img_lat)
        in_ward = bool(study_poly_buff15.contains(img_pt))
        
        # 1. master_images row (Standardized schema requested by user)
        # Standardize: Street_ID, Street_Name, Image_ID, Latitude, Longitude, Image_Path, Capture_Order, Source, Zone_Type
        images_rows.append({
            "Street_ID": s_id,
            "Street_Name": s_name,
            "Image_ID": img_id,
            "Latitude": img_lat,
            "Longitude": img_lon,
            "Image_Path": rel_path,
            "Capture_Order": capture_order,
            "Source": s_def["Source"],
            "Zone_Type": z_type,
            "File_Name": f,
            "Width_px": w,
            "Height_px": h,
            "In_Study_Boundary": in_ward
        })
        
        # 2. master_metadata row (Comprehensive technical catalog)
        metadata_rows.append({
            "Image_ID": img_id,
            "Street_ID": s_id,
            "Street_Name": s_name,
            "Capture_Order": capture_order,
            "File_Name": f,
            "Image_Path": rel_path,
            "Latitude": img_lat,
            "Longitude": img_lon,
            "Coordinate_CRS": "EPSG:4326 (WGS 84)",
            "Coordinate_Derivation": "Linear Road Transect Interpolation",
            "In_Study_Boundary": in_ward,
            "Boundary_Status": boundary_status,
            "Zone_Type": z_type,
            "Road_Type": s_def["Road_Type"],
            "Source": s_def["Source"],
            "Format": fmt,
            "Color_Mode": mode,
            "Width_px": w,
            "Height_px": h,
            "Aspect_Ratio": round(w / h, 3),
            "File_Size_KB": round(f_size / 1024, 1),
            "MD5_Checksum": f_md5,
            "Mean_Brightness": round(mean_b, 1),
            "Contrast_Std": round(std_b, 1),
            "Sharpness_Score": round(blur, 1),
            "Quality_Status": "PASSED" if blur > 80 and 40 < mean_b < 220 else "LOW_QUALITY",
            "Study_Area_Ward": s_def["Study_Area_Ward"],
            "Corporation": s_def["Corporation"],
            "State": s_def["State"]
        })

df_images = pd.DataFrame(images_rows)
df_streets = pd.DataFrame(streets_rows)
df_meta = pd.DataFrame(metadata_rows)

p_images = r"D:\farm ai\master_images.csv"
p_streets = r"D:\farm ai\master_streets.csv"
p_meta = r"D:\farm ai\master_metadata.csv"

df_images.to_csv(p_images, index=False)
df_streets.to_csv(p_streets, index=False)
df_meta.to_csv(p_meta, index=False)

print(f"Generated {p_images} with {len(df_images)} rows.")
print(f"Generated {p_streets} with {len(df_streets)} rows.")
print(f"Generated {p_meta} with {len(df_meta)} rows.")
