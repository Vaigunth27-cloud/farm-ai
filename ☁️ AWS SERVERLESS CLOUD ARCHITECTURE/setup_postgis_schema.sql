-- ==============================================================================
-- CCMC Ward 29 Urban Digital Twin — PostGIS Spatial Database Schema
-- Designed for AWS RDS PostgreSQL + PostGIS Extension
-- FarmwiseAI Product Challenge 2026 — Team 22 / 24
-- ==============================================================================

-- 1. Enable PostGIS Spatial Extensions
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;

-- 2. Road Network Table
CREATE TABLE IF NOT EXISTS road_network (
    id SERIAL PRIMARY KEY,
    street_id VARCHAR(16) UNIQUE NOT NULL,
    street_name VARCHAR(128) NOT NULL,
    length_m NUMERIC(10, 2),
    road_width_m NUMERIC(6, 2),
    surface_type VARCHAR(64),
    geom GEOMETRY(LineString, 4326) NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_road_network_geom ON road_network USING GIST(geom);

-- 3. Fixed Urban Assets Table
CREATE TABLE IF NOT EXISTS urban_assets (
    id SERIAL PRIMARY KEY,
    asset_id VARCHAR(32) UNIQUE NOT NULL,
    legacy_id VARCHAR(32),
    asset_class VARCHAR(64) NOT NULL,
    asset_subtype VARCHAR(128),
    physical_condition VARCHAR(64),
    maintenance_priority VARCHAR(32),
    managing_authority VARCHAR(128),
    latitude NUMERIC(10, 6) NOT NULL,
    longitude NUMERIC(10, 6) NOT NULL,
    road_offset_m NUMERIC(8, 2),
    road_side VARCHAR(32),
    geom GEOMETRY(Point, 4326) NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_urban_assets_geom ON urban_assets USING GIST(geom);
CREATE INDEX IF NOT EXISTS idx_urban_assets_class ON urban_assets(asset_class);
CREATE INDEX IF NOT EXISTS idx_urban_assets_priority ON urban_assets(maintenance_priority);

-- 4. Building Intelligence Table
CREATE TABLE IF NOT EXISTS building_intelligence (
    id SERIAL PRIMARY KEY,
    building_id VARCHAR(32) UNIQUE NOT NULL,
    street_id VARCHAR(16) REFERENCES road_network(street_id),
    floors INT NOT NULL,
    floor_notation VARCHAR(16),
    estimated_height_m NUMERIC(6, 2),
    building_usage VARCHAR(128),
    facade_type VARCHAR(128),
    ground_floor_activity VARCHAR(128),
    setback_distance_m NUMERIC(6, 2),
    establishment_name VARCHAR(256),
    cadastre_match_status VARCHAR(32),
    latitude NUMERIC(10, 6) NOT NULL,
    longitude NUMERIC(10, 6) NOT NULL,
    geom GEOMETRY(Point, 4326) NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_building_geom ON building_intelligence USING GIST(geom);

-- 5. Commercial Tax Recovery Ledger
CREATE TABLE IF NOT EXISTS ccmc_tax_ledger (
    id SERIAL PRIMARY KEY,
    property_id VARCHAR(32) UNIQUE NOT NULL,
    building_id VARCHAR(32) REFERENCES building_intelligence(building_id),
    business_name VARCHAR(256),
    trade_category VARCHAR(128),
    assessed_annual_tax_inr NUMERIC(12, 2) NOT NULL,
    compliance_status VARCHAR(64) NOT NULL,
    geom GEOMETRY(Point, 4326) NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_tax_ledger_geom ON ccmc_tax_ledger USING GIST(geom);

-- ==============================================================================
-- ADVANCED CIVIC SPATIAL QUERIES
-- ==============================================================================

-- Query 1: Detect TANGEDCO clearance violations (< 2.5m buffer from building facade)
CREATE OR REPLACE VIEW view_tangedco_clearance_violations AS
SELECT 
    p.asset_id AS pole_id,
    p.asset_subtype,
    b.building_id,
    b.establishment_name,
    ROUND(ST_Distance(p.geom::geography, b.geom::geography)::numeric, 2) AS clearance_distance_m,
    'P1-Critical' AS violation_severity
FROM urban_assets p
JOIN building_intelligence b 
    ON ST_DWithin(p.geom::geography, b.geom::geography, 2.5)
WHERE p.asset_class = 'electric_pole'
ORDER BY clearance_distance_m ASC;

-- Query 2: Detect CCMC Streetlight Infill Dark Spots (> 35m gap between luminaires)
CREATE OR REPLACE VIEW view_streetlight_coverage_gaps AS
SELECT 
    l1.asset_id AS light_a,
    l2.asset_id AS light_b,
    ROUND(ST_Distance(l1.geom::geography, l2.geom::geography)::numeric, 2) AS inter_distance_m
FROM urban_assets l1
JOIN urban_assets l2 
    ON l1.id < l2.id
    AND l1.asset_class = 'streetlight'
    AND l2.asset_class = 'streetlight'
    AND ST_DWithin(l1.geom::geography, l2.geom::geography, 80)
WHERE ST_Distance(l1.geom::geography, l2.geom::geography) > 35.0
ORDER BY inter_distance_m DESC;
