import os
import pandas as pd

base = r"D:\farm ai"
for name in ['building_intelligence.csv', 'urban_asset_inventory.csv', 'spatial_relationships.csv', 'corridor_intelligence_scorecard.csv', 'ocr_intelligence.csv']:
    path = os.path.join(base, name)
    if os.path.exists(path):
        df = pd.read_csv(path)
        print(f"=== {name} ({len(df)} rows) ===")
        print("Columns:", list(df.columns)[:10], f"... (+ {len(df.columns)-10} more)" if len(df.columns) > 10 else "")
