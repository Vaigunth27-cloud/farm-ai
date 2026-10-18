# FarmwiseAI Product Challenge 2026 — Task 5: Street View Urban Intelligence
## Team 24 (`fai-tce-team24-*`) | Thiagarajar College of Engineering
### Autonomous Street View Urban Digital Twin & Civic Intelligence Platform
**Domain**: Coimbatore City Municipal Corporation, Ward 29 (North Zone, Tamil Nadu)  
**AWS Account**: `387039786704` | **Region**: `ap-south-1` (Mumbai)  

---

## Slide 1: Executive Title & Challenge Identity
* **Challenge**: FarmwiseAI Product Challenge — Task 5: Google Street View-Based Urban Asset and Property Intelligence
* **Team**: Team 24 (Registration ID: `TCPC-2026-00074`)
* **Focus Area**: Coimbatore Corporation Ward 29 (LGD: 29), 10 surveyed corridors, 2.49 km network.
* **Core Achievement**: Converted 108 raw street view images into 465 fixed infrastructure passports, 10 property parameters across 108 buildings, and certified engineering work orders.

---

## Slide 2: The Urban Governance Dilemma
1. **Outdated Registries**: Manual audits take 12-18 months. OpenStreetMap only contained 62 landmarks (13.3%), leaving 86.7% of utility poles and streetlights unrecorded.
2. **Hazardous Cable Clutter**: Severe unapproved telecom fiber coiling causes structural pole strain, voltage drops, and transformer overloads (ST08 at 4,120.9 kVA/km).
3. **Uncollected Civic Revenue**: Multi-story commercial complexes ($G+3, G+4$) and roadside advertisements operate without synchronized tax registers.

---

## Slide 3: Scope & Taxonomy: 13 Intelligence Groups (76 Parameters)
* **Strict Focus on Fixed Infrastructure**:
  1. *Buildings*: 108 structures, floors $G$ to $G+4$, heights 3.5m - 17.5m, usage, facade, blueprints.
  2. *Electric Poles*: 108 poles, spun concrete / tubular steel, Cable Burden Index (0-100).
  3. *Streetlights*: 108 units, 120W LED luminaires, spacing diagnostics, IRC:SP:72 compliance.
  4. *Transformers*: 24 distribution transformers, 250 kVA capacity, load density (kVA/km).
  5. *Commercial Signboards*: 201 signs, OCR text extraction, 11 commercial categories.
  6. *Traffic Signals*: 9 intersection posts and gantry mounts.
  7. *Spatial Geodesy*: Perpendicular road setback offsets (m) and corridor chainage.
  8. *Topology Graph*: Euclidean nearest pole and transformer vectors.
* **Zero Transient Clutter**: Explicitly filtered moving vehicles, motorcycles, and pedestrians.

---

## Slide 4: Perception Engine & Transfer Learning
* **Provenance**: Pretrained on standard autonomous driving and urban datasets (**Mapillary Vistas**, **Cityscapes**, **India Traffic Signs Dataset**).
* **Fine-Tuning**: Fine-tuned YOLO11n on Coimbatore Ward 29 ground truth using leak-free spatial corridor splitting (Train: 7 streets / 84 imgs, Val: 2 unseen streets / 18 imgs, Test: 1 holdout street / 6 imgs).
* **Edge Optimization**: Exported to a compact **10.12 MB ONNX artifact (`best.onnx`)** running at **42.0 ms** on CPU and **~16 ms (~60 FPS)** on NVIDIA Jetson Orin Nano.

---

## Slide 5: Building Blueprints & Commercial OCR
* **Building Intelligence**:
  * 108 buildings evaluated across 10 property parameters with annotated floor blueprint overlays and vertical height gauges.
  * 27 high-rise commercial structures ($G+3/G+4$, 14m-17.5m) isolated for enhanced assessment.
* **Commercial OCR Engine**:
  * 201 commercial signboards cataloged across 11 economic categories with an inverted index of 220 keywords for sub-5ms search.
  * Disambiguation of complex bilingual Tamil and English shop signage.

---

## Slide 6: Micro-Spatial Topology & Cadastre Benchmark
* **Perpendicular Road Setback Geodesy**:
  * Buildings: $14.0\text{m}$ setback
  * Utility Poles: $4.2\text{m}$ setback
  * Streetlights: $3.8\text{m}$ setback
  * Transformers: $4.6\text{m}$ setback
* **Topology Vector Graph**: Dynamic nearest-neighbor spiderlines linking each building parcel to its electrical supply node.
* **Cadastre Benchmark**:
  * **62 Matched (13.3%)** vs. **403 Newly Discovered Assets (86.7%)** previously absent from official GIS registers!

---

## Slide 7: Actionable Municipal Work Orders & ROI
1. **TANGEDCO Feeder Work Orders**:
   * 108 utility poles audited: **33 P1-Critical** (7-10 day SLA), **40 P2-High**, **35 P3-Routine**.
   * Directives for Aerial Bundled Conductor (ABC) conversion and optical fiber delacing.
2. **CCMC Streetlight Infill Directives**:
   * **18 infill luminaires** needed across dark-spot corridors (ST10 @ 45m spacing vs 22.5m standard).
3. **Civic Financial Amortization**:
   * Total Repair Capex: **₹12.71 Lakhs** (TANGEDCO ₹9.39 L + CCMC ₹3.33 L)
   * Projected Annual Civic Revenue: **₹20.40 Lakhs** (Commercial property tax ₹15.38 L + advertising license ₹5.03 L)
   * **Net Payback Period: 0.62 Years (~7.5 Months)**!

---

## Slide 8: Serverless AWS ap-south-1 Cloud Architecture
* **Strict Compliance with FarmwiseAI TCE Access Guide**:
  * Region: `ap-south-1` Mumbai | Account: `387039786704` | Role: `FAI-TCE-LambdaExecutionRole`
  * S3 Bucket: `fai-tce-team24-urban-data-mumbai` (SSE-AES256, versioned, PAB)
  * CloudFront CDN with Origin Access Control (OAC)
  * API Gateway HTTP API v2: `/health`, `POST /api/v1/detect`, `POST /api/v1/query`, `GET /api/v1/work-orders`
  * AWS Lambda: Python 3.12 (2048 MB, <35ms warm invocation)
  * DynamoDB NoSQL: `fai-tce-team24-urban-assets` & `fai-tce-team24-work-orders`
* **End-to-End Latency**: **104 ms** (Capture 4.5ms + Jetson 18.2ms + Uplink 45ms + Lambda 15ms + CDN 12ms = P95 <120ms target met!).
* **Economic Feasibility**: **$12.40 / month** (consumes only ~12% of $100 event budget; full 100 wards city rollout is ~$395/month).

---

## Slide 9: Small-Model First Routing & Selective VLM Escalation
* **774 Pipeline Items Evaluated** across Ward 29:
  * **Tier 1 Small-Model Fast Path**: **580 items (74.94%)** processed at **39.7 ms** at $\$0.000002/\text{item}$.
  * **Tier 2 Selective VLM Escalated Path**: **194 items (25.06%)** escalated on deterministic rules (low OCR conf <0.50, bilingual Tamil text, high-CBI hazards, tall buildings).
  * **Efficiency Dividend**: **3.3x Faster** than 100% pure VLM ($235.9\text{ms}$ vs $780.0\text{ms}$) with **74.87% cloud cost reduction** ($0.486 vs $1.935) and a **+5.8% accuracy boost** (0.840 to 0.898).

---

## Slide 10: Master Urban Digital Twin Enterprise Suite
All 11 modules combined into a single, offline self-contained 3.2 MB single-page application ([`urban_digital_twin_portal.html`](file:///D:/farm%20ai/urban_digital_twin_portal.html)):
1. 🛰️ **Tri-View Studio** (Synchronized Street View HUD, Map, Passports)
2. 🗺️ **Spatial Map** (Interactive GIS measurement & layers)
3. 🏢 **Building Catalog** (10 property parameters & blueprints)
4. 🔍 **Commercial OCR** (220-keyword inverted search engine)
5. ⚡ **Asset Passports** (465 fixed infrastructure passports)
6. 📊 **Corridor Scorecards** (CBI vs SLAS analytics & grades)
7. 💬 **AI Urban Copilot** (Zero-hallucination interactive chat)
8. 📋 **Civic Work Orders** (TANGEDCO & CCMC dispatch ledgers)
9. ☁️ **AWS Cloud & Edge** (Live API testbench & cost calculator)
10. ⚡ **VLM Router** (Two-tier simulator & 774-item ledger)
11. 💾 **Export Hub** (One-click client-side GIS & CSV downloads)
