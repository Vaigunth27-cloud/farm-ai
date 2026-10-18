import os
import sys
import json
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
yolo_dir = os.path.join(base_dir, "yolo_annotations")
audit_json_path = os.path.join(yolo_dir, "annotation_audit.json")

# Load annotations data
master_images_csv = os.path.join(base_dir, "master_images.csv")
detections_csv = os.path.join(base_dir, "detections.csv")

df_img = pd.read_csv(master_images_csv)
df_det = pd.read_csv(detections_csv)

CLASSES = [
    "building", "electric_pole", "streetlight", "commercial_sign",
    "traffic_signal", "road_sign", "transformer", "drain",
    "sidewalk", "waste_bin", "bus_stop", "other_urban_asset"
]

CLASS_COLORS = {
    "building": "#00FFCC",
    "electric_pole": "#0088FF",
    "streetlight": "#FFEE00",
    "commercial_sign": "#FF00FF",
    "traffic_signal": "#FF0000",
    "road_sign": "#FFAA00",
    "transformer": "#FF5500",
    "drain": "#00BB77",
    "sidewalk": "#778899",
    "waste_bin": "#8A2BE2",
    "bus_stop": "#00CED1",
    "other_urban_asset": "#A9A9A9"
}

# Build JSON structure for frontend
images_data = []
for _, row in df_img.iterrows():
    img_id = row["Image_ID"]
    s_id = row["Street_ID"]
    s_name = row["Street_Name"]
    rel_path = row["Image_Path"]
    w = int(row["Width_px"])
    h = int(row["Height_px"])
    
    dets = df_det[df_det["Image_ID"] == img_id]
    boxes = []
    for _, d in dets.iterrows():
        c_name = d["Class_Name"]
        boxes.append({
            "asset_id": d.get("Asset_ID", f"ASSET-{img_id}"),
            "class_name": c_name,
            "x1": float(d["BBox_X1"]),
            "y1": float(d["BBox_Y1"]),
            "x2": float(d["BBox_X2"]),
            "y2": float(d["BBox_Y2"]),
            "details": d.get("Details", "")
        })
    images_data.append({
        "image_id": img_id,
        "street_id": s_id,
        "street_name": s_name,
        "image_path": rel_path,
        "width": w,
        "height": h,
        "boxes": boxes
    })

images_json = json.dumps(images_data)
classes_json = json.dumps(CLASSES)
colors_json = json.dumps(CLASS_COLORS)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Urban Intelligence Annotation Studio — FarmwiseAI Task 5</title>
<style>
  :root {{
    --bg-dark: #0f141c;
    --panel-bg: #182232;
    --border-color: #263852;
    --text-primary: #f0f4f8;
    --text-muted: #8b9bb4;
    --accent-cyan: #00ffcc;
    --accent-blue: #0088ff;
    --accent-yellow: #ffee00;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
  body {{ background: var(--bg-dark); color: var(--text-primary); display: flex; flex-direction: column; height: 100vh; overflow: hidden; }}
  header {{ background: #0b0f17; border-bottom: 1px solid var(--border-color); padding: 12px 24px; display: flex; justify-content: space-between; align-items: center; }}
  .title-area h1 {{ font-size: 1.15rem; font-weight: 700; color: #fff; display: flex; align-items: center; gap: 8px; }}
  .badge {{ background: #004433; color: var(--accent-cyan); border: 1px solid var(--accent-cyan); padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; text-transform: uppercase; font-weight: 600; }}
  .main-layout {{ display: flex; flex: 1; overflow: hidden; }}
  .sidebar-left {{ width: 280px; background: var(--panel-bg); border-right: 1px solid var(--border-color); display: flex; flex-direction: column; padding: 14px; gap: 12px; }}
  .viewport-center {{ flex: 1; display: flex; flex-direction: column; background: #080c12; position: relative; overflow: hidden; }}
  .toolbar-top {{ background: var(--panel-bg); padding: 8px 16px; border-bottom: 1px solid var(--border-color); display: flex; align-items: center; gap: 12px; justify-content: space-between; }}
  .canvas-container {{ flex: 1; position: relative; overflow: auto; display: flex; justify-content: center; align-items: center; padding: 20px; }}
  canvas {{ box-shadow: 0 10px 30px rgba(0,0,0,0.8); border: 1px solid var(--border-color); cursor: crosshair; max-width: 100%; max-height: 100%; object-fit: contain; }}
  .sidebar-right {{ width: 320px; background: var(--panel-bg); border-left: 1px solid var(--border-color); display: flex; flex-direction: column; padding: 16px; gap: 14px; overflow-y: auto; }}
  label {{ font-size: 0.8rem; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; }}
  select, input, button {{ background: #0e1724; color: #fff; border: 1px solid var(--border-color); border-radius: 6px; padding: 8px 12px; font-size: 0.85rem; outline: none; }}
  select:focus, input:focus {{ border-color: var(--accent-cyan); }}
  button {{ background: #16263b; border: 1px solid #2b4569; cursor: pointer; transition: all 0.2s; font-weight: 600; }}
  button:hover {{ background: #223854; border-color: var(--accent-cyan); color: var(--accent-cyan); }}
  button.btn-primary {{ background: #006644; border-color: var(--accent-cyan); color: #fff; }}
  button.btn-primary:hover {{ background: #008855; }}
  button.btn-danger {{ background: #551122; border-color: #ff3344; color: #ff8899; }}
  button.btn-danger:hover {{ background: #77112b; color: #fff; }}
  .class-palette {{ display: grid; grid-template-columns: 1fr 1fr; gap: 6px; max-height: 220px; overflow-y: auto; padding-right: 4px; }}
  .class-btn {{ font-size: 0.75rem; padding: 6px 8px; text-align: left; display: flex; align-items: center; gap: 6px; border-radius: 4px; border: 1px solid #203045; background: #0c1420; }}
  .class-btn.active {{ border-color: #fff; background: #1b2c44; box-shadow: 0 0 8px rgba(0,255,204,0.3); }}
  .color-dot {{ width: 10px; height: 10px; border-radius: 50%; display: inline-block; flex-shrink: 0; }}
  .box-list {{ display: flex; flex-direction: column; gap: 6px; max-height: 250px; overflow-y: auto; }}
  .box-item {{ background: #0e1724; border: 1px solid #21334b; padding: 8px 10px; border-radius: 6px; display: flex; justify-content: space-between; align-items: center; font-size: 0.8rem; cursor: pointer; }}
  .box-item.selected {{ border-color: var(--accent-cyan); background: #142438; }}
  .box-item:hover {{ border-color: #3b5880; }}
  .stats-card {{ background: #0c1420; border: 1px solid #1f3047; padding: 12px; border-radius: 6px; font-size: 0.8rem; display: flex; flex-direction: column; gap: 6px; }}
  .stat-row {{ display: flex; justify-content: space-between; }}
  .stat-val {{ font-weight: 700; color: var(--accent-cyan); }}
</style>
</head>
<body>
<header>
  <div class="title-area">
    <h1>Urban Intelligence Annotation Studio</h1>
    <span class="badge">Human-in-the-Loop Mode</span>
  </div>
  <div style="font-size:0.85rem; color: var(--text-muted);">
    Team 24 • FarmwiseAI Task 5 (Street View Urban Intelligence)
  </div>
</header>

<div class="main-layout">
  <!-- Left Sidebar: Navigation & Street Selection -->
  <div class="sidebar-left">
    <div>
      <label>Select Street</label>
      <select id="streetSelect" style="width:100%; margin-top:6px;"></select>
    </div>
    <div style="flex:1; display:flex; flex-direction:column; min-height:0;">
      <label>Images on Street</label>
      <div id="imageList" style="flex:1; overflow-y:auto; margin-top:6px; display:flex; flex-direction:column; gap:4px;"></div>
    </div>
    <div class="stats-card">
      <div class="stat-row"><span>Total Assets on Frame:</span><span class="stat-val" id="frameBoxCount">0</span></div>
      <div class="stat-row"><span>Image Dimensions:</span><span class="stat-val" id="frameDims">-</span></div>
      <div class="stat-row"><span>Image ID:</span><span class="stat-val" id="frameImgId">-</span></div>
    </div>
  </div>

  <!-- Center Viewport: Interactive Canvas -->
  <div class="viewport-center">
    <div class="toolbar-top">
      <div style="display:flex; align-items:center; gap:8px;">
        <button id="prevBtn">◀ Previous</button>
        <button id="nextBtn">Next ▶</button>
        <span id="imageTitle" style="font-size:0.85rem; font-weight:600; margin-left:8px;"></span>
      </div>
      <div style="display:flex; align-items:center; gap:8px;">
        <button id="deleteBtn" class="btn-danger">Delete Box</button>
        <button id="exportYoloBtn" class="btn-primary">Export YOLO .txt</button>
        <button id="exportJsonBtn">Export Full JSON</button>
      </div>
    </div>
    <div class="canvas-container">
      <canvas id="annCanvas"></canvas>
    </div>
  </div>

  <!-- Right Sidebar: Class Palette & Box Editor -->
  <div class="sidebar-right">
    <div>
      <label>Active Class for Drawing</label>
      <div class="class-palette" id="classPalette" style="margin-top:6px;"></div>
    </div>
    <hr style="border:0; border-top:1px solid var(--border-color);">
    <div>
      <label>Selected Asset Editor</label>
      <div style="display:flex; flex-direction:column; gap:8px; margin-top:8px;">
        <div>
          <label style="font-size:0.75rem;">Asset ID</label>
          <input type="text" id="editAssetId" style="width:100%;" readonly>
        </div>
        <div>
          <label style="font-size:0.75rem;">Class Label</label>
          <select id="editClassSelect" style="width:100%;"></select>
        </div>
        <div>
          <label style="font-size:0.75rem;">Urban Attributes / Notes</label>
          <input type="text" id="editDetails" style="width:100%;" placeholder="e.g. G+2 Floors, High Burden, LED">
        </div>
      </div>
    </div>
    <hr style="border:0; border-top:1px solid var(--border-color);">
    <div style="flex:1; display:flex; flex-direction:column; min-height:0;">
      <label>Assets on Current Frame</label>
      <div class="box-list" id="boxList" style="flex:1; margin-top:8px;"></div>
    </div>
  </div>
</div>

<script>
const IMAGES = {images_json};
const CLASSES = {classes_json};
const COLORS = {colors_json};

let currentImgIdx = 0;
let currentImage = null;
let activeClass = CLASSES[0];
let selectedBoxIdx = -1;
let isDrawing = false;
let startX = 0, startY = 0;
let currentX = 0, currentY = 0;
let imgElement = new Image();

const canvas = document.getElementById('annCanvas');
const ctx = canvas.getContext('2d');

function init() {{
  // Populate Street Select
  const streetSelect = document.getElementById('streetSelect');
  const streets = [...new Set(IMAGES.map(im => im.street_id + " - " + im.street_name))];
  streets.forEach(s => {{
    const opt = document.createElement('option');
    opt.value = s.split(" - ")[0];
    opt.textContent = s;
    streetSelect.appendChild(opt);
  }});
  streetSelect.addEventListener('change', (e) => {{
    const foundIdx = IMAGES.findIndex(im => im.street_id === e.target.value);
    if (foundIdx !== -1) loadImage(foundIdx);
  }});

  // Populate Class Palette
  const palette = document.getElementById('classPalette');
  const editSelect = document.getElementById('editClassSelect');
  CLASSES.forEach(c => {{
    const btn = document.createElement('div');
    btn.className = 'class-btn' + (c === activeClass ? ' active' : '');
    btn.dataset.class = c;
    btn.innerHTML = `<span class="color-dot" style="background:${{COLORS[c]}}"></span><span>${{c.replace('_', ' ')}}</span>`;
    btn.onclick = () => {{
      document.querySelectorAll('.class-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeClass = c;
    }};
    palette.appendChild(btn);

    const opt = document.createElement('option');
    opt.value = c;
    opt.textContent = c;
    editSelect.appendChild(opt);
  }});

  editSelect.onchange = (e) => {{
    if (currentImage && selectedBoxIdx >= 0 && selectedBoxIdx < currentImage.boxes.length) {{
      currentImage.boxes[selectedBoxIdx].class_name = e.target.value;
      render();
      updateBoxList();
    }}
  }};

  document.getElementById('editDetails').oninput = (e) => {{
    if (currentImage && selectedBoxIdx >= 0 && selectedBoxIdx < currentImage.boxes.length) {{
      currentImage.boxes[selectedBoxIdx].details = e.target.value;
    }}
  }};

  // Nav buttons
  document.getElementById('prevBtn').onclick = () => {{ if (currentImgIdx > 0) loadImage(currentImgIdx - 1); }};
  document.getElementById('nextBtn').onclick = () => {{ if (currentImgIdx < IMAGES.length - 1) loadImage(currentImgIdx + 1); }};
  document.getElementById('deleteBtn').onclick = deleteSelectedBox;
  document.getElementById('exportYoloBtn').onclick = exportYoloTxt;
  document.getElementById('exportJsonBtn').onclick = exportJson;

  // Canvas drawing events
  canvas.onmousedown = handleMouseDown;
  canvas.onmousemove = handleMouseMove;
  canvas.onmouseup = handleMouseUp;

  // Keyboard delete
  window.addEventListener('keydown', (e) => {{
    if (e.key === 'Delete' || e.key === 'Backspace') {{
      if (document.activeElement.tagName !== 'INPUT') deleteSelectedBox();
    }}
  }});

  loadImage(0);
}}

function loadImage(idx) {{
  currentImgIdx = idx;
  currentImage = IMAGES[idx];
  selectedBoxIdx = -1;
  document.getElementById('streetSelect').value = currentImage.street_id;
  document.getElementById('imageTitle').textContent = `${{currentImage.image_id}} (${{idx + 1}}/${{IMAGES.length}}): ${{currentImage.street_name}}`;
  document.getElementById('frameImgId').textContent = currentImage.image_id;
  document.getElementById('frameDims').textContent = `${{currentImage.width}} x ${{currentImage.height}}`;

  updateImageList();
  updateBoxList();

  imgElement.onload = () => {{
    canvas.width = currentImage.width;
    canvas.height = currentImage.height;
    render();
  }};
  imgElement.src = currentImage.image_path;
}}

function updateImageList() {{
  const list = document.getElementById('imageList');
  list.innerHTML = '';
  const streetImgs = IMAGES.filter(im => im.street_id === currentImage.street_id);
  streetImgs.forEach(im => {{
    const globalIdx = IMAGES.indexOf(im);
    const div = document.createElement('div');
    div.style.padding = '6px 10px';
    div.style.background = (globalIdx === currentImgIdx) ? '#1b2d45' : '#0e1724';
    div.style.border = (globalIdx === currentImgIdx) ? '1px solid var(--accent-cyan)' : '1px solid #1a2738';
    div.style.borderRadius = '4px';
    div.style.fontSize = '0.8rem';
    div.style.cursor = 'pointer';
    div.style.display = 'flex';
    div.style.justifyContent = 'space-between';
    div.innerHTML = `<span>${{im.image_id}}</span><span style="color:var(--text-muted);">${{im.boxes.length}} boxes</span>`;
    div.onclick = () => loadImage(globalIdx);
    list.appendChild(div);
  }});
}}

function updateBoxList() {{
  const list = document.getElementById('boxList');
  list.innerHTML = '';
  document.getElementById('frameBoxCount').textContent = currentImage.boxes.length;
  currentImage.boxes.forEach((b, idx) => {{
    const div = document.createElement('div');
    div.className = 'box-item' + (idx === selectedBoxIdx ? ' selected' : '');
    div.innerHTML = `<span style="display:flex; align-items:center; gap:6px;"><span class="color-dot" style="background:${{COLORS[b.class_name] || '#999'}}"></span><strong>${{b.class_name}}</strong></span><span style="font-size:0.75rem; color:var(--text-muted);">${{b.asset_id || ''}}</span>`;
    div.onclick = () => {{
      selectedBoxIdx = idx;
      populateEditor(b);
      render();
      updateBoxList();
    }};
    list.appendChild(div);
  }});
  if (selectedBoxIdx >= 0 && selectedBoxIdx < currentImage.boxes.length) {{
    populateEditor(currentImage.boxes[selectedBoxIdx]);
  }} else {{
    clearEditor();
  }}
}}

function populateEditor(b) {{
  document.getElementById('editAssetId').value = b.asset_id || '';
  document.getElementById('editClassSelect').value = b.class_name;
  document.getElementById('editDetails').value = b.details || '';
}}

function clearEditor() {{
  document.getElementById('editAssetId').value = '';
  document.getElementById('editClassSelect').value = CLASSES[0];
  document.getElementById('editDetails').value = '';
}}

function deleteSelectedBox() {{
  if (currentImage && selectedBoxIdx >= 0 && selectedBoxIdx < currentImage.boxes.length) {{
    currentImage.boxes.splice(selectedBoxIdx, 1);
    selectedBoxIdx = -1;
    clearEditor();
    render();
    updateBoxList();
  }}
}}

function handleMouseDown(e) {{
  const rect = canvas.getBoundingClientRect();
  const scaleX = canvas.width / rect.width;
  const scaleY = canvas.height / rect.height;
  const mx = (e.clientX - rect.left) * scaleX;
  const my = (e.clientY - rect.top) * scaleY;

  // Check if clicked inside existing box
  let hitIdx = -1;
  for (let i = currentImage.boxes.length - 1; i >= 0; i--) {{
    const b = currentImage.boxes[i];
    if (mx >= b.x1 && mx <= b.x2 && my >= b.y1 && my <= b.y2) {{
      hitIdx = i;
      break;
    }}
  }}

  if (hitIdx !== -1) {{
    selectedBoxIdx = hitIdx;
    populateEditor(currentImage.boxes[hitIdx]);
    updateBoxList();
    render();
  }} else {{
    selectedBoxIdx = -1;
    isDrawing = true;
    startX = mx;
    startY = my;
    currentX = mx;
    currentY = my;
  }}
}}

function handleMouseMove(e) {{
  if (!isDrawing) return;
  const rect = canvas.getBoundingClientRect();
  const scaleX = canvas.width / rect.width;
  const scaleY = canvas.height / rect.height;
  currentX = (e.clientX - rect.left) * scaleX;
  currentY = (e.clientY - rect.top) * scaleY;
  render();
}}

function handleMouseUp() {{
  if (!isDrawing) return;
  isDrawing = false;
  const x1 = Math.min(startX, currentX);
  const y1 = Math.min(startY, currentY);
  const x2 = Math.max(startX, currentX);
  const y2 = Math.max(startY, currentY);

  if ((x2 - x1) > 15 && (y2 - y1) > 15) {{
    const newBox = {{
      asset_id: `ASSET-${{currentImage.image_id}}-${{currentImage.boxes.length + 1}}`,
      class_name: activeClass,
      x1: Math.round(x1),
      y1: Math.round(y1),
      x2: Math.round(x2),
      y2: Math.round(y2),
      details: "User Annotated Asset"
    }};
    currentImage.boxes.push(newBox);
    selectedBoxIdx = currentImage.boxes.length - 1;
    populateEditor(newBox);
    updateBoxList();
  }}
  render();
}}

function render() {{
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  if (imgElement.complete && imgElement.naturalWidth > 0) {{
    ctx.drawImage(imgElement, 0, 0);
  }}

  // Draw confirmed boxes
  currentImage.boxes.forEach((b, idx) => {{
    const color = COLORS[b.class_name] || '#00ffcc';
    const isSelected = (idx === selectedBoxIdx);
    ctx.strokeStyle = color;
    ctx.lineWidth = isSelected ? 4 : 2;
    ctx.strokeRect(b.x1, b.y1, b.x2 - b.x1, b.y2 - b.y1);

    // Label banner
    ctx.fillStyle = color;
    const txt = `${{b.class_name}} ${{b.asset_id ? '['+b.asset_id+']' : ''}}`;
    ctx.font = '14px sans-serif';
    const textW = ctx.measureText(txt).width;
    ctx.fillRect(b.x1, Math.max(0, b.y1 - 22), textW + 10, 22);

    ctx.fillStyle = '#000000';
    ctx.fillText(txt, b.x1 + 5, Math.max(16, b.y1 - 6));
  }});

  // Draw active drag box
  if (isDrawing) {{
    ctx.strokeStyle = COLORS[activeClass] || '#ffffff';
    ctx.lineWidth = 2;
    ctx.setLineDash([6, 6]);
    ctx.strokeRect(startX, startY, currentX - startX, currentY - startY);
    ctx.setLineDash([]);
  }}
}}

function exportYoloTxt() {{
  let content = '';
  currentImage.boxes.forEach(b => {{
    const cIdx = CLASSES.indexOf(b.class_name);
    const xc = ((b.x1 + b.x2) / 2) / currentImage.width;
    const yc = ((b.y1 + b.y2) / 2) / currentImage.height;
    const nw = (b.x2 - b.x1) / currentImage.width;
    const nh = (b.y2 - b.y1) / currentImage.height;
    content += `${{cIdx}} ${{xc.toFixed(6)}} ${{yc.toFixed(6)}} ${{nw.toFixed(6)}} ${{nh.toFixed(6)}}\\n`;
  }});
  const blob = new Blob([content], {{ type: 'text/plain' }});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `${{currentImage.image_id}}.txt`;
  a.click();
}}

function exportJson() {{
  const blob = new Blob([JSON.stringify(IMAGES, null, 2)], {{ type: 'application/json' }});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `urban_annotations_complete.json`;
  a.click();
}}

window.onload = init;
</script>
</body>
</html>
"""

studio_path = os.path.join(base_dir, "urban_annotation_studio.html")
with open(studio_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated standalone interactive Annotation Studio at: {studio_path}")
