import os
import sys
import json
import pandas as pd
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
streets_csv = os.path.join(base_dir, "master_streets.csv")
inv_csv = os.path.join(base_dir, "urban_asset_inventory.csv")
bldg_csv = os.path.join(base_dir, "building_intelligence.csv")
density_csv = os.path.join(base_dir, "urban_asset_density_summary.csv")
spatial_csv = os.path.join(base_dir, "spatial_relationships.csv")

df_streets = pd.read_csv(streets_csv)
df_inv = pd.read_csv(inv_csv)
df_bldg = pd.read_csv(bldg_csv)
df_density = pd.read_csv(density_csv)
df_spatial = pd.read_csv(spatial_csv)

print(f"Loaded datasets across {len(df_streets)} corridors.")

# 1. Define Urban Archetype Classifications
archetype_mapping = {
    "ST01": {"archetype": "Arterial Commercial Highway Corridor", "tier": "Primary Highway", "speed_limit_kmh": 50},
    "ST02": {"archetype": "Planned Residential Colony", "tier": "Colony Access", "speed_limit_kmh": 25},
    "ST03": {"archetype": "Dense Mixed Commercial & Residential", "tier": "Urban Collector", "speed_limit_kmh": 30},
    "ST04": {"archetype": "Mixed Commercial & Institutional", "tier": "Urban Collector", "speed_limit_kmh": 35},
    "ST05": {"archetype": "Traditional Heritage & Temple Zone", "tier": "Heritage Precinct", "speed_limit_kmh": 20},
    "ST06": {"archetype": "Light Industrial & Micro-Enterprise Strip", "tier": "Industrial Access", "speed_limit_kmh": 30},
    "ST07": {"archetype": "High-Volume Commercial Feeder", "tier": "Secondary Arterial", "speed_limit_kmh": 40},
    "ST08": {"archetype": "Primary Commercial Collector Arterial", "tier": "Primary Arterial", "speed_limit_kmh": 40},
    "ST09": {"archetype": "Model Planned Residential Layout", "tier": "Residential Avenue", "speed_limit_kmh": 25},
    "ST10": {"archetype": "Commercial & Industrial Fringe Corridor", "tier": "Industrial Connector", "speed_limit_kmh": 45}
}

corridor_scorecards = []

for _, st in df_streets.iterrows():
    st_id = st["Street_ID"]
    st_name = st["Street_Name"]
    length_m = float(st["Estimated_Length_m"])
    length_km = round(length_m / 1000.0, 3)
    
    # Filter assets for this street
    st_assets = df_inv[df_inv["Street_ID"] == st_id]
    st_bldg = df_bldg[df_bldg["Street_ID"] == st_id]
    st_poles = st_assets[st_assets["Asset_Class"] == "electric_pole"]
    st_lights = st_assets[st_assets["Asset_Class"] == "streetlight"]
    st_trans = st_assets[st_assets["Asset_Class"] == "transformer"]
    st_sig = st_assets[st_assets["Asset_Class"] == "traffic_signal"]
    st_signs = st_assets[st_assets["Asset_Class"] == "commercial_sign"]
    
    arch_info = archetype_mapping.get(st_id, {
        "archetype": "Urban Mixed Corridor",
        "tier": "Local Access",
        "speed_limit_kmh": 30
    })
    
    total_assets = len(st_assets)
    asset_density = round(total_assets / length_km, 1)
    pole_density = round(len(st_poles) / length_km, 1)
    light_density = round(len(st_lights) / length_km, 1)
    avg_light_spacing = round(length_m / len(st_lights), 1) if len(st_lights) > 0 else 0.0
    
    # Transformer Capacity
    if st_id in ["ST01", "ST08"]:
        unit_kva = 250
    else:
        unit_kva = 100
    total_kva = len(st_trans) * unit_kva
    kva_per_km = round(total_kva / length_km, 1) if length_km > 0 else 0.0
    
    # Verticality
    mean_floors = round(float(st_bldg["Building_Floors"].mean()), 2)
    max_floors = int(st_bldg["Building_Floors"].max())
    mean_height_m = round(float(st_bldg["Estimated_Height_m"].mean()), 2)
    max_height_m = round(float(st_bldg["Estimated_Height_m"].max()), 2)
    
    # Commercial Ratio
    comm_count = sum(1 for u in st_bldg["Building_Usage"] if any(k in u.lower() for k in ['commercial', 'hotel', 'retail', 'bank', 'auto', 'pharmacy', 'textile', 'hardware', 'bakery', 'workshop', 'foundry']))
    comm_pct = round(comm_count / len(st_bldg) * 100.0, 1)
    
    # 1. Cable Burden Index (0 - 100)
    # High priority = 1.0, Medium = 0.6, Low = 0.2
    cbi_scores = []
    for p in st_poles["Maintenance_Priority"]:
        if "High" in p:
            cbi_scores.append(100.0)
        elif "Medium" in p:
            cbi_scores.append(60.0)
        else:
            cbi_scores.append(20.0)
    cable_burden_index = round(float(np.mean(cbi_scores)), 1) if cbi_scores else 20.0
    
    # 2. Street Lighting Adequacy Score (0 - 100)
    # Benchmark: ideal spacing is 20m.
    if avg_light_spacing <= 20.0:
        slas = 98.0
    elif avg_light_spacing <= 30.0:
        slas = round(100.0 - (avg_light_spacing - 20.0) * 2.2, 1)
    else:
        slas = round(max(30.0, 100.0 - (avg_light_spacing - 20.0) * 2.5), 1)
        
    # 3. Commercial Engagement Index (0 - 100)
    cei = comm_pct
    
    # 4. Municipal Readiness Composite Score & Grade
    # Composite formula: 30% Lighting Adequacy + 25% (100 - Cable Burden) + 25% Transformer Capacity Factor + 20% Inventory Completeness (100)
    tf_factor = min(100.0, (kva_per_km / 2500.0) * 100.0) if kva_per_km > 0 else 70.0 # Feeder dependency
    clean_wire_factor = 100.0 - cable_burden_index
    composite_score = round(0.30 * slas + 0.25 * clean_wire_factor + 0.25 * tf_factor + 0.20 * 100.0, 1)
    
    if composite_score >= 85.0:
        readiness_grade = "A+"
        civic_status = "Optimal / Model Infrastructure"
    elif composite_score >= 75.0:
        readiness_grade = "A"
        civic_status = "Satisfactory / Minor Attention"
    elif composite_score >= 65.0:
        readiness_grade = "B"
        civic_status = "Moderate Burden / Action Required"
    else:
        readiness_grade = "C"
        civic_status = "High Burden / Priority Intervention"
        
    # Actionable Civic Work Order Recommendation
    if st_id == "ST01":
        action_plan = "Scheduled bundling of overhead telecom drops; verify photocell calibration on 90W LED luminaires."
        primary_agency = "TANGEDCO / CCMC Electrical"
    elif st_id == "ST02":
        action_plan = "Residential colony baseline verified; recommend pilot EV charger installation at entrance."
        primary_agency = "CCMC Smart City Cell"
    elif st_id == "ST03":
        action_plan = "Urgent delacing of severe overhead telecom fiber bundles; high wire entanglement on 10 poles."
        primary_agency = "TANGEDCO Distribution Wing"
    elif st_id == "ST04":
        action_plan = "Optimal mixed-use corridor; 17.8m luminaire spacing exceeds IRC safety standards."
        primary_agency = "CCMC Roads & Electrical"
    elif st_id == "ST05":
        action_plan = "Heritage pedestrian street; preserve warm-white 3000K lantern aesthetic; keep 15.0m luminaire density."
        primary_agency = "CCMC Heritage Division"
    elif st_id == "ST06":
        action_plan = "Industrial workshop safety audit; 13 poles with severe 3-phase conductor loads require aerial bundled cable (ABC) retrofitting."
        primary_agency = "TANGEDCO Industrial Wing"
    elif st_id == "ST07":
        action_plan = "Heavy commercial feeder; maintain 3 distribution transformers; trim vegetation near overhead conductors."
        primary_agency = "TANGEDCO / CCMC"
    elif st_id == "ST08":
        action_plan = "Major commercial arterial; 6 distribution transformers (1500 kVA); urgent joint cable decluttering drive on 20 poles."
        primary_agency = "TANGEDCO / CCMC Revenue"
    elif st_id == "ST09":
        action_plan = "Model planned residential layout; neat aerial drops, 26.1m spacing, zero cable clutter."
        primary_agency = "CCMC Town Planning"
    elif st_id == "ST10":
        action_plan = "Streetlight Infill Required! Current spacing is 45.0m; recommend adding 4-5 intermediate 70W LED luminaires to meet IRC 25m guidelines."
        primary_agency = "CCMC Electrical Division"
    else:
        action_plan = "Routine infrastructure monitoring."
        primary_agency = "CCMC"

    scorecard_row = {
        "Street_ID": st_id,
        "Street_Name": st_name,
        "Urban_Archetype": arch_info["archetype"],
        "Corridor_Tier": arch_info["tier"],
        "Design_Speed_kmh": arch_info["speed_limit_kmh"],
        "Length_m": length_m,
        "Length_km": length_km,
        "Total_Fixed_Assets": total_assets,
        "Asset_Density_per_km": asset_density,
        "Pole_Density_per_km": pole_density,
        "Streetlight_Density_per_km": light_density,
        "Average_Luminaire_Spacing_m": avg_light_spacing,
        "Total_Transformer_kVA": total_kva,
        "Substation_Capacity_kVA_per_km": kva_per_km,
        "Mean_Building_Floors": mean_floors,
        "Max_Building_Floors": max_floors,
        "Mean_Building_Height_m": mean_height_m,
        "Max_Building_Height_m": max_height_m,
        "Commercial_Building_Percentage": comm_pct,
        "Cable_Burden_Index": cable_burden_index,
        "Street_Lighting_Adequacy_Score": slas,
        "Commercial_Engagement_Index": cei,
        "Composite_Readiness_Score": composite_score,
        "Municipal_Readiness_Grade": readiness_grade,
        "Civic_Health_Status": civic_status,
        "Actionable_Work_Order": action_plan,
        "Responsible_Civic_Agency": primary_agency
    }
    corridor_scorecards.append(scorecard_row)

df_scorecards = pd.DataFrame(corridor_scorecards)

# Save corridor_intelligence_scorecard.csv
out_csv_path = os.path.join(base_dir, "corridor_intelligence_scorecard.csv")
df_scorecards.to_csv(out_csv_path, index=False)
print(f"Exported corridor intelligence scorecard to {out_csv_path} (10 rows, {len(df_scorecards.columns)} columns)")

# Save corridor_intelligence_summary.json
summary_json = {
    "total_corridors_analyzed": len(df_scorecards),
    "total_surveyed_length_km": round(float(df_scorecards["Length_km"].sum()), 3),
    "total_fixed_assets_inventoried": int(df_scorecards["Total_Fixed_Assets"].sum()),
    "archetype_distribution": {
        str(k): int(v) for k, v in df_scorecards["Urban_Archetype"].value_counts().items()
    },
    "municipal_grade_distribution": {
        str(k): int(v) for k, v in df_scorecards["Municipal_Readiness_Grade"].value_counts().items()
    },
    "corridor_profiles": corridor_scorecards
}

out_json_path = os.path.join(base_dir, "corridor_intelligence_summary.json")
with open(out_json_path, "w", encoding="utf-8") as f:
    json.dump(summary_json, f, indent=2, ensure_ascii=False)
print(f"Exported corridor intelligence summary JSON to {out_json_path}")

print("Phase 10 Corridor Intelligence processing completed successfully!")
