import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
bldg_json_path = os.path.join(base_dir, "building_intelligence.json")
out_html_path = os.path.join(base_dir, "building_explorer.html")

if not os.path.exists(bldg_json_path):
    print("building_intelligence.json does not exist yet.")
    sys.exit(1)

with open(bldg_json_path, "r", encoding="utf-8") as f:
    buildings = json.load(f)

# Build HTML content
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Building & Property Intelligence Explorer — FarmwiseAI Task 5</title>
<style>
  :root {{
    --bg-dark: #080c14;
    --panel-bg: #101726;
    --panel-border: #1b283d;
    --accent-cyan: #00f2fe;
    --accent-emerald: #00ff88;
    --accent-gold: #ffbe0b;
    --accent-magenta: #f72585;
    --text-primary: #e6edf8;
    --text-muted: #8899b0;
    --card-bg: #141e30;
    --card-hover: #1c2b44;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background-color: var(--bg-dark);
    color: var(--text-primary);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.5;
    padding-bottom: 60px;
  }}
  header {{
    background: linear-gradient(180deg, #121c2e 0%, #0a101c 100%);
    border-bottom: 1px solid var(--panel-border);
    padding: 24px 36px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.5);
  }}
  .badge-tag {{
    display: inline-block;
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    background: rgba(0, 242, 254, 0.15);
    color: var(--accent-cyan);
    border: 1px solid rgba(0, 242, 254, 0.35);
  }}
  h1 {{
    font-size: 26px;
    font-weight: 800;
    margin-top: 8px;
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  h1 span.title-gradient {{
    background: linear-gradient(90deg, #00f2fe, #4facfe, #00ff88);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .subtitle {{
    color: var(--text-muted);
    font-size: 14px;
    margin-top: 4px;
  }}
  .container {{
    max-width: 1600px;
    margin: 0 auto;
    padding: 24px 36px;
  }}
  /* Stats Dashboard */
  .stats-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
  }}
  .stat-card {{
    background: var(--panel-bg);
    border: 1px solid var(--panel-border);
    border-radius: 8px;
    padding: 16px 20px;
    position: relative;
    overflow: hidden;
  }}
  .stat-card::before {{
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: var(--accent-cyan);
  }}
  .stat-card.emerald::before {{ background: var(--accent-emerald); }}
  .stat-card.gold::before {{ background: var(--accent-gold); }}
  .stat-card.magenta::before {{ background: var(--accent-magenta); }}
  .stat-label {{
    font-size: 12px;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .stat-val {{
    font-size: 28px;
    font-weight: 800;
    color: #fff;
    margin-top: 4px;
  }}
  .stat-sub {{
    font-size: 11px;
    color: var(--text-muted);
    margin-top: 2px;
  }}
  /* Controls Panel */
  .controls-panel {{
    background: var(--panel-bg);
    border: 1px solid var(--panel-border);
    border-radius: 8px;
    padding: 18px 24px;
    margin-bottom: 24px;
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    align-items: center;
  }}
  .filter-group {{
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .filter-group label {{
    font-size: 11px;
    text-transform: uppercase;
    font-weight: 700;
    color: var(--text-muted);
    letter-spacing: 0.5px;
  }}
  .filter-group input, .filter-group select {{
    background: #0d131f;
    border: 1px solid #25354e;
    color: var(--text-primary);
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 13px;
    outline: none;
    min-width: 180px;
    transition: border-color 0.2s;
  }}
  .filter-group input:focus, .filter-group select:focus {{
    border-color: var(--accent-cyan);
  }}
  .reset-btn {{
    background: #1e2c44;
    border: 1px solid #33486a;
    color: #d0ddec;
    padding: 8px 16px;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 600;
    font-size: 13px;
    margin-top: auto;
    transition: all 0.2s;
  }}
  .reset-btn:hover {{
    background: #2a3d5e;
    color: #fff;
  }}
  /* Building Grid */
  .buildings-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 20px;
  }}
  .bldg-card {{
    background: var(--card-bg);
    border: 1px solid var(--panel-border);
    border-radius: 10px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
    cursor: pointer;
  }}
  .bldg-card:hover {{
    transform: translateY(-3px);
    border-color: var(--accent-cyan);
    box-shadow: 0 10px 28px rgba(0, 242, 254, 0.12);
  }}
  .img-wrapper {{
    position: relative;
    width: 100%;
    height: 200px;
    background: #05080f;
    overflow: hidden;
  }}
  .img-wrapper img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s;
  }}
  .bldg-card:hover .img-wrapper img {{
    transform: scale(1.03);
  }}
  .img-overlay-badge {{
    position: absolute;
    top: 10px;
    left: 10px;
    background: rgba(8, 12, 20, 0.85);
    border: 1px solid var(--accent-cyan);
    color: var(--accent-cyan);
    font-family: monospace;
    font-size: 12px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 4px;
    backdrop-filter: blur(4px);
  }}
  .floor-badge {{
    position: absolute;
    top: 10px;
    right: 10px;
    background: rgba(0, 255, 136, 0.9);
    color: #05140b;
    font-size: 11px;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 4px;
    letter-spacing: 0.5px;
  }}
  .card-body {{
    padding: 16px 18px;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    gap: 8px;
  }}
  .bldg-title {{
    font-size: 16px;
    font-weight: 700;
    color: #fff;
    line-height: 1.3;
  }}
  .bldg-street {{
    font-size: 12px;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .pill-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 4px;
  }}
  .pill {{
    font-size: 11px;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 4px;
    background: #19273c;
    color: #adc4e2;
    border: 1px solid #273d5e;
  }}
  .pill.usage {{
    background: rgba(255, 190, 11, 0.15);
    color: var(--accent-gold);
    border-color: rgba(255, 190, 11, 0.35);
  }}
  .pill.height {{
    background: rgba(0, 242, 254, 0.15);
    color: var(--accent-cyan);
    border-color: rgba(0, 242, 254, 0.35);
  }}
  .attr-table {{
    font-size: 12px;
    margin-top: 6px;
    border-top: 1px solid #1c2b42;
    padding-top: 8px;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }}
  .attr-row {{
    display: flex;
    justify-content: space-between;
    gap: 8px;
  }}
  .attr-k {{
    color: var(--text-muted);
    font-weight: 500;
  }}
  .attr-v {{
    color: #e0e9f6;
    font-weight: 600;
    text-align: right;
  }}
  .card-footer {{
    margin-top: auto;
    padding: 12px 18px;
    border-top: 1px solid var(--panel-border);
    background: #0d1422;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .maps-link {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    font-weight: 600;
    color: var(--accent-cyan);
    text-decoration: none;
    transition: color 0.2s;
  }}
  .maps-link:hover {{
    color: #fff;
    text-decoration: underline;
  }}
  .blueprint-btn {{
    font-size: 11px;
    font-weight: 700;
    background: #1b293d;
    border: 1px solid #2c4263;
    color: #b0c8e6;
    padding: 4px 10px;
    border-radius: 4px;
    cursor: pointer;
  }}
  .blueprint-btn:hover {{
    background: var(--accent-cyan);
    color: #080c14;
    border-color: var(--accent-cyan);
  }}
  /* Modal */
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
  .modal-backdrop.active {{
    display: flex;
  }}
  .modal-box {{
    background: #0f1624;
    border: 1px solid var(--panel-border);
    box-shadow: 0 16px 48px rgba(0,0,0,0.8);
    border-radius: 12px;
    max-width: 950px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
  }}
  .modal-header {{
    padding: 18px 24px;
    border-bottom: 1px solid var(--panel-border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #141c2c;
  }}
  .modal-close {{
    background: none;
    border: none;
    color: var(--text-muted);
    font-size: 24px;
    cursor: pointer;
    line-height: 1;
  }}
  .modal-close:hover {{ color: #fff; }}
  .modal-body {{
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }}
  .modal-img-container {{
    width: 100%;
    max-height: 480px;
    background: #000;
    border-radius: 8px;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 1px solid #1c2b42;
  }}
  .modal-img-container img {{
    max-width: 100%;
    max-height: 480px;
    object-fit: contain;
  }}
  .param-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 12px;
  }}
  .param-item {{
    background: #141e30;
    border: 1px solid #20304a;
    padding: 10px 14px;
    border-radius: 6px;
  }}
  .param-label {{
    font-size: 11px;
    color: var(--accent-cyan);
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.5px;
  }}
  .param-val {{
    font-size: 13px;
    font-weight: 600;
    color: #f0f4f8;
    margin-top: 3px;
  }}
</style>
</head>
<body>

<header>
  <div style="max-width: 1600px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
    <div>
      <span class="badge-tag">FarmwiseAI Task 5 &bull; Team 24</span>
      <h1><span class="title-gradient">Building & Property Intelligence Engine</span></h1>
      <p class="subtitle">Complete 10-Property Urban Architecture Catalog across 108 Street Captures &bull; Coimbatore Ward 29 (LGD: 29)</p>
    </div>
    <div style="display: flex; gap: 10px;">
      <a href="ocr_search_explorer.html" style="text-decoration:none; padding: 8px 14px; background: #162438; border: 1px solid #2b3f5c; color: var(--accent-cyan); border-radius: 6px; font-size: 12px; font-weight: 700;">&larr; OCR Explorer</a>
      <a href="urban_annotation_studio.html" style="text-decoration:none; padding: 8px 14px; background: #162438; border: 1px solid #2b3f5c; color: var(--accent-emerald); border-radius: 6px; font-size: 12px; font-weight: 700;">Annotation Studio &rarr;</a>
    </div>
  </div>
</header>

<div class="container">
  <!-- Stats Cards -->
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-label">Total Buildings Cataloged</div>
      <div class="stat-val">{len(buildings)}</div>
      <div class="stat-sub">100% of surveyed street transects</div>
    </div>
    <div class="stat-card emerald">
      <div class="stat-label">Surveyed Corridors</div>
      <div class="stat-val">10 Streets</div>
      <div class="stat-sub">2.49 km total road network</div>
    </div>
    <div class="stat-card gold">
      <div class="stat-label">Floor Height Span</div>
      <div class="stat-val">3.5m &ndash; 17.5m</div>
      <div class="stat-sub">Ground (G) up to 5-Story (G+4)</div>
    </div>
    <div class="stat-card magenta">
      <div class="stat-label">Geospatially Linked</div>
      <div class="stat-val">100% Mapped</div>
      <div class="stat-sub">With Google Maps Navigation</div>
    </div>
  </div>

  <!-- Filter & Search Controls -->
  <div class="controls-panel">
    <div class="filter-group">
      <label>Search Keyword</label>
      <input type="text" id="searchInput" placeholder="Search building or business...">
    </div>
    <div class="filter-group">
      <label>Street Corridor</label>
      <select id="streetFilter">
        <option value="ALL">All 10 Corridors</option>
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
    <div class="filter-group">
      <label>Floor Notation</label>
      <select id="floorFilter">
        <option value="ALL">All Floor Heights</option>
        <option value="G">G (Ground Only &bull; 3.5m)</option>
        <option value="G+1">G+1 (2 Floors &bull; 7.0m)</option>
        <option value="G+2">G+2 (3 Floors &bull; 10.5m)</option>
        <option value="G+3">G+3 (4 Floors &bull; 14.0m)</option>
        <option value="G+4">G+4 (5 Floors &bull; 17.5m)</option>
      </select>
    </div>
    <div class="filter-group">
      <label>Primary Usage</label>
      <select id="usageFilter">
        <option value="ALL">All Building Usages</option>
        <option value="Hotel">Hospitality & Dining</option>
        <option value="Banking">Banking & Financial</option>
        <option value="Retail">Commercial Retail</option>
        <option value="Residential">Residential Villas & Apts</option>
        <option value="Textile">Textile Showrooms</option>
        <option value="Automobile">Automobile & Fuel</option>
        <option value="Healthcare">Healthcare & Pharmacy</option>
        <option value="Religious">Religious Temples</option>
        <option value="Workshop">Industrial & Workshops</option>
      </select>
    </div>
    <button class="reset-btn" onclick="resetFilters()">Reset Filters</button>
    <div style="margin-left: auto; font-size: 13px; color: var(--text-muted);">
      Showing <span id="visibleCount" style="color:#fff; font-weight:700;">{len(buildings)}</span> / {len(buildings)} buildings
    </div>
  </div>

  <!-- Building Cards Grid -->
  <div class="buildings-grid" id="buildingsGrid">
    <!-- Populated by JavaScript -->
  </div>
</div>

<!-- Modal Dialog -->
<div class="modal-backdrop" id="bldgModal">
  <div class="modal-box">
    <div class="modal-header">
      <div>
        <span class="badge-tag" id="modalPassportTag">BLDG-ST01-001</span>
        <h2 id="modalTitle" style="font-size: 18px; margin-top: 4px; color: #fff;">Building Details</h2>
      </div>
      <button class="modal-close" onclick="closeModal()">&times;</button>
    </div>
    <div class="modal-body">
      <div class="modal-img-container">
        <img id="modalImg" src="" alt="Floor Segmentation Overlay">
      </div>
      <div class="param-grid">
        <div class="param-item">
          <div class="param-label">1. Building Passport ID</div>
          <div class="param-val" id="mParamId"></div>
        </div>
        <div class="param-item">
          <div class="param-label">2. Floors & Height</div>
          <div class="param-val" id="mParamFloors"></div>
        </div>
        <div class="param-item">
          <div class="param-label">3. Primary Usage</div>
          <div class="param-val" id="mParamUsage"></div>
        </div>
        <div class="param-item">
          <div class="param-label">4. Architectural Facade</div>
          <div class="param-val" id="mParamFacade"></div>
        </div>
        <div class="param-item">
          <div class="param-label">5. Construction Stage</div>
          <div class="param-val" id="mParamStage"></div>
        </div>
        <div class="param-item">
          <div class="param-label">6. Ground Floor Activity</div>
          <div class="param-val" id="mParamGround"></div>
        </div>
        <div class="param-item">
          <div class="param-label">7. Urban Density</div>
          <div class="param-val" id="mParamDensity"></div>
        </div>
        <div class="param-item">
          <div class="param-label">8. GPS Coordinates</div>
          <div class="param-val" id="mParamGPS"></div>
        </div>
        <div class="param-item" style="grid-column: 1 / -1;">
          <div class="param-label">9. Special Features & Amenities</div>
          <div class="param-val" id="mParamSpecial"></div>
        </div>
        <div class="param-item" style="grid-column: 1 / -1;">
          <div class="param-label">10. Detected OCR Signboards on Property</div>
          <div class="param-val" id="mParamOCR" style="color: var(--accent-gold);"></div>
        </div>
        <div class="param-item" style="grid-column: 1 / -1;">
          <div class="param-label">Official Place Navigation Link</div>
          <div class="param-val"><a id="mParamLink" href="" target="_blank" style="color: var(--accent-cyan); text-decoration: underline;">Open Google Maps Place Pin &rarr;</a></div>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
const BUILDINGS = {json.dumps(buildings, ensure_ascii=False)};

function renderCards(list) {{
  const grid = document.getElementById("buildingsGrid");
  grid.innerHTML = "";
  document.getElementById("visibleCount").innerText = list.length;

  list.forEach(b => {{
    const card = document.createElement("div");
    card.className = "bldg-card";
    card.onclick = () => openModal(b);

    card.innerHTML = `
      <div class="img-wrapper">
        <img src="${{b.Annotated_Floor_Image}}" alt="${{b.Building_ID}}" loading="lazy">
        <div class="img-overlay-badge">${{b.Building_ID}}</div>
        <div class="floor-badge">${{b.Floor_Notation}} &bull; ${{b.Estimated_Height_m}}m</div>
      </div>
      <div class="card-body">
        <div class="bldg-title">${{b.Establishment_Name}}</div>
        <div class="bldg-street">
          <svg width="12" height="12" fill="currentColor" viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
          ${{b.Street_Name}}
        </div>
        <div class="pill-row">
          <span class="pill usage">${{b.Building_Usage.split("&")[0].trim()}}</span>
          <span class="pill height">${{b.Building_Floors}} Story (${{b.Estimated_Height_m}}m)</span>
          <span class="pill">${{b.Ground_Floor_Activity.split("&")[0].trim()}}</span>
        </div>
        <div class="attr-table">
          <div class="attr-row">
            <span class="attr-k">Facade:</span>
            <span class="attr-v">${{b.Facade_Type.split("&")[0].trim()}}</span>
          </div>
          <div class="attr-row">
            <span class="attr-k">OCR Signs:</span>
            <span class="attr-v">${{b.Detected_Signboards_Count}} detected</span>
          </div>
        </div>
      </div>
      <div class="card-footer" onclick="event.stopPropagation()">
        <a class="maps-link" href="${{b.Official_Links}}" target="_blank">
          <svg width="12" height="12" fill="currentColor" viewBox="0 0 16 16"><path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0zm3.5 7.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z"/></svg>
          Google Maps
        </a>
        <button class="blueprint-btn" onclick="openModalById('${{b.Building_ID}}')">Inspect Blueprint &rarr;</button>
      </div>
    `;
    grid.appendChild(card);
  }});
}}

function filterBuildings() {{
  const q = document.getElementById("searchInput").value.toLowerCase();
  const st = document.getElementById("streetFilter").value;
  const fl = document.getElementById("floorFilter").value;
  const us = document.getElementById("usageFilter").value.toLowerCase();

  const filtered = BUILDINGS.filter(b => {{
    const matchQ = !q || b.Establishment_Name.toLowerCase().includes(q) || b.Building_ID.toLowerCase().includes(q) || b.Building_Usage.toLowerCase().includes(q) || b.Detected_OCR_Text.toLowerCase().includes(q);
    const matchSt = st === "ALL" || b.Street_ID === st;
    const matchFl = fl === "ALL" || b.Floor_Notation === fl;
    const matchUs = us === "all" || b.Building_Usage.toLowerCase().includes(us);
    return matchQ && matchSt && matchFl && matchUs;
  }});

  renderCards(filtered);
}}

function resetFilters() {{
  document.getElementById("searchInput").value = "";
  document.getElementById("streetFilter").value = "ALL";
  document.getElementById("floorFilter").value = "ALL";
  document.getElementById("usageFilter").value = "ALL";
  renderCards(BUILDINGS);
}}

function openModal(b) {{
  document.getElementById("modalPassportTag").innerText = b.Building_ID;
  document.getElementById("modalTitle").innerText = b.Establishment_Name;
  document.getElementById("modalImg").src = b.Annotated_Floor_Image;
  document.getElementById("mParamId").innerText = `${{b.Building_ID}} (Legacy: ${{b.Legacy_Building_ID}})`;
  document.getElementById("mParamFloors").innerText = `${{b.Floor_Notation}} (${{b.Building_Floors}} Floors) &bull; ${{b.Estimated_Height_m}}m Height`;
  document.getElementById("mParamUsage").innerText = b.Building_Usage;
  document.getElementById("mParamFacade").innerText = b.Facade_Type;
  document.getElementById("mParamStage").innerText = b.Construction_Stage;
  document.getElementById("mParamGround").innerText = b.Ground_Floor_Activity;
  document.getElementById("mParamDensity").innerText = b.Building_Density;
  document.getElementById("mParamGPS").innerText = `${{b.Latitude.toFixed(6)}}°N, ${{b.Longitude.toFixed(6)}}°E &bull; ${{b.Street_Name}}`;
  document.getElementById("mParamSpecial").innerText = b.Special_Features;
  document.getElementById("mParamOCR").innerText = b.Detected_OCR_Text !== "None Detected" ? b.Detected_OCR_Text : "No commercial signboards detected on building envelope.";
  document.getElementById("mParamLink").href = b.Official_Links;

  document.getElementById("bldgModal").classList.add("active");
}}

function openModalById(id) {{
  const b = BUILDINGS.find(x => x.Building_ID === id);
  if (b) openModal(b);
}}

function closeModal() {{
  document.getElementById("bldgModal").classList.remove("active");
}}

document.getElementById("searchInput").addEventListener("input", filterBuildings);
document.getElementById("streetFilter").addEventListener("change", filterBuildings);
document.getElementById("floorFilter").addEventListener("change", filterBuildings);
document.getElementById("usageFilter").addEventListener("change", filterBuildings);

// Initial Render
renderCards(BUILDINGS);
</script>
</body>
</html>
"""

with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {out_html_path} ({len(html_content)} bytes)")
