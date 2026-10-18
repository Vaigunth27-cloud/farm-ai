# FarmwiseAI Project 2 — Dashboard Prototype Setup and Run Instructions

**Isolated Prototype Location:** `d:\farm ai\dashboard_redesign_prototype\`  
**Entry Point:** `d:\farm ai\dashboard_redesign_prototype\index.html`  
**Platform Architecture:** Zero-dependency static web application (HTML5, Vanilla JS, CSS3, Leaflet 1.9.4)  

---

## 1. Quick Launch Options

### Option A: Instant Direct Browser Launch (No Server Required)
The prototype is 100% self-contained and functions directly via the Windows file protocol:
1. Open Windows File Explorer and navigate to:
   `D:\farm ai\dashboard_redesign_prototype\`
2. Double-click **`index.html`** to open in Google Chrome, Microsoft Edge, or Mozilla Firefox.
3. The dashboard will load immediately with all 12 workspaces, 465 digital assets, and interactive GIS layers enabled.

### Option B: Local Python HTTP Server (Recommended for Full Media Streaming)
To run the prototype with local HTTP asset streaming:
1. Open PowerShell or Terminal in the project root:
   ```powershell
   python -m http.server 8080 --directory "D:\farm ai"
   ```
2. Open your browser and navigate to:
   ```
   http://localhost:8080/dashboard_redesign_prototype/index.html
   ```
3. Use the sidebar rail to navigate across all 12 workspaces or append route hashes (e.g. `http://localhost:8080/dashboard_redesign_prototype/index.html#explorer`).

---

## 2. Recommended System Requirements & Browsers

- **Supported Browsers:**
  - Google Chrome 110+ (Recommended)
  - Microsoft Edge 110+
  - Mozilla Firefox 115+
  - Safari 16+
- **Optimal Display Resolution:**
  - Desktop / Workstation: $1920 \times 1080$ or $1440 \times 900$ (Full layout with expanded sidebar)
  - Laptop: $1366 \times 768$ (Compact responsive layout)
  - Tablet: $1024 \times 768$ (Auto-collapsed sidebar rail)
  - Mobile: $375 \times 812$ (Responsive drawer with slide-in navigation)
- **Internet Connection:**
  - Required only for downloading CartoDB Positron map base tiles (`cartocdn.com`) and Leaflet CSS/JS.
  - All municipal data (GeoJSON, 465 assets, 108 buildings, 201 signboards) is embedded locally in `data/farmwise_data.js` and requires zero external database connection.

---

## 3. Directory Layout & Protected Asset Safeguards

```
D:\farm ai\
├── 🌟 MASTER UNIFIED PLATFORM\
│   └── urban_digital_twin_portal.html        <- 100% PROTECTED & UNTOUCHED
├── 🗺️ MASTER GIS & TABULAR DATASETS\          <- 100% PROTECTED & UNTOUCHED
├── 📸 RAW & ANNOTATED CORRIDOR IMAGERY\       <- 100% PROTECTED & UNTOUCHED
├── 🧠 MACHINE LEARNING MODELS & ROUTING\      <- 100% PROTECTED & UNTOUCHED
│
└── 🚀 dashboard_redesign_prototype\           <- NEW ISOLATED REDESIGN
    ├── index.html                            <- Master SPA Entry Point
    ├── assets\
    │   ├── css\
    │   │   └── design_system.css             <- White & Forest Green Design System
    │   └── js\
    │       └── app.js                        <- Router & Application Controller
    ├── data\
    │   └── farmwise_data.js                  <- 1.32 MB Authoritative Data Bundle
    └── docs\
        ├── DESIGN_SYSTEM.md                  <- Visual Identity & Token Specs
        ├── PAGE_AND_NAVIGATION_MAP.md        <- Route Hierarchy & Capabilities
        ├── REUSABLE_COMPONENTS.md            <- UI Component Library
        ├── RUN_INSTRUCTIONS.md               <- Setup & Verification Guide
        ├── TEST_REPORT.md                    <- Automated Selenium Test Results
        ├── INTEGRATION_DEPENDENCIES.md       <- Demo Elements vs Production Deps
        ├── PROTECTED_ASSETS_INTEGRITY_REPORT.md <- Asset Verification Checksums
        └── screenshots\                      <- High-Res Captured Screenshots
```
