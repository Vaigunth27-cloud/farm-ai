# FarmwiseAI Product Challenge 2026 — Task 5: Street View Urban Intelligence
## Team 24 (`fai-tce-team24-*`) | Video Walkthrough Demonstration Script
**Application Target**: `urban_digital_twin_portal.html` (Master Flagship Digital Twin Platform)  
**Target Audience**: FarmwiseAI & Thiagarajar College of Engineering Hackathon Evaluation Panel  

---

# Part 1: Fast-Paced 3-Minute Executive Pitch Script

### [00:00 - 00:30] Introduction & Problem Statement
* **Screen Target**: Slide 1 of `HACKATHON_PRESENTATION.html` $\rightarrow$ Transition to `urban_digital_twin_portal.html`.
* **Presenter Voiceover**:
  > *"Respected judges and organizers of the FarmwiseAI Product Challenge. Welcome to Team 24's demonstration of our Autonomous Street View Urban Digital Twin Platform for Coimbatore Corporation Ward 29. Traditional municipal asset management is broken: manual surveys take months, while illegal overhead cable clutter and missing streetlights pose daily civic hazards. Across 10 surveyed corridors and 2.49 kilometers of road network, we transformed 108 raw street view images into 465 fixed infrastructure digital passports, 10 building property parameters, and certified engineering work orders."*

### [00:30 - 01:15] Tri-View Studio & Micro-Spatial Digital Twin
* **Screen Target**: Tab 1 (Tri-View Studio) $\rightarrow$ select corridor `ST01`, toggle floor blueprints, click "Next Transect".
* **Presenter Voiceover**:
  > *"Here is our flagship Tri-View Studio. On the left, our Street View HUD automatically extracts building floor blueprints, estimated heights, and commercial signboards. Notice the 3-way synchronization: as I advance along Sathy Road, the Leaflet map in the center tracks our survey position, dynamically rendering Euclidean spiderlines to the nearest utility pole and transformer. On the right, the digital passport updates in real time with mounting specifications, physical condition, and managing civic authority."*

### [00:15 - 01:50] AI Urban Copilot & Zero-Hallucination Query Engine
* **Screen Target**: Tab 7 (AI Copilot) $\rightarrow$ click prompt *"⚡ Highest Electrical Load"*, then *"🚨 Poles Requiring Decluttering"*.
* **Presenter Voiceover**:
  > *"Unlike generic chatbots that hallucinate non-existent addresses, our AI Urban Copilot connects deterministically to verified Ward 29 spatial registries. Clicking 'Highest Electrical Load' instantly identifies Corridor ST08 Raja Street with a staggering 4,120.9 kVA per kilometer electrical density across 6 transformers. Clicking 'Poles Requiring Decluttering' isolates all 43 high-risk poles requiring immediate municipal intervention."*

### [01:50 - 02:25] Actionable Municipal Work Orders & Civic ROI
* **Screen Target**: Tab 8 (Civic Work Orders) $\rightarrow$ filter TANGEDCO by `P1-Critical`, switch to Streetlight Infill, show Tax Ledger.
* **Presenter Voiceover**:
  > *"We don't just detect objects; we generate certified engineering work orders. Under Civic Work Orders, TANGEDCO engineers receive 33 P1-Critical dispatch orders for Aerial Bundled Conductor (ABC) conversion. The CCMC Streetlighting Division receives directives for 18 infill luminaires to fix dark spots on Avarampalayam Road where spacing exceeds 45 meters. Best of all, our commercial tax ledger identifies ₹20.40 Lakhs in annual revenue potential, fully amortizing the entire ₹12.71 Lakhs repair capex in just 0.62 years—roughly 7.5 months!"*

### [02:25 - 03:00] AWS Serverless Architecture, VLM Routing & Conclusion
* **Screen Target**: Tab 9 (AWS Cloud & Edge) $\rightarrow$ send a live test request $\rightarrow$ switch to Tab 10 (VLM Router) $\rightarrow$ Tab 11 (Export Hub).
* **Presenter Voiceover**:
  > *"Under the hood, our architecture strictly complies with FarmwiseAI rules: Core serverless services in ap-south-1 Mumbai using our assigned account 387039786704 and FAI-TCE-LambdaExecutionRole. Our 10.12 MB fine-tuned YOLO11n ONNX model runs at 42ms on CPU and ~16ms on Jetson hardware. By routing 74.9% of standard frames through Tier 1 fast path and selectively escalating only ambiguous edge cases to Tier 2 VLM, we cut cloud costs by 74.9% with an end-to-end P95 latency of just 104 milliseconds at only $12.40 a month. All GeoJSON and CSV layers are exportable in one click. Thank you!"*

---

# Part 2: Detailed 5-Minute Technical Deep-Dive Script

| Timestamp | Screen Target | Action to Perform | Key Technical Talking Points |
|---|---|---|---|
| **00:00 - 00:45** | `urban_digital_twin_portal.html` Header & KPI Telemetry | Point to header badges: 465 assets, 2.49 km, 86.7% AI Discoveries, Grade B+ 79.4, Capex Payback 0.62 Yrs. | Frame challenge scope, dataset integrity (10 corridors, Ward 29), zero transient clutter mandate (fixed infrastructure focus). |
| **00:45 - 01:30** | Tab 1: Tri-View Studio | Select `ST01` $\rightarrow$ `ST08`. Toggle "Floor Blueprints", "Height Gauges", "Spiderlines". Click filmstrip. | 3-way synchronization, normal setback offsets (buildings 14m, poles 4.2m), dynamic Euclidean vector calculation, physical condition inspection. |
| **01:30 - 02:15** | Tab 2: Spatial Map & Tab 3: Building Catalog | In Tab 2, toggle asset layers, click road measurement tool. In Tab 3, filter by `G+4` floors. | Interactive chainage measurement, cadastre benchmark (62 matched vs 403 unmapped AI discoveries), 10 property parameters across 108 buildings. |
| **02:15 - 02:55** | Tab 4: Commercial OCR & Tab 6: Scorecards | Search "Hotel" or "AutoZone" in OCR engine. Switch to Corridor Scorecards table. | 201 commercial signboards, 11 categories, inverted index of 220 keywords. Cable Burden Index (CBI) vs Street Lighting Adequacy (SLAS), municipal grading (5 A, 3 B, 2 C). |
| **02:55 - 03:40** | Tab 7: AI Copilot & Tab 8: Civic Work Orders | Run query *"What is the nearest transformer to Hotel Anandha Residency?"*. Switch to Work Orders. | Deterministic NLP query engine (0% hallucination), Euclidean spatial distance calculation (67.83m). TANGEDCO 33 P1 orders, CCMC 18 infill lights, ₹20.40 L revenue ledger. |
| **03:40 - 04:25** | Tab 9: AWS Cloud & Edge Platform | Click `/health` and `/api/v1/detect` in live API Testbench. Show real-time vehicle telemetry streamer. Move ward slider. | ap-south-1 Mumbai, HTTP API v2, Lambda Python 3.12 (2048 MB), S3 AES-256 + CloudFront OAC. 104ms P95 latency. $12.40/mo pilot cost (12% of $100 budget). |
| **04:25 - 05:00** | Tab 10: VLM Router & Tab 11: Export Hub | Run archetype simulation (`Low-Conf Tamil Sign`). Show 3-way trade-off. Download GeoJSON in Export Hub. | Two-tier routing: 74.9% Tier 1 Fast Path (39.7ms), 25.1% Tier 2 VLM Escalated. 3.3x faster, 74.9% cheaper, +5.8% accuracy boost. One-click open data client export. |

---

# Part 3: Live Demo Pre-Flight Checklist

- [x] Open `urban_digital_twin_portal.html` in Chrome/Edge/Firefox — verify all 11 tabs switch smoothly.
- [x] Verify Tri-View canvas renders street view and blueprint toggles without console errors.
- [x] Verify Leaflet map tiles render cleanly with dark-mode basemap.
- [x] Click all 6 quick-query pills in AI Copilot — confirm deterministic responses.
- [x] Test API testbench in AWS tab (`GET /health` returns 200 OK in ~11ms).
- [x] Run VLM routing simulator on sample items — confirm trace and badge updates.
- [x] Test GeoJSON and CSV download buttons in Export Hub.
