# FarmwiseAI — Street View Urban Intelligence Platform
## Simple Step-by-Step User Guide

A beginner-friendly, operational handbook for starting, using, and troubleshooting the FarmwiseAI platform.

---

## 1. Prerequisites & Software Installation

To run FarmwiseAI on a local computer or laptop, ensure the following software is installed:

### Required Software:
- **Operating System**: Windows 10/11, macOS, or Ubuntu Linux (64-bit).
- **Python**: Version **3.10, 3.11, or 3.12** (Verify by running `python --version` in terminal).
- **Web Browser**: Any modern browser (Google Chrome, Microsoft Edge, Mozilla Firefox, Brave).
- **Git**: Git 2.30+ installed for version control.

### Python Package Installation:
Open PowerShell or Command Prompt, navigate to the project directory, and install the required dependencies:

```powershell
pip install fastapi uvicorn ultralytics opencv-python pillow exifread pydantic requests
```

*(Optional for OCR text extraction)*:
```powershell
pip install easyocr
```

*(Optional for PowerPoint presentation generation)*:
```powershell
pip install python-pptx
```

---

## 2. Project Directory Structure

When navigating `D:\farm ai`, the major folders and files are organized as follows:

```
D:\farm ai\
├── dashboard_redesign_prototype/      # Master Application Prototype
│   ├── index.html                    # Main user dashboard interface
│   ├── backend/                      # Backend Python server
│   │   └── urban_agent_server.py     # FastAPI application server
│   └── assets/                       # UI scripts, styles, raw street frames
├── 🌟 MASTER UNIFIED PLATFORM/        # Unified Digital Twin Hub
│   └── urban_digital_twin_portal.html# Master portal connecting all studios
├── 🌐 INDIVIDUAL STANDALONE STUDIOS/  # Specialized analytical studios
│   ├── tri_view_studio.html          # Verification slider studio
│   ├── ocr_search_explorer.html      # Shop signboard text search
│   ├── building_explorer.html        # Building footprint intelligence
│   └── gis_digital_twin_baseline.html# MapLibre GIS viewer
├── 🗺️ MASTER GIS & TABULAR DATASETS/  # Core datasets, CSVs, GeoJSONs
├── 📋 MUNICIPAL REPORTS & WORK ORDERS/# Tax ledgers, streetlight directives
├── 🧠 MACHINE LEARNING MODELS & ROUTING/# YOLO weights, training notebooks
└── project_documentation/             # Complete manuals, diagrams, PPTX
```

---

## 3. Environment Configuration

FarmwiseAI is designed to run locally without complex credential setup:
- **No Secrets Required**: The local YOLO perception model, EasyOCR, and spatial engines run entirely on your local machine without needing OpenAI, Google, or AWS API keys.
- **Port Assignment**:
  - Backend API: `http://127.0.0.1:8000`
  - Frontend Web Server: `http://127.0.0.1:5500` or `http://127.0.0.1:8080` (or direct browser file opening).

---

## 4. How to Start the Backend Server

1. Open PowerShell or Terminal.
2. Navigate to the backend directory:
   ```powershell
   cd "D:\farm ai\dashboard_redesign_prototype\backend"
   ```
3. Start the FastAPI server using Uvicorn:
   ```powershell
   python urban_agent_server.py
   ```
   *(Or alternatively via uvicorn directly)*:
   ```powershell
   uvicorn urban_agent_server:app --host 127.0.0.1 --port 8000 --reload
   ```
4. Verify the server is running by opening `http://127.0.0.1:8000/health` in your browser. You should see:
   ```json
   {"status":"healthy","model_loaded":true,"ocr_available":true,"device":"cpu"}
   ```

---

## 5. How to Start the Frontend Application

You can open the frontend in one of two easy ways:

### Method A: Using Python's Built-in HTTP Server (Recommended)
1. Open a second PowerShell window.
2. Navigate to the prototype directory:
   ```powershell
   cd "D:\farm ai\dashboard_redesign_prototype"
   ```
3. Run the HTTP server:
   ```powershell
   python -m http.server 5500
   ```
4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5500/index.html
   ```

### Method B: Direct File Open
Double-click `D:\farm ai\dashboard_redesign_prototype\index.html` to open it directly in Google Chrome or Microsoft Edge.

---

## 6. How to Use the Application

### 6.1 Selecting a Street or Study Area
1. On the left navigation sidebar, click **"Overview"** or **"Corridor Intelligence"**.
2. View the 10 corridors in Ward 29 (e.g., *ST01 - Gopalasamy Kovil Street*, *ST08 - Raja Street - Sanganur Road*).
3. Review baseline metrics: Total assets, road length, pole density, and compliance rating.

---

### 6.2 OPTION A — Find a Place & Capture Street View
Use this option when you want to look up an address or landmark and capture street view imagery for instant AI detection.

1. In the left sidebar under **"Street Intelligence"**, click **"Find a Place & Capture Street View"**.
2. In the location search bar at the top, type a street name, temple, or landmark in Coimbatore (for example, *"Gopalasamy Kovil Street"* or *"Gandhi Nagar, Coimbatore"*).
3. The interactive map will center on the coordinates and display available coverage.
4. Navigate the street view panorama or map viewport to frame the infrastructure you want to inspect.
5. Click the large button:
   $$\text{\textbf{CAPTURE CURRENT STREET VIEW}}$$
6. A captured snapshot preview appears immediately in the review drawer.
7. Click **"Proceed with AI Analysis"**.
8. The backend analyzes the image and presents detected bounding boxes, asset counts, and passports.

---

### 6.3 OPTION B — Upload Street Images & Analyze
Use this option when you have survey photos, camera snapshots, or dashcam frames stored on your computer.

1. In the left sidebar under **"Street Intelligence"**, click **"Upload Street Images & Analyze"**.
2. Drag and drop one or more images into the dashed dropzone, or click **"Browse Files"**.
3. You can select sample images directly from the local archive:
   `D:\farm ai\dashboard_redesign_prototype\assets\raw_frames\`
4. The files appear in your upload queue with thumbnail previews and file sizes.
5. In the corridor selector dropdown, select the matching street (e.g., *"ST01 - Gopalasamy Kovil Street"*).
6. Click **"Start Street Intelligence Analysis"**.
7. The progress indicator will run, and the **Analysis Results Dashboard** will open automatically.

---

### 6.4 Inspecting Detections & Asset Passports
1. On the results page, the analyzed image is displayed with color-coded bounding boxes:
   - 🔵 **Building** (Blue)
   - 🟡 **Electric Pole** (Yellow)
   - 🟢 **Streetlight** (Green)
   - 🟣 **Commercial Sign** (Purple)
   - 🔴 **Transformer** (Red)
2. Hover over or click any bounding box to view its class name and detection confidence percentage.
3. Use the filter chips at the top to toggle specific asset classes on or off.
4. Scroll down to inspect the **Urban Asset Passports**:
   - Each unique asset displays its assigned UID (e.g., `AST-ST01-POLE-003`).
   - Displays estimated GPS coordinates, physical condition, and municipal flags.

---

### 6.5 Interacting with the Urban AI Agent
1. Click the **"Urban AI Agent"** button in the top navigation or sidebar.
2. In the chat input, type any municipal or technical question:
   - *"Which corridor has the highest number of leaning electric poles?"*
   - *"How many unassessed commercial hoardings were identified on Patel Road?"*
   - *"What is the streetlight infill requirement for ST06 Sanganur Canal Road?"*
3. Click **Send**. The AI Agent will respond with exact statistics, referencing the underlying municipal ledgers.

---

### 6.6 Reviewing Standalone Specialized Studios
Click **"Standalone Studios"** on the sidebar to access deep-dive tools:
- **Tri-View Studio (`tri_view_studio.html`)**: Interactive side-by-side split slider comparing raw street photography, YOLO AI bounding box predictions, and 3D architectural wireframes.
- **OCR Search Explorer (`ocr_search_explorer.html`)**: Search commercial establishments by name (Tamil or English) to detect unregistered shop signs.
- **Building Footprint Explorer (`building_explorer.html`)**: Cadastral map displaying polygon building boundaries, floor counts, and estimated property tax assessments.

---

### 6.7 Exporting Data & Reports
1. On any results page or municipal ledger, click the **"Export Data"** button.
2. Select your preferred export format:
   - **GeoJSON**: Exports vector points of all detected assets for import into QGIS, ArcGIS, or Google Earth.
   - **CSV**: Downloads formatted municipal ledgers (e.g., `ccmc_commercial_tax_ledger.csv`).
   - **JSON**: Downloads raw asset passport definitions.

---

## 7. Troubleshooting Common Errors

| Issue / Error | Likely Cause | Solution |
| :--- | :--- | :--- |
| **"Failed to connect to backend server"** | FastAPI server is not running on port 8000 | Open PowerShell, navigate to `dashboard_redesign_prototype/backend` and run `python urban_agent_server.py`. Verify `http://127.0.0.1:8000/health`. |
| **"CORS policy error in browser console"** | Direct file opening (`file:///`) blocked by browser security | Start local web server via `python -m http.server 5500` inside `dashboard_redesign_prototype/` and browse to `http://127.0.0.1:5500/index.html`. |
| **"EasyOCR not available / skipping OCR"** | `easyocr` library not installed or PyTorch lacks TorchVision | Run `pip install easyocr torchvision`. If on a lightweight CPU, OCR gracefully skips and YOLO detection proceeds normally. |
| **"No street view available at location"** | OpenStreetMap / Nominatim has limited panorama tiles at pin | Select a prominent road intersection (e.g., *Raja Street* or *Sathy Road*), or use Option B to upload a local street frame. |
| **"Out of Memory (OOM) during inference"** | Image resolution exceeds 4000x3000 on low-RAM laptop | The backend automatically resizes inputs to 640x640; ensure system has at least 2 GB free RAM. |

---

## 8. How to Stop the Application Safely

1. In the terminal window running the Python HTTP frontend server, press `Ctrl + C`.
2. In the terminal window running the FastAPI backend server, press `Ctrl + C`.
3. Close the browser tabs.
4. All generated logs, asset records, and exported CSVs remain safely preserved on your disk.
