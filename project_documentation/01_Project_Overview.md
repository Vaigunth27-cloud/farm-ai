# FarmwiseAI — Street View Urban Intelligence Platform
## Comprehensive Project Overview & Executive Summary

---

## 1. Executive Summary

### 1.1 Simple Non-Technical Explanation
Cities in India and around the developing world struggle to keep track of their physical infrastructure. Municipal corporations currently rely on slow, manual field inspections where surveyors walk down streets with clipboards to count streetlights, inspect electrical transformers, note road signs, and record commercial shops. This process is expensive, prone to human error, and becomes out of date within months.

**FarmwiseAI (Street View Urban Intelligence Platform)** transforms this paradigm. By turning ordinary street-level photos and dashcam footage into an intelligent, computer-vision-powered digital twin of the city, FarmwiseAI automatically identifies, classifies, georeferences, and tallies urban assets. When a photo of a street is captured—whether via live location search or batch image upload—our AI perception engine identifies buildings, utility poles, streetlights, transformers, and commercial signboards. It links each asset directly to its geographic coordinates on the city map and generates actionable municipal reports, such as commercial property tax ledgers and electric feeder maintenance work orders.

### 1.2 Technical Summary
FarmwiseAI is a dual-tier geospatial and computer vision platform engineered specifically for Indian urban streetscapes, with an empirical baseline deployed across **Ward 29 (North Zone), Coimbatore, Tamil Nadu**. The system integrates:
1. **Object Perception**: Ultralytics YOLO11 architectures (`yolo11n`, `yolo11s`, and fine-tuned custom weights `best.pt` / `best.onnx`) trained across 12 urban infrastructure classes.
2. **Text & Signage Extraction**: An EasyOCR deep learning pipeline parsing multilingual commercial signage (Tamil and English).
3. **Geospatial & Topological Association**: A Python/GeoJSON spatial association engine that binds detected asset bounding boxes to camera EXIF GPS tags and snaps them to verified corridor centerlines (`road_network_topology.geojson`).
4. **Contextual Urban AI Agent**: A zero-shot VLM routing engine coupled with a retrieval-augmented generation (RAG) assistant running on FastAPI, allowing city engineers to interrogate municipal datasets in natural language.
5. **Interactive Operations Dashboards**: A responsive web application featuring dual-mode street intelligence (Option A: Location Search & Street View Capture; Option B: Batch Image Upload & Analysis), alongside dedicated analytical studios for building footprints, commercial OCR, and tri-view verification.

---

## 2. Problem Statement & Motivation

### 2.1 The Urban Governance Blindspot
Municipal corporations like Coimbatore City Municipal Corporation (CCMC) and state utilities such as TANGEDCO (Tamil Nadu Generation and Distribution Corporation) face critical operational hurdles:
- **Revenue Leakage from Unassessed Commercial Property**: Up to 35% of commercial establishments operate with unassessed exterior floor additions or unregistered large commercial signage that evades property and advertisement tax.
- **Hazardous Electrical Infrastructure**: Overloaded distribution transformers, leaning low-tension (LT) electric poles, and uninsulated cables encroaching on residential tree canopies create lethal fire and electrocution hazards during monsoon seasons.
- **Infill Deficits in Street Lighting**: Public safety and women's nighttime mobility are severely compromised by unmapped "dark spots" where streetlights are either non-functional, missing from poles, or spaced beyond the standard 25–30 meter illumination threshold.
- **Disjointed Municipal Data Silos**: Engineering, tax, town planning, and electricity boards maintain disconnected paper records or isolated spreadsheets without shared geospatial coordinates or verifiable photographic evidence.

### 2.2 Why Existing Commercial Solutions Fail
Existing commercial mapping tools (such as proprietary global street view APIs) are either prohibitively expensive for municipal scale, legally restrict automated pixel analysis, or lack object detection models calibrated to the dense, cluttered visual complexity of Tier-II Indian cities. Typical western-trained models misclassify concrete electric poles as trees, fail on chaotic storefront signage, and ignore local drainage infrastructure.

---

## 3. The Proposed Solution

FarmwiseAI bridges the gap between raw street imagery and auditable municipal governance through an end-to-end intelligence pipeline:

```
[ Street Imagery ] ──> [ YOLO11 Perception ] ──> [ Spatial Association ] ──> [ Digital Twin & Ledgers ]
 (Option A / B)         (12 Urban Classes)        (GPS & Polyline Snap)       (Tax & Feeder Directives)
```

### Key Solution Pillars:
1. **Evidence-Linked Infrastructure Registry**: Every detected asset maintains a permanent visual audit trail, linking its unique identifier (e.g., `AST-ST01-POLE-004`) to its exact pixel bounding box and camera GPS coordinates.
2. **Flexible Dual Ingestion Modalities**:
   - **Option A (Find & Capture)**: Allows municipal officers to search any street, landmark, or temple, navigate an interactive street view viewport, and capture real-time snapshots for analysis.
   - **Option B (Upload & Analyze)**: Enables field survey vehicles or dashcams to upload batches of high-resolution images with automatic EXIF GPS extraction and corridor queue processing.
3. **Automated Municipal Actionability**: Rather than outputting abstract bounding boxes, FarmwiseAI directly populates standardized government deliverables:
   - **CCMC Commercial Property Tax Ledger**
   - **CCMC Streetlight Infill Directives**
   - **TANGEDCO Feeder Work Orders**
4. **Natural Language Urban AI Assistant**: A conversational agent allowing municipal commissioners to ask questions such as *"How many leaning poles exist along Sanganur Canal Road?"* and receive immediate data-backed responses with source ledger citations.

---

## 4. Target Users & Stakeholders

| Stakeholder Group | Operational Use Case | Core Platform Touchpoint |
| :--- | :--- | :--- |
| **CCMC Revenue & Tax Officers** | Identify unassessed commercial shops, hoardings, and illegal building floor expansions | Option B Batch Processing, OCR Search Explorer, Tax Ledger CSV |
| **TANGEDCO Utility Engineers** | Audit electric pole alignment, transformer clearances, and vegetation encroachment | Option A Viewport, Urgent Issue Feed, Feeder Work Order Directives |
| **Municipal Streetlight Contractors** | Identify unlit pole intervals, dark spots, and missing luminaire fixtures | Streetlight Infill Directives, Corridor Intelligence Scorecard |
| **City Planners & Ward Councilors** | Prioritize capital expenditure, pedestrian sidewalk infill, and storm drainage | Master Digital Twin Portal, GeoJSON GIS Layers, Urban AI Agent |
| **Field Survey Crews** | Capture geotagged dashcam runs and ground-truth AI detections | Option B Upload Queue, Tri-View Verification Studio |

---

## 5. Study Area & Dataset Specification

### 5.1 Study Area
The primary empirical study area is **Ward 29, North Zone, Coimbatore City Municipal Corporation, Tamil Nadu, India**, encompassing a dense mix of residential layouts, high-traffic commercial arterial roads, canal corridors, and mixed-use commercial junctions.

### 5.2 Curated Corridor Dataset
The verified field dataset contains **108 high-resolution street-level frames** systematically gathered across **10 representative urban corridors**:

| Corridor ID | Corridor Name | Street Character & Context | Image Count |
| :--- | :--- | :--- | :---: |
| **ST01** | Gopalasamy Kovil Street | Mixed commercial & temple approach, narrow carriage | 10 |
| **ST02** | Gandhi Nagar | Residential layout with regular pole spacing | 11 |
| **ST03** | Ganapathy Pudur 3rd Street | Medium density residential, overhead powerlines | 10 |
| **ST04** | Sridevi Nagar 4th Street | Residential, high tree canopy encroachment | 11 |
| **ST05** | Bharathi Nagar / Sathy Road | High-density arterial transition, commercial frontage | 10 |
| **ST06** | Sanganur Canal Road / KRG Nagar | Open storm drainage, high utility density | 13 |
| **ST07** | Patel Road / PN Palayam | Dense retail storefronts and heavy commercial signage | 10 |
| **ST08** | Raja Street - Sanganur Road | Major arterial corridor, high pedestrian/vehicle activity | 20 |
| **ST09** | Sri Ganapathy Gardens 3rd Street | Compact residential cul-de-sac | 6 |
| **ST10** | Avaram Palayam Street | Industrial-commercial arterial with distribution transformers | 7 |
| **Total** | **10 Distinct Urban Corridors** | **Full Spectrum of Tier-II Indian Urban Topologies** | **108 Frames** |

---

## 6. Implementation Status & Feature Matrix

To maintain strict architectural honesty, the platform features are categorized by verified status:

```
[ IMPLEMENTED & TESTED ] ──────────> Working code, verified in browser/backend
[ PARTIALLY IMPLEMENTED ] ─────────> Core logic functional; refinement ongoing
[ ONGOING WORK ] ──────────────────> Active dataset annotation & model retraining
[ PLANNED ARCHITECTURE ] ──────────> Documented specifications for future scale
```

| Subsystem / Feature | Implementation Status | Supporting Source Code / Evidence |
| :--- | :---: | :--- |
| **Option A (Find & Capture)** | **IMPLEMENTED** | `dashboard_redesign_prototype/index.html`, `app.js` |
| **Option B (Upload & Analyze)** | **IMPLEMENTED** | `dashboard_redesign_prototype/index.html`, `app.js` |
| **FastAPI Backend Service** | **IMPLEMENTED** | `dashboard_redesign_prototype/backend/urban_agent_server.py` |
| **YOLO11 Model Inference** | **IMPLEMENTED** | `yolo11n.pt`, `yolo11s.pt`, `prototype_model/best.pt` |
| **EasyOCR Signage Extraction** | **IMPLEMENTED** | `urban_agent_server.py` (`get_ocr_reader()`) |
| **Urban AI Agent (RAG Chat)** | **IMPLEMENTED** | `urban_agent_server.py` (`POST /api/chat`) |
| **Master Digital Twin Portal** | **IMPLEMENTED** | `🌟 MASTER UNIFIED PLATFORM/urban_digital_twin_portal.html` |
| **Standalone Analytical Studios** | **IMPLEMENTED** | `🌐 INDIVIDUAL STANDALONE STUDIOS/` (4 studios) |
| **Municipal Directives & Ledgers** | **IMPLEMENTED** | `📋 MUNICIPAL REPORTS & WORK ORDERS/` |
| **Corridor GeoJSON Topology** | **IMPLEMENTED** | `🗺️ MASTER GIS & TABULAR DATASETS/road_network_topology.geojson` |
| **EXIF GPS Coordinate Parser** | **IMPLEMENTED** | `urban_agent_server.py` (`extract_exif_gps()`) |
| **Manual Ground-Truth Annotation** | **ONGOING** | `🧠 MACHINE LEARNING MODELS & ROUTING/dataset_splits/` |
| **YOLO Retraining on Verified Labels**| **ONGOING** | `runs/detect/val-1 to val-34/`, `train_yolo_gpu.py` |
| **Cross-Frame Asset Deduplication** | **PARTIAL** | Spatial buffer logic active; Hungarian matcher planned |
| **AWS Cloud Serverless Sync** | **CONFIGURED** | `☁️ AWS SERVERLESS CLOUD ARCHITECTURE/` (IaC & Lambda) |

---

## 7. Current Limitations & Technical Constraints

1. **Monocular Depth & GPS Inaccuracies**: Consumer dashcam imagery lacks native LiDAR depth. The current system projects coordinates using bottom-center bounding box heuristics combined with camera EXIF GPS. Severe GPS multi-path errors between multi-story buildings can offset asset coordinates by 5–10 meters.
2. **Visual Occlusion & Clutter**: Dense tree canopies in residential streets (e.g., ST04) frequently obscure streetlights and transformers, causing false negatives in automated detection passes.
3. **Fine-Tuning on Local Datasets**: Pre-trained YOLO models perform well on general building facades and vehicles but require extensive local re-annotation to distinguish between low-tension electric poles, high-tension towers, and telephone distribution pillars. Active annotation is ongoing.
4. **Duplicate Matching Across Overlapping Frames**: When a vehicle drives at 20 km/h taking 1 frame per second, the same transformer appears across 3–4 consecutive images. Spatial clustering currently groups these within a 5-meter window, but automated cross-frame feature re-identification is still in development.

---

## 8. Strategic Roadmap & Future Milestones

- **Milestone 1 (Immediate)**: Complete manual bounding-box annotation across all 108 corridor frames with 100% verified labels.
- **Milestone 2 (Short-Term)**: Execute full hyperparameter training on GPU (50–100 epochs) to achieve mAP50 $\ge 0.75$ across all 12 classes on unseen test corridors.
- **Milestone 3 (Medium-Term)**: Deploy automated multi-view Hungarian matching algorithm for cross-frame asset deduplication.
- **Milestone 4 (Long-Term)**: Provision AWS serverless pipeline (S3 $\to$ Lambda $\to$ RDS PostGIS) for continuous streaming ingestion from municipal garbage collection vehicle cameras.
