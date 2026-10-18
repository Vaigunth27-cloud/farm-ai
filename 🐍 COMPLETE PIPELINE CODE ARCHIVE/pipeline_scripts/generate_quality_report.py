import os
import json
import hashlib
import numpy as np
import pandas as pd
from PIL import Image
from shapely.geometry import shape, Point, LineString, MultiPolygon

# 1. Load Study Area Polygon
with open(r"D:\Study_area.geojson", "r", encoding="utf-8") as f:
    study_data = json.load(f)
study_poly = shape(study_data["features"][0]["geometry"])
study_poly_buff15 = study_poly.buffer(0.00015) # ~16.5m buffer for road width / centerline tolerance

# 2. Street Definitions & Known Coordinates from Project Files
# We cross-reference folder names, v5-corrected workbook, team geojson, and GIS layers
street_metadata = {
    "Sathy Road": {
        "street_id": "ST01",
        "canonical_name": "Sathy Road (NH 948 / Sathyamangalam Road)",
        "zone_type": "Commercial Highway Corridor",
        "start_coord": (11.035355, 76.973424),
        "end_coord": (11.032812, 76.974161),
        "road_type": "4-Lane Divided Asphalt Highway",
        "traffic_level": "High Commercial Traffic"
    },
    "Sridevi Nagar 4th Street": {
        "street_id": "ST02",
        "canonical_name": "4th Street, Sridevi Nagar",
        "zone_type": "Residential Colony",
        "start_coord": (11.036796, 76.973404),
        "end_coord": (11.034500, 76.974801),
        "road_type": "Paved Concrete Colony Road",
        "traffic_level": "Low Local Residential"
    },
    "Ganapathy Pudur 3rd Street": {
        "street_id": "ST03",
        "canonical_name": "Ganapathy Pudur 3rd Street",
        "zone_type": "Mixed (Commercial Ground Floor + Residential)",
        "start_coord": (11.033632, 76.974801),
        "end_coord": (11.032400, 76.976212),
        "road_type": "2-Lane Bitumen Road",
        "traffic_level": "Medium Mixed Traffic"
    },
    "Gandhi Nagar": {
        "street_id": "ST04",
        "canonical_name": "Gandhi Nagar Street",
        "zone_type": "Mixed Commercial & Institutional",
        "start_coord": (11.038200, 76.974500),
        "end_coord": (11.039600, 76.975600),
        "road_type": "2-Lane Bitumen Road",
        "traffic_level": "Moderate Traffic"
    },
    "Gopalasamy Kovil Street": {
        "street_id": "ST05",
        "canonical_name": "Gopalasamy Kovil Street",
        "zone_type": "Traditional Residential & Temple Zone",
        "start_coord": (11.034497, 76.971928),
        "end_coord": (11.035279, 76.973046),
        "road_type": "Narrow Bitumen Street",
        "traffic_level": "Low Residential / Pedestrian"
    },
    "KRG Nagar - Kattabomman Street": {
        "street_id": "ST06",
        "canonical_name": "KRG Nagar - Kattabomman Street",
        "zone_type": "Dense Residential & Small Workshops",
        "start_coord": (11.037542, 76.980593),
        "end_coord": (11.037795, 76.982755),
        "road_type": "Paved Concrete & Bitumen",
        "traffic_level": "Moderate Residential & Auto"
    },
    "PN palayam street": {
        "street_id": "ST07",
        "canonical_name": "PN Palayam Street / Road",
        "zone_type": "Mixed Residential & Textile Retail",
        "start_coord": (11.028301, 76.972502),
        "end_coord": (11.027349, 76.974835),
        "road_type": "2-Lane Bitumen Road",
        "traffic_level": "Moderate Mixed Traffic"
    },
    "Raja Street - Sanganur Road": {
        "street_id": "ST08",
        "canonical_name": "Raja Street - Sanganur Road",
        "zone_type": "Primary Commercial Collector Road",
        "start_coord": (11.035397, 76.974161),
        "end_coord": (11.032241, 76.975105),
        "road_type": "2-Lane High Capacity Bitumen",
        "traffic_level": "Heavy Commercial & Transit"
    },
    "Sri Ganapathy Gardens 3rd Street": {
        "street_id": "ST09",
        "canonical_name": "Sri Ganapathy Gardens 3rd Street",
        "zone_type": "Planned Residential Layout",
        "start_coord": (11.039200, 76.972200),
        "end_coord": (11.040300, 76.973100),
        "road_type": "Paved Concrete Residential Way",
        "traffic_level": "Very Low Local Traffic"
    },
    "Avaram Palayam Street": {
        "street_id": "ST10",
        "canonical_name": "Ganapathy - Avarampalayam Road",
        "zone_type": "Commercial & Industrial Fringe",
        "start_coord": (11.031061, 76.978492),
        "end_coord": (11.033774, 76.979375),
        "road_type": "2-Lane Bitumen Road",
        "traffic_level": "Medium Commercial & Goods"
    }
}

base_dir = r"D:\farm ai"
street_folders = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])

street_records = []
image_records = []
md5_dict = {}

for folder in street_folders:
    s_meta = street_metadata.get(folder, {})
    s_id = s_meta.get("street_id", "UNKNOWN")
    c_name = s_meta.get("canonical_name", folder)
    z_type = s_meta.get("zone_type", "Unknown")
    r_type = s_meta.get("road_type", "Unknown")
    t_level = s_meta.get("traffic_level", "Unknown")
    
    start_c = s_meta.get("start_coord", (None, None))
    end_c = s_meta.get("end_coord", (None, None))
    
    # Check geospatial boundary membership
    if start_c[0] and end_c[0]:
        start_pt = Point(start_c[1], start_c[0])
        end_pt = Point(end_c[1], end_c[0])
        line = LineString([(start_c[1], start_c[0]), (end_c[1], end_c[0])])
        
        # Exact containment
        start_in_exact = bool(study_poly.contains(start_pt))
        end_in_exact = bool(study_poly.contains(end_pt))
        inter_exact = study_poly.intersection(line)
        pct_in_exact = round((inter_exact.length / line.length * 100), 1) if line.length > 0 else 0
        
        # Road corridor buffer (15m tolerance for road boundary centerlines)
        start_in_buff = bool(study_poly_buff15.contains(start_pt))
        end_in_buff = bool(study_poly_buff15.contains(end_pt))
        inter_buff = study_poly_buff15.intersection(line)
        pct_in_buff = round((inter_buff.length / line.length * 100), 1) if line.length > 0 else 0
        
        dist_start_m = round(float(study_poly.distance(start_pt)) * 111000, 1)
        dist_end_m = round(float(study_poly.distance(end_pt)) * 111000, 1)
        
        # Length in meters approx
        deg_len = line.length
        # lat mid:
        mid_lat = (start_c[0] + end_c[0]) / 2.0
        # 1 deg lat = 110574m, 1 deg lon = 111320 * cos(mid_lat)
        dlat = (end_c[0] - start_c[0]) * 110574.0
        dlon = (end_c[1] - start_c[1]) * 111320.0 * np.cos(np.radians(mid_lat))
        length_m = round(float(np.hypot(dlat, dlon)), 1)
        
        if pct_in_buff >= 95.0:
            bound_status = "INSIDE (Compliant)"
        elif pct_in_buff > 0.0:
            bound_status = f"PARTIALLY INSIDE ({pct_in_buff}% inside 15m road buffer)"
        else:
            bound_status = f"OUTSIDE (Min dist: {min(dist_start_m, dist_end_m)}m from Ward 29)"
    else:
        start_in_exact = end_in_exact = False
        start_in_buff = end_in_buff = False
        pct_in_exact = pct_in_buff = 0.0
        dist_start_m = dist_end_m = -1
        length_m = 0.0
        bound_status = "COORDINATES MISSING"

    # Scan images
    s_path = os.path.join(base_dir, folder)
    files = sorted([f for f in os.listdir(s_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    
    img_count = len(files)
    
    # Check images in folder
    for idx, f in enumerate(files):
        img_id = f"{s_id}-IMG-{idx+1:02d}"
        f_path = os.path.join(s_path, f)
        f_size = os.path.getsize(f_path)
        
        # MD5
        hasher = hashlib.md5()
        with open(f_path, 'rb') as fp:
            while chunk := fp.read(65536):
                hasher.update(chunk)
        f_hash = hasher.hexdigest()
        
        is_dup = f_hash in md5_dict
        if is_dup:
            md5_dict[f_hash].append((folder, f))
        else:
            md5_dict[f_hash] = [(folder, f)]
            
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
            
        # Interpolated coordinate along street
        if img_count > 1 and start_c[0] and end_c[0]:
            alpha = idx / (img_count - 1)
            img_lat = round(start_c[0] + alpha * (end_c[0] - start_c[0]), 6)
            img_lon = round(start_c[1] + alpha * (end_c[1] - start_c[1]), 6)
            img_pt = Point(img_lon, img_lat)
            img_in_ward = bool(study_poly_buff15.contains(img_pt))
        else:
            img_lat = start_c[0]
            img_lon = start_c[1]
            img_in_ward = start_in_buff
            
        image_records.append({
            "image_id": img_id,
            "street_id": s_id,
            "street_folder": folder,
            "canonical_street_name": c_name,
            "file_name": f,
            "relative_path": os.path.join(folder, f),
            "file_size_kb": round(f_size / 1024, 1),
            "width_px": w,
            "height_px": h,
            "format": fmt,
            "color_mode": mode,
            "mean_brightness": round(mean_b, 1),
            "contrast_std": round(std_b, 1),
            "sharpness_score": round(blur, 1),
            "quality_flag": "PASSED" if blur > 80 and 40 < mean_b < 220 else "LOW_QUALITY",
            "is_duplicate": is_dup,
            "estimated_lat": img_lat,
            "estimated_lon": img_lon,
            "in_ward_boundary_15m": img_in_ward
        })
        
    street_records.append({
        "street_id": s_id,
        "folder_name": folder,
        "canonical_name": c_name,
        "zone_type": z_type,
        "road_type": r_type,
        "traffic_level": t_level,
        "image_count": img_count,
        "target_count": 10,
        "count_status": "EXACT (10/10)" if img_count == 10 else ("DEFICIT" if img_count < 10 else "SURPLUS"),
        "length_meters": length_m,
        "start_latitude": start_c[0],
        "start_longitude": start_c[1],
        "end_latitude": end_c[0],
        "end_longitude": end_c[1],
        "start_in_boundary_exact": start_in_exact,
        "end_in_boundary_exact": end_in_exact,
        "pct_inside_exact": pct_in_exact,
        "pct_inside_15m_buffer": pct_in_buff,
        "dist_start_to_ward_m": dist_start_m,
        "dist_end_to_ward_m": dist_end_m,
        "boundary_compliance": bound_status
    })

df_streets = pd.DataFrame(street_records)
df_images = pd.DataFrame(image_records)

# Save reports to D:\farm ai
csv_report_path = r"D:\farm ai\data_quality_report.csv"
json_report_path = r"D:\farm ai\data_quality_report.json"

df_images.to_csv(csv_report_path, index=False)

summary_json = {
    "project": "FarmwiseAI Task 5 — Street View Urban Intelligence",
    "ward": "Ward 29, North Zone, Coimbatore Corporation, Tamil Nadu",
    "audit_timestamp": "2026-10-02T16:55:00",
    "audit_scope": {
        "total_street_folders": len(street_folders),
        "total_images": len(df_images),
        "unique_images": len(df_images) - sum(1 for v in md5_dict.values() if len(v) > 1),
        "exact_duplicates": sum(1 for v in md5_dict.values() if len(v) > 1),
        "total_road_network_km": round(float(df_streets["length_meters"].sum()) / 1000.0, 2),
        "study_area_bounds": {
            "min_lon": 76.969936, "min_lat": 11.027257,
            "max_lon": 76.986753, "max_lat": 11.037881
        }
    },
    "street_audits": df_streets.to_dict(orient="records"),
    "quality_metrics_summary": {
        "mean_image_width": round(float(df_images["width_px"].mean()), 1),
        "mean_image_height": round(float(df_images["height_px"].mean()), 1),
        "mean_file_size_kb": round(float(df_images["file_size_kb"].mean()), 1),
        "mean_sharpness": round(float(df_images["sharpness_score"].mean()), 1),
        "images_passing_quality": int((df_images["quality_flag"] == "PASSED").sum()),
        "images_low_quality": int((df_images["quality_flag"] == "LOW_QUALITY").sum())
    }
}

with open(json_report_path, "w", encoding="utf-8") as f:
    json.dump(summary_json, f, indent=2)

print(f"Generated {csv_report_path} with {len(df_images)} image rows.")
print(f"Generated {json_report_path} with {len(df_streets)} street rows.")
print("\n--- STREET AUDIT TABLE ---")
print(df_streets[["street_id", "folder_name", "image_count", "count_status", "length_meters", "pct_inside_15m_buffer", "boundary_compliance"]].to_string())
