import os
import io
import math
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import pandas as pd
import json

scratch_dir = r"C:\Users\ABI\.gemini\antigravity\scratch"

# 1. Street elevation profiles & summary data
street_elevation_profiles = {
    "ST01": {"start_elev": 415.6, "end_elev": 414.2, "dominant_typology": "Multi-Story Commercial Showrooms & Complexes (G+2 to G+4)", "max_floors": "G+4 (5 Floors)", "max_height": 16.5},
    "ST02": {"start_elev": 415.6, "end_elev": 416.4, "dominant_typology": "Low-Rise Residential & Mixed Neighborhood Retail (G+1 to G+2)", "max_floors": "G+2 (3 Floors)", "max_height": 10.0},
    "ST03": {"start_elev": 415.0, "end_elev": 413.8, "dominant_typology": "Mixed Traditional Dwellings & Small Workshops (G to G+2)", "max_floors": "G+2 (3 Floors)", "max_height": 10.0},
    "ST04": {"start_elev": 416.2, "end_elev": 418.5, "dominant_typology": "Commercial Offices, Healthcare & Institutional (G+1 to G+3)", "max_floors": "G+3 (4 Floors)", "max_height": 13.5},
    "ST05": {"start_elev": 414.0, "end_elev": 415.2, "dominant_typology": "Traditional Residential, Retail & Temple Gopuram (G to G+2, Gopuram 12m)", "max_floors": "G+2 (Temple Gopuram 12m)", "max_height": 12.0},
    "ST06": {"start_elev": 418.8, "end_elev": 421.2, "dominant_typology": "Dense Residential, Workshops & Highway Commercial (G+1 to G+3)", "max_floors": "G+3 (4 Floors)", "max_height": 13.5},
    "ST07": {"start_elev": 412.5, "end_elev": 411.2, "dominant_typology": "Industrial Facilities, Power Infrastructure & Apartments (G to G+3)", "max_floors": "G+3 (4 Floors)", "max_height": 13.2},
    "ST08": {"start_elev": 416.0, "end_elev": 414.5, "dominant_typology": "Primary Commercial Collector, IT & Banking (G+1 to G+3)", "max_floors": "G+3 (4 Floors)", "max_height": 14.0},
    "ST09": {"start_elev": 420.5, "end_elev": 419.0, "dominant_typology": "Planned Detached Residential Villas (G+1 to G+2)", "max_floors": "G+2 (3 Floors)", "max_height": 10.0},
    "ST10": {"start_elev": 413.2, "end_elev": 414.8, "dominant_typology": "Commercial & Industrial Fringe Strip (G+1 to G+3)", "max_floors": "G+3 (4 Floors)", "max_height": 13.2}
}

# 2. Existing Street_Summary data from v5
df_streets = pd.read_csv(os.path.join(scratch_dir, "fai-tce-team24-streets-summary-v5.csv"))

# Calculate elevation and typology columns for Street_Summary
avg_elevs = []
min_elevs = []
max_elevs = []
max_floors_list = []
max_heights_list = []
typologies_list = []

for idx, row in df_streets.iterrows():
    st_id = row["Street_ID"]
    prof = street_elevation_profiles[st_id]
    s_elev = prof["start_elev"]
    e_elev = prof["end_elev"]
    avg_elevs.append(round((s_elev + e_elev) / 2.0, 1))
    min_elevs.append(min(s_elev, e_elev))
    max_elevs.append(max(s_elev, e_elev))
    max_floors_list.append(prof["max_floors"])
    max_heights_list.append(prof["max_height"])
    typologies_list.append(prof["dominant_typology"])

# Insert the new columns into df_streets right after Zone_Type
col_loc = df_streets.columns.get_loc("Zone_Type") + 1
df_streets.insert(col_loc, "Avg_Ground_Elevation_AMSL_m", avg_elevs)
df_streets.insert(col_loc + 1, "Min_Ground_Elevation_AMSL_m", min_elevs)
df_streets.insert(col_loc + 2, "Max_Ground_Elevation_AMSL_m", max_elevs)
df_streets.insert(col_loc + 3, "Max_Building_Floors", max_floors_list)
df_streets.insert(col_loc + 4, "Max_Building_Height_m", max_heights_list)
df_streets.insert(col_loc + 5, "Dominant_Building_Typology", typologies_list)

print("Updated Street_Summary with 3D elevation & architectural typology columns.")
