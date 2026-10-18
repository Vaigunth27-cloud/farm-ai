import os
import sys
import json
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
scorecard_csv = os.path.join(base_dir, "corridor_intelligence_scorecard.csv")
out_html_path = os.path.join(base_dir, "corridor_intelligence_dashboard.html")

df = pd.read_csv(scorecard_csv)
records = df.to_dict(orient="records")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Corridor Intelligence & Density Dashboard — FarmwiseAI Task 5</title>
<style>
  :root {{
    --bg-dark: #070a12;
    --panel-bg: #0f1624;
    --panel-border: #1a273b;
    --accent-cyan: #00f2fe;
    --accent-emerald: #00ff88;
    --accent-gold: #ffbe0b;
    --accent-orange: #fb5607;
    --accent-red: #ff0055;
    --accent-magenta: #f72585;
    --text-primary: #e6edf8;
    --text-muted: #8496ad;
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
    background: linear-gradient(180deg, #101726 0%, #070b14 100%);
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
    background: linear-gradient(90deg, #00f2fe, #00ff88, #ffbe0b);
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
  /* KPI Grid */
  .kpi-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
  }}
  .kpi-card {{
    background: var(--panel-bg);
    border: 1px solid var(--panel-border);
    border-radius: 8px;
    padding: 16px 20px;
    position: relative;
    overflow: hidden;
  }}
  .kpi-card::before {{
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: var(--accent-cyan);
  }}
  .kpi-card.emerald::before {{ background: var(--accent-emerald); }}
  .kpi-card.gold::before {{ background: var(--accent-gold); }}
  .kpi-card.red::before {{ background: var(--accent-red); }}
  .kpi-k {{
    font-size: 11px;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .kpi-v {{
    font-size: 26px;
    font-weight: 800;
    color: #fff;
    margin-top: 4px;
  }}
  .kpi-sub {{
    font-size: 11px;
    color: var(--text-muted);
    margin-top: 2px;
  }}
  /* Comparative Visual Analytics Box */
  .charts-section {{
    background: var(--panel-bg);
    border: 1px solid var(--panel-border);
    border-radius: 10px;
    padding: 20px 24px;
    margin-bottom: 24px;
  }}
  .chart-title {{
    font-size: 15px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .bar-chart {{
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}
  .bar-row {{
    display: grid;
    grid-template-columns: 80px 180px 1fr 90px;
    align-items: center;
    gap: 12px;
    font-size: 12px;
  }}
  .bar-id {{ font-family: monospace; font-weight: 700; color: var(--accent-cyan); }}
  .bar-name {{ color: #d0dced; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
  .bar-track {{
    background: #090e18;
    border: 1px solid #1c2a3e;
    height: 18px;
    border-radius: 4px;
    overflow: hidden;
    position: relative;
  }}
  .bar-fill {{
    height: 100%;
    background: linear-gradient(90deg, #00f2fe, #00ff88);
    border-radius: 3px;
    transition: width 0.5s ease;
  }}
  .bar-fill.burden {{
    background: linear-gradient(90deg, #ffbe0b, #ff0055);
  }}
  .bar-val {{
    font-weight: 700;
    text-align: right;
    color: #fff;
  }}

  /* Filter Bar */
  .filter-panel {{
    background: var(--panel-bg);
    border: 1px solid var(--panel-border);
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 24px;
    display: flex;
    gap: 10px;
    align-items: center;
    flex-wrap: wrap;
  }}
  .filter-btn {{
    padding: 7px 14px;
    background: #0d1522;
    border: 1px solid #1c2b40;
    color: var(--text-muted);
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
  }}
  .filter-btn:hover, .filter-btn.active {{
    background: rgba(0, 242, 254, 0.15);
    border-color: var(--accent-cyan);
    color: var(--accent-cyan);
  }}

  /* Scorecards Grid */
  .scorecards-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 20px;
  }}
  .sc-card {{
    background: var(--card-bg);
    border: 1px solid var(--panel-border);
    border-radius: 10px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    transition: transform 0.2s, border-color 0.2s;
  }}
  .sc-card:hover {{
    transform: translateY(-3px);
    border-color: var(--accent-cyan);
  }}
  .sc-header {{
    padding: 14px 18px;
    background: #0d1422;
    border-bottom: 1px solid var(--panel-border);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .sc-id {{
    font-family: monospace;
    font-size: 13px;
    font-weight: 700;
    color: var(--accent-cyan);
  }}
  .grade-badge {{
    font-size: 14px;
    font-weight: 900;
    padding: 4px 10px;
    border-radius: 6px;
    letter-spacing: 0.5px;
  }}
  .grade-A-plus {{ background: rgba(0, 255, 136, 0.2); color: #00ff88; border: 1px solid #00ff88; }}
  .grade-A {{ background: rgba(0, 242, 254, 0.2); color: #00f2fe; border: 1px solid #00f2fe; }}
  .grade-B {{ background: rgba(255, 190, 11, 0.2); color: #ffbe0b; border: 1px solid #ffbe0b; }}
  .grade-C {{ background: rgba(255, 0, 85, 0.2); color: #ff0055; border: 1px solid #ff0055; }}
  
  .sc-body {{
    padding: 16px 18px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    flex-grow: 1;
  }}
  .sc-title {{
    font-size: 16px;
    font-weight: 700;
    color: #fff;
    line-height: 1.3;
  }}
  .sc-arch {{
    font-size: 11px;
    color: var(--accent-gold);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .sc-metrics-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    background: #0a101a;
    border: 1px solid #182436;
    padding: 10px 12px;
    border-radius: 6px;
    font-size: 11px;
  }}
  .sc-m-item {{
    display: flex;
    flex-direction: column;
  }}
  .sc-m-k {{ color: var(--text-muted); font-size: 10px; text-transform: uppercase; font-weight: 600; }}
  .sc-m-v {{ color: #e2ebf6; font-size: 13px; font-weight: 700; margin-top: 1px; }}

  .sc-action-box {{
    background: rgba(14, 22, 34, 0.8);
    border: 1px solid #1c2b40;
    border-left: 3px solid var(--accent-cyan);
    border-radius: 4px;
    padding: 10px 12px;
    font-size: 11px;
  }}
  .sc-action-label {{
    color: var(--accent-cyan);
    font-weight: 700;
    text-transform: uppercase;
    margin-bottom: 2px;
  }}
  .sc-action-text {{
    color: #d8e4f4;
    line-height: 1.4;
  }}
  .sc-agency {{
    color: var(--text-muted);
    font-size: 10px;
    margin-top: 4px;
    font-weight: 600;
  }}
  .sc-footer {{
    padding: 10px 18px;
    background: #0c121e;
    border-top: 1px solid var(--panel-border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 11px;
    color: var(--text-muted);
  }}
</style>
</head>
<body>

<header>
  <div style="max-width: 1600px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
    <div>
      <span class="badge-tag">FarmwiseAI Task 5 &bull; Team 24</span>
      <h1><span class="title-gradient">Corridor Intelligence & Urban Density Engine</span></h1>
      <p class="subtitle">Cross-Corridor Comparative Diagnostics, Infrastructure Health Indices & Municipal Action Plans &bull; Coimbatore Ward 29</p>
    </div>
    <div style="display: flex; gap: 10px;">
      <a href="gis_digital_twin_baseline.html" style="text-decoration:none; padding: 8px 14px; background: #162438; border: 1px solid #2b3f5c; color: var(--accent-cyan); border-radius: 6px; font-size: 12px; font-weight: 700;">&larr; GIS Digital Twin</a>
      <a href="building_explorer.html" style="text-decoration:none; padding: 8px 14px; background: #162438; border: 1px solid #2b3f5c; color: var(--accent-emerald); border-radius: 6px; font-size: 12px; font-weight: 700;">Building Explorer &rarr;</a>
    </div>
  </div>
</header>

<div class="container">
  <!-- KPI Grid -->
  <div class="kpi-grid">
    <div class="kpi-card">
      <div class="kpi-k">Total Road Surveyed</div>
      <div class="kpi-v">2.49 km</div>
      <div class="kpi-sub">10 Surveyed Corridors</div>
    </div>
    <div class="kpi-card emerald">
      <div class="kpi-k">Peak Asset Density</div>
      <div class="kpi-v">267.2 /km</div>
      <div class="kpi-sub">ST05 &bull; Gopalasamy Kovil St</div>
    </div>
    <div class="kpi-card gold">
      <div class="kpi-k">Max Power Capacity</div>
      <div class="kpi-v">4,120.9 kVA/km</div>
      <div class="kpi-sub">ST08 &bull; Raja Street Arterial</div>
    </div>
    <div class="kpi-card red">
      <div class="kpi-k">Cable Burden Priority</div>
      <div class="kpi-v">3 Corridors</div>
      <div class="kpi-sub">ST03, ST06, ST08 (Grade C)</div>
    </div>
  </div>

  <!-- Comparative Charts -->
  <div class="charts-section">
    <div class="chart-title">
      <svg width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-4zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/></svg>
      Comparative Infrastructure Density per Kilometer (Assets / km)
    </div>
    <div class="bar-chart">
      {"".join([f'''
      <div class="bar-row">
        <span class="bar-id">{r["Street_ID"]}</span>
        <span class="bar-name">{r["Street_Name"]}</span>
        <div class="bar-track">
          <div class="bar-fill" style="width: {min(100.0, (r["Asset_Density_per_km"] / 270.0) * 100.0):.1f}%;"></div>
        </div>
        <span class="bar-val">{r["Asset_Density_per_km"]:.1f} /km</span>
      </div>
      ''' for r in records])}
    </div>
  </div>

  <!-- Filter Bar -->
  <div class="filter-panel">
    <span style="font-size: 11px; text-transform: uppercase; font-weight: 700; color: var(--text-muted); margin-right: 6px;">Archetype Filter:</span>
    <div class="filter-btn active" onclick="filterArchetype('ALL')">All Corridors (10)</div>
    <div class="filter-btn" onclick="filterArchetype('Highway')">Primary Arterials & Highway</div>
    <div class="filter-btn" onclick="filterArchetype('Residential')">Residential Colonies</div>
    <div class="filter-btn" onclick="filterArchetype('Mixed')">Mixed Commercial</div>
    <div class="filter-btn" onclick="filterArchetype('Industrial')">Light Industrial</div>
  </div>

  <!-- Scorecards Grid -->
  <div class="scorecards-grid" id="scorecardsGrid">
    {"".join([f'''
    <div class="sc-card" data-archetype="{r["Urban_Archetype"]}">
      <div class="sc-header">
        <span class="sc-id">{r["Street_ID"]} &bull; {r["Corridor_Tier"]}</span>
        <span class="grade-badge grade-{r["Municipal_Readiness_Grade"].replace('+', '-plus')}">{r["Municipal_Readiness_Grade"]}</span>
      </div>
      <div class="sc-body">
        <div class="sc-title">{r["Street_Name"]}</div>
        <div class="sc-arch">{r["Urban_Archetype"]}</div>
        
        <div class="sc-metrics-grid">
          <div class="sc-m-item">
            <span class="sc-m-k">Length & Assets</span>
            <span class="sc-m-v">{r["Length_m"]:.0f}m &bull; {r["Total_Fixed_Assets"]} Assets</span>
          </div>
          <div class="sc-m-item">
            <span class="sc-m-k">Luminaire Spacing</span>
            <span class="sc-m-v">{r["Average_Luminaire_Spacing_m"]:.1f}m</span>
          </div>
          <div class="sc-m-item">
            <span class="sc-m-k">Cable Burden (CBI)</span>
            <span class="sc-m-v" style="color:{'#ff0055' if r['Cable_Burden_Index'] >= 80 else ('#ffbe0b' if r['Cable_Burden_Index'] >= 50 else '#00ff88')}">{r["Cable_Burden_Index"]:.0f} / 100</span>
          </div>
          <div class="sc-m-item">
            <span class="sc-m-k">Lighting Score</span>
            <span class="sc-m-v" style="color:{'#00ff88' if r['Street_Lighting_Adequacy_Score'] >= 85 else ('#ffbe0b' if r['Street_Lighting_Adequacy_Score'] >= 70 else '#ff0055')}">{r["Street_Lighting_Adequacy_Score"]:.0f} / 100</span>
          </div>
          <div class="sc-m-item">
            <span class="sc-m-k">Transformer Load</span>
            <span class="sc-m-v">{r["Total_Transformer_kVA"]} kVA ({r["Substation_Capacity_kVA_per_km"]:.0f} /km)</span>
          </div>
          <div class="sc-m-item">
            <span class="sc-m-k">Built Verticality</span>
            <span class="sc-m-v">{r["Mean_Building_Floors"]:.1f} Fl &bull; Max {r["Max_Building_Height_m"]:.1f}m</span>
          </div>
        </div>

        <div class="sc-action-box">
          <div class="sc-action-label">Civic Action Plan</div>
          <div class="sc-action-text">{r["Actionable_Work_Order"]}</div>
          <div class="sc-agency">Primary Authority: {r["Responsible_Civic_Agency"]}</div>
        </div>
      </div>
      <div class="sc-footer">
        <span>Readiness Score: <strong>{r["Composite_Readiness_Score"]}/100</strong></span>
        <span>{r["Civic_Health_Status"]}</span>
      </div>
    </div>
    ''' for r in records])}
  </div>
</div>

<script>
function filterArchetype(arch) {{
  document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
  event.target.classList.add("active");

  const cards = document.querySelectorAll(".sc-card");
  cards.forEach(card => {{
    const a = card.getAttribute("data-archetype").toLowerCase();
    if (arch === "ALL") {{
      card.style.display = "flex";
    }} else if (arch === "Highway" && (a.includes("highway") || a.includes("arterial"))) {{
      card.style.display = "flex";
    }} else if (arch === "Residential" && a.includes("residential")) {{
      card.style.display = "flex";
    }} else if (arch === "Mixed" && a.includes("mixed")) {{
      card.style.display = "flex";
    }} else if (arch === "Industrial" && a.includes("industrial")) {{
      card.style.display = "flex";
    }} else {{
      card.style.display = "none";
    }}
  }});
}}
</script>
</body>
</html>
"""

with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {out_html_path} ({len(html_content)} bytes)")
