import os
import sys
import json
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
assets_geojson_path = os.path.join(base_dir, "urban_assets_digital_twin.geojson")
roads_geojson_path = os.path.join(base_dir, "road_network_topology.geojson")
study_area_path = r"D:\Study_area.geojson"
images_csv_path = os.path.join(base_dir, "master_images.csv")
bldg_csv_path = os.path.join(base_dir, "building_intelligence.csv")
inv_csv_path = os.path.join(base_dir, "urban_asset_inventory.csv")
ocr_csv_path = os.path.join(base_dir, "ocr_intelligence.csv")
rel_csv_path = os.path.join(base_dir, "spatial_relationships.csv")
scorecard_csv_path = os.path.join(base_dir, "corridor_intelligence_scorecard.csv")
out_html_path = os.path.join(base_dir, "urban_digital_twin_portal.html")

# Load all core datasets
with open(assets_geojson_path, "r", encoding="utf-8") as f:
    assets_geojson = json.load(f)

with open(roads_geojson_path, "r", encoding="utf-8") as f:
    roads_geojson = json.load(f)

with open(study_area_path, "r", encoding="utf-8") as f:
    boundary_geojson = json.load(f)

df_img = pd.read_csv(images_csv_path)
df_bldg = pd.read_csv(bldg_csv_path)
df_inv = pd.read_csv(inv_csv_path)
df_ocr = pd.read_csv(ocr_csv_path)
df_rel = pd.read_csv(rel_csv_path)
df_scorecard = pd.read_csv(scorecard_csv_path)

# Build Tri-View records
inv_by_img = {}
for img_id, grp in df_inv.groupby("Image_ID"):
    inv_by_img[img_id] = grp.to_dict(orient="records")

ocr_by_img = {}
for img_id, grp in df_ocr.groupby("Image_ID"):
    ocr_by_img[img_id] = grp.to_dict(orient="records")

rel_by_bldg = df_rel.set_index("Building_ID").to_dict(orient="index")
bldg_by_img = df_bldg.set_index("Image_ID").to_dict(orient="index")

tri_records = []
for idx, r in df_img.iterrows():
    img_id = r["Image_ID"]
    st_id = r["Street_ID"]
    bldg = bldg_by_img.get(img_id, {})
    b_id = bldg.get("Building_ID", f"BLDG-{st_id}-001")
    rel = rel_by_bldg.get(b_id, {})
    assets = inv_by_img.get(img_id, [])
    ocr_items = ocr_by_img.get(img_id, [])

    clean_assets = []
    for a in assets:
        a_copy = dict(a)
        if isinstance(a_copy.get("Technical_Specifications"), str):
            try:
                a_copy["Technical_Specifications"] = json.loads(a_copy["Technical_Specifications"])
            except Exception:
                pass
        clean_assets.append(a_copy)

    rec = {
        "index": idx,
        "image_id": img_id,
        "street_id": st_id,
        "street_name": r["Street_Name"],
        "capture_order": int(r["Capture_Order"]),
        "latitude": float(r["Latitude"]),
        "longitude": float(r["Longitude"]),
        "image_path": r["Image_Path"].replace("\\", "/"),
        "annotated_floor_image": bldg.get("Annotated_Floor_Image", "").replace("\\", "/"),
        "building": {
            "building_id": b_id,
            "establishment_name": bldg.get("Establishment_Name", "Urban Property"),
            "building_floors": int(bldg.get("Building_Floors", 2)),
            "floor_notation": bldg.get("Floor_Notation", "G+1"),
            "estimated_height_m": float(bldg.get("Estimated_Height_m", 7.0)),
            "building_usage": bldg.get("Building_Usage", "Commercial"),
            "facade_type": bldg.get("Facade_Type", "Plaster"),
            "ground_floor_activity": bldg.get("Ground_Floor_Activity", "Commercial Retail"),
            "building_density": bldg.get("Building_Density", "Medium Density"),
            "special_features": bldg.get("Special_Features", "Standard commercial amenities"),
            "official_links": bldg.get("Official_Links", f"https://www.google.com/maps?q={r['Latitude']},{r['Longitude']}"),
            "confidence": float(bldg.get("Confidence", 0.9))
        },
        "spatial_relationships": {
            "nearest_pole_id": rel.get("Nearest_Pole_ID", "POLE-001"),
            "nearest_pole_distance_m": float(rel.get("Nearest_Pole_Distance_m", 15.0)),
            "nearest_pole_coord": [float(rel.get("Nearest_Pole_Longitude", r["Longitude"])), float(rel.get("Nearest_Pole_Latitude", r["Latitude"]))],
            "nearest_pole_burden": rel.get("Nearest_Pole_Burden", "Standard Aerial Drop"),
            "nearest_transformer_id": rel.get("Nearest_Transformer_ID", "TRANS-001"),
            "nearest_transformer_distance_m": float(rel.get("Nearest_Transformer_Distance_m", 45.0)),
            "nearest_transformer_coord": [float(rel.get("Nearest_Transformer_Longitude", r["Longitude"])), float(rel.get("Nearest_Transformer_Latitude", r["Latitude"]))],
            "transformer_scope": rel.get("Transformer_Coverage_Scope", "Corridor Substation"),
            "nearest_light_id": rel.get("Nearest_Streetlight_ID", "LIGHT-001"),
            "nearest_light_distance_m": float(rel.get("Nearest_Streetlight_Distance_m", 15.0)),
            "chainage_m": float(rel.get("Corridor_Chainage_m", 0.0)),
            "road_offset_m": float(rel.get("Road_Offset_m", 14.0)),
            "road_side": rel.get("Road_Side", "Right of Roadway"),
            "reference_status": rel.get("Reference_Status", "UNMATCHED"),
            "reference_source": rel.get("Reference_Source", "None (Street View AI Discovery)")
        },
        "fixed_assets": clean_assets,
        "ocr_detections": ocr_items
    }
    tri_records.append(rec)

buildings_list = df_bldg.to_dict(orient="records")
ocr_list = df_ocr.to_dict(orient="records")
assets_list = df_inv.to_dict(orient="records")
for a in assets_list:
    if isinstance(a.get("Technical_Specifications"), str):
        try:
            a["Technical_Specifications"] = json.loads(a["Technical_Specifications"])
        except Exception:
            pass

scorecard_list = df_scorecard.to_dict(orient="records")
rel_list = df_rel.to_dict(orient="records")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Urban Digital Twin Web Portal — FarmwiseAI Task 5</title>
<!-- Leaflet CSS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<style>
  :root {{
    --bg-dark: #05080f;
    --panel-bg: #0b111c;
    --panel-header: #111a2a;
    --panel-border: #1a283e;
    --accent-cyan: #00f2fe;
    --accent-emerald: #00ff88;
    --accent-gold: #ffbe0b;
    --accent-orange: #fb5607;
    --accent-red: #ff0055;
    --accent-magenta: #f72585;
    --text-primary: #e6edf8;
    --text-muted: #8496ad;
    --card-bg: #101928;
    --card-hover: #18253c;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{
    width: 100%;
    height: 100%;
    background-color: var(--bg-dark);
    color: var(--text-primary);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }}
  /* Top Portal Navigation Bar */
  header {{
    background: #090e17;
    border-bottom: 1px solid var(--panel-border);
    padding: 8px 18px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 3000;
  }}
  .brand-group {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .badge-tag {{
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    background: rgba(0, 242, 254, 0.15);
    color: var(--accent-cyan);
    border: 1px solid rgba(0, 242, 254, 0.35);
  }}
  .brand-title {{
    font-size: 16px;
    font-weight: 800;
    color: #fff;
  }}
  .brand-title span {{
    background: linear-gradient(90deg, #00f2fe, #00ff88, #ffbe0b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .nav-tabs {{
    display: flex;
    gap: 4px;
    background: #05080f;
    padding: 3px;
    border-radius: 8px;
    border: 1px solid var(--panel-border);
  }}
  .tab-btn {{
    background: none;
    border: none;
    color: var(--text-muted);
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 5px;
    transition: all 0.2s;
  }}
  .tab-btn:hover {{ color: #fff; background: rgba(255,255,255,0.05); }}
  .tab-btn.active {{
    background: rgba(0, 242, 254, 0.15);
    color: var(--accent-cyan);
    border: 1px solid rgba(0, 242, 254, 0.35);
  }}
  .header-telemetry {{
    display: flex;
    gap: 14px;
    font-size: 11px;
    color: var(--text-muted);
  }}
  .telemetry-item strong {{ color: #fff; }}

  /* Main Workspace Content Area */
  .workspace {{
    flex: 1;
    position: relative;
    overflow: hidden;
  }}
  .view-pane {{
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    display: none;
    flex-direction: column;
    overflow: hidden;
  }}
  .view-pane.active {{ display: flex; }}

  /* TAB 1: TRI-VIEW STUDIO STYLES */
  .triview-container {{
    display: flex;
    flex-direction: column;
    height: 100%;
  }}
  .triview-topbar {{
    background: #0d1422;
    border-bottom: 1px solid var(--panel-border);
    padding: 8px 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .triview-body {{
    flex: 1;
    display: grid;
    grid-template-columns: 38% 32% 30%;
    overflow: hidden;
  }}
  .panel {{
    display: flex;
    flex-direction: column;
    background: var(--panel-bg);
    border-right: 1px solid var(--panel-border);
    overflow: hidden;
    position: relative;
  }}
  .panel:last-child {{ border-right: none; }}
  .panel-header {{
    background: var(--panel-header);
    border-bottom: 1px solid var(--panel-border);
    padding: 8px 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    color: #fff;
  }}
  .visualizer-container {{
    flex: 1;
    position: relative;
    background: #030508;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }}
  .visualizer-img {{
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
  }}
  .layer-toggles {{
    position: absolute;
    top: 10px;
    left: 10px;
    background: rgba(10, 16, 26, 0.88);
    backdrop-filter: blur(8px);
    border: 1px solid var(--panel-border);
    border-radius: 6px;
    padding: 6px 10px;
    font-size: 11px;
    font-weight: 600;
    z-index: 10;
  }}
  .img-hud-bottom {{
    position: absolute;
    bottom: 8px;
    left: 10px;
    right: 10px;
    background: rgba(10, 16, 26, 0.85);
    border: 1px solid var(--panel-border);
    border-radius: 6px;
    padding: 5px 10px;
    font-size: 11px;
    color: #c8d8ec;
    display: flex;
    justify-content: space-between;
    backdrop-filter: blur(6px);
  }}
  #triviewMap {{ width: 100%; height: 100%; background: #090e17; }}
  .inspector-content {{
    flex: 1;
    overflow-y: auto;
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}
  .inspect-card {{
    background: #0f1624;
    border: 1px solid var(--panel-border);
    border-radius: 8px;
    overflow: hidden;
  }}
  .inspect-header {{
    background: #141c2c;
    padding: 7px 12px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--accent-cyan);
    border-bottom: 1px solid var(--panel-border);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .inspect-body {{
    padding: 10px 12px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    font-size: 11px;
  }}
  .info-row {{ display: flex; justify-content: space-between; gap: 8px; }}
  .info-k {{ color: var(--text-muted); }}
  .info-v {{ color: #e4edf8; font-weight: 600; text-align: right; }}
  .filmstrip {{
    height: 56px;
    background: #090d16;
    border-top: 1px solid var(--panel-border);
    display: flex;
    align-items: center;
    padding: 0 12px;
    gap: 6px;
    overflow-x: auto;
    z-index: 1000;
  }}
  .thumb-item {{
    height: 42px;
    width: 72px;
    border-radius: 4px;
    overflow: hidden;
    border: 2px solid #1a273b;
    cursor: pointer;
    flex-shrink: 0;
    position: relative;
  }}
  .thumb-item.active {{
    border-color: var(--accent-cyan);
    box-shadow: 0 0 8px rgba(0, 242, 254, 0.4);
  }}
  .thumb-item img {{ width: 100%; height: 100%; object-fit: cover; }}
  .thumb-label {{
    position: absolute;
    bottom: 1px;
    left: 2px;
    background: rgba(0,0,0,0.7);
    color: #fff;
    font-size: 8px;
    font-weight: 700;
    padding: 1px 2px;
  }}

  /* TAB 2: GIS DIGITAL TWIN FULL MAP */
  #fullGisMap {{ width: 100%; height: 100%; background: #080d16; }}
  .map-overlay-panel {{
    position: absolute;
    top: 16px;
    left: 16px;
    z-index: 1000;
    width: 310px;
    background: rgba(12, 18, 28, 0.92);
    backdrop-filter: blur(10px);
    border: 1px solid var(--panel-border);
    border-radius: 8px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.6);
  }}
  .measure-btn {{
    background: #141f30;
    border: 1px solid #233550;
    color: var(--accent-gold);
    padding: 7px 12px;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 700;
    font-size: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
  }}
  .measure-btn.active {{
    background: rgba(255, 190, 11, 0.2);
    border-color: var(--accent-gold);
  }}

  /* TAB 3: BUILDING CATALOG */
  .catalog-scrollable {{
    flex: 1;
    overflow-y: auto;
    padding: 20px 28px;
  }}
  .catalog-controls {{
    display: flex;
    gap: 12px;
    align-items: center;
    flex-wrap: wrap;
    margin-bottom: 20px;
    background: var(--panel-bg);
    border: 1px solid var(--panel-border);
    padding: 14px 18px;
    border-radius: 8px;
  }}
  .catalog-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 18px;
  }}
  .bldg-card {{
    background: var(--card-bg);
    border: 1px solid var(--panel-border);
    border-radius: 8px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    cursor: pointer;
    transition: transform 0.2s, border-color 0.2s;
  }}
  .bldg-card:hover {{ transform: translateY(-3px); border-color: var(--accent-cyan); }}
  .bldg-thumb-wrap {{
    width: 100%;
    height: 180px;
    position: relative;
    background: #000;
  }}
  .bldg-thumb-wrap img {{ width: 100%; height: 100%; object-fit: cover; }}
  .bldg-card-body {{ padding: 14px; display: flex; flex-direction: column; gap: 6px; flex-grow: 1; }}

  /* TAB 4: OCR SEARCH */
  .ocr-scrollable {{
    flex: 1;
    overflow-y: auto;
    padding: 20px 28px;
  }}
  .ocr-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 16px;
  }}
  .ocr-card {{
    background: var(--card-bg);
    border: 1px solid var(--panel-border);
    border-radius: 8px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}

  /* TAB 5: ASSET PASSPORTS */
  .passports-scrollable {{
    flex: 1;
    overflow-y: auto;
    padding: 20px 28px;
  }}
  .assets-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
  }}
  .assets-table th {{
    background: #0f1624;
    padding: 10px;
    color: var(--accent-cyan);
    text-transform: uppercase;
    font-size: 11px;
    border-bottom: 1px solid var(--panel-border);
    text-align: left;
  }}
  .assets-table td {{
    padding: 10px;
    border-bottom: 1px solid #141f30;
    color: #dbe4f0;
  }}
  .assets-table tr:hover td {{ background: #131c2c; }}

  /* TAB 6: CORRIDOR SCORECARDS */
  .scorecards-scrollable {{
    flex: 1;
    overflow-y: auto;
    padding: 20px 28px;
  }}

  /* TAB 7: EXPORT HUB */
  .export-scrollable {{
    flex: 1;
    overflow-y: auto;
    padding: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }}
  .export-box {{
    max-width: 900px;
    width: 100%;
    background: var(--panel-bg);
    border: 1px solid var(--panel-border);
    border-radius: 12px;
    padding: 28px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }}
  .download-btn {{
    padding: 12px 20px;
    background: #142032;
    border: 1px solid #233752;
    color: #e2ebf6;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.2s;
  }}
  .download-btn:hover {{
    background: rgba(0, 242, 254, 0.15);
    border-color: var(--accent-cyan);
    color: var(--accent-cyan);
  }}

  /* TAB 8: AI COPILOT CHAT PANE */
  .copilot-scrollable {{
    flex: 1;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    max-width: 1100px;
    width: 100%;
    margin: 0 auto;
    padding: 16px 20px;
  }}
  .copilot-pills {{
    display: flex;
    gap: 8px;
    overflow-x: auto;
    padding-bottom: 10px;
  }}
  .cp-pill {{
    background: #0f1624;
    border: 1px solid #1c2b42;
    color: #c4d6ec;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
    cursor: pointer;
    white-space: nowrap;
  }}
  .cp-pill:hover {{
    background: rgba(0, 242, 254, 0.15);
    border-color: var(--accent-cyan);
    color: var(--accent-cyan);
  }}
  .cp-stream {{
    flex: 1;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 14px;
    padding: 10px 0;
  }}
  .cp-bubble {{ display: flex; gap: 12px; max-width: 90%; }}
  .cp-bubble.user {{ align-self: flex-end; flex-direction: row-reverse; }}
  .cp-avatar {{
    width: 32px;
    height: 32px;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    font-weight: 800;
    flex-shrink: 0;
  }}
  .cp-ai {{ background: linear-gradient(135deg, #00f2fe, #00ff88); color: #050a12; }}
  .cp-user {{ background: #1c2a3e; color: #c0d4ec; border: 1px solid #2b405e; }}
  .cp-body {{
    background: #0d1522;
    border: 1px solid var(--panel-border);
    border-radius: 8px;
    padding: 12px 16px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    font-size: 13px;
    line-height: 1.5;
  }}
  .cp-bubble.user .cp-body {{ background: #121c2c; color: #fff; }}
  .cp-input-panel {{
    background: #0b111c;
    border: 1px solid var(--panel-border);
    border-radius: 8px;
    padding: 8px 12px;
    display: flex;
    gap: 10px;
    align-items: center;
    margin-top: 8px;
  }}

  /* Floating Copilot Button */
  .floating-copilot-btn {{
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 4000;
    background: linear-gradient(135deg, #00f2fe, #00ff88);
    color: #040810;
    font-weight: 800;
    font-size: 12px;
    padding: 10px 18px;
    border-radius: 30px;
    box-shadow: 0 6px 24px rgba(0, 242, 254, 0.4);
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: transform 0.2s;
  }}
  .floating-copilot-btn:hover {{ transform: scale(1.06); }}

  /* Modals */
  .modal-backdrop {{
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(4, 7, 13, 0.88);
    backdrop-filter: blur(6px);
    z-index: 9999;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }}
  .modal-backdrop.active {{ display: flex; }}
  .modal-box {{
    background: #0f1624;
    border: 1px solid var(--panel-border);
    border-radius: 12px;
    max-width: 900px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }}
</style>
</head>
<body>

<header>
  <div class="brand-group">
    <span class="badge-tag">FarmwiseAI Task 5 &bull; Team 24</span>
    <div class="brand-title"><span>Urban Digital Twin Platform</span> &bull; Coimbatore Ward 29 (LGD: 29)</div>
  </div>

  <nav class="nav-tabs">
    <button class="tab-btn active" id="tab_triview" onclick="switchTab('triview')">🛰️ Tri-View Studio</button>
    <button class="tab-btn" id="tab_gis" onclick="switchTab('gis')">🗺️ Spatial Map</button>
    <button class="tab-btn" id="tab_buildings" onclick="switchTab('buildings')">🏢 Building Catalog</button>
    <button class="tab-btn" id="tab_ocr" onclick="switchTab('ocr')">🔍 Commercial OCR</button>
    <button class="tab-btn" id="tab_passports" onclick="switchTab('passports')">⚡ Asset Passports</button>
    <button class="tab-btn" id="tab_scorecards" onclick="switchTab('scorecards')">📊 Corridor Scorecards</button>
    <button class="tab-btn" id="tab_copilot" onclick="switchTab('copilot')">💬 AI Copilot</button>
    <button class="tab-btn" id="tab_export" onclick="switchTab('export')">💾 Export Hub</button>
    <a href="municipal_report_portal.html" target="_blank" class="tab-btn" style="text-decoration:none; color:#10b981; border:1px solid rgba(16,185,129,0.35); background:rgba(16,185,129,0.1);">📋 Civic Work Orders &rarr;</a>
    <a href="cloud_architecture_dashboard.html" target="_blank" class="tab-btn" style="text-decoration:none; color:#f59e0b; border:1px solid rgba(245,158,11,0.35); background:rgba(245,158,11,0.1);">☁️ AWS Cloud & Edge &rarr;</a>
    <a href="vlm_routing_visualizer.html" target="_blank" class="tab-btn" style="text-decoration:none; color:#a855f7; border:1px solid rgba(168,85,247,0.35); background:rgba(168,85,247,0.1);">⚡ VLM Router &rarr;</a>
  </nav>

  <div class="header-telemetry">
    <div class="telemetry-item">Assets: <strong>{len(assets_geojson["features"])}</strong></div>
    <div class="telemetry-item">Network: <strong>2.49 km</strong></div>
    <div class="telemetry-item">Matched: <strong>62 (13.3%)</strong></div>
  </div>
</header>

<div class="workspace">
  <!-- TAB 1: TRI-VIEW STUDIO -->
  <div class="view-pane active" id="pane_triview">
    <div class="triview-container">
      <div class="triview-topbar">
        <div style="display:flex; align-items:center; gap:10px;">
          <select id="tvStreetSelect" onchange="tvChangeStreet()" style="background:#090e18; border:1px solid #1a283e; color:#e0ebf8; padding:5px 10px; border-radius:6px; font-size:12px;">
            <option value="ALL">All 10 Surveyed Corridors</option>
            <option value="ST01">ST01 &bull; Sathy Road (NH 948)</option>
            <option value="ST02">ST02 &bull; Sridevi Nagar</option>
            <option value="ST03">ST03 &bull; Ganapathy Pudur</option>
            <option value="ST04">ST04 &bull; Gandhi Nagar</option>
            <option value="ST05">ST05 &bull; Gopalasamy Kovil</option>
            <option value="ST06">ST06 &bull; KRG Nagar</option>
            <option value="ST07">ST07 &bull; PN Palayam</option>
            <option value="ST08">ST08 &bull; Raja Street - Sanganur</option>
            <option value="ST09">ST09 &bull; Sri Ganapathy Gardens</option>
            <option value="ST10">ST10 &bull; Ganapathy - Avarampalayam</option>
          </select>
          <button onclick="tvPrev()" style="background:#141f30; border:1px solid #233550; color:#c0d4ec; padding:4px 10px; border-radius:4px; cursor:pointer; font-weight:700;">&larr; Prev</button>
          <span style="font-size:12px; font-weight:600;">Capture <span id="tvCurrent" style="color:var(--accent-gold); font-family:monospace; font-weight:700;">1</span> / 108</span>
          <button onclick="tvNext()" style="background:#141f30; border:1px solid #233550; color:#c0d4ec; padding:4px 10px; border-radius:4px; cursor:pointer; font-weight:700;">Next &rarr;</button>
        </div>
        <div style="display:flex; gap:8px;">
          <button onclick="alert('Detections Verified & Approved for Cadastre!')" style="padding:4px 10px; background:rgba(0,255,136,0.15); color:var(--accent-emerald); border:1px solid rgba(0,255,136,0.3); border-radius:4px; font-size:11px; font-weight:700; cursor:pointer;">&check; Approve AI</button>
          <button onclick="alert('Escalated to Selective VLM Review!')" style="padding:4px 10px; background:rgba(255,190,11,0.15); color:var(--accent-gold); border:1px solid rgba(255,190,11,0.3); border-radius:4px; font-size:11px; font-weight:700; cursor:pointer;">&Delta; Escalate VLM</button>
        </div>
      </div>

      <div class="triview-body">
        <div class="panel">
          <div class="panel-header">
            <span>1. Street View Perception HUD</span>
            <span id="tvImgTag" style="font-size:10px; background:#19273c; padding:2px 6px; border-radius:4px; color:var(--accent-cyan);">IMG-ST01-001</span>
          </div>
          <div class="visualizer-container">
            <img id="tvImage" class="visualizer-img" src="" alt="Street View">
            <div class="layer-toggles">
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
                <input type="checkbox" id="tvChkBlueprint" checked onchange="tvRender()">
                <span>Floor Bands & Height Blueprint</span>
              </label>
            </div>
            <div class="img-hud-bottom">
              <span id="tvHudStreet">Sathy Road (NH 948)</span>
              <span id="tvHudGPS">11.035355°N, 76.973424°E</span>
            </div>
          </div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span>2. Synchronized Digital Twin Map</span>
            <span style="font-size:10px; color:var(--accent-emerald); font-weight:700;">LIVE SYNC</span>
          </div>
          <div id="triviewMap"></div>
        </div>

        <div class="panel">
          <div class="panel-header">
            <span>3. Urban Asset Passport Inspector</span>
            <span id="tvPassportTag" style="font-size:10px; color:var(--accent-cyan); font-weight:700;">BLDG-ST01-001</span>
          </div>
          <div class="inspector-content">
            <div class="inspect-card">
              <div class="inspect-header">
                <span>Building Envelope</span>
                <span id="tvFloorsBadge" style="color:var(--accent-emerald);">G+3 &bull; 14.0m</span>
              </div>
              <div class="inspect-body">
                <div id="tvBldgName" style="font-size:14px; font-weight:700; color:#fff;">Hotel Anandha Residency</div>
                <div class="info-row"><span class="info-k">Usage:</span><span class="info-v" id="tvUsage">Commercial Hotel</span></div>
                <div class="info-row"><span class="info-k">Facade:</span><span class="info-v" id="tvFacade">Glass Curtain Wall</span></div>
                <div class="info-row"><span class="info-k">Ground Floor:</span><span class="info-v" id="tvGround">Hotel Lobby & Dining</span></div>
                <div style="margin-top:4px;"><a id="tvMapLink" href="" target="_blank" style="color:var(--accent-cyan); font-weight:700; text-decoration:underline;">Open Google Maps Place &rarr;</a></div>
              </div>
            </div>

            <div class="inspect-card">
              <div class="inspect-header">
                <span>Spatial Graph Topology</span>
                <span style="color:var(--accent-gold);">Nearest Vectors</span>
              </div>
              <div class="inspect-body">
                <div class="info-row"><span class="info-k">Nearest Pole:</span><span class="info-v" id="tvPole">POLE-ST01-001 (18.9m)</span></div>
                <div class="info-row"><span class="info-k">Nearest Transformer:</span><span class="info-v" id="tvTrans">TRANS-ST01-003 (67.8m)</span></div>
                <div class="info-row"><span class="info-k">Nearest Streetlight:</span><span class="info-v" id="tvLight">LIGHT-ST01-001 (18.6m)</span></div>
                <div class="info-row"><span class="info-k">Road Chainage & Offset:</span><span class="info-v" id="tvOffset">0.0m / +14.8m (Right)</span></div>
              </div>
            </div>

            <div class="inspect-card">
              <div class="inspect-header">
                <span>Commercial OCR Signage</span>
                <span id="tvOcrCount" style="color:var(--accent-cyan);">1 Detected</span>
              </div>
              <div class="inspect-body">
                <div class="info-row"><span class="info-k">Text:</span><span class="info-v" id="tvOcrText">Hotel Anandha Residency</span></div>
                <div class="info-row"><span class="info-k">Sector:</span><span class="info-v" id="tvOcrSector">Dining & Hospitality</span></div>
              </div>
            </div>

            <div class="inspect-card">
              <div class="inspect-header">
                <span>Municipal Cadastre Baseline</span>
                <span id="tvRefBadge" class="badge-tag" style="background:rgba(0,255,136,0.15); color:#00ff88;">MATCHED</span>
              </div>
              <div class="inspect-body">
                <div class="info-row"><span class="info-k">Source:</span><span class="info-v" id="tvRefSource">OpenStreetMap Cadastre</span></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="filmstrip" id="tvFilmstrip"></div>
    </div>
  </div>

  <!-- TAB 2: FULL GIS DIGITAL TWIN MAP -->
  <div class="view-pane" id="pane_gis">
    <div id="fullGisMap"></div>
    <div class="map-overlay-panel">
      <div style="font-size:12px; font-weight:700; color:#fff; text-transform:uppercase; letter-spacing:0.5px;">Spatial Map Controls</div>
      
      <button class="measure-btn" id="btnMeasure" onclick="toggleMeasureTool()">
        <svg width="14" height="14" fill="currentColor" viewBox="0 0 16 16"><path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm2-1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H2z"/></svg>
        <span id="measureBtnText">Measure Road Setback / Distance</span>
      </button>
      <div id="measureOutput" style="font-size:11px; color:var(--accent-gold); display:none; padding:4px 8px; background:#080c14; border-radius:4px; text-align:center;">Click 2 points on map</div>

      <div style="font-size:11px; font-weight:700; color:var(--text-muted); text-transform:uppercase; margin-top:4px;">Layer Toggles</div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; font-size:11px;">
        <label style="display:flex; align-items:center; gap:6px; cursor:pointer;"><input type="checkbox" checked id="gChk_building" onchange="gisApplyFilters()"><span style="color:#00ff88;">Buildings (108)</span></label>
        <label style="display:flex; align-items:center; gap:6px; cursor:pointer;"><input type="checkbox" checked id="gChk_electric_pole" onchange="gisApplyFilters()"><span style="color:#fb5607;">Poles (108)</span></label>
        <label style="display:flex; align-items:center; gap:6px; cursor:pointer;"><input type="checkbox" checked id="gChk_streetlight" onchange="gisApplyFilters()"><span style="color:#ffbe0b;">Lights (108)</span></label>
        <label style="display:flex; align-items:center; gap:6px; cursor:pointer;"><input type="checkbox" checked id="gChk_transformer" onchange="gisApplyFilters()"><span style="color:#ff0055;">Transformers (24)</span></label>
        <label style="display:flex; align-items:center; gap:6px; cursor:pointer;"><input type="checkbox" checked id="gChk_traffic_signal" onchange="gisApplyFilters()"><span style="color:#f72585;">Signals (9)</span></label>
        <label style="display:flex; align-items:center; gap:6px; cursor:pointer;"><input type="checkbox" checked id="gChk_commercial_sign" onchange="gisApplyFilters()"><span style="color:#00f2fe;">Signs (108)</span></label>
      </div>

      <div style="font-size:11px; font-weight:700; color:var(--text-muted); text-transform:uppercase; margin-top:4px;">Reference Filter</div>
      <div style="display:flex; gap:6px;">
        <button id="gRefAll" onclick="gisSetRef('ALL')" style="flex:1; padding:4px; font-size:10px; font-weight:700; background:rgba(0,242,254,0.2); border:1px solid var(--accent-cyan); color:var(--accent-cyan); border-radius:4px; cursor:pointer;">All</button>
        <button id="gRefMatch" onclick="gisSetRef('MATCHED')" style="flex:1; padding:4px; font-size:10px; font-weight:700; background:#080d16; border:1px solid #1a283e; color:#c0d0e4; border-radius:4px; cursor:pointer;">Matched (62)</button>
        <button id="gRefUnmatch" onclick="gisSetRef('UNMATCHED')" style="flex:1; padding:4px; font-size:10px; font-weight:700; background:#080d16; border:1px solid #1a283e; color:#c0d0e4; border-radius:4px; cursor:pointer;">New (403)</button>
      </div>
    </div>
  </div>

  <!-- TAB 3: BUILDING CATALOG -->
  <div class="view-pane" id="pane_buildings">
    <div class="catalog-scrollable">
      <div class="catalog-controls">
        <input type="text" id="bldgSearchInput" oninput="filterBuildings()" placeholder="Search building name, ID, business..." style="background:#090e18; border:1px solid #1c2a3e; color:#fff; padding:8px 12px; border-radius:6px; font-size:12px; min-width:220px;">
        <select id="bldgFloorFilter" onchange="filterBuildings()" style="background:#090e18; border:1px solid #1c2a3e; color:#fff; padding:8px 12px; border-radius:6px; font-size:12px;">
          <option value="ALL">All Floor Heights</option>
          <option value="G">G (Ground Only &bull; 3.5m)</option>
          <option value="G+1">G+1 (2 Floors &bull; 7.0m)</option>
          <option value="G+2">G+2 (3 Floors &bull; 10.5m)</option>
          <option value="G+3">G+3 (4 Floors &bull; 14.0m)</option>
          <option value="G+4">G+4 (5 Floors &bull; 17.5m)</option>
        </select>
        <select id="bldgStreetFilter" onchange="filterBuildings()" style="background:#090e18; border:1px solid #1c2a3e; color:#fff; padding:8px 12px; border-radius:6px; font-size:12px;">
          <option value="ALL">All 10 Corridors</option>
          <option value="ST01">ST01 &bull; Sathy Road</option>
          <option value="ST02">ST02 &bull; Sridevi Nagar</option>
          <option value="ST03">ST03 &bull; Ganapathy Pudur</option>
          <option value="ST04">ST04 &bull; Gandhi Nagar</option>
          <option value="ST05">ST05 &bull; Gopalasamy Kovil</option>
          <option value="ST06">ST06 &bull; KRG Nagar</option>
          <option value="ST07">ST07 &bull; PN Palayam</option>
          <option value="ST08">ST08 &bull; Raja Street</option>
          <option value="ST09">ST09 &bull; Ganapathy Gardens</option>
          <option value="ST10">ST10 &bull; Avarampalayam</option>
        </select>
        <span style="margin-left:auto; font-size:12px; color:var(--text-muted);">Showing <strong id="bldgCount" style="color:#fff;">{len(buildings_list)}</strong> buildings</span>
      </div>

      <div class="catalog-grid" id="catalogGrid">
        {"".join([f'''
        <div class="bldg-card" onclick="openBldgModal('{b["Building_ID"]}')">
          <div class="bldg-thumb-wrap">
            <img src="{b["Annotated_Floor_Image"].replace('\\', '/')}" alt="{b["Building_ID"]}" loading="lazy">
            <span style="position:absolute; top:8px; left:8px; background:rgba(0,0,0,0.8); border:1px solid var(--accent-cyan); color:var(--accent-cyan); font-size:11px; font-weight:700; padding:2px 6px; border-radius:4px; font-family:monospace;">{b["Building_ID"]}</span>
            <span style="position:absolute; top:8px; right:8px; background:var(--accent-emerald); color:#041008; font-size:11px; font-weight:800; padding:2px 6px; border-radius:4px;">{b["Floor_Notation"]} &bull; {b["Estimated_Height_m"]}m</span>
          </div>
          <div class="bldg-card-body">
            <div style="font-size:15px; font-weight:700; color:#fff;">{b["Establishment_Name"]}</div>
            <div style="font-size:11px; color:var(--text-muted);">{b["Street_Name"]}</div>
            <div style="display:flex; gap:6px; margin-top:4px;">
              <span style="font-size:10px; padding:2px 6px; border-radius:3px; background:#19273c; color:#adc4e2;">{b["Building_Usage"].split("&")[0].strip()}</span>
              <span style="font-size:10px; padding:2px 6px; border-radius:3px; background:rgba(255,190,11,0.15); color:var(--accent-gold);">{b["Facade_Type"].split("&")[0].strip()}</span>
            </div>
            <div style="margin-top:auto; padding-top:8px; border-top:1px solid #1a283e; display:flex; justify-content:space-between; align-items:center;">
              <a href="{b["Official_Links"]}" target="_blank" onclick="event.stopPropagation()" style="font-size:11px; color:var(--accent-cyan); text-decoration:none; font-weight:700;">Google Maps &rarr;</a>
              <span style="font-size:10px; color:var(--text-muted); font-weight:600;">Inspect Blueprint</span>
            </div>
          </div>
        </div>
        ''' for b in buildings_list])}
      </div>
    </div>
  </div>

  <!-- TAB 4: OCR COMMERCIAL SEARCH -->
  <div class="view-pane" id="pane_ocr">
    <div class="ocr-scrollable">
      <div class="catalog-controls">
        <input type="text" id="ocrSearchInput" oninput="filterOcr()" placeholder="Search sign text, brand, pharmacy, hotel..." style="background:#090e18; border:1px solid #1c2a3e; color:#fff; padding:8px 12px; border-radius:6px; font-size:12px; min-width:240px;">
        <select id="ocrSectorFilter" onchange="filterOcr()" style="background:#090e18; border:1px solid #1c2a3e; color:#fff; padding:8px 12px; border-radius:6px; font-size:12px;">
          <option value="ALL">All 11 Sectors</option>
          <option value="Retail">Retail & General Commerce</option>
          <option value="Dining">Dining & Hospitality</option>
          <option value="Financial">Financial & Banking</option>
          <option value="Healthcare">Healthcare & Pharmacy</option>
          <option value="Hardware">Hardware & Materials</option>
          <option value="Automotive">Automotive & Mobility</option>
        </select>
        <span style="margin-left:auto; font-size:12px; color:var(--text-muted);">Found <strong id="ocrCount" style="color:#fff;">{len(ocr_list)}</strong> signboards</span>
      </div>

      <div class="ocr-grid" id="ocrGrid">
        {"".join([f'''
        <div class="ocr-card">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-family:monospace; font-size:11px; color:var(--accent-cyan); font-weight:700;">{o["OCR_ID"]}</span>
            <span style="font-size:10px; background:rgba(0,242,254,0.15); color:var(--accent-cyan); padding:2px 6px; border-radius:4px; font-weight:700;">{(o["Confidence"]*100):.1f}% Conf</span>
          </div>
          <div style="font-size:14px; font-weight:700; color:#fff; margin-top:2px;">"{o["Cleaned_Text"]}"</div>
          <div style="font-size:11px; color:var(--accent-gold); font-weight:600;">{o["Commercial_Category"]}</div>
          <div style="font-size:11px; color:var(--text-muted);">{o["Street_Name"]} &bull; {o["Associated_Building_ID"]}</div>
        </div>
        ''' for o in ocr_list])}
      </div>
    </div>
  </div>

  <!-- TAB 5: ASSET PASSPORTS -->
  <div class="view-pane" id="pane_passports">
    <div class="passports-scrollable">
      <div class="catalog-controls">
        <input type="text" id="passSearch" oninput="filterPassports()" placeholder="Filter by Asset ID, Subtype, Authority..." style="background:#090e18; border:1px solid #1c2a3e; color:#fff; padding:8px 12px; border-radius:6px; font-size:12px; min-width:240px;">
        <select id="passClassFilter" onchange="filterPassports()" style="background:#090e18; border:1px solid #1c2a3e; color:#fff; padding:8px 12px; border-radius:6px; font-size:12px;">
          <option value="ALL">All Asset Classes (465)</option>
          <option value="electric_pole">Electric Utility Poles (108)</option>
          <option value="streetlight">Streetlight Luminaires (108)</option>
          <option value="transformer">Distribution Transformers (24)</option>
          <option value="traffic_signal">Traffic Signals (9)</option>
          <option value="commercial_sign">Commercial Signs (108)</option>
          <option value="building">Building Envelopes (108)</option>
        </select>
        <span style="margin-left:auto; font-size:12px; color:var(--text-muted);">Showing <strong id="passCount" style="color:#fff;">{len(assets_list)}</strong> assets</span>
      </div>

      <table class="assets-table" id="passportsTable">
        <thead>
          <tr>
            <th>Asset Passport ID</th>
            <th>Asset Subtype</th>
            <th>Corridor</th>
            <th>Condition</th>
            <th>Managing Authority</th>
            <th>Lifespan</th>
            <th>GPS Pin</th>
          </tr>
        </thead>
        <tbody>
          {"".join([f'''
          <tr>
            <td><strong style="color:var(--accent-cyan); font-family:monospace;">{a["Asset_ID"]}</strong></td>
            <td>{a["Asset_Subtype"]}</td>
            <td>{a["Street_Name"]}</td>
            <td><span style="color:{'#ff0055' if 'High' in str(a['Maintenance_Priority']) else ('#ffbe0b' if 'Medium' in str(a['Maintenance_Priority']) else '#00ff88')}; font-weight:700;">{str(a["Physical_Condition"]).split('/')[0].strip()}</span></td>
            <td>{str(a["Managing_Authority"]).split('(')[0].strip()}</td>
            <td>{a["Estimated_Lifespan_Years"]} yrs</td>
            <td><a href="https://www.google.com/maps?q={a['Latitude']},{a['Longitude']}" target="_blank" style="color:var(--accent-cyan); text-decoration:none; font-weight:700;">Pin &rarr;</a></td>
          </tr>
          ''' for a in assets_list])}
        </tbody>
      </table>
    </div>
  </div>

  <!-- TAB 6: CORRIDOR SCORECARDS -->
  <div class="view-pane" id="pane_scorecards">
    <div class="scorecards-scrollable">
      <div style="font-size:18px; font-weight:800; color:#fff; margin-bottom:16px;">
        Corridor Comparative Infrastructure Diagnostics & Municipal Health (10 Surveyed Corridors)
      </div>
      <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(360px, 1fr)); gap:18px;">
        {"".join([f'''
        <div style="background:var(--card-bg); border:1px solid var(--panel-border); border-radius:8px; padding:16px; display:flex; flex-direction:column; gap:10px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-family:monospace; font-size:13px; font-weight:700; color:var(--accent-cyan);">{s["Street_ID"]} &bull; {s["Corridor_Tier"]}</span>
            <span style="font-size:13px; font-weight:900; padding:2px 8px; border-radius:4px; background:{'rgba(0,255,136,0.2)' if 'A' in s['Municipal_Readiness_Grade'] else ('rgba(255,190,11,0.2)' if 'B' in s['Municipal_Readiness_Grade'] else 'rgba(255,0,85,0.2)')}; color:{'#00ff88' if 'A' in s['Municipal_Readiness_Grade'] else ('#ffbe0b' if 'B' in s['Municipal_Readiness_Grade'] else '#ff0055')};">Grade {s["Municipal_Readiness_Grade"]}</span>
          </div>
          <div style="font-size:15px; font-weight:700; color:#fff;">{s["Street_Name"]}</div>
          <div style="font-size:11px; color:var(--accent-gold);">{s["Urban_Archetype"]}</div>
          
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; background:#080c14; padding:8px 10px; border-radius:6px; font-size:11px;">
            <div><span style="color:var(--text-muted); font-size:10px;">DENSITY:</span> <strong>{s["Asset_Density_per_km"]:.1f}/km</strong></div>
            <div><span style="color:var(--text-muted); font-size:10px;">SPACING:</span> <strong>{s["Average_Luminaire_Spacing_m"]:.1f}m</strong></div>
            <div><span style="color:var(--text-muted); font-size:10px;">CABLE BURDEN:</span> <strong style="color:{'#ff0055' if s['Cable_Burden_Index']>=80 else '#00ff88'};">{s["Cable_Burden_Index"]:.0f}/100</strong></div>
            <div><span style="color:var(--text-muted); font-size:10px;">LIGHTING:</span> <strong style="color:{'#00ff88' if s['Street_Lighting_Adequacy_Score']>=80 else '#ff0055'};">{s["Street_Lighting_Adequacy_Score"]:.0f}/100</strong></div>
          </div>

          <div style="background:#090f1a; border-left:3px solid var(--accent-cyan); padding:8px 10px; border-radius:4px; font-size:11px;">
            <div style="color:var(--accent-cyan); font-weight:700; font-size:10px; text-transform:uppercase;">Municipal Action Plan</div>
            <div style="color:#d8e5f6; margin-top:2px;">{s["Actionable_Work_Order"]}</div>
            <div style="color:var(--text-muted); font-size:10px; margin-top:3px;">Agency: {s["Responsible_Civic_Agency"]}</div>
          </div>
        </div>
        ''' for s in scorecard_list])}
      </div>
    </div>
  </div>

  <!-- TAB 8: AI URBAN COPILOT CHAT PANE -->
  <div class="view-pane" id="pane_copilot">
    <div class="copilot-scrollable">
      <div class="copilot-pills">
        <button class="cp-pill" onclick="cpSendPrompt('Which corridor has the highest electrical burden and transformer capacity?')">⚡ Highest Electrical Load</button>
        <button class="cp-pill" onclick="cpSendPrompt('Show all utility poles requiring urgent cable decluttering and delacing')">🚨 Poles Requiring Decluttering</button>
        <button class="cp-pill" onclick="cpSendPrompt('List all commercial buildings with 4 or more floors')">🏢 Tall Buildings (G+3 & G+4)</button>
        <button class="cp-pill" onclick="cpSendPrompt('What is the streetlight spacing on Avarampalayam Road and what is the municipal recommendation?')">💡 Streetlight Spacing Hazard</button>
        <button class="cp-pill" onclick="cpSendPrompt('What is the nearest transformer to Hotel Anandha Residency and how far is it?')">📍 Nearest Transformer Topology</button>
        <button class="cp-pill" onclick="cpSendPrompt('Find all healthcare clinics and pharmacies in the study area')">🏥 Healthcare & Clinics</button>
      </div>

      <div class="cp-stream" id="cpStream">
        <div class="cp-bubble">
          <div class="cp-avatar cp-ai">AI</div>
          <div class="cp-body">
            <div style="font-size:15px; font-weight:700; color:#fff;">Welcome to the AI Urban Intelligence Copilot! 👋</div>
            <div>
              Ask natural language questions about Coimbatore Ward 29's <strong>465 assets</strong>, building floor heights, transformer substation loads, or streetlight hazards.
            </div>
          </div>
        </div>
      </div>

      <div class="cp-input-panel">
        <input type="text" id="cpInput" class="query-input" placeholder="Type your municipal question (e.g. Which corridor has highest load?)..." onkeydown="if(event.key==='Enter') cpSubmitQuery()">
        <button class="send-btn" onclick="cpSubmitQuery()">Send Query &rarr;</button>
      </div>
    </div>
  </div>

  <!-- TAB 7: EXPORT HUB -->
  <div class="view-pane" id="pane_export">
    <div class="export-scrollable">
      <div class="export-box">
        <div>
          <span class="badge-tag">One-Click Client Export Hub</span>
          <h2 style="font-size:22px; font-weight:800; color:#fff; margin-top:4px;">Municipal GIS & Intelligence Exports</h2>
          <p style="color:var(--text-muted); font-size:13px; margin-top:4px;">Instant client-side download of certified municipal GIS layers, digital twin passports, and diagnostic scorecards for Coimbatore Ward 29.</p>
        </div>

        <div style="display:flex; flex-direction:column; gap:12px;">
          <button class="download-btn" onclick="downloadJSON(ASSETS_GEOJSON, 'fai-tce-team24-urban-assets.geojson')">
            <div>
              <div style="font-weight:700;">Urban Assets Digital Twin GeoJSON</div>
              <div style="font-size:11px; color:var(--text-muted);">465 point features with passports, nearest neighbors, and reference match status</div>
            </div>
            <span>Download .geojson &darr;</span>
          </button>

          <button class="download-btn" onclick="downloadJSON(ROADS_GEOJSON, 'fai-tce-team24-road-network.geojson')">
            <div>
              <div style="font-weight:700;">Road Network Topology GeoJSON</div>
              <div style="font-size:11px; color:var(--text-muted);">10 surveyed road centerlines with stationing, lengths, and asset densities</div>
            </div>
            <span>Download .geojson &darr;</span>
          </button>

          <button class="download-btn" onclick="downloadJSON(BOUNDARY_GEOJSON, 'fai-tce-team24-ward29-boundary.geojson')">
            <div>
              <div style="font-weight:700;">Ward 29 Municipal Boundary GeoJSON</div>
              <div style="font-size:11px; color:var(--text-muted);">Official Corporation boundary polygon for Coimbatore Ward 29 North Zone</div>
            </div>
            <span>Download .geojson &darr;</span>
          </button>

          <button class="download-btn" onclick="downloadCSV(BUILDINGS_DATA, 'fai-tce-team24-building-intelligence.csv')">
            <div>
              <div style="font-weight:700;">Building & Property Intelligence CSV</div>
              <div style="font-size:11px; color:var(--text-muted);">108 cataloged buildings with floors (G to G+4), heights, usages, and Google Maps links</div>
            </div>
            <span>Download .csv &darr;</span>
          </button>

          <button class="download-btn" onclick="downloadCSV(SCORECARDS_DATA, 'fai-tce-team24-corridor-scorecards.csv')">
            <div>
              <div style="font-weight:700;">Corridor Diagnostics Scorecard CSV</div>
              <div style="font-size:11px; color:var(--text-muted);">Comparative density analytics, Cable Burden vs Lighting Adequacy, and municipal work orders</div>
            </div>
            <span>Download .csv &darr;</span>
          </button>

          <a href="municipal_reports/tangedco_feeder_work_orders.csv" download class="download-btn" style="text-decoration:none; color:inherit;">
            <div>
              <div style="font-weight:700; color:#fb7185;">⚡ TANGEDCO Feeder Work Orders CSV</div>
              <div style="font-size:11px; color:var(--text-muted);">108 utility poles audited, 73 priority delacing & ABC cable conversion work orders</div>
            </div>
            <span style="color:#fb7185;">Download .csv &darr;</span>
          </a>

          <a href="municipal_reports/ccmc_streetlight_infill_directives.csv" download class="download-btn" style="text-decoration:none; color:inherit;">
            <div>
              <div style="font-weight:700; color:#fde68a;">💡 CCMC Streetlight Infill Directives CSV</div>
              <div style="font-size:11px; color:var(--text-muted);">IRC:SP:72 compliance directives, dark-spot locations, and 18 proposed infill luminaires</div>
            </div>
            <span style="color:#fde68a;">Download .csv &darr;</span>
          </a>

          <a href="municipal_reports/ccmc_commercial_tax_ledger.csv" download class="download-btn" style="text-decoration:none; color:inherit;">
            <div>
              <div style="font-weight:700; color:#34d399;">🏢 CCMC Commercial Property Tax & Signboard Ledger CSV</div>
              <div style="font-size:11px; color:var(--text-muted);">201 OCR-verified commercial signboards, building floor counts, and ₹20.40 L revenue potential</div>
            </div>
            <span style="color:#34d399;">Download .csv &darr;</span>
          </a>

          <a href="municipal_report_portal.html" target="_blank" class="download-btn" style="text-decoration:none; color:inherit; background:rgba(6,182,212,0.12); border-color:rgba(6,182,212,0.4);">
            <div>
              <div style="font-weight:700; color:var(--accent-cyan);">📑 Open Interactive Municipal Work Order & Reporting Portal</div>
              <div style="font-size:11px; color:var(--text-muted);">Dedicated civic portal with search, priority filtering, and print-ready official report generation</div>
            </div>
            <span style="color:var(--accent-cyan);">Launch Portal &rarr;</span>
          </a>

          <a href="cloud_architecture_dashboard.html" target="_blank" class="download-btn" style="text-decoration:none; color:inherit; background:rgba(245,158,11,0.12); border-color:rgba(245,158,11,0.4);">
            <div>
              <div style="font-weight:700; color:#f59e0b;">☁️ Open AWS Serverless Cloud & Edge Architecture Dashboard</div>
              <div style="font-size:11px; color:var(--text-muted);">Interactive topology, live API testbench (/detect, /query, /work-orders), edge telemetry stream, and cost calculator</div>
            </div>
            <span style="color:#f59e0b;">Launch AWS Dashboard &rarr;</span>
          </a>

          <a href="vlm_routing_visualizer.html" target="_blank" class="download-btn" style="text-decoration:none; color:inherit; background:rgba(168,85,247,0.12); border-color:rgba(168,85,247,0.4);">
            <div>
              <div style="font-weight:700; color:#a855f7;">⚡ Open Small-Model First Routing & VLM Escalation Studio</div>
              <div style="font-size:11px; color:var(--text-muted);">Interactive two-tier decision simulator, 774-item routing ledger, latency-accuracy tradeoffs, and 74.9% cost reduction metrics</div>
            </div>
            <span style="color:#a855f7;">Launch VLM Router &rarr;</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Floating Copilot Button -->
<div class="floating-copilot-btn" onclick="switchTab('copilot')">
  <span>💬</span> AI Copilot
</div>

<!-- Building Blueprint Modal -->
<div class="modal-backdrop" id="bldgModal">
  <div class="modal-box">
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--panel-border); padding-bottom:10px;">
      <div>
        <span class="badge-tag" id="mBldgId">BLDG-ST01-001</span>
        <h3 id="mBldgTitle" style="font-size:18px; color:#fff; margin-top:4px;">Building Title</h3>
      </div>
      <button onclick="closeBldgModal()" style="background:none; border:none; color:var(--text-muted); font-size:24px; cursor:pointer;">&times;</button>
    </div>
    <div style="display:flex; gap:16px;">
      <div style="flex:1; max-height:360px; background:#000; border-radius:6px; overflow:hidden; display:flex; align-items:center; justify-content:center;">
        <img id="mBldgImg" src="" style="max-width:100%; max-height:360px; object-fit:contain;">
      </div>
      <div style="flex:1; display:flex; flex-direction:column; gap:8px; font-size:12px;" id="mBldgParams">
      </div>
    </div>
  </div>
</div>

<!-- Leaflet JS -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
const TRI_RECORDS = {json.dumps(tri_records, ensure_ascii=False)};
const ASSETS_GEOJSON = {json.dumps(assets_geojson, ensure_ascii=False)};
const ROADS_GEOJSON = {json.dumps(roads_geojson, ensure_ascii=False)};
const BOUNDARY_GEOJSON = {json.dumps(boundary_geojson, ensure_ascii=False)};
const BUILDINGS_DATA = {json.dumps(buildings_list, ensure_ascii=False)};
const OCR_DATA = {json.dumps(ocr_list, ensure_ascii=False)};
const SCORECARDS_DATA = {json.dumps(scorecard_list, ensure_ascii=False)};
const RELATIONS_DATA = {json.dumps(rel_list, ensure_ascii=False)};

// 1. Tab Switching
function switchTab(tabId) {{
  document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
  document.querySelectorAll(".view-pane").forEach(p => p.classList.remove("active"));
  
  const btn = document.getElementById(`tab_${{tabId}}`);
  if (btn) btn.classList.add("active");

  const targetPane = document.getElementById(`pane_${{tabId}}`);
  if (targetPane) targetPane.classList.add("active");

  if (tabId === "triview") {{
    setTimeout(() => tvMap.invalidateSize(), 200);
  }} else if (tabId === "gis") {{
    setTimeout(() => fullMap.invalidateSize(), 200);
  }}
}}

// 2. TRI-VIEW STUDIO ENGINE
let tvCurrentIdx = 0;
let tvMap, tvCameraMarker, tvSpiderLines = [];

function initTvMap() {{
  tvMap = L.map("triviewMap", {{ zoomControl: true, attributionControl: false }}).setView([11.0345, 76.9745], 16);
  L.tileLayer("https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png", {{ maxZoom: 20, subdomains: "abcd" }}).addTo(tvMap);
  
  L.geoJSON(BOUNDARY_GEOJSON, {{ style: {{ color: "#00f2fe", weight: 2, dashArray: "4, 4", fillColor: "#00f2fe", fillOpacity: 0.03 }} }}).addTo(tvMap);
  L.geoJSON(ROADS_GEOJSON, {{ style: {{ color: "#00f2fe", weight: 3, opacity: 0.8 }} }}).addTo(tvMap);

  ASSETS_GEOJSON.features.forEach(f => {{
    const color = f.properties.asset_class === "building" ? "#00ff88" : (f.properties.asset_class === "transformer" ? "#ff0055" : "#ffbe0b");
    const m = L.circleMarker([f.geometry.coordinates[1], f.geometry.coordinates[0]], {{
      radius: f.properties.asset_class === "building" ? 6 : 4,
      fillColor: color,
      color: "#05080f",
      weight: 1,
      fillOpacity: 0.85
    }}).addTo(tvMap);
  }});
}}

function tvRender() {{
  const r = TRI_RECORDS[tvCurrentIdx];
  if (!r) return;

  document.getElementById("tvCurrent").innerText = tvCurrentIdx + 1;
  document.getElementById("tvImgTag").innerText = r.image_id;
  document.getElementById("tvPassportTag").innerText = r.building.building_id;

  const useBp = document.getElementById("tvChkBlueprint").checked;
  document.getElementById("tvImage").src = useBp ? r.annotated_floor_image : r.image_path;
  document.getElementById("tvHudStreet").innerText = `${{r.street_name}} (${{r.street_id}})`;
  document.getElementById("tvHudGPS").innerText = `${{r.latitude.toFixed(6)}}°N, ${{r.longitude.toFixed(6)}}°E &bull; #${{r.capture_order}}`;

  // Map Camera Marker
  if (tvCameraMarker) tvMap.removeLayer(tvCameraMarker);
  tvCameraMarker = L.circleMarker([r.latitude, r.longitude], {{
    radius: 8,
    fillColor: "#00f2fe",
    color: "#fff",
    weight: 2,
    fillOpacity: 1
  }}).addTo(tvMap);

  // Spider Lines
  tvSpiderLines.forEach(l => tvMap.removeLayer(l));
  tvSpiderLines = [];

  const bCoords = [r.latitude, r.longitude];
  const sp = r.spatial_relationships;
  if (sp.nearest_pole_coord) {{
    tvSpiderLines.push(L.polyline([bCoords, [sp.nearest_pole_coord[1], sp.nearest_pole_coord[0]]], {{ color: "#ffbe0b", weight: 2.5, dashArray: "4, 4" }}).addTo(tvMap));
  }}
  if (sp.nearest_transformer_coord) {{
    tvSpiderLines.push(L.polyline([bCoords, [sp.nearest_transformer_coord[1], sp.nearest_transformer_coord[0]]], {{ color: "#ff0055", weight: 2.5, dashArray: "4, 6" }}).addTo(tvMap));
  }}

  tvMap.panTo([r.latitude, r.longitude], {{ animate: true, duration: 0.5 }});

  // Inspector
  const b = r.building;
  document.getElementById("tvFloorsBadge").innerText = `${{b.floor_notation}} &bull; ${{b.estimated_height_m}}m`;
  document.getElementById("tvBldgName").innerText = b.establishment_name;
  document.getElementById("tvUsage").innerText = b.building_usage;
  document.getElementById("tvFacade").innerText = b.facade_type;
  document.getElementById("tvGround").innerText = b.ground_floor_activity;
  document.getElementById("tvMapLink").href = b.official_links;

  document.getElementById("tvPole").innerText = `${{sp.nearest_pole_id}} (${{sp.nearest_pole_distance_m}}m)`;
  document.getElementById("tvTrans").innerText = `${{sp.nearest_transformer_id}} (${{sp.nearest_transformer_distance_m}}m)`;
  document.getElementById("tvLight").innerText = `${{sp.nearest_light_id}} (${{sp.nearest_light_distance_m}}m)`;
  document.getElementById("tvOffset").innerText = `${{sp.chainage_m}}m / ${{sp.road_offset_m}}m (${{sp.road_side}})`;

  if (r.ocr_detections && r.ocr_detections.length > 0) {{
    document.getElementById("tvOcrCount").innerText = `${{r.ocr_detections.length}} Detected`;
    document.getElementById("tvOcrText").innerText = r.ocr_detections.map(o => o.Cleaned_Text).join(" | ");
    document.getElementById("tvOcrSector").innerText = r.ocr_detections[0].Commercial_Category || "Retail";
  }} else {{
    document.getElementById("tvOcrCount").innerText = "0 Detected";
    document.getElementById("tvOcrText").innerText = "No signboards detected";
    document.getElementById("tvOcrSector").innerText = "None";
  }}

  const refBadge = document.getElementById("tvRefBadge");
  if (sp.reference_status === "MATCHED") {{
    refBadge.style.background = "rgba(0,255,136,0.15)";
    refBadge.style.color = "#00ff88";
    refBadge.innerText = "MATCHED";
  }} else {{
    refBadge.style.background = "rgba(255,190,11,0.15)";
    refBadge.style.color = "#ffbe0b";
    refBadge.innerText = "UNMATCHED (AI Discovery)";
  }}
  document.getElementById("tvRefSource").innerText = sp.reference_source;

  // Filmstrip highlight
  document.querySelectorAll(".thumb-item").forEach(t => t.classList.remove("active"));
  const act = document.getElementById(`tvThumb_${{tvCurrentIdx}}`);
  if (act) {{
    act.classList.add("active");
    act.scrollIntoView({{ behavior: "smooth", inline: "center" }});
  }}
}}

function tvNext() {{
  tvCurrentIdx = (tvCurrentIdx < TRI_RECORDS.length - 1) ? tvCurrentIdx + 1 : 0;
  tvRender();
}}

function tvPrev() {{
  tvCurrentIdx = (tvCurrentIdx > 0) ? tvCurrentIdx - 1 : TRI_RECORDS.length - 1;
  tvRender();
}}

function tvChangeStreet() {{
  const st = document.getElementById("tvStreetSelect").value;
  if (st === "ALL") {{
    renderTvFilmstrip(TRI_RECORDS);
    tvCurrentIdx = 0;
  }} else {{
    const filtered = TRI_RECORDS.filter(r => r.street_id === st);
    renderTvFilmstrip(filtered);
    if (filtered.length > 0) tvCurrentIdx = filtered[0].index;
  }}
  tvRender();
}}

function renderTvFilmstrip(list) {{
  const strip = document.getElementById("tvFilmstrip");
  strip.innerHTML = "";
  list.forEach(r => {{
    const div = document.createElement("div");
    div.className = "thumb-item";
    div.id = `tvThumb_${{r.index}}`;
    div.onclick = () => {{ tvCurrentIdx = r.index; tvRender(); }};
    div.innerHTML = `<img src="${{r.image_path}}" alt="${{r.image_id}}"><div class="thumb-label">${{r.street_id}} #${{r.capture_order}}</div>`;
    strip.appendChild(div);
  }});
}}

// 3. FULL GIS MAP WITH MEASUREMENT TOOL
let fullMap, fullMarkers = [], measureActive = false, measurePoints = [], measureLine = null;

function initFullMap() {{
  fullMap = L.map("fullGisMap", {{ zoomControl: false, attributionControl: false }}).setView([11.0345, 76.9745], 15);
  L.control.zoom({{ position: "bottomleft" }}).addTo(fullMap);
  L.tileLayer("https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png", {{ maxZoom: 20, subdomains: "abcd" }}).addTo(fullMap);

  L.geoJSON(BOUNDARY_GEOJSON, {{ style: {{ color: "#00f2fe", weight: 2, dashArray: "5, 5", fillColor: "#00f2fe", fillOpacity: 0.04 }} }}).addTo(fullMap);
  L.geoJSON(ROADS_GEOJSON, {{ style: {{ color: "#00f2fe", weight: 4, opacity: 0.85 }} }}).addTo(fullMap);

  const colors = {{ building: "#00ff88", electric_pole: "#fb5607", streetlight: "#ffbe0b", transformer: "#ff0055", traffic_signal: "#f72585", commercial_sign: "#00f2fe" }};

  ASSETS_GEOJSON.features.forEach(f => {{
    const p = f.properties;
    const m = L.circleMarker([f.geometry.coordinates[1], f.geometry.coordinates[0]], {{
      radius: p.asset_class === "building" ? 6 : 4.5,
      fillColor: colors[p.asset_class] || "#fff",
      color: "#05080f",
      weight: 1,
      fillOpacity: 0.9
    }});
    m.bindPopup(`<strong>${{p.asset_id}}</strong><br>${{p.asset_subtype}}<br>Corridor: ${{p.street_name}}<br>Chainage: ${{p.chainage_m}}m &bull; Offset: ${{p.road_offset_m}}m`);
    m.feature = f;
    m.addTo(fullMap);
    fullMarkers.push(m);
  }});

  fullMap.on("click", (e) => {{
    if (!measureActive) return;
    measurePoints.push(e.latlng);

    if (measurePoints.length === 1) {{
      document.getElementById("measureOutput").innerText = "Point 1 set. Click second point...";
    }} else if (measurePoints.length === 2) {{
      const d = measurePoints[0].distanceTo(measurePoints[1]);
      if (measureLine) fullMap.removeLayer(measureLine);
      measureLine = L.polyline(measurePoints, {{ color: "#ffbe0b", weight: 3, dashArray: "6, 6" }}).addTo(fullMap);
      document.getElementById("measureOutput").innerText = `Distance: ${{d.toFixed(1)}} meters`;
      measurePoints = [];
    }}
  }});
}}

function toggleMeasureTool() {{
  measureActive = !measureActive;
  measurePoints = [];
  if (measureLine) {{ fullMap.removeLayer(measureLine); measureLine = null; }}
  const btn = document.getElementById("btnMeasure");
  const out = document.getElementById("measureOutput");
  if (measureActive) {{
    btn.classList.add("active");
    out.style.display = "block";
    out.innerText = "Click first point on map...";
  }} else {{
    btn.classList.remove("active");
    out.style.display = "none";
  }}
}}

let gisRefState = "ALL";
function gisApplyFilters() {{
  const allowed = [];
  ["building", "electric_pole", "streetlight", "transformer", "traffic_signal", "commercial_sign"].forEach(cls => {{
    if (document.getElementById(`gChk_${{cls}}`).checked) allowed.push(cls);
  }});

  fullMarkers.forEach(m => {{
    const p = m.feature.properties;
    const matchCls = allowed.includes(p.asset_class);
    const matchRef = gisRefState === "ALL" || p.reference_status === gisRefState;

    if (matchCls && matchRef) {{
      if (!fullMap.hasLayer(m)) fullMap.addLayer(m);
    }} else {{
      if (fullMap.hasLayer(m)) fullMap.removeLayer(m);
    }}
  }});
}}

function gisSetRef(st) {{
  gisRefState = st;
  document.getElementById("gRefAll").style.background = st === "ALL" ? "rgba(0,242,254,0.2)" : "#080d16";
  document.getElementById("gRefMatch").style.background = st === "MATCHED" ? "rgba(0,242,254,0.2)" : "#080d16";
  document.getElementById("gRefUnmatch").style.background = st === "UNMATCHED" ? "rgba(0,242,254,0.2)" : "#080d16";
  gisApplyFilters();
}}

// 4. BUILDING CATALOG MODAL & FILTERS
function openBldgModal(bId) {{
  const b = BUILDINGS_DATA.find(x => x.Building_ID === bId);
  if (!b) return;

  document.getElementById("mBldgId").innerText = b.Building_ID;
  document.getElementById("mBldgTitle").innerText = b.Establishment_Name;
  document.getElementById("mBldgImg").src = b.Annotated_Floor_Image.replace("\\\\", "/");

  document.getElementById("mBldgParams").innerHTML = `
    <div><span style="color:var(--text-muted);">Floors & Height:</span> <strong>${{b.Floor_Notation}} (${{b.Building_Floors}} Floors) &bull; ${{b.Estimated_Height_m}}m</strong></div>
    <div><span style="color:var(--text-muted);">Usage:</span> <strong>${{b.Building_Usage}}</strong></div>
    <div><span style="color:var(--text-muted);">Facade:</span> <strong>${{b.Facade_Type}}</strong></div>
    <div><span style="color:var(--text-muted);">Ground Activity:</span> <strong>${{b.Ground_Floor_Activity}}</strong></div>
    <div><span style="color:var(--text-muted);">Amenities:</span> <strong>${{b.Special_Features}}</strong></div>
    <div><span style="color:var(--text-muted);">GPS:</span> <strong>${{b.Latitude.toFixed(6)}}°N, ${{b.Longitude.toFixed(6)}}°E &bull; ${{b.Street_Name}}</strong></div>
    <div style="margin-top:6px;"><a href="${{b.Official_Links}}" target="_blank" style="color:var(--accent-cyan); font-weight:700; text-decoration:underline;">Open in Google Maps &rarr;</a></div>
  `;

  document.getElementById("bldgModal").classList.add("active");
}}

function closeBldgModal() {{
  document.getElementById("bldgModal").classList.remove("active");
}}

function filterBuildings() {{
  const q = document.getElementById("bldgSearchInput").value.toLowerCase();
  const fl = document.getElementById("bldgFloorFilter").value;
  const st = document.getElementById("bldgStreetFilter").value;

  const cards = document.querySelectorAll(".bldg-card");
  let count = 0;
  BUILDINGS_DATA.forEach((b, idx) => {{
    const matchQ = !q || b.Establishment_Name.toLowerCase().includes(q) || b.Building_ID.toLowerCase().includes(q) || b.Building_Usage.toLowerCase().includes(q);
    const matchFl = fl === "ALL" || b.Floor_Notation === fl;
    const matchSt = st === "ALL" || b.Street_ID === st;

    if (matchQ && matchFl && matchSt) {{
      cards[idx].style.display = "flex";
      count++;
    }} else {{
      cards[idx].style.display = "none";
    }}
  }});
  document.getElementById("bldgCount").innerText = count;
}}

// 5. OCR SEARCH FILTER
function filterOcr() {{
  const q = document.getElementById("ocrSearchInput").value.toLowerCase();
  const sec = document.getElementById("ocrSectorFilter").value.toLowerCase();

  const cards = document.querySelectorAll(".ocr-card");
  let count = 0;
  OCR_DATA.forEach((o, idx) => {{
    const matchQ = !q || o.Cleaned_Text.toLowerCase().includes(q) || o.OCR_ID.toLowerCase().includes(q);
    const matchSec = sec === "all" || o.Commercial_Category.toLowerCase().includes(sec);

    if (matchQ && matchSec) {{
      cards[idx].style.display = "flex";
      count++;
    }} else {{
      cards[idx].style.display = "none";
    }}
  }});
  document.getElementById("ocrCount").innerText = count;
}}

// 6. ASSETS FILTER
function filterPassports() {{
  const q = document.getElementById("passSearch").value.toLowerCase();
  const cls = document.getElementById("passClassFilter").value;

  const rows = document.querySelectorAll("#passportsTable tbody tr");
  let count = 0;
  ASSETS_DATA.features.forEach((f, idx) => {{
    const p = f.properties;
    const matchQ = !q || p.asset_id.toLowerCase().includes(q) || p.asset_subtype.toLowerCase().includes(q) || p.managing_authority.toLowerCase().includes(q);
    const matchCls = cls === "ALL" || p.asset_class === cls;

    if (matchQ && matchCls) {{
      rows[idx].style.display = "";
      count++;
    }} else {{
      rows[idx].style.display = "none";
    }}
  }});
  document.getElementById("passCount").innerText = count;
}}

// 7. AI COPILOT LOGIC
function cpSendPrompt(text) {{
  document.getElementById("cpInput").value = text;
  cpSubmitQuery();
}}

function cpSubmitQuery() {{
  const input = document.getElementById("cpInput");
  const q = input.value.trim();
  if (!q) return;

  const stream = document.getElementById("cpStream");
  const userDiv = document.createElement("div");
  userDiv.className = "cp-bubble user";
  userDiv.innerHTML = `<div class="cp-avatar cp-user">ME</div><div class="cp-body">${{q}}</div>`;
  stream.appendChild(userDiv);
  input.value = "";
  stream.scrollTop = stream.scrollHeight;

  setTimeout(() => {{
    const answer = cpExecute(q);
    const aiDiv = document.createElement("div");
    aiDiv.className = "cp-bubble";
    aiDiv.innerHTML = `<div class="cp-avatar cp-ai">AI</div><div class="cp-body">${{answer}}</div>`;
    stream.appendChild(aiDiv);
    stream.scrollTop = stream.scrollHeight;
  }}, 150);
}}

function cpExecute(qText) {{
  const q = qText.toLowerCase();

  // Nearest transformer / spatial topology
  if (q.includes("nearest transformer") || q.includes("hotel anandha") || q.includes("transformer to hotel") || q.includes("how far")) {{
    const anandha = RELATIONS_DATA.find(r => r.Building_Name.toLowerCase().includes("anandha")) || RELATIONS_DATA[0];
    return `
      <div style="font-size:14px; font-weight:700; color:#fff;">Spatial Topology: ${{anandha.Building_Name}}</div>
      <div>The nearest distribution transformer to <strong>${{anandha.Building_Name}}</strong> (${{anandha.Building_ID}}) is <strong>${{anandha.Nearest_Transformer_ID}}</strong> located at a spatial distance of <strong>${{anandha.Nearest_Transformer_Distance_m}} meters</strong>.</div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; background:#080c14; padding:8px 10px; border-radius:6px; font-size:11px; margin-top:4px;">
        <div><span style="color:var(--text-muted);">TRANSFORMER:</span> <strong>${{anandha.Nearest_Transformer_ID}}</strong></div>
        <div><span style="color:var(--text-muted);">DISTANCE:</span> <strong>${{anandha.Nearest_Transformer_Distance_m}}m</strong></div>
        <div><span style="color:var(--text-muted);">NEAREST POLE:</span> <strong>${{anandha.Nearest_Pole_ID}} (${{anandha.Nearest_Pole_Distance_m}}m)</strong></div>
        <div><span style="color:var(--text-muted);">CHAINAGE:</span> <strong>${{anandha.Corridor_Chainage_m}}m (${{anandha.Road_Side}})</strong></div>
      </div>
    `;
  }}

  // Highest electrical load
  if (q.includes("highest electrical") || q.includes("highest load") || q.includes("most power") || q.includes("transformer capacity") || q.includes("max transformer")) {{
    const top = [...SCORECARDS_DATA].sort((a,b) => b.Substation_Capacity_kVA_per_km - a.Substation_Capacity_kVA_per_km)[0];
    return `
      <div style="font-size:14px; font-weight:700; color:#fff;">Highest Load Corridor: ${{top.Street_ID}} (${{top.Street_Name}})</div>
      <div>Corridor <strong>${{top.Street_ID}}</strong> exhibits the highest electrical substation load density in Ward 29 at <strong>${{top.Substation_Capacity_kVA_per_km.toFixed(1)}} kVA/km</strong> across ${{top.Total_Transformer_kVA}} kVA total capacity (6 substations).</div>
      <div style="background:#090f1a; border-left:3px solid var(--accent-cyan); padding:8px 10px; border-radius:4px; font-size:11px; margin-top:4px;">
        <strong>Work Order:</strong> ${{top.Actionable_Work_Order}}<br>
        <span style="color:var(--text-muted); font-size:10px;">Agency: ${{top.Responsible_Civic_Agency}}</span>
      </div>
    `;
  }}

  // Decluttering
  if (q.includes("declutter") || q.includes("delacing") || q.includes("cable") || q.includes("wire clutter")) {{
    return `
      <div style="font-size:14px; font-weight:700; color:#fff;">Utility Poles Requiring Urgent Cable Decluttering (43 Poles Flagged)</div>
      <div>A total of <strong>43 utility poles (39.8%)</strong> exhibit severe overhead telecom fiber coiling and bundled multi-service drops.</div>
      <div style="margin-top:4px; font-size:11px;">
        &bull; <strong>ST08 (Raja Street):</strong> 20 poles flagged<br>
        &bull; <strong>ST06 (KRG Nagar):</strong> 13 poles flagged<br>
        &bull; <strong>ST03 (Ganapathy Pudur):</strong> 10 poles flagged
      </div>
      <div style="background:rgba(255,0,85,0.1); border-left:3px solid #ff0055; padding:6px 10px; border-radius:4px; font-size:11px; margin-top:4px;">
        <strong>Recommended Action:</strong> TANGEDCO joint delacing drive and Aerial Bundled Conductor (ABC) conversion.
      </div>
    `;
  }}

  // Tall buildings
  if (q.includes("4 or more") || q.includes("4+") || q.includes("tall") || q.includes("g+3") || q.includes("g+4")) {{
    const tall = BUILDINGS_DATA.filter(b => b.Building_Floors >= 4);
    return `
      <div style="font-size:14px; font-weight:700; color:#fff;">Multi-Story Buildings with 4+ Floors (${{tall.length}} Structures)</div>
      <div>Detected ${{tall.length}} properties with 4 to 5 floors (14.0m to 17.5m height) along commercial corridors. Prominent examples: <strong>Hotel Anandha Residency</strong> (G+3), <strong>AutoZone Showroom</strong> (G+4), and <strong>Hotel Sree Saravana Grand</strong> (G+4).</div>
    `;
  }}

  // Streetlight spacing
  if (q.includes("spacing") || q.includes("avarampalayam") || q.includes("dark spot") || q.includes("lighting")) {{
    return `
      <div style="font-size:14px; font-weight:700; color:#fff;">Streetlight Diagnostic: ST10 (Avarampalayam Road)</div>
      <div>Corridor ST10 exhibits an average luminaire spacing of <strong>45.0 meters</strong>, which significantly exceeds the Indian Road Congress safety standard (20m - 25m), creating severe dark-spot hazards.</div>
      <div style="background:#090f1a; border-left:3px solid var(--accent-gold); padding:8px 10px; border-radius:4px; font-size:11px; margin-top:4px;">
        <strong>Work Order:</strong> Streetlight Infill Required! Install 4-5 intermediate 70W LED luminaires.<br>
        <span style="color:var(--text-muted); font-size:10px;">Agency: CCMC Electrical Division</span>
      </div>
    `;
  }}

  // Healthcare
  if (q.includes("pharmacy") || q.includes("healthcare") || q.includes("clinic") || q.includes("medical")) {{
    return `
      <div style="font-size:14px; font-weight:700; color:#fff;">Healthcare & Pharmacy Establishments (7 Surveyed)</div>
      <div>Identified 7 healthcare facilities and retail pharmacies across Ward 29, including <strong>Apollo Pharmacy</strong> (ST01), <strong>Aarthy Dental Clinic & Health Centre</strong> (ST04), and <strong>Sri Sai Medicals & Doctor Clinic</strong> (ST07).</div>
    `;
  }}

  // Default Overview
  return `
    <div style="font-size:14px; font-weight:700; color:#fff;">Coimbatore Ward 29 Digital Twin Overview</div>
    <div>Surveyed <strong>10 corridors (2.49 km network)</strong> cataloging <strong>465 fixed assets</strong>, <strong>108 buildings</strong>, <strong>201 OCR signs</strong>, and <strong>24 distribution transformers</strong> with 13.3% cadastre reference matching.</div>
  `;
}}

// 8. CLIENT-SIDE DOWNLOAD HELPERS
function downloadJSON(data, filename) {{
  const blob = new Blob([JSON.stringify(data, null, 2)], {{ type: "application/json" }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  a.click();
  URL.revokeObjectURL(url);
}}

function downloadCSV(data, filename) {{
  if (!data || data.length === 0) return;
  const headers = Object.keys(data[0]);
  const rows = data.map(r => headers.map(h => `"${{String(r[h] || '').replace(/"/g, '""')}}"`).join(","));
  const csvStr = [headers.join(","), ...rows].join("\\n");
  const blob = new Blob([csvStr], {{ type: "text/csv;charset=utf-8;" }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  a.click();
  URL.revokeObjectURL(url);
}}

// Launch Initializers
initTvMap();
initFullMap();
renderTvFilmstrip(TRI_RECORDS);
tvRender();
</script>
</body>
</html>
"""

with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated updated {out_html_path} ({len(html_content)} bytes)")
