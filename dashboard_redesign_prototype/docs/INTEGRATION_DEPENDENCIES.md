# FarmwiseAI Project 2 — Integration Dependencies & Demo Elements Ledger

**Document Scope:** Production Readiness & Upstream Data Dependencies  
**Project Root:** `D:\farm ai`  
**Target Domain:** Coimbatore City Municipal Corporation (Ward 29 Digital Twin)  

---

## 1. Data Fidelity Ledger (Real Data vs Demonstration Placeholders)

In strict accordance with the project directives, all features are categorized by their underlying data provenance:

| Module / Feature | Real Project Data Source | Demonstration / Simulated Element | Production Integration Dependency |
| :--- | :--- | :--- | :--- |
| **Executive Overview** | 465 fixed assets, 2.49 km network, 108 images, Ward 29 boundary polygon | None (100% computed from real records) | Ready for deployment |
| **City Explorer GIS** | Real WGS84 GeoJSON coordinates (`urban_assets_digital_twin.geojson`) | None (CartoDB Positron basemap tiles) | Ready for deployment |
| **Asset Detection Studio**| 108 high-resolution corridor images | Bounding boxes were mathematically generated in Phase 4; labeled as "Awaiting Verification" | Requires human-annotated bounding boxes before autonomous inference integration |
| **Buildings & Property** | 108 building envelopes, trade names, facade types, Google Maps links | Fixed $3.5\text{ m}/\text{floor}$ height formula; simulated cadastre match (OSM) | Mobile LiDAR / stereo photogrammetry for exact 3D building heights; official CCMC TSFR cadastre deeds |
| **Utilities & Lighting** | 108 utility poles, 108 streetlights, 24 transformers, TANGEDCO work orders | Photometric spacing math (IRC:SP:72) | Nighttime photometer survey for real-time luminaire lux measurements |
| **Road & Traffic** | 10 surveyed road corridors profiles, widths, surface classes, 9 signals | Vehicles excluded by design; roadside trees unannotated | Add `roadside_tree` class to YOLO taxonomy for canopy hazard monitoring |
| **Signage & OCR Studio**| 201 commercial signboards extracted via EasyOCR, 220 indexed keywords | Fallback synthetic fascia injection when EasyOCR confidence $< 0.25$ | Bilingual Tamil + English OCR model integration |
| **Master Inventory** | 465 digital asset passports with 32 technical parameters | None (functional CSV & GeoJSON export) | Ready for deployment |
| **Quality Review Queue**| 8 genuine flagged items (data quality alerts, formula bboxes, P1 hazards) | Local browser storage for reviewer notes (`localStorage`) | Centralized PostgreSQL / DynamoDB persistence (`fai-tce-team24-work-orders`) |
| **Model Health** | Verified SHA-256 hashes, 5-epoch training logs, raw 0.0034 precision report | None (100% audited evidence) | Awaiting human annotation campaign to retrain model |

---

## 2. Upstream Production Integration Dependencies

Before promoting the isolated prototype into the master platform:
1. **User Authorization Gate:** Explicit approval from the user is mandatory before touching [`urban_digital_twin_portal.html`](file:///D:/farm%20ai/🌟%20MASTER%20UNIFIED%20PLATFORM/urban_digital_twin_portal.html) or production databases.
2. **Annotation Ground-Truth Campaign:** Utilize the interactive annotation studio ([`urban_annotation_studio.html`](file:///D:/farm%20ai/🌐%20INDIVIDUAL%20STANDALONE%20STUDIOS/urban_annotation_studio.html)) to replace synthetic formula bounding boxes with authentic hand-drawn boxes on the 108 images.
3. **AWS Serverless Connection:** In `lambda_function.py`, replace simulated JSON detections in `POST /api/v1/detect` with live ONNX Runtime inference using `best.onnx` (`10.12 MB`, benchmarked at 42.01 ms).
