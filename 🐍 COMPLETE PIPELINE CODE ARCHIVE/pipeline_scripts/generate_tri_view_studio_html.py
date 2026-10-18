import os
import sys
import json
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
images_csv = os.path.join(base_dir, "master_images.csv")
bldg_csv = os.path.join(base_dir, "building_intelligence.csv")
inv_csv = os.path.join(base_dir, "urban_asset_inventory.csv")
ocr_csv = os.path.join(base_dir, "ocr_intelligence.csv")
rel_csv = os.path.join(base_dir, "spatial_relationships.csv")
streets_csv = os.path.join(base_dir, "master_streets.csv")
study_area_path = r"D:\Study_area.geojson"
roads_geojson_path = os.path.join(base_dir, "road_network_topology.geojson")
out_html_path = os.path.join(base_dir, "tri_view_studio.html")

df_img = pd.read_csv(images_csv)
df_bldg = pd.read_csv(bldg_csv)
df_inv = pd.read_csv(inv_csv)
df_ocr = pd.read_csv(ocr_csv)
df_rel = pd.read_csv(rel_csv)
df_streets = pd.read_csv(streets_csv)

with open(study_area_path, "r", encoding="utf-8") as f:
    boundary_geojson = json.load(f)

with open(roads_geojson_path, "r", encoding="utf-8") as f:
    roads_geojson = json.load(f)

# Group inventory and OCR by Image_ID
inv_by_img = {}
for img_id, grp in df_inv.groupby("Image_ID"):
    inv_by_img[img_id] = grp.to_dict(orient="records")

ocr_by_img = {}
for img_id, grp in df_ocr.groupby("Image_ID"):
    ocr_by_img[img_id] = grp.to_dict(orient="records")

rel_by_bldg = df_rel.set_index("Building_ID").to_dict(orient="index")
bldg_by_img = df_bldg.set_index("Image_ID").to_dict(orient="index")

# Build comprehensive unified image records
records = []
for idx, r in df_img.iterrows():
    img_id = r["Image_ID"]
    st_id = r["Street_ID"]
    bldg = bldg_by_img.get(img_id, {})
    b_id = bldg.get("Building_ID", f"BLDG-{st_id}-001")
    rel = rel_by_bldg.get(b_id, {})
    assets = inv_by_img.get(img_id, [])
    ocr_items = ocr_by_img.get(img_id, [])

    # Clean technical specs in assets
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
            "confidence": float(bldg.get("Confidence", 0.9)),
            "bbox": [float(bldg.get("BBox_X1", 0)), float(bldg.get("BBox_Y1", 0)), float(bldg.get("BBox_X2", 0)), float(bldg.get("BBox_Y2", 0))],
            "norm_bbox": [float(bldg.get("Norm_X1", 0)), float(bldg.get("Norm_Y1", 0)), float(bldg.get("Norm_X2", 0)), float(bldg.get("Norm_Y2", 0))]
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
    records.append(rec)

print(f"Compiled {len(records)} synchronized Tri-View records.")

# Build HTML content
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Synchronized Tri-View Urban Intelligence Studio — FarmwiseAI Task 5</title>
<!-- Leaflet CSS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<style>
  :root {{
    --bg-dark: #06090f;
    --panel-bg: #0c121d;
    --panel-header: #121b2b;
    --panel-border: #1a283e;
    --accent-cyan: #00f2fe;
    --accent-emerald: #00ff88;
    --accent-gold: #ffbe0b;
    --accent-orange: #fb5607;
    --accent-red: #ff0055;
    --accent-magenta: #f72585;
    --text-primary: #e6edf8;
    --text-muted: #8496ad;
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
  /* Header Navbar */
  header {{
    background: #090e17;
    border-bottom: 1px solid var(--panel-border);
    padding: 10px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 2000;
  }}
  .brand {{
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
    background: linear-gradient(90deg, #00f2fe, #00ff88);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .nav-controls {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .nav-btn {{
    background: #141f30;
    border: 1px solid #233550;
    color: #c0d4ec;
    padding: 6px 14px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 12px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s;
  }}
  .nav-btn:hover {{ background: #1c2d46; color: #fff; border-color: var(--accent-cyan); }}
  .street-select {{
    background: #101928;
    border: 1px solid #233550;
    color: var(--text-primary);
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 12px;
    outline: none;
    cursor: pointer;
  }}
  .counter-badge {{
    font-family: monospace;
    font-size: 13px;
    color: var(--accent-gold);
    font-weight: 700;
    padding: 0 4px;
  }}
  .header-actions {{
    display: flex;
    gap: 10px;
    align-items: center;
  }}
  .action-btn {{
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 700;
    text-decoration: none;
    cursor: pointer;
    border: 1px solid transparent;
  }}
  .btn-approve {{
    background: rgba(0, 255, 136, 0.15);
    color: var(--accent-emerald);
    border-color: rgba(0, 255, 136, 0.35);
  }}
  .btn-approve:hover {{ background: rgba(0, 255, 136, 0.25); }}
  .btn-escalate {{
    background: rgba(255, 190, 11, 0.15);
    color: var(--accent-gold);
    border-color: rgba(255, 190, 11, 0.35);
  }}
  .btn-escalate:hover {{ background: rgba(255, 190, 11, 0.25); }}

  /* Tri-View Layout */
  .studio-main {{
    flex: 1;
    display: grid;
    grid-template-columns: 38% 32% 30%;
    overflow: hidden;
    position: relative;
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
    padding: 10px 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 12px;
    font-weight: 700;
    color: #fff;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .panel-header span.tag {{
    font-size: 10px;
    padding: 2px 6px;
    border-radius: 4px;
    background: #19273c;
    color: var(--accent-cyan);
  }}

  /* Panel 1: Street View Visualizer */
  .visualizer-container {{
    flex: 1;
    position: relative;
    background: #04060a;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }}
  .visualizer-img {{
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    transition: opacity 0.2s;
  }}
  .layer-toggles {{
    position: absolute;
    top: 12px;
    left: 12px;
    background: rgba(10, 16, 26, 0.88);
    backdrop-filter: blur(8px);
    border: 1px solid var(--panel-border);
    border-radius: 6px;
    padding: 8px 12px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    font-size: 11px;
    font-weight: 600;
    z-index: 10;
  }}
  .layer-toggle-item {{
    display: flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
    user-select: none;
  }}
  .img-hud-bottom {{
    position: absolute;
    bottom: 10px;
    left: 12px;
    right: 12px;
    background: rgba(10, 16, 26, 0.85);
    border: 1px solid var(--panel-border);
    border-radius: 6px;
    padding: 6px 12px;
    font-size: 11px;
    color: #c8d8ec;
    display: flex;
    justify-content: space-between;
    backdrop-filter: blur(6px);
  }}

  /* Panel 2: Geospatial Digital Twin */
  #studioMap {{
    width: 100%;
    height: 100%;
    background: #090e17;
  }}

  /* Panel 3: Live Intelligence Inspector */
  .inspector-content {{
    flex: 1;
    overflow-y: auto;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }}
  .inspect-card {{
    background: #0f1624;
    border: 1px solid var(--panel-border);
    border-radius: 8px;
    overflow: hidden;
  }}
  .inspect-header {{
    background: #141c2c;
    padding: 8px 14px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--accent-cyan);
    letter-spacing: 0.5px;
    border-bottom: 1px solid var(--panel-border);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .inspect-body {{
    padding: 12px 14px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    font-size: 12px;
  }}
  .info-row {{
    display: flex;
    justify-content: space-between;
    gap: 8px;
  }}
  .info-k {{ color: var(--text-muted); font-size: 11px; }}
  .info-v {{ color: #e4edf8; font-weight: 600; text-align: right; }}

  .highlight-badge {{
    font-size: 11px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 4px;
    display: inline-block;
  }}
  .badge-matched {{ background: rgba(0, 255, 136, 0.2); color: #00ff88; border: 1px solid #00ff88; }}
  .badge-unmatched {{ background: rgba(255, 190, 11, 0.2); color: #ffbe0b; border: 1px solid #ffbe0b; }}

  /* Bottom Transect Filmstrip */
  .filmstrip {{
    height: 64px;
    background: #090d16;
    border-top: 1px solid var(--panel-border);
    display: flex;
    align-items: center;
    padding: 0 16px;
    gap: 8px;
    overflow-x: auto;
    z-index: 1000;
  }}
  .thumb-item {{
    height: 48px;
    width: 80px;
    border-radius: 4px;
    overflow: hidden;
    border: 2px solid #1a273b;
    cursor: pointer;
    flex-shrink: 0;
    position: relative;
    transition: all 0.2s;
  }}
  .thumb-item:hover, .thumb-item.active {{
    border-color: var(--accent-cyan);
    transform: scale(1.05);
    box-shadow: 0 0 10px rgba(0, 242, 254, 0.4);
  }}
  .thumb-item img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .thumb-label {{
    position: absolute;
    bottom: 2px;
    left: 2px;
    background: rgba(0,0,0,0.7);
    color: #fff;
    font-size: 9px;
    font-weight: 700;
    padding: 1px 3px;
    border-radius: 2px;
  }}
</style>
</head>
<body>

<header>
  <div class="brand">
    <span class="badge-tag">FarmwiseAI Task 5 &bull; Team 24</span>
    <div class="brand-title"><span>Synchronized Tri-View Studio</span> &bull; Coimbatore Ward 29</div>
  </div>

  <div class="nav-controls">
    <select class="street-select" id="streetFilter" onchange="changeStreetFilter()">
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

    <button class="nav-btn" onclick="prevImage()">&larr; Prev</button>
    <div style="font-size: 12px; font-weight: 600;">
      Capture <span class="counter-badge" id="currentNum">1</span> / <span id="totalNum">108</span>
    </div>
    <button class="nav-btn" onclick="nextImage()">Next &rarr;</button>
  </div>

  <div class="header-actions">
    <button class="action-btn btn-approve" onclick="alert('AI Detections & Digital Passport Approved for Municipal Cadastre!')">&check; Approve AI</button>
    <button class="action-btn btn-escalate" onclick="alert('Flagged for Selective VLM Verification (Phase 16 Engine)!')">&Delta; Escalate VLM</button>
    <a href="gis_digital_twin_baseline.html" style="font-size:11px; color:var(--accent-cyan); text-decoration:none; font-weight:700; margin-left:8px;">Full Map &rarr;</a>
  </div>
</header>

<div class="studio-main">
  <!-- Panel 1: Street View Visualizer -->
  <div class="panel">
    <div class="panel-header">
      <span>1. Street View Perception HUD</span>
      <span class="tag" id="panel1ImageId">IMG-ST01-001</span>
    </div>
    <div class="visualizer-container">
      <img id="mainImage" class="visualizer-img" src="" alt="Street View Capture">
      
      <div class="layer-toggles">
        <label class="layer-toggle-item">
          <input type="checkbox" id="chkFloorBands" checked onchange="toggleFloorLayer()">
          <span>Floor Bands & Height Blueprint</span>
        </label>
      </div>

      <div class="img-hud-bottom">
        <span id="imgHudStreet">Sathy Road (NH 948)</span>
        <span id="imgHudGPS">11.035355°N, 76.973424°E</span>
      </div>
    </div>
  </div>

  <!-- Panel 2: Synchronized Geospatial Digital Twin -->
  <div class="panel">
    <div class="panel-header">
      <span>2. Synchronized GIS Digital Twin</span>
      <span class="tag" id="panel2StatusTag">LIVE SYNC</span>
    </div>
    <div id="studioMap"></div>
  </div>

  <!-- Panel 3: Live Urban Intelligence Passport Inspector -->
  <div class="panel">
    <div class="panel-header">
      <span>3. Urban Asset Passport Inspector</span>
      <span class="tag" id="panel3PassportTag">BLDG-ST01-001</span>
    </div>
    <div class="inspector-content">
      <!-- Building Card -->
      <div class="inspect-card">
        <div class="inspect-header">
          <span>Building Envelope & Properties</span>
          <span id="inspectFloorsBadge" style="color:var(--accent-emerald); font-weight:700;">G+3 &bull; 14.0m</span>
        </div>
        <div class="inspect-body">
          <div style="font-size:15px; font-weight:700; color:#fff;" id="insTitle">Hotel Anandha Residency</div>
          <div class="info-row"><span class="info-k">Usage:</span><span class="info-v" id="insUsage">Commercial Hotel & Dining</span></div>
          <div class="info-row"><span class="info-k">Facade:</span><span class="info-v" id="insFacade">Glass Curtain Wall & ACP</span></div>
          <div class="info-row"><span class="info-k">Ground Floor:</span><span class="info-v" id="insGround">Hotel Reception & Dining</span></div>
          <div class="info-row"><span class="info-k">Amenities:</span><span class="info-v" id="insSpecial">24h lodging, AC banquet</span></div>
          <div style="margin-top:4px;">
            <a id="insMapsLink" href="" target="_blank" style="color:var(--accent-cyan); font-size:12px; font-weight:700; text-decoration:underline;">Open Google Maps Navigation &rarr;</a>
          </div>
        </div>
      </div>

      <!-- Spatial Topologies Card -->
      <div class="inspect-card">
        <div class="inspect-header">
          <span>Spatial Graph Topology</span>
          <span style="color:var(--accent-gold); font-weight:700;">Nearest Neighbors</span>
        </div>
        <div class="inspect-body">
          <div class="info-row"><span class="info-k">Nearest Utility Pole:</span><span class="info-v" id="insPole">POLE-ST01-001 (18.9m)</span></div>
          <div class="info-row"><span class="info-k">Pole Wiring Burden:</span><span class="info-v" id="insPoleBurden">High Telecom Bundle</span></div>
          <div class="info-row"><span class="info-k">Nearest Transformer:</span><span class="info-v" id="insTrans">TRANS-ST01-003 (67.8m)</span></div>
          <div class="info-row"><span class="info-k">Nearest Streetlight:</span><span class="info-v" id="insLight">LIGHT-ST01-001 (18.6m)</span></div>
          <div class="info-row"><span class="info-k">Road Chainage & Offset:</span><span class="info-v" id="insChainage">0.0m / +14.8m (Right)</span></div>
        </div>
      </div>

      <!-- OCR Commercial Intelligence Card -->
      <div class="inspect-card">
        <div class="inspect-header">
          <span>OCR Commercial Intelligence</span>
          <span style="color:var(--accent-cyan); font-weight:700;" id="insOcrCount">1 Detected</span>
        </div>
        <div class="inspect-body">
          <div class="info-row"><span class="info-k">Extracted Sign Text:</span><span class="info-v" id="insOcrText">Hotel Anandha Residency</span></div>
          <div class="info-row"><span class="info-k">Commercial Category:</span><span class="info-v" id="insOcrCat">Dining & Hospitality</span></div>
          <div class="info-row"><span class="info-k">OCR Confidence:</span><span class="info-v" id="insOcrConf">94.0%</span></div>
        </div>
      </div>

      <!-- Municipal Baseline Card -->
      <div class="inspect-card">
        <div class="inspect-header">
          <span>Reference Dataset Cadastre</span>
          <span id="insRefBadge" class="highlight-badge badge-matched">MATCHED</span>
        </div>
        <div class="inspect-body">
          <div class="info-row"><span class="info-k">Baseline Source:</span><span class="info-v" id="insRefSource">OpenStreetMap Cadastre</span></div>
          <div class="info-row"><span class="info-k">Jurisdiction:</span><span class="info-v">Coimbatore Corp (CCMC) &bull; Ward 29</span></div>
          <div class="info-row"><span class="info-k">Managing Body:</span><span class="info-v">TANGEDCO &bull; CCMC Electrical</span></div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Bottom Filmstrip -->
<div class="filmstrip" id="filmstrip">
  <!-- Injected by JS -->
</div>

<!-- Leaflet JS -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
const RECORDS = {json.dumps(records, ensure_ascii=False)};
const BOUNDARY_GEOJSON = {json.dumps(boundary_geojson, ensure_ascii=False)};
const ROADS_GEOJSON = {json.dumps(roads_geojson, ensure_ascii=False)};

let currentIndex = 0;
let filteredRecords = [...RECORDS];

// Initialize Map
const map = L.map("studioMap", {{
  zoomControl: true,
  attributionControl: false
}}).setView([11.0345, 76.9745], 16);

L.tileLayer("https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png", {{
  maxZoom: 20,
  subdomains: "abcd"
}}).addTo(map);

// Ward 29 Boundary Layer
L.geoJSON(BOUNDARY_GEOJSON, {{
  style: {{
    color: "#00f2fe",
    weight: 2,
    dashArray: "5, 5",
    fillColor: "#00f2fe",
    fillOpacity: 0.04
  }}
}}).addTo(map);

// Road Centerlines Layer
L.geoJSON(ROADS_GEOJSON, {{
  style: {{
    color: "#00f2fe",
    weight: 3,
    opacity: 0.8
  }}
}}).addTo(map);

// Dynamic Map Elements
let cameraMarker = null;
let spiderLines = [];
let assetMarkers = [];

// Color scheme for asset classes
const classColors = {{
  building: "#00ff88",
  electric_pole: "#fb5607",
  streetlight: "#ffbe0b",
  transformer: "#ff0055",
  traffic_signal: "#f72585",
  commercial_sign: "#00f2fe"
}};

// Render Asset Markers
RECORDS.forEach(r => {{
  r.fixed_assets.forEach(a => {{
    const color = classColors[a.Asset_Class] || "#ffffff";
    const radius = a.Asset_Class === "building" ? 6 : (a.Asset_Class === "transformer" ? 5 : 4);
    const m = L.circleMarker([a.Precise_Latitude, a.Precise_Longitude], {{
      radius: radius,
      fillColor: color,
      color: "#05080f",
      weight: 1.5,
      opacity: 1,
      fillOpacity: 0.85
    }});
    m.on("click", () => {{
      jumpToIndex(r.index);
    }});
    m.addTo(map);
    assetMarkers.push(m);
  }});
}});

// Camera Position Marker with Viewing Frustum
function updateCameraMarker(lat, lon) {{
  if (cameraMarker) map.removeLayer(cameraMarker);

  cameraMarker = L.circleMarker([lat, lon], {{
    radius: 9,
    fillColor: "#00f2fe",
    color: "#ffffff",
    weight: 2,
    opacity: 1,
    fillOpacity: 0.95
  }}).addTo(map);
}}

// Draw Spider-Lines connecting building to nearest pole and transformer
function updateSpiderLines(r) {{
  spiderLines.forEach(l => map.removeLayer(l));
  spiderLines = [];

  const bCoords = [r.latitude, r.longitude];
  const sp = r.spatial_relationships;

  // Pole Line
  if (sp.nearest_pole_coord) {{
    const pLine = L.polyline([bCoords, [sp.nearest_pole_coord[1], sp.nearest_pole_coord[0]]], {{
      color: "#ffbe0b",
      weight: 2.5,
      dashArray: "5, 5",
      opacity: 0.9
    }}).addTo(map);
    spiderLines.push(pLine);
  }}

  // Transformer Line
  if (sp.nearest_transformer_coord) {{
    const tLine = L.polyline([bCoords, [sp.nearest_transformer_coord[1], sp.nearest_transformer_coord[0]]], {{
      color: "#ff0055",
      weight: 2.5,
      dashArray: "4, 6",
      opacity: 0.9
    }}).addTo(map);
    spiderLines.push(tLine);
  }}
}}

// Display Record in Studio
function showRecord(idx) {{
  const r = RECORDS[idx];
  if (!r) return;
  currentIndex = idx;

  // Update Header Badges
  document.getElementById("currentNum").innerText = idx + 1;
  document.getElementById("totalNum").innerText = RECORDS.length;
  document.getElementById("panel1ImageId").innerText = r.image_id;
  document.getElementById("panel3PassportTag").innerText = r.building.building_id;

  // Panel 1: Image
  const useBlueprint = document.getElementById("chkFloorBands").checked;
  const imgSrc = useBlueprint ? r.annotated_floor_image : r.image_path;
  document.getElementById("mainImage").src = imgSrc;
  document.getElementById("imgHudStreet").innerText = `${{r.street_name}} (${{r.street_id}})`;
  document.getElementById("imgHudGPS").innerText = `${{r.latitude.toFixed(6)}}°N, ${{r.longitude.toFixed(6)}}°E &bull; Order #${{r.capture_order}}`;

  // Panel 2: Map
  updateCameraMarker(r.latitude, r.longitude);
  updateSpiderLines(r);
  map.panTo([r.latitude, r.longitude], {{ animate: true, duration: 0.5 }});

  // Panel 3: Inspector
  const b = r.building;
  const sp = r.spatial_relationships;
  document.getElementById("inspectFloorsBadge").innerText = `${{b.floor_notation}} &bull; ${{b.estimated_height_m}}m`;
  document.getElementById("insTitle").innerText = b.establishment_name;
  document.getElementById("insUsage").innerText = b.building_usage;
  document.getElementById("insFacade").innerText = b.facade_type;
  document.getElementById("insGround").innerText = b.ground_floor_activity;
  document.getElementById("insSpecial").innerText = b.special_features;
  document.getElementById("insMapsLink").href = b.official_links;

  document.getElementById("insPole").innerText = `${{sp.nearest_pole_id}} (${{sp.nearest_pole_distance_m}}m)`;
  document.getElementById("insPoleBurden").innerText = sp.nearest_pole_burden;
  document.getElementById("insTrans").innerText = `${{sp.nearest_transformer_id}} (${{sp.nearest_transformer_distance_m}}m &bull; ${{sp.transformer_scope}})`;
  document.getElementById("insLight").innerText = `${{sp.nearest_light_id}} (${{sp.nearest_light_distance_m}}m)`;
  document.getElementById("insChainage").innerText = `${{sp.chainage_m}}m &bull; ${{sp.road_offset_m}}m (${{sp.road_side}})`;

  // OCR
  if (r.ocr_detections && r.ocr_detections.length > 0) {{
    document.getElementById("insOcrCount").innerText = `${{r.ocr_detections.length}} Detected`;
    document.getElementById("insOcrText").innerText = r.ocr_detections.map(o => o.Cleaned_Text).join(" | ");
    document.getElementById("insOcrCat").innerText = r.ocr_detections[0].Commercial_Category || "Commercial Retail";
    document.getElementById("insOcrConf").innerText = `${{(r.ocr_detections[0].Confidence * 100).toFixed(1)}}%`;
  }} else {{
    document.getElementById("insOcrCount").innerText = "0 Detected";
    document.getElementById("insOcrText").innerText = "No commercial signboards detected";
    document.getElementById("insOcrCat").innerText = "None";
    document.getElementById("insOcrConf").innerText = "N/A";
  }}

  // Reference Cadastre
  const refBadge = document.getElementById("insRefBadge");
  if (sp.reference_status === "MATCHED") {{
    refBadge.className = "highlight-badge badge-matched";
    refBadge.innerText = "MATCHED";
  }} else {{
    refBadge.className = "highlight-badge badge-unmatched";
    refBadge.innerText = "UNMATCHED (AI Discovery)";
  }}
  document.getElementById("insRefSource").innerText = sp.reference_source;

  // Filmstrip active highlight
  document.querySelectorAll(".thumb-item").forEach(t => t.classList.remove("active"));
  const activeThumb = document.getElementById(`thumb_${{idx}}`);
  if (activeThumb) {{
    activeThumb.classList.add("active");
    activeThumb.scrollIntoView({{ behavior: "smooth", inline: "center" }});
  }}
}}

function toggleFloorLayer() {{
  showRecord(currentIndex);
}}

function nextImage() {{
  if (currentIndex < RECORDS.length - 1) {{
    showRecord(currentIndex + 1);
  }} else {{
    showRecord(0);
  }}
}}

function prevImage() {{
  if (currentIndex > 0) {{
    showRecord(currentIndex - 1);
  }} else {{
    showRecord(RECORDS.length - 1);
  }}
}}

function jumpToIndex(idx) {{
  showRecord(idx);
}}

function changeStreetFilter() {{
  const st = document.getElementById("streetFilter").value;
  if (st === "ALL") {{
    renderFilmstrip(RECORDS);
    showRecord(0);
  }} else {{
    const filtered = RECORDS.filter(r => r.street_id === st);
    renderFilmstrip(filtered);
    if (filtered.length > 0) {{
      showRecord(filtered[0].index);
    }}
  }}
}}

function renderFilmstrip(list) {{
  const strip = document.getElementById("filmstrip");
  strip.innerHTML = "";
  list.forEach(r => {{
    const div = document.createElement("div");
    div.className = "thumb-item";
    div.id = `thumb_${{r.index}}`;
    div.onclick = () => showRecord(r.index);
    div.innerHTML = `
      <img src="${{r.image_path}}" alt="${{r.image_id}}">
      <div class="thumb-label">${{r.street_id}} #${{r.capture_order}}</div>
    `;
    strip.appendChild(div);
  }});
}}

// Keyboard Navigation
window.addEventListener("keydown", (e) => {{
  if (e.key === "ArrowRight") nextImage();
  if (e.key === "ArrowLeft") prevImage();
}});

// Initial Launch
renderFilmstrip(RECORDS);
showRecord(0);
</script>
</body>
</html>
"""

with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {out_html_path} ({len(html_content)} bytes)")
