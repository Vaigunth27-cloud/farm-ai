# FarmwiseAI — Street View Urban Intelligence Platform
## API & Data Reference Manual

---

## 1. REST API Specification

The FarmwiseAI backend service is implemented in `dashboard_redesign_prototype/backend/urban_agent_server.py` using **FastAPI**. It exposes synchronous and asynchronous REST endpoints over HTTP/1.1.

### Base URL:
`http://127.0.0.1:8000`

---

### Endpoint 1: System Health & Hardware Diagnostics

#### `GET /health`
Returns the operational health, hardware acceleration status, and AI model liveness.

- **Method**: `GET`
- **Headers**: None required.
- **Request Parameters**: None.

#### Example Response: `HTTP 200 OK`
```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_path": "D:\\farm ai\\yolo11s.pt",
  "ocr_available": true,
  "device": "cpu",
  "timestamp": "2026-10-19T10:30:00Z"
}
```

#### Error Responses:
- `HTTP 500 Internal Server Error`: If AI model weights cannot be loaded or memory initialization fails.

---

### Endpoint 2: Street Intelligence Image Analysis

#### `POST /api/analyze-street`
Accepts a street-level image payload (either binary multipart file or base64 data URL) and executes object detection, EXIF GPS extraction, optional OCR text transcription, and asset passport generation.

- **Method**: `POST`
- **Content-Type**: `multipart/form-data` or `application/x-www-form-urlencoded`

#### Request Parameters:

| Field Name | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `file` | Binary File | Optional* | Image file (`.png`, `.jpg`, `.jpeg`, `.webp`). Maximum size: 25 MB. |
| `image_data` | String | Optional* | Base64-encoded Data URL string (e.g., `data:image/png;base64,...`) from HTML5 Canvas. |
| `street_code` | String | No | Target corridor ID (`ST01` through `ST10`). Default: `"ST01"`. |
| `latitude` | Float | No | Explicit latitude coordinate if camera EXIF data is missing. |
| `longitude` | Float | No | Explicit longitude coordinate if camera EXIF data is missing. |

*\*Note: Either `file` or `image_data` must be provided.*

#### Example `curl` Request:
```bash
curl -X POST "http://127.0.0.1:8000/api/analyze-street" \
  -F "file=@D:/farm ai/dashboard_redesign_prototype/assets/raw_frames/IMG-ST01-001.png" \
  -F "street_code=ST01"
```

#### Example Response: `HTTP 200 OK`
```json
{
  "success": true,
  "street_code": "ST01",
  "street_name": "Gopalasamy Kovil Street",
  "coordinates": [11.028421, 76.974152],
  "exif_gps_found": true,
  "summary": {
    "total_detections": 12,
    "buildings": 3,
    "electric_poles": 4,
    "streetlights": 3,
    "commercial_signs": 2,
    "transformers": 0,
    "compliance_rating": "B+"
  },
  "detections": [
    {
      "id": "DET-ST01-001",
      "class_id": 1,
      "class_name": "electric_pole",
      "confidence": 0.884,
      "bbox": [92, 114, 156, 842],
      "normalized_bbox": [0.071, 0.105, 0.121, 0.779],
      "passport_id": "AST-ST01-POLE-001",
      "estimated_gps": [11.028435, 76.974148],
      "condition": "Good",
      "ocr_text": null
    },
    {
      "id": "DET-ST01-002",
      "class_id": 3,
      "class_name": "commercial_sign",
      "confidence": 0.912,
      "bbox": [410, 320, 680, 410],
      "normalized_bbox": [0.320, 0.296, 0.531, 0.379],
      "passport_id": "AST-ST01-SIGN-001",
      "estimated_gps": [11.028450, 76.974160],
      "condition": "Commercial Active",
      "ocr_text": "Sri Krishna Medicals - Pharmacy & Surgical"
    }
  ],
  "timestamp": "2026-10-19T10:30:15Z"
}
```

#### Error Responses:
- `HTTP 400 Bad Request`: If neither `file` nor `image_data` is supplied, or payload format is invalid.
  ```json
  {"success": false, "error": "No image payload provided in request"}
  ```
- `HTTP 500 Internal Server Error`: If image decompression or YOLO forward pass fails.
  ```json
  {"success": false, "error": "Inference execution error: CUDA out of memory"}
  ```

---

### Endpoint 3: Urban AI Agent Contextual Assistant

#### `POST /api/chat`
Answers natural language municipal, engineering, and compliance questions using knowledge lookup over master GIS tables.

- **Method**: `POST`
- **Content-Type**: `application/json`

#### Request Payload Model (`ChatRequest`):
```json
{
  "query": "Which streets in Ward 29 have missing streetlights or dark spots?",
  "street_context": "ST06"
}
```

#### Example Response: `HTTP 200 OK` (`ChatResponse`):
```json
{
  "answer": "Based on the CCMC Streetlight Infill Directives, Corridor ST06 (Sanganur Canal Road) has 5 unlit poles and 2 dark spot spans exceeding 45 meters between pole AST-ST06-POLE-004 and AST-ST06-POLE-005. A total infill of 4 LED luminaires (70W) is mandated under Work Order DIR-CCMC-SL-2026-06.",
  "corridor_code": "ST06",
  "confidence": 0.94,
  "sources": [
    "ccmc_streetlight_infill_directives.csv",
    "corridor_intelligence_scorecard.csv"
  ]
}
```

---

## 2. Core Data Models & Schemas

### 2.1 Road Network Topology (`road_network_topology.geojson`)
Defines the spatial centerlines, road widths, and survey metadata for the 10 corridors in Ward 29.

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "CORR-ST01",
      "properties": {
        "corridor_code": "ST01",
        "name": "Gopalasamy Kovil Street",
        "ward": 29,
        "zone": "North",
        "city": "Coimbatore",
        "road_type": "Mixed Commercial / Access",
        "surface": "Bituminous Asphalt",
        "carriageway_width_m": 7.5,
        "length_m": 385.0,
        "baseline_pole_count": 14,
        "baseline_streetlight_count": 11,
        "compliance_rating": "B+"
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [76.974100, 11.028400],
          [76.974350, 11.028750],
          [76.974600, 11.029100]
        ]
      }
    }
  ]
}
```

---

### 2.2 Urban Asset Digital Twin (`urban_assets_digital_twin.geojson`)
Spatial point layer representing verified physical infrastructure assets.

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "AST-ST01-POLE-004",
      "properties": {
        "uid": "AST-ST01-POLE-004",
        "asset_class": "electric_pole",
        "street_code": "ST01",
        "street_name": "Gopalasamy Kovil Street",
        "height_m": 8.5,
        "material": "Pre-stressed Concrete (PSCC)",
        "has_streetlight": true,
        "streetlight_condition": "Functional",
        "structural_status": "Hazardous Leaning (Angle 12 deg)",
        "photo_evidence": "dashboard_redesign_prototype/assets/raw_frames/IMG-ST01-004.png",
        "bbox": [140, 95, 210, 810],
        "verified": true,
        "jurisdiction": "TANGEDCO Ganapathy Feeder Section"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [76.974352, 11.028758]
      }
    }
  ]
}
```

---

### 2.3 Municipal Directives & Ledgers

#### A. CCMC Commercial Property Tax Ledger (`ccmc_commercial_tax_ledger.csv`)
Columns and data types:

| Column Name | Data Type | Description |
| :--- | :---: | :--- |
| `assessment_id` | String | Municipal commercial assessment reference (e.g., `CCMC-TAX-W29-014`). |
| `corridor_code` | String | Street identifier (`ST01` – `ST10`). |
| `establishment_name` | String | Transcribed business name from EasyOCR extraction. |
| `door_no` | String | Extracted or spatial parcel door address. |
| `signage_area_sqft`| Float | Calculated hoarding/signage area in square feet. |
| `declared_floors` | Integer | Municipal records declared floor count. |
| `detected_floors` | Integer | AI building facade detected floor count. |
| `tax_deficiency_status` | String | `Tax Compliant`, `Unassessed Floor Addition`, `Illegal Hoarding`. |
| `annual_penalty_inr` | Float | Calculated municipal penalty assessment in Indian Rupees. |

#### B. TANGEDCO Feeder Work Orders (`tangedco_feeder_work_orders.csv`)
Columns and data types:

| Column Name | Data Type | Description |
| :--- | :---: | :--- |
| `work_order_id` | String | TANGEDCO maintenance order ID (e.g., `WO-TANG-2026-081`). |
| `corridor_code` | String | Corridor identifier (`ST01` – `ST10`). |
| `asset_uid` | String | Target asset unique identifier (`AST-ST06-POLE-008`). |
| `issue_category` | String | `Leaning Pole`, `Tree Canopy Encroachment`, `Transformer Oil Leakage`. |
| `severity` | String | `CRITICAL`, `HIGH`, `MEDIUM`. |
| `latitude` / `longitude` | Float | GPS coordinates for field repair crew dispatch. |
| `photo_ref` | String | Path to verifiable visual proof frame. |
| `action_required`| String | Specific directive (e.g., *"Re-straighten pole and trim branches"*). |

---

## 3. Storage Architecture & Relative File Layout

```
D:\farm ai\
├── 🗺️ MASTER GIS & TABULAR DATASETS/
│   ├── building_intelligence.csv       # Cadastral parcel tax & floor metrics
│   ├── detections.csv                  # Raw detection log entries
│   ├── master_images.csv               # 108 image registry with timestamps & GPS
│   ├── road_network_topology.geojson   # 10 corridor vector centerlines
│   └── urban_assets_digital_twin.geojson# Complete spatial asset passports
├── 📋 MUNICIPAL REPORTS & WORK ORDERS/
│   ├── ccmc_commercial_tax_ledger.csv  # Property tax assessment ledger
│   ├── ccmc_streetlight_infill_directives.csv # Dark spot remediation mandates
│   └── tangedco_feeder_work_orders.csv # Electrical maintenance work orders
└── dashboard_redesign_prototype/assets/raw_frames/ # Local 108 frame image store
```
