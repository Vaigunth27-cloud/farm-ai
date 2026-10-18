# Autonomous Street View Urban Digital Twin & AI Perception Pipeline
### FarmwiseAI Product Challenge 2026 — Task 5: Street View Urban Intelligence
**Team 24** | **Target Area**: Coimbatore City Municipal Corporation (CCMC) — Ward 29 (LGD: 29), North Zone, Tamil Nadu  
**Deployment Region**: AWS Mumbai (`ap-south-1`) | **Execution Role**: `arn:aws:iam::387039786704:role/FAI-TCE-LambdaExecutionRole`

---

## 🌟 Executive Project Directory Hierarchy

```
D:\farm ai\
├── 🌟 MASTER UNIFIED PLATFORM
│   ├── urban_digital_twin_portal.html        <- Master 11-in-1 Flagship Platform (3.21 MB)
│   ├── HACKATHON_PRESENTATION.html           <- Interactive 10-slide pitch deck (press 'F' for fullscreen)
│   ├── HACKATHON_PRESENTATION.md             <- Presentation slides text
│   ├── DEMO_VIDEO_WALKTHROUGH_SCRIPT.md      <- Timed 3-min & 5-min demo video recording scripts
│   ├── SUBMISSION_MANIFEST.md                <- Comprehensive judge documentation index
│   ├── PROJECT_AUDIT.md                      <- Complete 18-phase verification & audit report
│   └── index.html                            <- Sub-launcher for Master Platform
│
├── 🌐 INDIVIDUAL STANDALONE STUDIOS (Also accessible independently)
│   ├── tri_view_studio.html                  <- Synchronized Street View HUD + Map + Passports (1.13 MB)
│   ├── gis_digital_twin_baseline.html        <- Full GIS Map with road measurement tool (720 KB)
│   ├── building_explorer.html                <- 108 buildings with 10 property parameters & blueprints (208 KB)
│   ├── ocr_search_explorer.html              <- 201 OCR signboards with Tamil/English search (158 KB)
│   ├── asset_inventory_explorer.html         <- 465 fixed assets with digital passports & health grading (805 KB)
│   ├── corridor_intelligence_dashboard.html  <- 10 corridors with CBI & SLAS scorecards (36 KB)
│   ├── urban_ai_assistant.html               <- Zero-hallucination NLP assistant with 8 benchmark queries (1.12 MB)
│   ├── municipal_report_portal.html          <- TANGEDCO & CCMC work orders & ₹20.40 L revenue ledger (158 KB)
│   ├── cloud_architecture_dashboard.html     <- AWS Lambda + ONNX edge deployment & cost calculator (27 KB)
│   ├── vlm_routing_visualizer.html           <- Small-model first & selective VLM escalation visualizer (29 KB)
│   ├── urban_annotation_studio.html          <- Interactive YOLO annotation review studio (132 KB)
│   └── index.html                            <- Visual gallery launcher for all 11 studios
│
├── 🧠 MACHINE LEARNING MODELS & ROUTING
│   ├── prototype_model/
│   │   ├── best.pt                           <- PyTorch model weights (5.45 MB)
│   │   ├── best.onnx                         <- 10.12 MB ONNX artifact (Opset 18, 42ms CPU, ~16ms Jetson)
│   │   ├── urban_intel_v1/                   <- Training run artifacts, PR curves, F1 curves
│   │   └── urban_intel_val/                  <- Validation confusion matrices & batch predictions
│   ├── vlm_routing_engine/
│   │   ├── routing_engine.py                 <- Two-tier routing logic & cost/latency optimizer
│   │   ├── routing_decisions.csv             <- 774 pipeline classification decisions (201 KB)
│   │   └── routing_benchmark_results.json    <- 74.9% fast path, 74.9% cost reduction, +5.8% acc
│   ├── prototype_predictions/                <- Hold-out test set inference visuals
│   ├── yolo_annotations/                     <- 108 YOLO txt labels + classes.txt
│   └── README.md                             <- ML & routing engine documentation
│
├── ☁️ AWS SERVERLESS CLOUD ARCHITECTURE
│   ├── template.yaml                         <- AWS CloudFormation template (Lambda, S3, API Gateway)
│   ├── terraform/                            <- Terraform IaC (main.tf, variables.tf, outputs.tf)
│   ├── lambda_function.py                    <- Python 3.12 serverless handler with ONNX Runtime
│   ├── test_lambda_local.py                  <- 6/6 unit tests passing in 0.001s
│   ├── edge_capture_daemon.py                <- Vehicle camera edge simulator (HTTP POST & queue)
│   ├── architecture_specification.md         <- Cloud architecture specification & security policies
│   └── cloud_architecture_dashboard.html     <- Interactive architecture & pricing visualizer
│
├── 📋 MUNICIPAL REPORTS & WORK ORDERS
│   ├── tangedco_feeder_work_orders.csv       <- 108 TANGEDCO utility pole repair directives (33 P1)
│   ├── tangedco_feeder_work_orders.md        <- Executive summary with clearance violations
│   ├── ccmc_streetlight_infill_directives.csv <- 18 dark spot luminaire installations
│   ├── ccmc_streetlight_infill_directives.md  <- Photometric infill summary
│   ├── ccmc_commercial_tax_ledger.csv        <- 201 commercial properties with ₹20.40 L annual tax
│   ├── ccmc_commercial_tax_ledger.md         <- CCMC revenue recovery report
│   └── municipal_reporting_summary.json      <- Executive summary with 0.62 yr payback on ₹12.71 L capex
│
├── 🗺️ MASTER GIS & TABULAR DATASETS
│   ├── urban_assets_digital_twin.geojson     <- 465 point features with passports & spatial vectors (848 KB)
│   ├── road_network_topology.geojson         <- 10 surveyed road centerlines with stationing (15 KB)
│   ├── master_images.csv                     <- 108 standardized survey images (23 KB)
│   ├── master_streets.csv                    <- 10 surveyed corridor profiles (3 KB)
│   ├── master_metadata.csv                   <- 108 rows with 29 attributes per frame (47 KB)
│   ├── detections.csv                        <- 465 fixed infrastructure detections (114 KB)
│   ├── building_intelligence.csv             <- 108 buildings with 10 property parameters & map pins (110 KB)
│   ├── ocr_intelligence.csv                  <- 201 commercial signboards across 11 trade sectors (56 KB)
│   ├── spatial_relationships.csv             <- Perpendicular road setbacks & nearest-neighbor links (44 KB)
│   ├── corridor_intelligence_scorecard.csv   <- Corridor archetypes, CBI, SLAS, and municipal grades (4 KB)
│   └── README.md                             <- Spatial coordinate system (EPSG:4326) & data dictionary
│
├── 🐍 COMPLETE PIPELINE CODE ARCHIVE
│   └── pipeline_scripts/                     <- 42 Python generator and audit scripts archived from scratch!
│
├── 📸 RAW & ANNOTATED CORRIDOR IMAGERY
│   ├── annotated_images/                     <- 108 YOLO labeled frames
│   ├── building_annotated_images/            <- 108 floor blueprint & height overlays
│   ├── ocr_annotated_images/                 <- 201 OCR bounded commercial signage
│   └── (ST01 to ST10 Corridors...)/          <- Sathy Rd, Avaram Palayam, Gandhi Nagar, etc.
│
├── 🚀 index.html                             <- Master Enterprise Suite Launcher & Live KPI Filter Hub
├── ⚡ 00_START_HERE.html                     <- Auto-redirect Instant Launcher
└── 📖 README.md                              <- Master Markdown Repository Documentation
```

---

## 🚀 Quick Launch Guide

1. **Master Unified Digital Twin Platform (All 11 Modules in 1)**:
   - Double-click [`🌟 MASTER UNIFIED PLATFORM/urban_digital_twin_portal.html`](file:///D:/farm%20ai/🌟%20MASTER%20UNIFIED%20PLATFORM/urban_digital_twin_portal.html)
   - Features: Interactive 3D GIS Map, Street View HUD, Building Blueprints, OCR Search, Digital Asset Passports, AI Assistant, Municipal Work Orders, AWS Cloud Architecture, and VLM Routing!
2. **Interactive Hackathon Presentation Deck**:
   - Double-click [`🌟 MASTER UNIFIED PLATFORM/HACKATHON_PRESENTATION.html`](file:///D:/farm%20ai/🌟%20MASTER%20UNIFIED%20PLATFORM/HACKATHON_PRESENTATION.html)
   - Press **`F`** for Fullscreen, **`Right Arrow` / `Left Arrow`** to advance slides.
3. **Master Interactive File Browser**:
   - Double-click [`index.html`](file:///D:/farm%20ai/index.html) to open the Enterprise Suite Hub.

---

## 📊 Key Engineering & Financial Highlights

| Category | Benchmark Metric | Production Value | Verification File |
| :--- | :--- | :--- | :--- |
| **Fixed Assets** | Detected & Geotagged | **465 Infrastructure Assets** (100% Passports) | [`🗺️ MASTER GIS & TABULAR DATASETS/urban_assets_digital_twin.geojson`](file:///D:/farm%20ai/🗺️%20MASTER%20GIS%20&%20TABULAR%20DATASETS/urban_assets_digital_twin.geojson) |
| **Building Footprints** | 10 Property Parameters | **108 Buildings** (62 Cadastre Matches, 403 AI Additions) | [`🗺️ MASTER GIS & TABULAR DATASETS/building_intelligence.csv`](file:///D:/farm%20ai/🗺️%20MASTER%20GIS%20&%20TABULAR%20DATASETS/building_intelligence.csv) |
| **Commercial OCR** | Bi-lingual Signage | **201 Signboards** (220 extracted keywords, 11 trade sectors) | [`🗺️ MASTER GIS & TABULAR DATASETS/ocr_intelligence.csv`](file:///D:/farm%20ai/🗺️%20MASTER%20GIS%20&%20TABULAR%20DATASETS/ocr_intelligence.csv) |
| **Edge AI Engine** | ONNX Runtime Inference | **10.12 MB ONNX** (42.0ms on CPU, ~16ms on Jetson) | [`🧠 MACHINE LEARNING MODELS & ROUTING/prototype_model/best.onnx`](file:///D:/farm%20ai/🧠%20MACHINE%20LEARNING%20MODELS%20&%20ROUTING/prototype_model/best.onnx) |
| **Two-Tier Routing** | Small-Model First | **74.94% Fast Path (39.7ms)** / 25.06% VLM Escalation | [`🧠 MACHINE LEARNING MODELS & ROUTING/vlm_routing_engine/routing_decisions.csv`](file:///D:/farm%20ai/🧠%20MACHINE%20LEARNING%20MODELS%20&%20ROUTING/vlm_routing_engine/routing_decisions.csv) |
| **Routing Efficiency** | Cost & Latency Optimization | **-74.87% Cost Reduction**, **3.3x Speedup**, **+5.8% Accuracy** | [`🧠 MACHINE LEARNING MODELS & ROUTING/vlm_routing_engine/routing_benchmark_results.json`](file:///D:/farm%20ai/🧠%20MACHINE%20LEARNING%20MODELS%20&%20ROUTING/vlm_routing_engine/routing_benchmark_results.json) |
| **AI Assistant** | Zero-Hallucination Precision | **100.0% Precision (8/8 ground-truth benchmark queries)** | [`🌐 INDIVIDUAL STANDALONE STUDIOS/nlp_assistant_evaluation.json`](file:///D:/farm%20ai/🌐%20INDIVIDUAL%20STANDALONE%20STUDIOS/nlp_assistant_evaluation.json) |
| **TANGEDCO Utility** | Safety Work Orders | **108 Poles** (33 P1 Critical Clearance Violations) | [`📋 MUNICIPAL REPORTS & WORK ORDERS/tangedco_feeder_work_orders.csv`](file:///D:/farm%20ai/📋%20MUNICIPAL%20REPORTS%20&%20WORK%20ORDERS/tangedco_feeder_work_orders.csv) |
| **Streetlight Infill** | CCMC Dark Spot Directives | **18 Luminaire Installations** (Photometric Infill) | [`📋 MUNICIPAL REPORTS & WORK ORDERS/ccmc_streetlight_infill_directives.csv`](file:///D:/farm%20ai/📋%20MUNICIPAL%20REPORTS%20&%20WORK%20ORDERS/ccmc_streetlight_infill_directives.csv) |
| **Property Tax Recovery**| Unassessed Commercial Revenue | **₹20,40,000/year** (₹20.40 Lakhs from 201 commercial units) | [`📋 MUNICIPAL REPORTS & WORK ORDERS/ccmc_commercial_tax_ledger.csv`](file:///D:/farm%20ai/📋%20MUNICIPAL%20REPORTS%20&%20WORK%20ORDERS/ccmc_commercial_tax_ledger.csv) |
| **Municipal ROI** | Total Capex Payback | **0.62 Years (7.4 Months)** on ₹12,71,000 Capex | [`📋 MUNICIPAL REPORTS & WORK ORDERS/municipal_reporting_summary.json`](file:///D:/farm%20ai/📋%20MUNICIPAL%20REPORTS%20&%20WORK%20ORDERS/municipal_reporting_summary.json) |
| **AWS Serverless** | Unit Tests & Conformance | **6/6 Tests Passing in 0.001s** (Lambda, S3, API Gateway IaC) | [`☁️ AWS SERVERLESS CLOUD ARCHITECTURE/test_lambda_local.py`](file:///D:/farm%20ai/☁️%20AWS%20SERVERLESS%20CLOUD%20ARCHITECTURE/test_lambda_local.py) |

---
*Created by Team 24 for the FarmwiseAI TCE Product Challenge 2026.*
