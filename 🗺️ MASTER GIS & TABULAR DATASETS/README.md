# 🗺️ Master GIS & Tabular Datasets
### FarmwiseAI Product Challenge 2026 — Team 24 (Coimbatore Ward 29)

This folder contains the complete, authoritative spatial and tabular datasets covering the 10 surveyed corridors (2.49 km total road network) in Coimbatore City Municipal Corporation (CCMC) Ward 29.

---

## 📊 Datasets Catalog

| Filename | Format | Records / Features | Key Attributes |
| :--- | :--- | :--- | :--- |
| **`urban_assets_digital_twin.geojson`** | GeoJSON (EPSG:4326) | 465 Point Features | Asset UUID, Class (9 categories), GPS Coordinates, Condition Grade, Height, Setback, Maintenance Urgency |
| **`road_network_topology.geojson`** | GeoJSON (EPSG:4326) | 10 LineStrings | Corridor ID, Street Name, Chainage Stationing (km), Road Width, Surface Quality, Lighting Status |
| **`master_images.csv`** | CSV | 108 Rows | Frame UUID, Corridor ID, Original Filename, Standardized Filename, Dimensions (1280x720) |
| **`master_streets.csv`** | CSV | 10 Rows | Street Code (ST01-ST10), Official CCMC Name, Length (m), Asset Count, Building Count |
| **`master_metadata.csv`** | CSV | 108 Rows | 29 Telemetry Attributes: Timestamp, GPS Lat/Lng, Compass Heading, Lighting Lux, Weather, Road Classification |
| **`detections.csv`** | CSV | 465 Rows | Fixed Infrastructure Detections: Bounding Box (XYWH norm), Class, Confidence Score (0.0-1.0) |
| **`building_intelligence.csv`** | CSV | 108 Rows | 10 Building Parameters: Height, Floors, Footprint Area, Perpendicular Setback, Cadastre Match ID, Building Use |
| **`ocr_intelligence.csv`** | CSV | 201 Rows | Commercial Signboards: Tamil/English Raw Text, 220 Extracted Keywords, 11 Trade Sectors, Tax Valuation Band |
| **`spatial_relationships.csv`** | CSV | 465 Rows | Road Centerline Offset (m), Nearest Neighbor Asset UUID, Distance to Road Edge, Left/Right Side of Street |
| **`corridor_intelligence_scorecard.csv`** | CSV | 10 Rows | Corridor Archetypes, Corridor Burden Index (CBI: 0-100), Street Lighting Adequacy (SLAS: 0-100), Municipal Grade (A-D) |

---
*All geographic coordinates use WGS84 (EPSG:4326). All linear distances are in meters.*
