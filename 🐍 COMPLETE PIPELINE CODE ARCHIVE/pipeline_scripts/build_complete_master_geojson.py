import os
import json

scratch_dir = r"C:\Users\ABI\.gemini\antigravity\scratch"

# Load boundary
with open(os.path.join(scratch_dir, "ward29_boundary.geojson"), "r", encoding="utf-8") as f:
    boundary_data = json.load(f)
boundary_features = boundary_data.get("features", [])
for feat in boundary_features:
    feat["properties"]["layer"] = "ward_boundary"
    feat["properties"]["name"] = "Coimbatore Ward 29 (Official Municipal Study Area)"

# Load streets
with open(os.path.join(scratch_dir, "fai-tce-team24-streets.geojson"), "r", encoding="utf-8") as f:
    streets_data = json.load(f)
street_features = streets_data.get("features", [])

# Load assets
with open(os.path.join(scratch_dir, "fai-tce-team24-assets.geojson"), "r", encoding="utf-8") as f:
    assets_data = json.load(f)
asset_features = assets_data.get("features", [])

# Load images
with open(os.path.join(scratch_dir, "fai-tce-team24-images.geojson"), "r", encoding="utf-8") as f:
    images_data = json.load(f)
image_features = images_data.get("features", [])

# Combine all into master
all_master_features = boundary_features + street_features + asset_features + image_features

master_geojson = {
    "type": "FeatureCollection",
    "name": "FarmwiseAI_TCE_Team24_Urban_Intelligence_Master_3D",
    "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
    "features": all_master_features
}

p_master = os.path.join(scratch_dir, "fai-tce-team24-master.geojson")
with open(p_master, "w", encoding="utf-8") as f:
    json.dump(master_geojson, f, indent=2)

print(f"Master GeoJSON updated with {len(all_master_features)} total features:")
print(f"  - Boundary: {len(boundary_features)}")
print(f"  - Streets: {len(street_features)}")
print(f"  - Assets: {len(asset_features)}")
print(f"  - Images: {len(image_features)}")
