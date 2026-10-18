import json
from shapely.geometry import shape, Point, LineString, Polygon, MultiPolygon

with open(r"D:\Study_area.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

geom = shape(data["features"][0]["geometry"])
props = data["features"][0]["properties"]

print("Study Area Properties:", props)
print("Geometry Type:", geom.geom_type)
print("Bounds (minx, miny, maxx, maxy) [lng_min, lat_min, lng_max, lat_max]:", geom.bounds)
print("Is Valid:", geom.is_valid)

# Let's check the coordinate system:
# Lon: 76.9699 to 76.9868 (~76.97 to 76.98)
# Lat: 11.0272 to 11.0379 (~11.027 to 11.038)
print(f"Longitude range: {geom.bounds[0]:.6f} to {geom.bounds[2]:.6f}")
print(f"Latitude range: {geom.bounds[1]:.6f} to {geom.bounds[3]:.6f}")
