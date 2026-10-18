import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
assets_geojson_path = os.path.join(base_dir, "urban_assets_digital_twin.geojson")
roads_geojson_path = os.path.join(base_dir, "road_network_topology.geojson")
study_area_path = r"D:\Study_area.geojson"
metrics_json_path = os.path.join(base_dir, "spatial_engine_metrics.json")
out_html_path = os.path.join(base_dir, "gis_digital_twin_baseline.html")

with open(assets_geojson_path, "r", encoding="utf-8") as f:
    assets_data = json.load(f)

with open(roads_geojson_path, "r", encoding="utf-8") as f:
    roads_data = json.load(f)

with open(study_area_path, "r", encoding="utf-8") as f:
    boundary_data = json.load(f)

with open(metrics_json_path, "r", encoding="utf-8") as f:
    metrics_data = json.load(f)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GIS Digital Twin Baseline — FarmwiseAI Task 5</title>
<!-- Leaflet CSS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<style>
  :root {{
    --bg-dark: #070a10;
    --panel-bg: rgba(12, 18, 28, 0.94);
    --panel-border: #1a273b;
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
  }}
  #map {{
    width: 100%;
    height: 100%;
    background: #090e17;
  }}
  /* Top HUD Bar */
  .top-hud {{
    position: absolute;
    top: 16px;
    left: 16px;
    right: 16px;
    z-index: 1000;
    background: var(--panel-bg);
    border: 1px solid var(--panel-border);
    backdrop-filter: blur(10px);
    border-radius: 10px;
    padding: 12px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 8px 32px rgba(0,0,0,0.6);
  }}
  .hud-title-wrap {{
    display: flex;
    align-items: center;
    gap: 14px;
  }}
  .badge-tag {{
    padding: 3px 9px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    background: rgba(0, 242, 254, 0.15);
    color: var(--accent-cyan);
    border: 1px solid rgba(0, 242, 254, 0.35);
  }}
  .hud-title {{
    font-size: 16px;
    font-weight: 800;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .hud-title span {{
    background: linear-gradient(90deg, #00f2fe, #00ff88);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .kpi-row {{
    display: flex;
    gap: 20px;
  }}
  .kpi-item {{
    text-align: right;
  }}
  .kpi-k {{
    font-size: 10px;
    text-transform: uppercase;
    color: var(--text-muted);
    font-weight: 700;
    letter-spacing: 0.5px;
  }}
  .kpi-v {{
    font-size: 16px;
    font-weight: 800;
    color: #fff;
  }}
  /* Sidebar Controls Drawer */
  .control-drawer {{
    position: absolute;
    top: 86px;
    left: 16px;
    z-index: 1000;
    width: 320px;
    max-height: calc(100vh - 110px);
    background: var(--panel-bg);
    border: 1px solid var(--panel-border);
    backdrop-filter: blur(10px);
    border-radius: 10px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 14px;
    overflow-y: auto;
    box-shadow: 0 8px 32px rgba(0,0,0,0.6);
  }}
  .control-section {{
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .section-label {{
    font-size: 11px;
    text-transform: uppercase;
    font-weight: 700;
    color: var(--text-muted);
    letter-spacing: 0.5px;
    margin-bottom: 2px;
  }}
  select, input {{
    background: #090e17;
    border: 1px solid #1c2a3e;
    color: var(--text-primary);
    padding: 8px 10px;
    border-radius: 6px;
    font-size: 12px;
    outline: none;
    width: 100%;
  }}
  select:focus, input:focus {{ border-color: var(--accent-cyan); }}
  
  .legend-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-top: 4px;
  }}
  .legend-item {{
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    font-weight: 600;
    cursor: pointer;
    user-select: none;
  }}
  .legend-dot {{
    width: 10px;
    height: 10px;
    border-radius: 50%;
    display: inline-block;
  }}
  .ref-filter-row {{
    display: flex;
    gap: 6px;
  }}
  .ref-btn {{
    flex: 1;
    padding: 6px 8px;
    background: #090e17;
    border: 1px solid #1c2a3e;
    color: var(--text-muted);
    font-size: 11px;
    font-weight: 700;
    border-radius: 6px;
    cursor: pointer;
    text-align: center;
  }}
  .ref-btn.active {{
    background: rgba(0, 242, 254, 0.15);
    border-color: var(--accent-cyan);
    color: var(--accent-cyan);
  }}

  /* Bottom Right Topology HUD */
  .topology-hud {{
    position: absolute;
    bottom: 24px;
    right: 16px;
    z-index: 1000;
    width: 380px;
    background: var(--panel-bg);
    border: 1px solid var(--panel-border);
    backdrop-filter: blur(10px);
    border-radius: 10px;
    padding: 16px 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.6);
    display: none;
  }}
  .topology-hud.active {{ display: block; }}
  .topo-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #1a273b;
    padding-bottom: 8px;
    margin-bottom: 10px;
  }}
  .topo-close {{
    background: none;
    border: none;
    color: var(--text-muted);
    font-size: 18px;
    cursor: pointer;
  }}
  .topo-item {{
    background: #090e17;
    border: 1px solid #182436;
    border-radius: 6px;
    padding: 8px 10px;
    margin-bottom: 6px;
    font-size: 12px;
  }}
  .topo-k {{ color: var(--text-muted); font-size: 10px; text-transform: uppercase; font-weight: 700; }}
  .topo-v {{ color: #e0ebf8; font-weight: 600; margin-top: 2px; }}

  /* Leaflet Popups */
  .leaflet-popup-content-wrapper {{
    background: #0d1522 !important;
    border: 1px solid #20314a !important;
    color: #e4edf8 !important;
    border-radius: 8px !important;
    box-shadow: 0 8px 32px rgba(0,0,0,0.7) !important;
  }}
  .leaflet-popup-tip {{ background: #0d1522 !important; }}
  .popup-title {{
    font-size: 13px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 4px;
  }}
  .popup-meta {{
    font-size: 11px;
    color: var(--text-muted);
    line-height: 1.4;
  }}
  .popup-badge {{
    display: inline-block;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: 700;
    margin-top: 6px;
  }}
</style>
</head>
<body>

<div id="map"></div>

<!-- Top HUD Bar -->
<div class="top-hud">
  <div class="hud-title-wrap">
    <span class="badge-tag">FarmwiseAI Task 5 &bull; Team 24</span>
    <div class="hud-title"><span>GIS Digital Twin Baseline</span> &bull; Coimbatore Ward 29 (LGD: 29)</div>
  </div>
  <div class="kpi-row">
    <div class="kpi-item">
      <div class="kpi-k">Total Fixed Assets</div>
      <div class="kpi-v" style="color:var(--accent-cyan);">{len(assets_data["features"])}</div>
    </div>
    <div class="kpi-item">
      <div class="kpi-k">Reference Matched</div>
      <div class="kpi-v" style="color:var(--accent-emerald);">{metrics_data["reference_matching_summary"]["total_matched_assets"]}</div>
    </div>
    <div class="kpi-item">
      <div class="kpi-k">AI Discoveries</div>
      <div class="kpi-v" style="color:var(--accent-gold);">{metrics_data["reference_matching_summary"]["total_unmatched_new_discoveries"]}</div>
    </div>
    <div class="kpi-item">
      <div class="kpi-k">Surveyed Network</div>
      <div class="kpi-v">2.49 km</div>
    </div>
  </div>
</div>

<!-- Controls Drawer -->
<div class="control-drawer">
  <div class="control-section">
    <div class="section-label">Corridor Filter</div>
    <select id="streetSelect" onchange="applyFilters()">
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
  </div>

  <div class="control-section">
    <div class="section-label">Reference Baseline Status</div>
    <div class="ref-filter-row">
      <div class="ref-btn active" id="btnAllRef" onclick="setRefFilter('ALL')">All</div>
      <div class="ref-btn" id="btnMatched" onclick="setRefFilter('MATCHED')">Matched ({metrics_data["reference_matching_summary"]["total_matched_assets"]})</div>
      <div class="ref-btn" id="btnUnmatched" onclick="setRefFilter('UNMATCHED')">Unmatched ({metrics_data["reference_matching_summary"]["total_unmatched_new_discoveries"]})</div>
    </div>
  </div>

  <div class="control-section">
    <div class="section-label">Asset Layer Legend</div>
    <div class="legend-grid">
      <label class="legend-item"><input type="checkbox" checked id="chk_building" onchange="applyFilters()"><span class="legend-dot" style="background:var(--accent-emerald);"></span> Buildings (108)</label>
      <label class="legend-item"><input type="checkbox" checked id="chk_electric_pole" onchange="applyFilters()"><span class="legend-dot" style="background:var(--accent-orange);"></span> Poles (108)</label>
      <label class="legend-item"><input type="checkbox" checked id="chk_streetlight" onchange="applyFilters()"><span class="legend-dot" style="background:var(--accent-gold);"></span> Streetlights (108)</label>
      <label class="legend-item"><input type="checkbox" checked id="chk_transformer" onchange="applyFilters()"><span class="legend-dot" style="background:var(--accent-red);"></span> Transformers (24)</label>
      <label class="legend-item"><input type="checkbox" checked id="chk_traffic_signal" onchange="applyFilters()"><span class="legend-dot" style="background:var(--accent-magenta);"></span> Signals (9)</label>
      <label class="legend-item"><input type="checkbox" checked id="chk_commercial_sign" onchange="applyFilters()"><span class="legend-dot" style="background:var(--accent-cyan);"></span> Signs (108)</label>
    </div>
  </div>

  <div class="control-section" style="margin-top:auto; padding-top:10px; border-top:1px solid #1a273b;">
    <div style="font-size:11px; color:var(--text-muted); line-height:1.4;">
      <strong style="color:#fff;">Topology Graph Engine:</strong><br>
      Click any building (<span style="color:var(--accent-emerald); font-weight:700;">green marker</span>) to render live spatial spider-lines connecting it to its nearest electric pole (<span style="color:var(--accent-gold);">amber</span>) and transformer (<span style="color:var(--accent-red);">red</span>).
    </div>
  </div>
</div>

<!-- Bottom Right Topology HUD Card -->
<div class="topology-hud" id="topoHud">
  <div class="topo-header">
    <span class="badge-tag" id="hudBuildingId">BLDG-ST01-001</span>
    <button class="topo-close" onclick="closeTopologyHud()">&times;</button>
  </div>
  <div style="font-size:14px; font-weight:700; color:#fff; margin-bottom:8px;" id="hudBuildingName">Building Title</div>
  
  <div class="topo-item">
    <div class="topo-k">Spatial Position & Corridor Offset</div>
    <div class="topo-v" id="hudChainage">Chainage: 0.0m &bull; Offset: +14.2m (Right)</div>
  </div>

  <div class="topo-item" style="border-left: 3px solid var(--accent-gold);">
    <div class="topo-k" style="color:var(--accent-gold);">1. Nearest Electric Utility Pole</div>
    <div class="topo-v" id="hudPole">POLE-ST01-001 &bull; 15.2m Distance</div>
  </div>

  <div class="topo-item" style="border-left: 3px solid var(--accent-red);">
    <div class="topo-k" style="color:var(--accent-red);">2. Nearest Distribution Transformer</div>
    <div class="topo-v" id="hudTrans">TRANS-ST01-001 &bull; 45.8m Distance</div>
  </div>

  <div class="topo-item">
    <div class="topo-k">Reference Cross-Match Status</div>
    <div class="topo-v" id="hudRef">MATCHED &bull; OpenStreetMap Cadastre</div>
  </div>
</div>

<!-- Leaflet JS -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
// Embedded Data
const ASSETS_DATA = {json.dumps(assets_data, ensure_ascii=False)};
const ROADS_DATA = {json.dumps(roads_data, ensure_ascii=False)};
const BOUNDARY_DATA = {json.dumps(boundary_data, ensure_ascii=False)};

// Initialize Map
const map = L.map("map", {{
  zoomControl: false,
  attributionControl: false
}}).setView([11.0345, 76.9745], 15);

L.control.zoom({{ position: "bottomleft" }}).addTo(map);

// Dark Matter Basemap
L.tileLayer("https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png", {{
  maxZoom: 20,
  subdomains: "abcd"
}}).addTo(map);

// 1. Boundary Layer (Ward 29)
const boundaryLayer = L.geoJSON(BOUNDARY_DATA, {{
  style: {{
    color: "#00f2fe",
    weight: 2,
    dashArray: "6, 6",
    fillColor: "#00f2fe",
    fillOpacity: 0.04
  }}
}}).addTo(map);

// 2. Road Network Layer (10 Surveyed Streets)
const roadsLayer = L.geoJSON(ROADS_DATA, {{
  style: {{
    color: "#00f2fe",
    weight: 4,
    opacity: 0.85
  }},
  onEachFeature: (feature, layer) => {{
    const p = feature.properties;
    layer.bindTooltip(`<strong>${{p.street_id}}: ${{p.street_name}}</strong><br>Length: ${{p.length_m}}m &bull; Assets: ${{p.total_fixed_assets}}`, {{
      sticky: true,
      className: "custom-road-tooltip"
    }});
  }}
}}).addTo(map);

// 3. Asset Markers Layer
let markers = [];
let topologyLines = [];
let currentRefFilter = "ALL";

const classColors = {{
  building: "#00ff88",
  electric_pole: "#fb5607",
  streetlight: "#ffbe0b",
  transformer: "#ff0055",
  traffic_signal: "#f72585",
  commercial_sign: "#00f2fe"
}};

function createMarker(f) {{
  const p = f.properties;
  const coords = f.geometry.coordinates;
  const color = classColors[p.asset_class] || "#ffffff";
  const isBldg = p.asset_class === "building";

  const radius = isBldg ? 7 : (p.asset_class === "transformer" || p.asset_class === "traffic_signal" ? 6 : 4.5);

  const marker = L.circleMarker([coords[1], coords[0]], {{
    radius: radius,
    fillColor: color,
    color: "#070a10",
    weight: 1.5,
    opacity: 1,
    fillOpacity: 0.9
  }});

  // Popup
  const refBadge = p.reference_status === "MATCHED" 
    ? `<span class="popup-badge" style="background:rgba(0,255,136,0.2); color:#00ff88; border:1px solid #00ff88;">MATCHED &bull; OSM Cadastre</span>`
    : `<span class="popup-badge" style="background:rgba(255,190,11,0.2); color:#ffbe0b; border:1px solid #ffbe0b;">UNMATCHED &bull; AI Discovery</span>`;

  marker.bindPopup(`
    <div class="popup-title">${{p.asset_id}}</div>
    <div class="popup-meta">
      <strong>${{p.asset_subtype}}</strong><br>
      Corridor: ${{p.street_name}} (${{p.street_id}})<br>
      Chainage: ${{p.chainage_m}}m &bull; Offset: ${{p.road_offset_m}}m<br>
      Authority: ${{p.managing_authority.split("(")[0].trim()}}<br>
      ${{refBadge}}
    </div>
  `);

  if (isBldg) {{
    marker.on("click", () => renderBuildingTopology(f));
  }}

  marker.feature = f;
  return marker;
}}

ASSETS_DATA.features.forEach(f => {{
  const m = createMarker(f);
  markers.push(m);
  m.addTo(map);
}});

// 4. Dynamic Topology Graph Visualizer (Spider Lines)
function renderBuildingTopology(f) {{
  // Clear previous topology lines
  topologyLines.forEach(l => map.removeLayer(l));
  topologyLines = [];

  const p = f.properties;
  const bCoords = [f.geometry.coordinates[1], f.geometry.coordinates[0]];

  // Line to nearest pole
  if (p.nearest_pole_coord) {{
    const pCoords = [p.nearest_pole_coord[1], p.nearest_pole_coord[0]];
    const poleLine = L.polyline([bCoords, pCoords], {{
      color: "#ffbe0b",
      weight: 2.5,
      dashArray: "5, 5",
      opacity: 0.95
    }}).addTo(map);
    topologyLines.push(poleLine);
  }}

  // Line to nearest transformer
  if (p.nearest_transformer_coord) {{
    const tCoords = [p.nearest_transformer_coord[1], p.nearest_transformer_coord[0]];
    const transLine = L.polyline([bCoords, tCoords], {{
      color: "#ff0055",
      weight: 2.5,
      dashArray: "4, 6",
      opacity: 0.95
    }}).addTo(map);
    topologyLines.push(transLine);
  }}

  // Open Topology HUD
  document.getElementById("hudBuildingId").innerText = p.asset_id;
  document.getElementById("hudBuildingName").innerText = p.asset_subtype;
  document.getElementById("hudChainage").innerText = `Chainage: ${{p.chainage_m}}m &bull; Offset: ${{p.road_offset_m}}m (${{p.road_side}})`;
  document.getElementById("hudPole").innerText = `${{p.nearest_pole_id}} &bull; ${{p.nearest_pole_dist_m}}m Distance`;
  document.getElementById("hudTrans").innerText = `${{p.nearest_transformer_id}} &bull; ${{p.nearest_transformer_dist_m}}m Distance`;
  document.getElementById("hudRef").innerText = `${{p.reference_status}} &bull; ${{p.reference_source}}`;
  document.getElementById("topoHud").classList.add("active");
}}

function closeTopologyHud() {{
  document.getElementById("topoHud").classList.remove("active");
  topologyLines.forEach(l => map.removeLayer(l));
  topologyLines = [];
}}

// 5. Filtering Logic
function applyFilters() {{
  const street = document.getElementById("streetSelect").value;
  const allowedClasses = [];
  ["building", "electric_pole", "streetlight", "transformer", "traffic_signal", "commercial_sign"].forEach(cls => {{
    if (document.getElementById(`chk_${{cls}}`).checked) allowedClasses.push(cls);
  }});

  markers.forEach(m => {{
    const f = m.feature;
    const p = f.properties;

    const matchStreet = street === "ALL" || p.street_id === street;
    const matchClass = allowedClasses.includes(p.asset_class);
    const matchRef = currentRefFilter === "ALL" || p.reference_status === currentRefFilter;

    if (matchStreet && matchClass && matchRef) {{
      if (!map.hasLayer(m)) map.addLayer(m);
    }} else {{
      if (map.hasLayer(m)) map.removeLayer(m);
    }}
  }});

  // If specific street selected, fly to it
  if (street !== "ALL") {{
    const rd = ROADS_DATA.features.find(r => r.properties.street_id === street);
    if (rd) {{
      const b = L.geoJSON(rd).getBounds();
      map.fitBounds(b, {{ padding: [100, 100], maxZoom: 18 }});
    }}
  }} else {{
    map.fitBounds(boundaryLayer.getBounds(), {{ padding: [40, 40] }});
  }}
}}

function setRefFilter(val) {{
  currentRefFilter = val;
  document.querySelectorAll(".ref-btn").forEach(b => b.classList.remove("active"));
  if (val === "ALL") document.getElementById("btnAllRef").classList.add("active");
  if (val === "MATCHED") document.getElementById("btnMatched").classList.add("active");
  if (val === "UNMATCHED") document.getElementById("btnUnmatched").classList.add("active");
  applyFilters();
}}

// Initial Bounds
map.fitBounds(boundaryLayer.getBounds(), {{ padding: [40, 40] }});
</script>
</body>
</html>
"""

with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {out_html_path} ({len(html_content)} bytes)")
