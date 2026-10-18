import os
import sys
import json
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
ocr_csv_path = os.path.join(base_dir, "ocr_intelligence.csv")
df_ocr = pd.read_csv(ocr_csv_path)

records = df_ocr.to_dict(orient="records")
records_json = json.dumps(records)

total_signs = len(df_ocr)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OCR Commercial Intelligence Explorer — FarmwiseAI Task 5</title>
<style>
  :root {{
    --bg-dark: #0b0f17;
    --panel-bg: #141c28;
    --border-color: #223249;
    --text-primary: #f0f4f8;
    --text-muted: #8b9bb4;
    --accent-cyan: #00ffcc;
    --accent-magenta: #ff00ff;
    --accent-yellow: #ffee00;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
  body {{ background: var(--bg-dark); color: var(--text-primary); display: flex; flex-direction: column; height: 100vh; overflow: hidden; }}
  header {{ background: #080c13; border-bottom: 1px solid var(--border-color); padding: 12px 24px; display: flex; justify-content: space-between; align-items: center; }}
  .title-area h1 {{ font-size: 1.15rem; font-weight: 700; color: #fff; display: flex; align-items: center; gap: 8px; }}
  .badge {{ background: #440044; color: var(--accent-magenta); border: 1px solid var(--accent-magenta); padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; text-transform: uppercase; font-weight: 600; }}
  .main-layout {{ display: flex; flex: 1; overflow: hidden; }}
  .sidebar-left {{ width: 380px; background: var(--panel-bg); border-right: 1px solid var(--border-color); display: flex; flex-direction: column; padding: 16px; gap: 12px; }}
  .preview-area {{ flex: 1; background: #06090e; display: flex; flex-direction: column; overflow: hidden; position: relative; }}
  .search-box {{ width: 100%; background: #0a111a; border: 1px solid var(--border-color); padding: 10px 14px; border-radius: 6px; color: #fff; font-size: 0.9rem; outline: none; }}
  .search-box:focus {{ border-color: var(--accent-cyan); }}
  .filters-row {{ display: flex; gap: 8px; }}
  select {{ flex: 1; background: #0a111a; color: #fff; border: 1px solid var(--border-color); padding: 6px 10px; border-radius: 6px; font-size: 0.8rem; outline: none; }}
  .results-list {{ flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 6px; }}
  .ocr-card {{ background: #0e1622; border: 1px solid #1c2a3d; padding: 10px 12px; border-radius: 6px; cursor: pointer; transition: all 0.2s; display: flex; flex-direction: column; gap: 4px; }}
  .ocr-card:hover {{ border-color: var(--accent-cyan); background: #132032; }}
  .ocr-card.active {{ border-color: var(--accent-magenta); background: #1a2333; }}
  .card-top {{ display: flex; justify-content: space-between; align-items: center; }}
  .text-highlight {{ font-weight: 700; color: #fff; font-size: 0.95rem; }}
  .cat-badge {{ font-size: 0.7rem; padding: 2px 6px; border-radius: 3px; background: #203348; color: var(--accent-cyan); }}
  .card-sub {{ font-size: 0.75rem; color: var(--text-muted); display: flex; justify-content: space-between; }}
  .evidence-header {{ padding: 12px 20px; background: var(--panel-bg); border-bottom: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center; }}
  .image-viewport {{ flex: 1; overflow: auto; display: flex; justify-content: center; align-items: center; padding: 20px; position: relative; }}
  .canvas-wrapper {{ position: relative; box-shadow: 0 10px 30px rgba(0,0,0,0.8); }}
  canvas {{ max-width: 100%; max-height: calc(100vh - 180px); display: block; border: 1px solid var(--border-color); }}
  .details-banner {{ padding: 10px 20px; background: #0b1118; border-top: 1px solid var(--border-color); font-size: 0.85rem; display: flex; gap: 20px; }}
  .attr-val {{ color: var(--accent-cyan); font-weight: 600; }}
</style>
</head>
<body>
<header>
  <div class="title-area">
    <h1>OCR Commercial Intelligence Explorer</h1>
    <span class="badge">Phase 6 Active</span>
  </div>
  <div style="font-size:0.85rem; color: var(--text-muted);">
    Team 24 • Multilingual Commercial & Civic Signboard Search
  </div>
</header>

<div class="main-layout">
  <div class="sidebar-left">
    <div>
      <input type="text" id="searchInput" class="search-box" placeholder="🔍 Search shop name, hotel, brand, road...">
    </div>
    <div class="filters-row">
      <select id="catFilter">
        <option value="">All Categories</option>
      </select>
      <select id="streetFilter">
        <option value="">All Streets</option>
      </select>
    </div>
    <div style="font-size:0.75rem; color:var(--text-muted); display:flex; justify-content:space-between;">
      <span id="resultsCount">Loading...</span>
      <span>Total Indexed: {total_signs} signs</span>
    </div>
    <div class="results-list" id="resultsList"></div>
  </div>

  <div class="preview-area">
    <div class="evidence-header">
      <div>
        <strong id="dispTitle" style="font-size:1rem; color:#fff;">Select a signboard</strong>
        <div id="dispSub" style="font-size:0.8rem; color:var(--text-muted);">Street & Geographic Location</div>
      </div>
      <div>
        <span class="badge" id="dispConf">Conf: -</span>
      </div>
    </div>
    <div class="image-viewport">
      <div class="canvas-wrapper">
        <canvas id="imgCanvas"></canvas>
      </div>
    </div>
    <div class="details-banner">
      <div>Category: <span class="attr-val" id="dispCat">-</span></div>
      <div>Sign Type: <span class="attr-val" id="dispType">-</span></div>
      <div>GPS: <span class="attr-val" id="dispGps">-</span></div>
      <div>Building ID: <span class="attr-val" id="dispBld">-</span></div>
    </div>
  </div>
</div>

<script>
const RECORDS = {records_json};
let filteredRecords = [...RECORDS];
let activeRecord = null;
let imgObj = new Image();

const canvas = document.getElementById('imgCanvas');
const ctx = canvas.getContext('2d');

function init() {{
  // Populate category filter
  const cats = [...new Set(RECORDS.map(r => r.Commercial_Category))];
  const catSel = document.getElementById('catFilter');
  cats.forEach(c => {{
    const opt = document.createElement('option');
    opt.value = c; opt.textContent = c;
    catSel.appendChild(opt);
  }});

  // Populate street filter
  const streets = [...new Set(RECORDS.map(r => r.Street_ID + ": " + r.Street_Name))];
  const strSel = document.getElementById('streetFilter');
  streets.forEach(s => {{
    const opt = document.createElement('option');
    opt.value = s.split(':')[0]; opt.textContent = s;
    strSel.appendChild(opt);
  }});

  document.getElementById('searchInput').oninput = applyFilters;
  catSel.onchange = applyFilters;
  strSel.onchange = applyFilters;

  applyFilters();
  if (RECORDS.length > 0) selectRecord(RECORDS[0]);
}}

function applyFilters() {{
  const query = document.getElementById('searchInput').value.toLowerCase().trim();
  const cat = document.getElementById('catFilter').value;
  const str = document.getElementById('streetFilter').value;

  filteredRecords = RECORDS.filter(r => {{
    const matchQ = !query || r.OCR_Text.toLowerCase().includes(query) || r.Street_Name.toLowerCase().includes(query) || r.Commercial_Category.toLowerCase().includes(query);
    const matchC = !cat || r.Commercial_Category === cat;
    const matchS = !str || r.Street_ID === str;
    return matchQ && matchC && matchS;
  }});

  document.getElementById('resultsCount').textContent = `Showing ${{filteredRecords.length}} of ${{RECORDS.length}}`;
  renderResultsList();
}}

function renderResultsList() {{
  const container = document.getElementById('resultsList');
  container.innerHTML = '';
  filteredRecords.forEach(r => {{
    const card = document.createElement('div');
    card.className = 'ocr-card' + (activeRecord && activeRecord.OCR_ID === r.OCR_ID ? ' active' : '');
    const confPct = (r.Confidence * 100).toFixed(0);
    card.innerHTML = `
      <div class="card-top">
        <span class="text-highlight">${{r.OCR_Text}}</span>
        <span class="cat-badge">${{r.Commercial_Category}}</span>
      </div>
      <div class="card-sub">
        <span>${{r.Street_ID}} • ${{r.Street_Name.split('(')[0]}}</span>
        <span>Conf: ${{confPct}}%</span>
      </div>
    `;
    card.onclick = () => selectRecord(r);
    container.appendChild(card);
  }});
}}

function selectRecord(r) {{
  activeRecord = r;
  document.querySelectorAll('.ocr-card').forEach(c => c.classList.remove('active'));
  renderResultsList();

  document.getElementById('dispTitle').textContent = `"${{r.OCR_Text}}"`;
  document.getElementById('dispSub').textContent = `${{r.Street_ID}} - ${{r.Street_Name}} (${{r.Evidence_Image}})`;
  document.getElementById('dispConf').textContent = `Conf: ${(r.Confidence * 100).toFixed(1)}%`;
  document.getElementById('dispCat').textContent = r.Commercial_Category;
  document.getElementById('dispType').textContent = r.Sign_Type;
  document.getElementById('dispGps').textContent = `${{r.Latitude.toFixed(6)}}, ${{r.Longitude.toFixed(6)}}`;
  document.getElementById('dispBld').textContent = r.Associated_Building_ID;

  imgObj.onload = () => {{
    canvas.width = imgObj.width;
    canvas.height = imgObj.height;
    ctx.drawImage(imgObj, 0, 0);

    // Draw signboard box
    const x1 = r.BBox_X1, y1 = r.BBox_Y1, bw = r.BBox_X2 - r.BBox_X1, bh = r.BBox_Y2 - r.BBox_Y1;
    ctx.strokeStyle = '#ff00ff';
    ctx.lineWidth = 4;
    ctx.strokeRect(x1, y1, bw, bh);

    // Text banner
    ctx.fillStyle = '#ff00ff';
    ctx.font = 'bold 20px sans-serif';
    const tag = `"${{r.OCR_Text}}" [${{r.Commercial_Category}}]`;
    const tw = ctx.measureText(tag).width;
    ctx.fillRect(x1, Math.max(0, y1 - 30), tw + 14, 30);

    ctx.fillStyle = '#ffffff';
    ctx.fillText(tag, x1 + 6, Math.max(22, y1 - 8));
  }};
  imgObj.src = r.Evidence_Image;
}}

window.onload = init;
</script>
</body>
</html>
"""

explorer_path = os.path.join(base_dir, "ocr_search_explorer.html")
with open(explorer_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated OCR Search Explorer at: {explorer_path}")
