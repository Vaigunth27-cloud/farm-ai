"""
PostGIS Ingestion Script for AWS RDS PostgreSQL
Populates PostgreSQL tables from CCMC Ward 29 GeoJSON & CSV datasets
FarmwiseAI Product Challenge 2026 — Team 22 / 24
"""

import os
import sys
import json
import csv
import argparse

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASETS_DIR = os.path.join(ROOT, "🗺️ MASTER GIS & TABULAR DATASETS")
MUNI_DIR = os.path.join(ROOT, "📋 MUNICIPAL REPORTS & WORK ORDERS")

def generate_insert_statements():
    """Generates pure SQL INSERT statements ready to execute in PostGIS."""
    sql_statements = []

    # 1. Road Network
    road_geojson = os.path.join(DATASETS_DIR, "road_network_topology.geojson")
    if os.path.exists(road_geojson):
        with open(road_geojson, "r", encoding="utf-8") as f:
            data = json.load(f)
        for feat in data.get("features", []):
            props = feat.get("properties", {})
            coords = feat.get("geometry", {}).get("coordinates", [])
            coord_str = ", ".join([f"{c[0]} {c[1]}" for c in coords])
            wkt = f"LINESTRING({coord_str})"
            sql = f"""INSERT INTO road_network (street_id, street_name, length_m, road_width_m, surface_type, geom)
VALUES ('{props.get("street_id")}', '{props.get("street_name", "").replace("'", "''")}', {props.get("length_m", 0)}, {props.get("road_width_m", 7.0)}, '{props.get("surface_type", "Bitumen")}', ST_GeomFromText('{wkt}', 4326))
ON CONFLICT (street_id) DO NOTHING;"""
            sql_statements.append(sql)

    # 2. Urban Assets
    assets_geojson = os.path.join(DATASETS_DIR, "urban_assets_digital_twin.geojson")
    if os.path.exists(assets_geojson):
        with open(assets_geojson, "r", encoding="utf-8") as f:
            data = json.load(f)
        for feat in data.get("features", []):
            props = feat.get("properties", {})
            coords = feat.get("geometry", {}).get("coordinates", [0, 0])
            wkt = f"POINT({coords[0]} {coords[1]})"
            sql = f"""INSERT INTO urban_assets (asset_id, legacy_id, asset_class, asset_subtype, physical_condition, maintenance_priority, managing_authority, latitude, longitude, road_offset_m, road_side, geom)
VALUES ('{props.get("Asset_ID")}', '{props.get("Legacy_Asset_ID", "")}', '{props.get("Asset_Class")}', '{props.get("Asset_Subtype", "").replace("'", "''")}', '{props.get("Physical_Condition", "")}', '{props.get("Maintenance_Priority", "")}', '{props.get("Managing_Authority", "").replace("'", "''")}', {coords[1]}, {coords[0]}, {props.get("road_offset_m", 0)}, '{props.get("road_side", "")}', ST_GeomFromText('{wkt}', 4326))
ON CONFLICT (asset_id) DO NOTHING;"""
            sql_statements.append(sql)

    output_sql = os.path.join(os.path.dirname(os.path.abspath(__file__)), "postgis_seed_data.sql")
    with open(output_sql, "w", encoding="utf-8") as f:
        f.write("\n".join(sql_statements))
    print(f"Generated {len(sql_statements)} PostGIS INSERT queries in {output_sql}!")

if __name__ == "__main__":
    generate_insert_statements()
