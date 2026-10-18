import os
import sys
import json
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
passports_json = os.path.join(base_dir, "urban_asset_passports.json")
density_csv = os.path.join(base_dir, "urban_asset_density_summary.csv")
out_html_path = os.path.join(base_dir, "asset_inventory_explorer.html")

with open(passports_json, "r", encoding="utf-8") as f:
    passports = json.load(f)

df_density = pd.read_csv(density_csv)
density_records = df_density.to_dict(orient="records")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Urban Asset Digital Passport & Inventory — FarmwiseAI Task 5</title>
<style>
  :root {{
    --bg-dark: #070b12;
    --panel-bg: #0f1624;
    --panel-border: #1a273b;
    --accent-cyan: #00f2fe;
    --accent-emerald: #00ff88;
    --accent-gold: #ffbe0b;
    --accent-orange: #fb5607;
    --accent-magenta: #f72585;
    --accent-red: #ff0055;
    --text-primary: #e8eef8;
    --text-muted: #8395ad;
    --card-bg: #131c2e;
    --card-hover: #1b2842;
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
    background: linear-gradient(180deg, #101726 0%, #080d17 100%);
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
    background: linear-gradient(90deg, #00f2fe, #ffbe0b, #00ff88);
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
  /* KPI Stats Bar */
  .stats-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 14px;
    margin-bottom: 24px;
  }}
  .stat-card {{
    background: var(--panel-bg);
    border: 1px solid var(--panel-border);
    border-radius: 8px;
    padding: 14px 18px;
    position: relative;
    overflow: hidden;
  }}
  .stat-card::before {{
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: var(--accent-cyan);
  }}
  .stat-card.pole::before {{ background: var(--accent-orange); }}
  .stat-card.light::before {{ background: var(--accent-gold); }}
  .stat-card.trans::before {{ background: var(--accent-red); }}
  .stat-card.sig::before {{ background: var(--accent-magenta); }}
  .stat-card.bldg::before {{ background: var(--accent-emerald); }}
  .stat-label {{
    font-size: 11px;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .stat-val {{
    font-size: 26px;
    font-weight: 800;
    color: #fff;
    margin-top: 2px;
  }}
  .stat-sub {{
    font-size: 11px;
    color: var(--text-muted);
    margin-top: 2px;
  }}
  /* Density Table Collapsible */
  .collapsible-box {{
    background: var(--panel-bg);
    border: 1px solid var(--panel-border);
    border-radius: 8px;
    margin-bottom: 24px;
    overflow: hidden;
  }}
  .collapsible-header {{
    padding: 14px 20px;
    background: #141c2c;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 700;
    font-size: 14px;
    color: #fff;
    user-select: none;
  }}
  .collapsible-header:hover {{ background: #1a2538; }}
  .collapsible-body {{
    display: block;
    overflow-x: auto;
    padding: 16px 20px;
  }}
  .density-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
    text-align: left;
  }}
  .density-table th {{
    background: #0d1422;
    padding: 10px 12px;
    color: var(--accent-cyan);
    font-weight: 700;
    text-transform: uppercase;
    font-size: 11px;
    border-bottom: 1px solid var(--panel-border);
  }}
  .density-table td {{
    padding: 10px 12px;
    border-bottom: 1px solid #162234;
    color: #d8e2f0;
  }}
  .density-table tr:hover td {{ background: #152033; }}
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
    background: #0b111c;
    border: 1px solid #223249;
    color: var(--text-primary);
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 13px;
    outline: none;
    min-width: 170px;
  }}
  .filter-group input:focus, .filter-group select:focus {{
    border-color: var(--accent-cyan);
  }}
  .reset-btn {{
    background: #19273c;
    border: 1px solid #2d4263;
    color: #c8d8ec;
    padding: 8px 16px;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 600;
    font-size: 13px;
    margin-top: auto;
  }}
  .reset-btn:hover {{ background: #263a58; color: #fff; }}
  /* Asset Grid */
  .assets-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 20px;
  }}
  .asset-card {{
    background: var(--card-bg);
    border: 1px solid var(--panel-border);
    border-radius: 10px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
    cursor: pointer;
  }}
  .asset-card:hover {{
    transform: translateY(-3px);
    border-color: var(--accent-cyan);
    box-shadow: 0 10px 24px rgba(0, 242, 254, 0.1);
  }}
  .card-top {{
    padding: 14px 18px;
    background: #0d1524;
    border-bottom: 1px solid #1a273c;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .asset-passport-id {{
    font-family: monospace;
    font-size: 13px;
    font-weight: 700;
    color: var(--accent-cyan);
  }}
  .type-badge {{
    font-size: 11px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 4px;
    text-transform: uppercase;
  }}
  .badge-pole {{ background: rgba(251, 86, 7, 0.2); color: #ff7d3b; border: 1px solid rgba(251, 86, 7, 0.4); }}
  .badge-light {{ background: rgba(255, 190, 11, 0.2); color: #ffd152; border: 1px solid rgba(255, 190, 11, 0.4); }}
  .badge-trans {{ background: rgba(255, 0, 85, 0.2); color: #ff5288; border: 1px solid rgba(255, 0, 85, 0.4); }}
  .badge-sig {{ background: rgba(247, 37, 133, 0.2); color: #ff60aa; border: 1px solid rgba(247, 37, 133, 0.4); }}
  .badge-bldg {{ background: rgba(0, 255, 136, 0.2); color: #38ef7d; border: 1px solid rgba(0, 255, 136, 0.4); }}
  .badge-sign {{ background: rgba(0, 242, 254, 0.2); color: #52e5ff; border: 1px solid rgba(0, 242, 254, 0.4); }}
  
  .card-body {{
    padding: 16px 18px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    flex-grow: 1;
  }}
  .asset-title {{
    font-size: 15px;
    font-weight: 700;
    color: #fff;
    line-height: 1.3;
  }}
  .asset-meta-row {{
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
    padding: 2px 7px;
    border-radius: 4px;
    background: #172437;
    color: #b0c6e0;
    border: 1px solid #233752;
  }}
  .pill.priority-high {{ background: rgba(255, 0, 85, 0.15); color: #ff4d80; border-color: rgba(255, 0, 85, 0.35); }}
  .pill.priority-med {{ background: rgba(255, 190, 11, 0.15); color: #ffbe0b; border-color: rgba(255, 190, 11, 0.35); }}
  .pill.priority-low {{ background: rgba(0, 255, 136, 0.15); color: #00ff88; border-color: rgba(0, 255, 136, 0.35); }}
  
  .specs-box {{
    background: #0c121e;
    border: 1px solid #1a273b;
    border-radius: 6px;
    padding: 10px 12px;
    margin-top: 6px;
    font-size: 12px;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }}
  .spec-item {{
    display: flex;
    justify-content: space-between;
    gap: 8px;
  }}
  .spec-k {{ color: var(--text-muted); }}
  .spec-v {{ color: #e4edf8; font-weight: 600; text-align: right; }}

  .card-footer {{
    padding: 12px 18px;
    border-top: 1px solid var(--panel-border);
    background: #0d1422;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: auto;
  }}
  .card-footer a {{
    font-size: 12px;
    font-weight: 600;
    color: var(--accent-cyan);
    text-decoration: none;
  }}
  .card-footer a:hover {{ text-decoration: underline; }}
  .passport-btn {{
    font-size: 11px;
    font-weight: 700;
    background: #1b283d;
    border: 1px solid #2b3f5c;
    color: #adc7e6;
    padding: 4px 10px;
    border-radius: 4px;
    cursor: pointer;
  }}
  .passport-btn:hover {{
    background: var(--accent-cyan);
    color: #070b12;
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
  .modal-backdrop.active {{ display: flex; }}
  .modal-box {{
    background: #0f1624;
    border: 1px solid var(--panel-border);
    box-shadow: 0 16px 48px rgba(0,0,0,0.8);
    border-radius: 12px;
    max-width: 900px;
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
  }}
  .modal-body {{
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 18px;
  }}
  .passport-seal-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #141e30;
    border: 1px solid #22344f;
    padding: 14px 20px;
    border-radius: 8px;
  }}
  .param-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 12px;
  }}
  .param-item {{
    background: #121b2c;
    border: 1px solid #1f2e46;
    padding: 10px 14px;
    border-radius: 6px;
  }}
  .param-label {{
    font-size: 11px;
    color: var(--accent-cyan);
    text-transform: uppercase;
    font-weight: 700;
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
      <h1><span class="title-gradient">Urban Asset Digital Passport & Inventory Engine</span></h1>
      <p class="subtitle">Complete Municipal Registry of 465 Fixed Infrastructure Assets &bull; Coimbatore Ward 29 (LGD: 29)</p>
    </div>
    <div style="display: flex; gap: 10px;">
      <a href="building_explorer.html" style="text-decoration:none; padding: 8px 14px; background: #162438; border: 1px solid #2b3f5c; color: var(--accent-emerald); border-radius: 6px; font-size: 12px; font-weight: 700;">&larr; Building Explorer</a>
      <a href="ocr_search_explorer.html" style="text-decoration:none; padding: 8px 14px; background: #162438; border: 1px solid #2b3f5c; color: var(--accent-cyan); border-radius: 6px; font-size: 12px; font-weight: 700;">OCR Search &rarr;</a>
    </div>
  </div>
</header>

<div class="container">
  <!-- KPI Stats Grid -->
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-label">Total Assets Registered</div>
      <div class="stat-val">{len(passports)}</div>
      <div class="stat-sub">Across 10 Corridors (2.49 km)</div>
    </div>
    <div class="stat-card pole">
      <div class="stat-label">Electric Utility Poles</div>
      <div class="stat-val">108</div>
      <div class="stat-sub">TANGEDCO Distribution Network</div>
    </div>
    <div class="stat-card light">
      <div class="stat-label">Streetlight Luminaires</div>
      <div class="stat-val">108</div>
      <div class="stat-sub">CCMC Energy Efficient LEDs</div>
    </div>
    <div class="stat-card trans">
      <div class="stat-label">Distribution Transformers</div>
      <div class="stat-val">24</div>
      <div class="stat-sub">11kV / 433V Substations</div>
    </div>
    <div class="stat-card sig">
      <div class="stat-label">Traffic Signal Posts</div>
      <div class="stat-val">9</div>
      <div class="stat-sub">Highway & Collector Intersections</div>
    </div>
    <div class="stat-card bldg">
      <div class="stat-label">Building Envelopes</div>
      <div class="stat-val">108</div>
      <div class="stat-sub">Phase 7 Cataloged Properties</div>
    </div>
  </div>

  <!-- Corridor Density Table -->
  <div class="collapsible-box">
    <div class="collapsible-header" onclick="toggleDensityTable()">
      <span>Corridor Infrastructure Density Summary (10 Surveyed Streets &bull; 2.49 km Total Road Network)</span>
      <span id="densityToggleIcon">&#9660;</span>
    </div>
    <div class="collapsible-body" id="densityBody">
      <table class="density-table">
        <thead>
          <tr>
            <th>Corridor ID</th>
            <th>Street Name</th>
            <th>Zone Type</th>
            <th>Length (m)</th>
            <th>Total Assets</th>
            <th>Asset Density (/km)</th>
            <th>Pole Density (/km)</th>
            <th>Avg Light Spacing</th>
            <th>Transformers</th>
            <th>Traffic Signals</th>
          </tr>
        </thead>
        <tbody>
          {"".join([f'''
          <tr>
            <td><strong>{d["Street_ID"]}</strong></td>
            <td>{d["Street_Name"]}</td>
            <td>{d["Zone_Type"]}</td>
            <td>{d["Length_m"]:.0f}m</td>
            <td><strong style="color:var(--accent-cyan);">{d["Total_Fixed_Assets"]}</strong></td>
            <td><span style="color:var(--accent-gold); font-weight:700;">{d["Asset_Density_per_km"]:.1f}</span></td>
            <td>{d["Pole_Density_per_km"]:.1f}</td>
            <td>{d["Average_Luminaire_Spacing_m"]:.1f}m</td>
            <td>{d["Transformers_Count"]}</td>
            <td>{d["Traffic_Signals_Count"]}</td>
          </tr>
          ''' for d in density_records])}
        </tbody>
      </table>
    </div>
  </div>

  <!-- Filters & Controls -->
  <div class="controls-panel">
    <div class="filter-group">
      <label>Search Asset ID / Keyword</label>
      <input type="text" id="searchInput" placeholder="e.g. POLE-ST01, TANGEDCO, 90W...">
    </div>
    <div class="filter-group">
      <label>Asset Class</label>
      <select id="classFilter">
        <option value="ALL">All Asset Classes (465)</option>
        <option value="electric_pole">Electric Utility Poles (108)</option>
        <option value="streetlight">Streetlight Luminaires (108)</option>
        <option value="transformer">Distribution Transformers (24)</option>
        <option value="traffic_signal">Traffic Signals (9)</option>
        <option value="commercial_sign">Commercial Signboards (108)</option>
        <option value="building">Building Envelopes (108)</option>
      </select>
    </div>
    <div class="filter-group">
      <label>Corridor</label>
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
      <label>Maintenance Priority</label>
      <select id="maintFilter">
        <option value="ALL">All Priorities</option>
        <option value="High">High (Immediate Action)</option>
        <option value="Medium">Medium (Scheduled)</option>
        <option value="Low">Low (Routine)</option>
      </select>
    </div>
    <button class="reset-btn" onclick="resetFilters()">Reset Filters</button>
    <div style="margin-left: auto; font-size: 13px; color: var(--text-muted);">
      Showing <span id="visibleCount" style="color:#fff; font-weight:700;">{len(passports)}</span> / {len(passports)} assets
    </div>
  </div>

  <!-- Asset Grid -->
  <div class="assets-grid" id="assetsGrid">
    <!-- Populated by JS -->
  </div>
</div>

<!-- Modal Dialog -->
<div class="modal-backdrop" id="assetModal">
  <div class="modal-box">
    <div class="modal-header">
      <div>
        <span class="badge-tag" id="modalAssetId">ASSET-ID</span>
        <h2 id="modalTitle" style="font-size: 18px; margin-top: 4px; color: #fff;">Asset Digital Passport</h2>
      </div>
      <button class="modal-close" onclick="closeModal()">&times;</button>
    </div>
    <div class="modal-body">
      <div class="passport-seal-row">
        <div>
          <div style="font-size: 11px; text-transform: uppercase; color: var(--accent-cyan); font-weight: 700;">CIVIC JURISDICTION</div>
          <div style="font-size: 14px; font-weight: 700; color: #fff;">Coimbatore City Municipal Corporation (CCMC) &bull; Ward 29</div>
        </div>
        <div>
          <span class="badge-tag" id="modalAuthorityBadge">MANAGING AUTHORITY</span>
        </div>
      </div>
      <div class="param-grid" id="modalParams">
        <!-- Injected via JS -->
      </div>
      <div style="background: #0d1422; border: 1px solid #1a273b; padding: 14px 18px; border-radius: 6px; display: flex; justify-content: space-between; align-items: center;">
        <div>
          <div style="font-size: 11px; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">GEOGRAPHIC POSITION</div>
          <div id="modalCoordinates" style="font-size: 13px; font-weight: 600; color: #e0ebf8; margin-top: 2px;"></div>
        </div>
        <a id="modalMapLink" href="" target="_blank" style="padding: 6px 14px; background: var(--accent-cyan); color: #070b12; border-radius: 4px; font-size: 12px; font-weight: 700; text-decoration: none;">View GPS Pin &rarr;</a>
      </div>
    </div>
  </div>
</div>

<script>
const ASSETS = {json.dumps(passports, ensure_ascii=False)};

function getBadgeClass(cls) {{
  if (cls === "electric_pole") return "badge-pole";
  if (cls === "streetlight") return "badge-light";
  if (cls === "transformer") return "badge-trans";
  if (cls === "traffic_signal") return "badge-sig";
  if (cls === "building") return "badge-bldg";
  return "badge-sign";
}}

function getPriorityClass(p) {{
  if (p.includes("High")) return "priority-high";
  if (p.includes("Medium")) return "priority-med";
  return "priority-low";
}}

function renderAssets(list) {{
  const grid = document.getElementById("assetsGrid");
  grid.innerHTML = "";
  document.getElementById("visibleCount").innerText = list.length;

  list.forEach(a => {{
    const card = document.createElement("div");
    card.className = "asset-card";
    card.onclick = () => openModal(a);

    const bClass = getBadgeClass(a.Asset_Class);
    const pClass = getPriorityClass(a.Maintenance_Priority);

    const specs = a.Technical_Specifications;
    let specSnippet = "";
    if (a.Asset_Class === "electric_pole") {{
      specSnippet = `
        <div class="spec-item"><span class="spec-k">Height / Material:</span><span class="spec-v">${{specs.working_height_m || 8}}m PSC</span></div>
        <div class="spec-item"><span class="spec-k">Burden:</span><span class="spec-v">${{specs.wiring_burden_rating || "Moderate"}}</span></div>
      `;
    }} else if (a.Asset_Class === "streetlight") {{
      specSnippet = `
        <div class="spec-item"><span class="spec-k">Power / Lumens:</span><span class="spec-v">${{specs.rated_power_watts}}W &bull; ${{specs.luminous_flux_lumens}} lm</span></div>
        <div class="spec-item"><span class="spec-k">Tech:</span><span class="spec-v">${{specs.color_temperature || "5700K Daylight"}}</span></div>
      `;
    }} else if (a.Asset_Class === "transformer") {{
      specSnippet = `
        <div class="spec-item"><span class="spec-k">Rating:</span><span class="spec-v">${{specs.transformer_rating_kva}} kVA &bull; ${{specs.primary_voltage}}</span></div>
        <div class="spec-item"><span class="spec-k">Cooling:</span><span class="spec-v">${{specs.cooling_type || "ONAN"}}</span></div>
      `;
    }} else if (a.Asset_Class === "traffic_signal") {{
      specSnippet = `
        <div class="spec-item"><span class="spec-k">Aspects:</span><span class="spec-v">3-Aspect 300mm LED</span></div>
        <div class="spec-item"><span class="spec-k">Power:</span><span class="spec-v">Solar / UPS Backup</span></div>
      `;
    }} else if (a.Asset_Class === "building") {{
      specSnippet = `
        <div class="spec-item"><span class="spec-k">Floors / Height:</span><span class="spec-v">${{specs.floor_notation}} &bull; ${{specs.estimated_height_m}}m</span></div>
        <div class="spec-item"><span class="spec-k">Facade:</span><span class="spec-v">${{specs.facade_type ? specs.facade_type.split("&")[0].trim() : "Plaster"}}</span></div>
      `;
    }} else {{
      specSnippet = `
        <div class="spec-item"><span class="spec-k">Sector:</span><span class="spec-v">${{specs.commercial_sector || "Commercial"}}</span></div>
        <div class="spec-item"><span class="spec-k">Type:</span><span class="spec-v">Backlit Acrylic</span></div>
      `;
    }}

    card.innerHTML = `
      <div class="card-top">
        <span class="asset-passport-id">${{a.Asset_ID}}</span>
        <span class="type-badge ${{bClass}}">${{a.Asset_Type.split(" ")[0]}}</span>
      </div>
      <div class="card-body">
        <div class="asset-title">${{a.Asset_Subtype}}</div>
        <div class="asset-meta-row">
          <svg width="12" height="12" fill="currentColor" viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/></svg>
          ${{a.Street_Name}} (${{a.Street_ID}})
        </div>
        <div class="pill-row">
          <span class="pill">${{a.Physical_Condition.split("/")[0].trim()}}</span>
          <span class="pill ${{pClass}}">${{a.Maintenance_Priority.split("(")[0].trim()}} Priority</span>
          <span class="pill">${{a.Estimated_Lifespan_Years}}y Life</span>
        </div>
        <div class="specs-box">
          <div class="spec-item"><span class="spec-k">Authority:</span><span class="spec-v">${{a.Managing_Authority.split("(")[0].trim()}}</span></div>
          ${{specSnippet}}
        </div>
      </div>
      <div class="card-footer" onclick="event.stopPropagation()">
        <a href="https://www.google.com/maps?q=${{a.Latitude}},${{a.Longitude}}" target="_blank">
          <svg width="12" height="12" fill="currentColor" viewBox="0 0 16 16"><path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0zm3.5 7.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z"/></svg>
          GPS Pin
        </a>
        <button class="passport-btn" onclick="openModalById('${{a.Asset_ID}}')">Digital Passport &rarr;</button>
      </div>
    `;
    grid.appendChild(card);
  }});
}}

function filterAssets() {{
  const q = document.getElementById("searchInput").value.toLowerCase();
  const cls = document.getElementById("classFilter").value;
  const st = document.getElementById("streetFilter").value;
  const p = document.getElementById("maintFilter").value;

  const filtered = ASSETS.filter(a => {{
    const matchQ = !q || a.Asset_ID.toLowerCase().includes(q) || a.Asset_Subtype.toLowerCase().includes(q) || a.Managing_Authority.toLowerCase().includes(q) || a.Condition_Notes.toLowerCase().includes(q);
    const matchCls = cls === "ALL" || a.Asset_Class === cls;
    const matchSt = st === "ALL" || a.Street_ID === st;
    const matchP = p === "ALL" || a.Maintenance_Priority.includes(p);
    return matchQ && matchCls && matchSt && matchP;
  }});

  renderAssets(filtered);
}}

function resetFilters() {{
  document.getElementById("searchInput").value = "";
  document.getElementById("classFilter").value = "ALL";
  document.getElementById("streetFilter").value = "ALL";
  document.getElementById("maintFilter").value = "ALL";
  renderAssets(ASSETS);
}}

function toggleDensityTable() {{
  const body = document.getElementById("densityBody");
  const icon = document.getElementById("densityToggleIcon");
  if (body.style.display === "none") {{
    body.style.display = "block";
    icon.innerHTML = "&#9660;";
  }} else {{
    body.style.display = "none";
    icon.innerHTML = "&#9654;";
  }}
}}

function openModal(a) {{
  document.getElementById("modalAssetId").innerText = a.Asset_ID;
  document.getElementById("modalTitle").innerText = a.Asset_Subtype;
  document.getElementById("modalAuthorityBadge").innerText = a.Managing_Authority.split("(")[0].trim();
  document.getElementById("modalCoordinates").innerText = `${{a.Latitude.toFixed(6)}}°N, ${{a.Longitude.toFixed(6)}}°E &bull; ${{a.Street_Name}}`;
  document.getElementById("modalMapLink").href = `https://www.google.com/maps?q=${{a.Latitude}},${{a.Longitude}}`;

  const pGrid = document.getElementById("modalParams");
  pGrid.innerHTML = `
    <div class="param-item">
      <div class="param-label">Asset Standardized Key</div>
      <div class="param-val">${{a.Asset_ID}} (Legacy: ${{a.Legacy_Asset_ID}})</div>
    </div>
    <div class="param-item">
      <div class="param-label">High-Level Classification</div>
      <div class="param-val">${{a.Asset_Type}} &bull; ${{a.Asset_Class}}</div>
    </div>
    <div class="param-item">
      <div class="param-label">Physical Condition</div>
      <div class="param-val">${{a.Physical_Condition}}</div>
    </div>
    <div class="param-item">
      <div class="param-label">Maintenance Priority</div>
      <div class="param-val">${{a.Maintenance_Priority}}</div>
    </div>
    <div class="param-item">
      <div class="param-label">Foundation / Mounting</div>
      <div class="param-val">${{a.Mounting_Type}}</div>
    </div>
    <div class="param-item">
      <div class="param-label">Managing Utility / Civic Body</div>
      <div class="param-val">${{a.Managing_Authority}}</div>
    </div>
    <div class="param-item">
      <div class="param-label">Associated Building Envelope</div>
      <div class="param-val">${{a.Associated_Building_ID}}</div>
    </div>
    <div class="param-item">
      <div class="param-label">Design Lifespan</div>
      <div class="param-val">${{a.Estimated_Lifespan_Years}} Years &bull; Operational Status: ${{a.Operational_Status}}</div>
    </div>
    <div class="param-item" style="grid-column: 1 / -1;">
      <div class="param-label">Condition Notes & Diagnostic Observations</div>
      <div class="param-val">${{a.Condition_Notes}}</div>
    </div>
    <div class="param-item" style="grid-column: 1 / -1;">
      <div class="param-label">Technical Domain Specifications</div>
      <div class="param-val"><pre style="font-family:monospace; font-size:12px; color:var(--accent-gold); white-space:pre-wrap; margin-top:4px;">${{JSON.stringify(a.Technical_Specifications, null, 2)}}</pre></div>
    </div>
  `;

  document.getElementById("assetModal").classList.add("active");
}}

function openModalById(id) {{
  const a = ASSETS.find(x => x.Asset_ID === id);
  if (a) openModal(a);
}}

function closeModal() {{
  document.getElementById("assetModal").classList.remove("active");
}}

document.getElementById("searchInput").addEventListener("input", filterAssets);
document.getElementById("classFilter").addEventListener("change", filterAssets);
document.getElementById("streetFilter").addEventListener("change", filterAssets);
document.getElementById("maintFilter").addEventListener("change", filterAssets);

// Initial Render
renderAssets(ASSETS);
</script>
</body>
</html>
"""

with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {out_html_path} ({len(html_content)} bytes)")
