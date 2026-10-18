import os
import sys
import json
import urllib.parse
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
master_images_csv = os.path.join(base_dir, "master_images.csv")
master_meta_csv = os.path.join(base_dir, "master_metadata.csv")
bldg_csv_path = os.path.join(base_dir, "building_intelligence.csv")
ocr_csv_path = os.path.join(base_dir, "ocr_intelligence.csv")

annotated_bldg_dir = os.path.join(base_dir, "building_annotated_images")
os.makedirs(annotated_bldg_dir, exist_ok=True)

# Load existing files
df_images = pd.read_csv(master_images_csv)
df_meta = pd.read_csv(master_meta_csv)
df_bldg_orig = pd.read_csv(bldg_csv_path)
df_ocr = pd.read_csv(ocr_csv_path)

print(f"Loaded {len(df_bldg_orig)} building records and {len(df_ocr)} OCR records.")

# Aggregate OCR records per building
ocr_by_bldg = {}
for bldg_id, grp in df_ocr.groupby("Associated_Building_ID"):
    ocr_by_bldg[bldg_id] = {
        "count": len(grp),
        "texts": [str(t) for t in grp["Cleaned_Text"].tolist() if pd.notna(t)],
        "categories": list(set([str(c) for c in grp["Commercial_Category"].tolist() if pd.notna(c)])),
        "max_conf": float(grp["Confidence"].max()) if not grp.empty else 0.0
    }

# Mapping floor notation to floor count and height
floor_specs = {
    "G": {"count": 1, "height": 3.5, "notation": "G"},
    "G+1": {"count": 2, "height": 7.0, "notation": "G+1"},
    "G+2": {"count": 3, "height": 10.5, "notation": "G+2"},
    "G+3": {"count": 4, "height": 14.0, "notation": "G+3"},
    "G+4": {"count": 5, "height": 17.5, "notation": "G+4"}
}

# Facade Type Determination
def get_facade_type(usage, name):
    u = usage.lower()
    n = name.lower()
    if "hotel" in u or "banquet" in u or "residency" in n:
        return "Glass Curtain Wall & ACP Cladding"
    elif "fuel" in u or "petroleum" in n:
        return "Structural Steel Canopy & Aluminum Composite Fascia"
    elif "banking" in u or "financial" in u:
        return "Glazed Commercial Tile & Painted Concrete Plaster"
    elif "automobile" in u or "autozone" in n:
        return "Double-Height Glass Showroom Facade with Steel Truss"
    elif "villa" in u or "duplex" in u or "residence" in n:
        return "Reinforced Concrete Frame & Weatherproof Acrylic Paint"
    elif "multi-family" in u or "apartments" in n:
        return "Plastered Masonry with External Balconies & MS Railings"
    elif "textile" in u or "hardware" in u or "emporium" in n:
        return "Commercial Glazed Display Facade & Signboard Fascia"
    elif "healthcare" in u or "clinic" in u or "pharmacy" in u:
        return "Modern ACP Composite & Tinted Glass Ribbon Windows"
    elif "bakery" in u or "store" in u or "grocery" in u:
        return "Painted Cement Plaster & Roll-Down Steel Shutter Front"
    elif "temple" in u or "shrine" in n:
        return "Traditional Dravidian Gopuram Stucco & Carved Granite Pillars"
    elif "agrahara" in u or "heritage" in u:
        return "Pitched Terracotta Mangalore Tile Roof & Timber Veranda"
    elif "foundry" in u or "workshop" in u or "lathe" in n:
        return "Industrial Pre-Engineered Steel Frame & Corrugated Sheet Roofing"
    else:
        return "Reinforced Concrete Plaster & Commercial Paint"

# Ground Floor Activity Determination
def get_ground_activity(usage, name):
    u = usage.lower()
    n = name.lower()
    if "hotel" in u or "dining" in u or "residency" in n:
        return "Hotel Reception Lobby & Multi-Cuisine Dining Hall"
    elif "fuel" in u or "petroleum" in n:
        return "Fuel Forecourt, Dispenser Islands & 24h Convenience Mart"
    elif "banking" in u or "financial" in u:
        return "Core Banking Customer Hall & 24/7 ATM Vestibule"
    elif "automobile" in u or "autozone" in n:
        return "Automobile Showroom Display & Customer Service Desk"
    elif "villa" in u or "duplex" in u:
        return "Covered Carport & Gated Pedestrian Entrance"
    elif "multi-family" in u or "apartments" in n:
        return "Stilt Covered Parking & Security Entry Gate"
    elif "textile" in u:
        return "Wholesale Textile Display & Counter Sales"
    elif "hardware" in u:
        return "Hardware Retail Display & Heavy Goods Storage"
    elif "healthcare" in u or "clinic" in u:
        return "Outpatient Registration & Pharmacy Counter"
    elif "bakery" in u:
        return "Fresh Confectionery Display & Sit-Out Tea Counter"
    elif "temple" in u or "shrine" in n:
        return "Mandapam Entrance & Devotional Walkway"
    elif "agrahara" in u:
        return "Traditional Thinnai Veranda & Residential Front Door"
    elif "foundry" in u or "workshop" in u:
        return "Heavy Machinery Lathe Bay & Workshop Floor"
    elif "community" in u or "association" in n:
        return "Community Reception & Resident Assembly Office"
    else:
        return "Commercial Ground Retail Shutter Front"

# Building Density Classification
def get_building_density(street_id):
    if street_id in ["ST01", "ST08"]:
        return "High-Density Continuous Commercial Corridor"
    elif street_id in ["ST03", "ST04", "ST07", "ST10"]:
        return "High-Density Mixed-Use Arterial Strip"
    elif street_id in ["ST06"]:
        return "High-Density Mixed Light-Industrial & Residential Strip"
    elif street_id in ["ST02", "ST05"]:
        return "Medium-Density Residential Colony Corridor"
    elif street_id in ["ST09"]:
        return "Low-to-Medium Density Planned Residential Layout"
    return "Medium-Density Mixed Urban Corridor"

# Official Links Builder
def make_official_links(name, street_name, lat, lon):
    clean_street = street_name.split("(")[0].strip()
    query = f"{name}, {clean_street}, Ganapathy, Coimbatore, Tamil Nadu"
    encoded_query = urllib.parse.quote(query)
    search_link = f"https://www.google.com/maps/search/?api=1&query={encoded_query}"
    coord_link = f"https://www.google.com/maps?q={lat:.6f},{lon:.6f}"
    return {
        "google_maps_search": search_link,
        "google_maps_coordinates": coord_link,
        "primary_link": search_link
    }

# Load Fonts
font_path = r"C:\Windows\Fonts\segoeui.ttf"
bold_font_path = r"C:\Windows\Fonts\segoeuib.ttf"
mono_font_path = r"C:\Windows\Fonts\consola.ttf"

try:
    font_hud_title = ImageFont.truetype(bold_font_path, 18)
    font_hud_text = ImageFont.truetype(font_path, 14)
    font_floor_tag = ImageFont.truetype(bold_font_path, 14)
    font_gauge = ImageFont.truetype(mono_font_path, 12)
except Exception:
    font_hud_title = ImageFont.load_default()
    font_hud_text = ImageFont.load_default()
    font_floor_tag = ImageFont.load_default()
    font_gauge = ImageFont.load_default()

enriched_buildings = []

print("Processing building intelligence and generating annotated floor visualizations...")

for idx, row in df_bldg_orig.iterrows():
    orig_b_id = str(row["Building_ID"])
    # Standardized ID: BLDG-STxx-xxx
    b_id = orig_b_id.replace("BLD-", "BLDG-")
    img_id = str(row["Image_ID"])
    street_id = str(row["Street_ID"])
    street_name = str(row["Street_Name"])
    lat = float(row["Latitude"])
    lon = float(row["Longitude"])
    
    floor_not = str(row["Building_Floors"]).strip()
    f_info = floor_specs.get(floor_not, {"count": 2, "height": 7.0, "notation": floor_not})
    floor_count = f_info["count"]
    est_height_m = f_info["height"]
    
    usage = str(row["Building_Usage"])
    name = str(row["Establishment_Name"])
    special = str(row["Special_Features"])
    
    facade_type = get_facade_type(usage, name)
    ground_activity = get_ground_activity(usage, name)
    density = get_building_density(street_id)
    
    # Construction Stage: Operational / Fully Functional
    construction_stage = "Operational / Occupied"
    
    # Official Links
    links = make_official_links(name, street_name, lat, lon)
    
    # OCR Data
    ocr_info = ocr_by_bldg.get(orig_b_id, {
        "count": 0,
        "texts": [],
        "categories": [],
        "max_conf": 0.0
    })
    
    bx1 = int(row["BBox_X1"])
    by1 = int(row["BBox_Y1"])
    bx2 = int(row["BBox_X2"])
    by2 = int(row["BBox_Y2"])
    conf = float(row["Confidence"])
    rel_path = str(row["Evidence_Image"])
    full_img_path = os.path.join(base_dir, rel_path)
    
    # Image size for normalized coords
    orig_img = Image.open(full_img_path).convert("RGB")
    w_img, h_img = orig_img.size
    
    norm_x1 = round(bx1 / w_img, 4)
    norm_y1 = round(by1 / h_img, 4)
    norm_x2 = round(bx2 / w_img, 4)
    norm_y2 = round(by2 / h_img, 4)
    
    # Annotate Building with Floor Segmentation Bands & Height Gauge
    draw_img = orig_img.copy()
    overlay = Image.new("RGBA", draw_img.size, (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    
    # 1. Outer Building Box
    box_color_rgb = (0, 255, 140) # Neon Green / Emerald
    ov_draw.rectangle([bx1, by1, bx2, by2], outline=(0, 255, 140, 240), width=3)
    
    # Corner Accents
    corner_len = min(30, (bx2 - bx1) // 6, (by2 - by1) // 6)
    corner_color = (0, 255, 255, 255) # Cyan
    # Top-Left
    ov_draw.line([(bx1, by1), (bx1 + corner_len, by1)], fill=corner_color, width=5)
    ov_draw.line([(bx1, by1), (bx1, by1 + corner_len)], fill=corner_color, width=5)
    # Top-Right
    ov_draw.line([(bx2, by1), (bx2 - corner_len, by1)], fill=corner_color, width=5)
    ov_draw.line([(bx2, by1), (bx2, by1 + corner_len)], fill=corner_color, width=5)
    # Bottom-Left
    ov_draw.line([(bx1, by2), (bx1 + corner_len, by2)], fill=corner_color, width=5)
    ov_draw.line([(bx1, by2), (bx1, by2 - corner_len)], fill=corner_color, width=5)
    # Bottom-Right
    ov_draw.line([(bx2, by2), (bx2 - corner_len, by2)], fill=corner_color, width=5)
    ov_draw.line([(bx2, by2), (bx2, by2 - corner_len)], fill=corner_color, width=5)
    
    # 2. Floor Segmentation Bands (from bottom to top)
    b_height = by2 - by1
    floor_h = b_height / floor_count
    
    # Distinct pastel tones with alpha for floor tint
    band_colors = [
        (0, 200, 100, 35),   # Ground (greenish)
        (0, 150, 255, 35),   # Floor 1 (blueish)
        (255, 180, 0, 35),   # Floor 2 (amber)
        (255, 0, 150, 35),   # Floor 3 (magenta)
        (150, 50, 255, 35)   # Floor 4 (purple)
    ]
    
    for f_idx in range(floor_count):
        # floor_idx_from_bottom: 0 is Ground
        f_from_bot = f_idx
        y_bot_floor = int(by2 - f_from_bot * floor_h)
        y_top_floor = int(by2 - (f_from_bot + 1) * floor_h)
        if f_from_bot == floor_count - 1:
            y_top_floor = by1
            
        color_rgba = band_colors[f_from_bot % len(band_colors)]
        ov_draw.rectangle([bx1 + 2, y_top_floor + 2, bx2 - 2, y_bot_floor - 2], fill=color_rgba)
        
        # Horizontal dividing line between floors (except bottom of ground)
        if f_from_bot > 0:
            ov_draw.line([(bx1, y_bot_floor), (bx2, y_bot_floor)], fill=(0, 255, 255, 180), width=2)
            
        # Floor Notation Badge
        if f_from_bot == 0:
            fl_label = " G : GROUND FLOOR "
        else:
            fl_label = f" L{f_from_bot} : FLOOR {f_from_bot} (G+{f_from_bot}) "
            
        badge_x = bx1 + 10
        badge_y = (y_top_floor + y_bot_floor) // 2 - 10
        
        # Badge background
        ov_draw.rectangle([badge_x, badge_y - 2, badge_x + len(fl_label)*9 + 8, badge_y + 18], fill=(10, 16, 26, 220), outline=(0, 255, 255, 200), width=1)
        ov_draw.text((badge_x + 4, badge_y), fl_label, fill=(255, 255, 255, 255), font=font_floor_tag)
        
    # 3. Vertical Height Gauge
    gauge_x = max(10, bx1 - 25)
    ov_draw.line([(gauge_x, by1), (gauge_x, by2)], fill=(255, 230, 0, 220), width=2)
    # Top & bottom ticks
    ov_draw.line([(gauge_x - 6, by1), (gauge_x + 6, by1)], fill=(255, 230, 0, 240), width=2)
    ov_draw.line([(gauge_x - 6, by2), (gauge_x + 6, by2)], fill=(255, 230, 0, 240), width=2)
    
    # Tick for each floor
    for f_idx in range(1, floor_count):
        y_tick = int(by2 - f_idx * floor_h)
        h_val = round(f_idx * 3.5, 1)
        ov_draw.line([(gauge_x - 4, y_tick), (gauge_x + 4, y_tick)], fill=(255, 230, 0, 200), width=1)
        ov_draw.text((max(2, gauge_x - 38), y_tick - 7), f"{h_val}m", fill=(255, 230, 0, 240), font=font_gauge)
        
    ov_draw.text((max(2, gauge_x - 38), by2 - 14), "0.0m", fill=(255, 230, 0, 240), font=font_gauge)
    ov_draw.text((max(2, gauge_x - 45), by1 - 16), f"{est_height_m}m", fill=(255, 230, 0, 255), font=font_gauge)

    # 4. Futuristic HUD Header Card
    hud_w = min(w_img - 20, max(520, bx2 - bx1))
    hud_h = 95
    hud_x = max(10, min(bx1, w_img - hud_w - 10))
    hud_y = max(10, by1 - hud_h - 10)
    if hud_y < 10:
        hud_y = by1 + 10 # Place inside top if not enough room above
        
    ov_draw.rectangle([hud_x, hud_y, hud_x + hud_w, hud_y + hud_h], fill=(11, 16, 24, 235), outline=(0, 255, 200, 240), width=2)
    
    # Header Accent Bar
    ov_draw.rectangle([hud_x, hud_y, hud_x + hud_w, hud_y + 4], fill=(0, 255, 200, 255))
    
    # Text lines
    line1 = f"[{b_id}]  FLOORS: {floor_not} ({floor_count})  |  HEIGHT: {est_height_m}m  |  CONF: {conf*100:.1f}%"
    line2 = f"USAGE: {usage}"
    line3 = f"NAME: {name[:40]}"
    line4 = f"FACADE: {facade_type[:32]}  |  GROUND: {ground_activity[:28]}"
    
    ov_draw.text((hud_x + 12, hud_y + 10), line1, fill=(0, 255, 200, 255), font=font_hud_title)
    ov_draw.text((hud_x + 12, hud_y + 34), line2, fill=(255, 230, 100, 255), font=font_hud_text)
    ov_draw.text((hud_x + 12, hud_y + 54), line3, fill=(255, 255, 255, 255), font=font_hud_text)
    ov_draw.text((hud_x + 12, hud_y + 74), line4, fill=(180, 200, 220, 255), font=font_hud_text)
    
    # Merge overlay
    annotated_img = Image.alpha_composite(draw_img.convert("RGBA"), overlay).convert("RGB")
    
    # Save annotated image
    street_annot_dir = os.path.join(annotated_bldg_dir, street_id)
    os.makedirs(street_annot_dir, exist_ok=True)
    out_annot_filename = os.path.basename(rel_path)
    out_annot_path = os.path.join(street_annot_dir, out_annot_filename)
    annotated_img.save(out_annot_path, quality=92)
    
    rel_annot_path = os.path.relpath(out_annot_path, base_dir).replace("\\", "/")
    
    # Build complete record
    rec = {
        # 10 Core Property Parameters
        "Building_ID": b_id,
        "Building_Floors": floor_count,
        "Floor_Notation": floor_not,
        "Estimated_Height_m": est_height_m,
        "Building_Usage": usage,
        "Facade_Type": facade_type,
        "Construction_Stage": construction_stage,
        "Ground_Floor_Activity": ground_activity,
        "Building_Density": density,
        "Official_Links": links["primary_link"],
        
        # Extended Property & Commercial Intelligence
        "Legacy_Building_ID": orig_b_id,
        "Establishment_Name": name,
        "Special_Features": special,
        "Google_Maps_Search_Link": links["google_maps_search"],
        "Google_Maps_Pin_Link": links["google_maps_coordinates"],
        "Detected_Signboards_Count": ocr_info["count"],
        "Detected_OCR_Text": " | ".join(ocr_info["texts"]) if ocr_info["texts"] else "None Detected",
        "Detected_Commercial_Categories": ", ".join(ocr_info["categories"]) if ocr_info["categories"] else "General",
        "Max_OCR_Confidence": round(ocr_info["max_conf"], 3),
        
        # Spatial & Context Metadata
        "Image_ID": img_id,
        "Street_ID": street_id,
        "Street_Name": street_name,
        "Latitude": lat,
        "Longitude": lon,
        "Confidence": conf,
        
        # Bounding Box Coordinates
        "BBox_X1": bx1,
        "BBox_Y1": by1,
        "BBox_X2": bx2,
        "BBox_Y2": by2,
        "Norm_X1": norm_x1,
        "Norm_Y1": norm_y1,
        "Norm_X2": norm_x2,
        "Norm_Y2": norm_y2,
        
        # Evidence Files
        "Evidence_Image": rel_path.replace("\\", "/"),
        "Annotated_Floor_Image": rel_annot_path
    }
    enriched_buildings.append(rec)

# Export updated building_intelligence.csv
df_enriched = pd.DataFrame(enriched_buildings)
df_enriched.to_csv(bldg_csv_path, index=False)
print(f"Exported updated building intelligence to {bldg_csv_path} ({len(df_enriched)} rows, {len(df_enriched.columns)} columns)")

# Export building_intelligence.json
bldg_json_path = os.path.join(base_dir, "building_intelligence.json")
with open(bldg_json_path, "w", encoding="utf-8") as f:
    json.dump(enriched_buildings, f, indent=2, ensure_ascii=False)
print(f"Exported rich JSON store to {bldg_json_path}")

# Compute Summary Statistics
summary_metrics = {
    "total_buildings_inventoried": len(df_enriched),
    "unique_streets_surveyed": int(df_enriched["Street_ID"].nunique()),
    "floor_count_distribution": {
        str(k): int(v) for k, v in df_enriched["Floor_Notation"].value_counts().items()
    },
    "height_statistics_m": {
        "mean_height_m": round(float(df_enriched["Estimated_Height_m"].mean()), 2),
        "min_height_m": round(float(df_enriched["Estimated_Height_m"].min()), 2),
        "max_height_m": round(float(df_enriched["Estimated_Height_m"].max()), 2),
        "median_height_m": round(float(df_enriched["Estimated_Height_m"].median()), 2)
    },
    "usage_distribution": {
        str(k): int(v) for k, v in df_enriched["Building_Usage"].value_counts().items()
    },
    "facade_type_distribution": {
        str(k): int(v) for k, v in df_enriched["Facade_Type"].value_counts().items()
    },
    "ground_floor_activity_distribution": {
        str(k): int(v) for k, v in df_enriched["Ground_Floor_Activity"].value_counts().items()
    },
    "density_distribution": {
        str(k): int(v) for k, v in df_enriched["Building_Density"].value_counts().items()
    },
    "ocr_correlation": {
        "buildings_with_detected_signage": int((df_enriched["Detected_Signboards_Count"] > 0).sum()),
        "total_signboards_linked": int(df_enriched["Detected_Signboards_Count"].sum()),
        "average_signboards_per_building": round(float(df_enriched["Detected_Signboards_Count"].mean()), 2)
    }
}

metrics_json_path = os.path.join(base_dir, "building_summary_metrics.json")
with open(metrics_json_path, "w", encoding="utf-8") as f:
    json.dump(summary_metrics, f, indent=2, ensure_ascii=False)
print(f"Exported building summary metrics to {metrics_json_path}")

print("Phase 7 Python engine execution finished successfully!")
