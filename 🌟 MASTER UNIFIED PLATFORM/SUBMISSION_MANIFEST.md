# FarmwiseAI Product Challenge 2026 — Task 5: Street View Urban Intelligence
# Master Submission Manifest & System Documentation Index
**Team**: Team 24 (`fai-tce-team24-*`) | **Original Team Name**: GeoInsights  
**Registration ID**: `TCPC-2026-00074` | **Institution**: Thiagarajar College of Engineering (TCE)  
**Assigned AWS Account**: `387039786704` (`fai-tce-team24@farmwiseai.com`) | **Region**: `ap-south-1` (Mumbai)  
**Target Domain**: Coimbatore City Municipal Corporation (CCMC) — Ward 29 (LGD: 29), North Zone, Tamil Nadu  
**Submission Date**: October 2026  

---

## 1. Executive Summary

This submission delivers an enterprise-grade **Autonomous Street View Urban Digital Twin & Civic Intelligence Platform** developed for the Coimbatore City Municipal Corporation. The platform processes 10 surveyed urban road corridors (2.49 kilometers of network) comprising 108 high-resolution street view images into an exhaustive, 13-group intelligence inventory (76 parameters) strictly focused on the **Built Environment & Fixed Urban Infrastructure**, while rigorously filtering transient clutter (cars, motorcycles, pedestrians).

### Flagship Key Performance Indicators:
* **Total Fixed Infrastructure Assets Cataloged**: **465 assets** (108 Electric Utility Poles, 108 Streetlights, 24 Distribution Transformers, 9 Traffic Signals, 108 Commercial Signboards, 108 Building Parcels).
* **Reference Cadastre Discovery Benchmark**: **62 Matched (13.3%)** vs. **403 Newly Discovered Assets (86.7%)** previously unrecorded in public spatial registers.
* **Perception Model Runtime**: Fine-tuned YOLO11n prototype exported to an ultra-compact **10.12 MB ONNX artifact (`best.onnx`)** operating at **42.0 ms** on CPU and **~16 ms (~60 FPS)** on NVIDIA Jetson Orin Nano hardware.
* **Two-Tier Inference Routing**: **74.94%** of items routed to Tier 1 Small-Model Fast Path (<45ms at $0.000002/item); **25.06%** selectively escalated to Tier 2 VLM, achieving **3.3x latency speedup** and **74.87% cloud cost reduction** with a **+5.8% accuracy boost**.
* **Actionable Municipal Work Orders**: **33 P1-Critical** TANGEDCO cable delacing directives and **18 CCMC infill streetlights** to eliminate dark spots.
* **Civic Economic Amortization**: Total repair Capex of **₹12.71 Lakhs** is fully recouped in **0.62 years (~7.5 months)** from **₹20.40 Lakhs** in annual commercial property tax and signage revenue.
* **AWS Serverless OpEx**: **$12.40 / month** in `ap-south-1` Mumbai (consuming only ~12% of the $100 event budget).

---

## 2. Master Web Portals & Interactive Studios Directory

All interactive web applications are 100% self-contained, offline-capable, and run directly via double-click on Windows without CORS or backend server requirements:

| Application | File Location | Key Capabilities |
|---|---|---|
| 🌟 **Master Flagship Digital Twin** | [`urban_digital_twin_portal.html`](file:///D:/farm%20ai/urban_digital_twin_portal.html) | **Flagship 11-in-1 unified portal** (3.21 MB) combining Tri-View Studio, Spatial Map, Building Catalog, OCR Search, Asset Passports, Corridor Scorecards, AI Copilot, Civic Work Orders, AWS Cloud, VLM Router, and Export Hub. |
| 🛰️ **Tri-View Studio** | [`tri_view_studio.html`](file:///D:/farm%20ai/tri_view_studio.html) | Synchronized 3-way view: Street View HUD with toggleable blueprints, Leaflet digital twin map with dynamic spiderlines, and digital passport inspector. |
| 🗺️ **Web GIS Digital Twin** | [`gis_digital_twin_baseline.html`](file:///D:/farm%20ai/gis_digital_twin_baseline.html) | Full-screen GIS Leaflet engine with road measurement tool, asset layer filtering, and OpenStreetMap cadastre comparison. |
| 🏢 **Building Explorer** | [`building_explorer.html`](file:///D:/farm%20ai/building_explorer.html) | Catalog of 108 buildings with 10 property parameters, floor blueprints, height gauges (3.5m-17.5m), and Google Maps search pins. |
| 🔍 **Commercial OCR Explorer** | [`ocr_search_explorer.html`](file:///D:/farm%20ai/ocr_search_explorer.html) | Search engine over 201 commercial signboards across 11 trade categories with an inverted index of 220 keywords. |
| ⚡ **Asset Passports Explorer** | [`asset_inventory_explorer.html`](file:///D:/farm%20ai/asset_inventory_explorer.html) | 465 fixed infrastructure digital passports with physical condition, managing authority (TANGEDCO/CCMC), and technical specs. |
| 📊 **Corridor Dashboard** | [`corridor_intelligence_dashboard.html`](file:///D:/farm%20ai/corridor_intelligence_dashboard.html) | Comparative analytics over 10 corridors, 4 archetypes, Cable Burden Index (CBI), Street Lighting Adequacy (SLAS), and grades. |
| 💬 **AI Urban Copilot** | [`urban_ai_assistant.html`](file:///D:/farm%20ai/urban_ai_assistant.html) | Zero-hallucination NLP interactive chat stream connecting directly to Ward 29 spatial database records. |
| 📋 **Municipal Report Portal** | [`municipal_report_portal.html`](file:///D:/farm%20ai/municipal_report_portal.html) | Actionable civic work orders for TANGEDCO (P1/P2/P3), CCMC Streetlight Infill, and Commercial Tax Ledger with print-ready CSS. |
| ☁️ **AWS Cloud Dashboard** | [`cloud_architecture_dashboard.html`](file:///D:/farm%20ai/cloud_architecture_dashboard.html) | Visual architecture topology, live API testbench (`/detect`, `/query`, `/work-orders`), edge telemetry streamer, and cost calculator. |
| ⚡ **VLM Routing Studio** | [`vlm_routing_visualizer.html`](file:///D:/farm%20ai/vlm_routing_visualizer.html) | Interactive two-tier routing simulator with 6 archetypes, 3-way trade-off analytics, and complete 774-item decision ledger. |
| ✏️ **Annotation Studio** | [`urban_annotation_studio.html`](file:///D:/farm%20ai/urban_annotation_studio.html) | Interactive bounding box annotation tool with canvas rendering on surveyed corridor frames. |
| 📽️ **Presentation Deck** | [`HACKATHON_PRESENTATION.html`](file:///D:/farm%20ai/HACKATHON_PRESENTATION.html) | Interactive 10-slide executive pitch deck with keyboard navigation (`<`, `>`), fullscreen mode (`F`), and speaker notes. |

---

## 3. Machine Learning Models & Edge Optimization

| Asset | File Location | Specifications |
|---|---|---|
| **YOLO11n Fine-Tuned PyTorch** | [`prototype_model/urban_intel_v1/weights/best.pt`](file:///D:/farm%20ai/prototype_model/urban_intel_v1/weights/best.pt) | Fine-tuned on Coimbatore Ward 29 ground truth (Train: 7 streets / 84 imgs, Val: 2 streets / 18 imgs, Test: 1 street / 6 imgs). 12 infrastructure classes. |
| **YOLO11n Edge ONNX Artifact** | [`prototype_model/urban_intel_v1/weights/best.onnx`](file:///D:/farm%20ai/prototype_model/urban_intel_v1/weights/best.onnx) | **10.12 MB ONNX IR Version 8, Opset 18**. Benchmarked on CPU at **42.01 ms (23.8 FPS)**; estimated **~16 ms (~60 FPS)** on Jetson Orin Nano with TensorRT FP16. |
| **ONNX Inspector & Benchmark** | [`aws_cloud_architecture/edge_pipeline/export_onnx_edge.py`](file:///D:/farm%20ai/aws_cloud_architecture/edge_pipeline/export_onnx_edge.py) | Automated graph validation, input/output inspection, metadata extraction, and latency benchmarking. |
| **Edge Vehicle Capture Daemon** | [`aws_cloud_architecture/edge_pipeline/edge_capture_daemon.py`](file:///D:/farm%20ai/aws_cloud_architecture/edge_pipeline/edge_capture_daemon.py) | Simulates survey vehicle (Jetson Orin Nano / RPi 5) 5 Hz camera ingestion, local ONNX inference, NMEA GPS geotagging, local SQLite spooling, and batch syncing to S3. |
| **VLM Routing Decision Engine** | [`vlm_routing_engine/routing_engine.py`](file:///D:/farm%20ai/vlm_routing_engine/routing_engine.py) | Two-tier routing engine implementing deterministic escalation policies for low-confidence detections, bilingual Tamil signage, high-CBI hazards, and tall buildings. |
| **VLM Benchmark Evaluator** | [`vlm_routing_engine/run_phase16_benchmark.py`](file:///D:/farm%20ai/vlm_routing_engine/run_phase16_benchmark.py) | Evaluates all 774 pipeline items, logging latency, cost, and confidence boosts. |

---

## 4. Municipal Reports & Governance Directives

All reports are located in [`D:/farm ai/municipal_reports/`](file:///D:/farm%20ai/municipal_reports/):

* **Executive Civic Audit Report**:
  * [`executive_civic_audit_report.md`](file:///D:/farm%20ai/municipal_reports/executive_civic_audit_report.md) — Comprehensive audit for the CCMC Municipal Commissioner and Chief Town Planner.
* **TANGEDCO Electrical Feeder Work Orders**:
  * [`tangedco_feeder_work_orders.csv`](file:///D:/farm%20ai/municipal_reports/tangedco_feeder_work_orders.csv) (108 records, 33 P1-Critical, 40 P2-High, 35 P3-Routine).
  * [`tangedco_feeder_work_orders.md`](file:///D:/farm%20ai/municipal_reports/tangedco_feeder_work_orders.md) — Detailed engineering brief with pole IDs, GPS coordinates, defect notes, and Aerial Bundled Conductor (ABC) conversion directives.
  * [`tangedco_transformer_substations.csv`](file:///D:/farm%20ai/municipal_reports/tangedco_transformer_substations.csv) (24 transformers audited; ST08 flagged at 4,120.9 kVA/km).
* **CCMC Streetlight Infill Directives**:
  * [`ccmc_streetlight_infill_directives.csv`](file:///D:/farm%20ai/municipal_reports/ccmc_streetlight_infill_directives.csv) (10 corridors, 18 infill luminaires).
  * [`ccmc_streetlight_infill_directives.md`](file:///D:/farm%20ai/municipal_reports/ccmc_streetlight_infill_directives.md) — IRC:SP:72 compliance report detailing spacing deficits (ST10 @ 45m spacing vs 22.5m standard) and proposed infill coordinates.
* **CCMC Commercial Property Tax & Signboard Ledger**:
  * [`ccmc_commercial_tax_ledger.csv`](file:///D:/farm%20ai/municipal_reports/ccmc_commercial_tax_ledger.csv) (201 records, ₹20.40 L revenue potential).
  * [`ccmc_commercial_tax_ledger.md`](file:///D:/farm%20ai/municipal_reports/ccmc_commercial_tax_ledger.md) — Property tax valuation for 27 high-rise commercial structures and advertising license fees across 201 hoardings.
* **Municipal Summary Metrics JSON**:
  * [`municipal_reporting_summary.json`](file:///D:/farm%20ai/municipal_reports/municipal_reporting_summary.json) — Machine-readable structured KPI ledger.

---

## 5. AWS Cloud Infrastructure as Code (IaC)

All configurations comply 100% with the **FarmwiseAI TCE AWS Access Guide**:
* **Target Region**: `ap-south-1` (Mumbai)
* **Team Resource Prefix**: `fai-tce-team24-*`
* **Pre-Existing IAM Role**: `arn:aws:iam::387039786704:role/FAI-TCE-LambdaExecutionRole`

| IaC Configuration | File Location | Scope & Target Resources |
|---|---|---|
| **AWS CloudFormation Stack** | [`aws_cloud_architecture/template.yaml`](file:///D:/farm%20ai/aws_cloud_architecture/template.yaml) | Parameterized CloudFormation template creating S3 bucket (`fai-tce-team24-urban-data-mumbai`), CloudFront CDN with OAC, DynamoDB tables (`fai-tce-team24-urban-assets`, `fai-tce-team24-work-orders`), HTTP API Gateway v2, Lambda, and CloudWatch alarms. |
| **Terraform Main Module** | [`aws_cloud_architecture/terraform/main.tf`](file:///D:/farm%20ai/aws_cloud_architecture/terraform/main.tf) | Production Terraform module ready for `terraform apply`. |
| **Terraform Variables** | [`aws_cloud_architecture/terraform/variables.tf`](file:///D:/farm%20ai/aws_cloud_architecture/terraform/variables.tf) | Parameters for region, team prefix, memory, and environment. |
| **Terraform Outputs** | [`aws_cloud_architecture/terraform/outputs.tf`](file:///D:/farm%20ai/aws_cloud_architecture/terraform/outputs.tf) | Exported endpoints, ARNs, and bucket identifiers. |
| **Serverless Lambda Handler** | [`aws_cloud_architecture/lambda/lambda_function.py`](file:///D:/farm%20ai/aws_cloud_architecture/lambda/lambda_function.py) | Python 3.12 handler implementing `/health`, `POST /api/v1/detect`, `POST /api/v1/query`, `GET /api/v1/work-orders`, and CORS preflight. |
| **Lambda Requirements** | [`aws_cloud_architecture/lambda/requirements.txt`](file:///D:/farm%20ai/aws_cloud_architecture/lambda/requirements.txt) | Runtime dependencies: `boto3`, `onnxruntime`, `numpy`, `pydantic`. |
| **Local Test Harness** | [`aws_cloud_architecture/test_lambda_local.py`](file:///D:/farm%20ai/aws_cloud_architecture/test_lambda_local.py) | Unit test suite; **all 6 test cases passed in 0.001s**. |
| **Architecture Specification** | [`aws_cloud_architecture/architecture_specification.md`](file:///D:/farm%20ai/aws_cloud_architecture/architecture_specification.md) | Comprehensive document with Mermaid topology, latency budget (104 ms P95), and economic feasibility ($12.40/mo pilot, $395/mo city-scale). |

---

## 6. Core Master Datasets & GIS Registries

All master datasets are structured in standard CSV and GeoJSON in [`D:/farm ai/`](file:///D:/farm%20ai/):

* **GIS Digital Twin Layers**:
  * [`urban_assets_digital_twin.geojson`](file:///D:/farm%20ai/urban_assets_digital_twin.geojson) — 465 point features with digital passports and reference status.
  * [`road_network_topology.geojson`](file:///D:/farm%20ai/road_network_topology.geojson) — 10 surveyed road centerlines with stationing and asset densities.
  * `D:\Study_area.geojson` — Official Corporation boundary polygon for Coimbatore Ward 29 North Zone.
* **Tabular Master Ledgers**:
  * [`master_images.csv`](file:///D:/farm%20ai/master_images.csv) — 108 standardized survey images across 10 corridors.
  * [`master_streets.csv`](file:///D:/farm%20ai/master_streets.csv) — 10 surveyed corridor profiles with lengths and road classes.
  * [`master_metadata.csv`](file:///D:/farm%20ai/master_metadata.csv) — 108 metadata rows with 29 attributes per frame.
  * [`detections.csv`](file:///D:/farm%20ai/detections.csv) — 465 fixed infrastructure detections.
  * [`building_intelligence.csv`](file:///D:/farm%20ai/building_intelligence.csv) — 108 buildings with 10 property parameters and Google Maps pins.
  * [`ocr_intelligence.csv`](file:///D:/farm%20ai/ocr_intelligence.csv) — 201 commercial signboards across 11 economic categories.
  * [`ocr_search_index.json`](file:///D:/farm%20ai/ocr_search_index.json) — Inverted keyword index over 220 tokens.
  * [`spatial_relationships.csv`](file:///D:/farm%20ai/spatial_relationships.csv) — Perpendicular road setbacks and nearest-neighbor vectors.
  * [`corridor_intelligence_scorecard.csv`](file:///D:/farm%20ai/corridor_intelligence_scorecard.csv) — Archetype diagnostics, CBI, SLAS, and municipal grades.
  * [`routing_decisions.csv`](file:///D:/farm%20ai/vlm_routing_engine/routing_decisions.csv) — 774 two-tier routing decisions with latency, cost, and VLM rationales.

---

## 7. Presentation & Demo Materials

* **Interactive Slide Deck**: [`HACKATHON_PRESENTATION.html`](file:///D:/farm%20ai/HACKATHON_PRESENTATION.html)
* **Markdown Slide Deck**: [`HACKATHON_PRESENTATION.md`](file:///D:/farm%20ai/HACKATHON_PRESENTATION.md)
* **Timed Video Walkthrough Script**: [`DEMO_VIDEO_WALKTHROUGH_SCRIPT.md`](file:///D:/farm%20ai/DEMO_VIDEO_WALKTHROUGH_SCRIPT.md) (Time-coded 3-minute & 5-minute guides).

---

## 8. Verification & Instructions for Judges

To launch and evaluate the entire platform:
1. **Open the Master Flagship Digital Twin**:
   * Double-click [`D:/farm ai/urban_digital_twin_portal.html`](file:///D:/farm%20ai/urban_digital_twin_portal.html) in any web browser.
   * Seamlessly switch across all **11 workspace tabs**:
     - *Tri-View Studio*: Explore corridor ST01, toggle blueprints, view dynamic spiderlines.
     - *Spatial Map*: Click on the road network to use the interactive measurement tool.
     - *AI Copilot*: Click the quick-query pills to test zero-hallucination spatial answers.
     - *Civic Work Orders*: Filter TANGEDCO orders by `P1-Critical` or review CCMC streetlight infill directives.
     - *AWS Cloud & Edge*: Test the serverless API testbench (`GET /health`, `POST /api/v1/detect`).
     - *VLM Router*: Simulate routing for low-confidence Tamil signs or tall commercial buildings.
     - *Export Hub*: Download any GIS GeoJSON layer or CSV ledger with a single click.
2. **Review the Interactive Presentation Deck**:
   * Double-click [`D:/farm ai/HACKATHON_PRESENTATION.html`](file:///D:/farm%20ai/HACKATHON_PRESENTATION.html). Use the left/right arrow keys or press `F` for full-screen mode.
3. **Execute Local Verification Scripts (Optional)**:
   * Test the serverless Lambda handler: `python "D:\farm ai\aws_cloud_architecture\test_lambda_local.py"` (all 6 tests pass in 0.001s).
   * Benchmark the 10.12 MB ONNX model: `python "D:\farm ai\aws_cloud_architecture\edge_pipeline\export_onnx_edge.py"`.
   * Run the two-tier routing benchmark: `python "D:\farm ai\vlm_routing_engine\run_phase16_benchmark.py"`.
