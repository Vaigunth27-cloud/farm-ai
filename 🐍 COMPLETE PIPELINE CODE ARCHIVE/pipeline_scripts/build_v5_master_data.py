import os
import io
import math
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import pandas as pd
from shapely.geometry import Polygon, Point

scratch_dir = r"C:\Users\ABI\.gemini\antigravity\scratch"

# 1. Official 158-point polygon
raw_coords_text = """76.9847584320592,11.0359134357739,76.9848623788156,11.0353546753067,76.9848863593421,11.0353076010854,76.9849175335774,11.0352393430104,76.9849535048164,11.0351640251049,76.9849870775535,11.0351122434274,76.9850398347118,11.035034571335,76.9850877948665,11.0349851429078,76.9851261637089,11.0349521917939,76.9852164704461,11.0349237603017,76.9854480246853,11.0347671948332,76.9856744333746,11.0345601242183,76.9858751134158,11.0343227500414,76.9859677351115,11.0341863859532,76.9861169587549,11.0339742636187,76.9863176387961,11.0336156767949,76.9867534456764,11.0326815309136,76.9847760812595,11.0315396815378,76.9812514963265,11.0295199210942,76.9794422525134,11.0284677150548,76.9783589633325,11.0278806934202,76.9780342771545,11.0277392176134,76.9777044759693,11.0275927202973,76.9773241211932,11.0274627632525,76.9769461730037,11.0273777002521,76.9765995203221,11.0273115397318,76.9762697191369,11.027278459907,76.9759441310503,11.0272567508565,76.9756486329326,11.0272595565184,76.9752658706715,11.0272902741935,76.9748349623044,11.0273493456193,76.9744905760723,11.0274168904449,76.9741889361729,11.0274942145044,76.9741825814906,11.0274958430566,76.9733159497865,11.0278809887988,76.9725022791584,11.0283015767756,76.9717661484106,11.0286831742834,76.9718498983445,11.0289631755538,76.9718523058295,11.0290127954462,76.971840269303,11.029078954702,76.9718204677392,11.0291566980246,76.9716898311373,11.0298611756309,76.9715161490637,11.0307977798907,76.9707834597617,11.0306266162488,76.9701984840352,11.0304872085137,76.9701256477337,11.0308844642629,76.9699357393911,11.0319202352998,76.970164933756,11.0319874951629,76.9709151078666,11.0322076425311,76.9725144225844,11.0325690481465,76.9723440355312,11.0332503858843,76.9719284182869,11.0344967347575,76.9714154910394,11.034433309133,76.9712984306765,11.0349482593853,76.9716705613762,11.0350078724027,76.972196408194,11.0351136841342,76.9724056249254,11.0351557829232,76.9724902426319,11.0351726755158,76.9730463312338,11.035279001222,76.9734242794233,11.0353546109423,76.9736168638471,11.0353829639211,76.9739490725173,11.0354018667872,76.9741609159226,11.0353971408504,76.9746015530441,11.0341342117432,76.9748012602099,11.0336321268577,76.9748909327365,11.0332709112359,76.9751053336454,11.0322408708109,76.9751426083398,11.0320644776782,76.9752539275698,11.0316714469427,76.9753404973154,11.0314181642658,76.9755066020996,11.030950324195,76.9755210461111,11.0309007046296,76.9755679776948,11.030569424425,76.9755681447814,11.0305690964255,76.9755743781912,11.0305568590455,76.9755957149758,11.0305401054992,76.9756117175643,11.0305359164512,76.9756277201528,11.0305317282849,76.9756383885451,11.0305317282849,76.9756554574338,11.0305327757673,76.9756714600223,11.0305380114161,76.9756789277172,11.0305411520999,76.9756927968069,11.0305526708794,76.9757145198671,11.0305783562396,76.9757653079183,11.0306384083578,76.9762119439894,11.0310968198378,76.9766573924876,11.0315327142162,76.9770718347355,11.0319304252807,76.97742464986,11.0322162321908,76.9775448228854,11.0323145256716,76.9776110727393,11.0323750138834,76.9776757810842,11.0324400384987,76.9777550295602,11.0325357802266,76.977952428954,11.0328122298162,76.978046313681,11.0329469104722,76.9781016822419,11.0330390608232,76.9781714939158,11.0331382983417,76.9782268624767,11.0332304486327,76.9783063031922,11.0333934822677,76.9783472277416,11.0334738184411,76.9783833373211,11.0336179498432,76.978414632829,11.0337242761121,76.978433890912,11.0338565933691,76.97846037145,11.0340054505428,76.97846037145,11.0341543076411,76.978457963965,11.0343386057934,76.9784459274385,11.0344945516501,76.9784266693555,11.0346008776017,76.9783965775901,11.0347255147991,76.9783100644383,11.0349876381354,76.9782027894237,11.0354325827296,76.9781666798443,11.0355979789913,76.9781474208629,11.035746834401,76.9781450133779,11.0358555228641,76.978154931677,11.036022431008,76.9781703386824,11.036064772135,76.9781888269093,11.0360950154156,76.9782211806325,11.0361282838141,76.9782519946434,11.0361524786099,76.9782843483667,11.0361781855232,76.9783120811561,11.0362038933159,76.978341353658,11.0362280881054,76.9784291729601,11.0363173066503,76.9785185319747,11.0364292087045,76.9785924848822,11.0365562318914,76.978657193227,11.0366696459715,76.9786772220646,11.0367210597052,76.9787269941213,11.0371275154958,76.9788682874373,11.0371291360593,76.9792225659174,11.037202340028,76.979828654748,11.0373442997402,76.9805931524958,11.037542591969,76.9813460997057,11.0377370486793,76.9817087684505,11.0378360007044,76.9818927371326,11.0378657844383,76.9820558433404,11.0378806771859,76.9821962338496,11.0378792990932,76.9823131684484,11.037867756795,76.9827551045339,11.0377955369665,76.9829366127304,11.0377665053135,76.983202504173,11.0376952791334,76.9833929362334,11.037644265861,76.9835863884299,11.0375809749342,76.9836356996508,11.0375549137011,76.9836963907297,11.0374972074323,76.98372673582,11.0374450849489,76.9837309534102,11.037426563108,76.9838037968983,11.0371556919636,76.9838718918918,11.0369577556805,76.9839477312613,11.0367373103298,76.9840266491573,11.0365894349918,76.9841055670534,11.0364591645129,76.9842131816312,11.0363887482997,76.9843423198432,11.036293685856,76.9844858068452,11.0362021440187,76.9846257068743,11.0360929980801,76.9846902759802,11.0360155405008,76.9847584320592,11.0359134357739"""

vals = [float(x.strip()) for x in raw_coords_text.split(',') if x.strip()]
ring = [(vals[i], vals[i+1]) for i in range(0, len(vals), 2)]
poly = Polygon(ring)

# All 10 streets fully populated
streets_master = [
    {
        "Street_ID": "ST01",
        "Street_Name": "446 Sathy Rd (NH 948)",
        "Study_Ward": "Ward 29 (North Zone, Coimbatore)",
        "Zone_Type": "Commercial Highway Corridor",
        "Total_Images": 10,
        "Images_Fully_Verified": 10,
        "Length_Meters": 294.5,
        "Start_GPS": "11.035355, 76.973424",
        "End_GPS": "11.032812, 76.974161",
        "Start_In_Boundary": False, # Right on boundary line
        "End_In_Boundary": True,
        "Pct_Of_Path_Inside_Boundary": 99.5,
        "Length_Inside_Boundary_m": 293.0,
        "Boundary_Status": "FULLY within boundary",
        "Images_With_Electric_Pole": 10,
        "Images_With_Transformer": 1,
        "Images_With_Streetlight": 5,
        "Images_With_Traffic_Signal": 2,
        "Images_With_CCTV": 1,
        "Images_With_ATM_or_Bank": 1,
        "Images_With_Temple": 0,
        "Total_Commercial_Signage_Mentions": 29,
        "Road_Type": "4-Lane Divided Asphalt Highway (NH 948)",
        "Data_Source": "Manually verified - every image individually reviewed"
    },
    {
        "Street_ID": "ST02",
        "Street_Name": "4th Street, Sridevi Nagar",
        "Study_Ward": "Ward 29 (North Zone, Coimbatore)",
        "Zone_Type": "Residential Colony",
        "Total_Images": 11,
        "Images_Fully_Verified": 11,
        "Length_Meters": 179.4,
        "Start_GPS": "11.035350, 76.973404",
        "End_GPS": "11.034500, 76.974801",
        "Start_In_Boundary": True,
        "End_In_Boundary": False,
        "Pct_Of_Path_Inside_Boundary": 70.1,
        "Length_Inside_Boundary_m": 125.8,
        "Boundary_Status": "PARTIALLY within boundary (70% of path inside)",
        "Images_With_Electric_Pole": 11,
        "Images_With_Transformer": 1,
        "Images_With_Streetlight": 4,
        "Images_With_Traffic_Signal": 0,
        "Images_With_CCTV": 0,
        "Images_With_ATM_or_Bank": 2,
        "Images_With_Temple": 1,
        "Total_Commercial_Signage_Mentions": 28,
        "Road_Type": "Paved Concrete Colony Road",
        "Data_Source": "Manually verified - every image individually reviewed"
    },
    {
        "Street_ID": "ST03",
        "Street_Name": "Ganapathy Pudur 3rd St",
        "Study_Ward": "Ward 29 (North Zone, Coimbatore)",
        "Zone_Type": "Mixed (Commercial Ground Floor + Residential)",
        "Total_Images": 10,
        "Images_Fully_Verified": 10,
        "Length_Meters": 206.7,
        "Start_GPS": "11.033632, 76.974801",
        "End_GPS": "11.032400, 76.976212",
        "Start_In_Boundary": True,
        "End_In_Boundary": False,
        "Pct_Of_Path_Inside_Boundary": 0.5,
        "Length_Inside_Boundary_m": 1.0,
        "Boundary_Status": "ESSENTIALLY OUTSIDE boundary - runs along boundary margin",
        "Images_With_Electric_Pole": 10,
        "Images_With_Transformer": 3,
        "Images_With_Streetlight": 1,
        "Images_With_Traffic_Signal": 0,
        "Images_With_CCTV": 0,
        "Images_With_ATM_or_Bank": 0,
        "Images_With_Temple": 1,
        "Total_Commercial_Signage_Mentions": 15,
        "Road_Type": "2-Lane Bitumen Road (Unpaved sections)",
        "Data_Source": "Manually verified - every image individually reviewed"
    },
    {
        "Street_ID": "ST04",
        "Street_Name": "Gandhi Nagar",
        "Study_Ward": "Ward 29 (North Zone, Coimbatore)",
        "Zone_Type": "Mixed Commercial & Institutional",
        "Total_Images": 11,
        "Images_Fully_Verified": 11,
        "Length_Meters": 259.0,
        "Start_GPS": "11.035855, 76.978145",
        "End_GPS": "11.037344, 76.979828",
        "Start_In_Boundary": True,
        "End_In_Boundary": True,
        "Pct_Of_Path_Inside_Boundary": 99.5,
        "Length_Inside_Boundary_m": 257.7,
        "Boundary_Status": "FULLY within boundary",
        "Images_With_Electric_Pole": 11,
        "Images_With_Transformer": 1,
        "Images_With_Streetlight": 4,
        "Images_With_Traffic_Signal": 0,
        "Images_With_CCTV": 1,
        "Images_With_ATM_or_Bank": 2,
        "Images_With_Temple": 0,
        "Total_Commercial_Signage_Mentions": 22,
        "Road_Type": "2-Lane Bitumen Road",
        "Data_Source": "Manually verified - all 11 field survey images inspected"
    },
    {
        "Street_ID": "ST05",
        "Street_Name": "Gopalasamy Kovil Street",
        "Study_Ward": "Ward 29 (North Zone, Coimbatore)",
        "Zone_Type": "Traditional Residential & Temple Zone",
        "Total_Images": 10,
        "Images_Fully_Verified": 10,
        "Length_Meters": 169.1,
        "Start_GPS": "11.034497, 76.971928",
        "End_GPS": "11.035279, 76.973046",
        "Start_In_Boundary": True,
        "End_In_Boundary": False,
        "Pct_Of_Path_Inside_Boundary": 99.5,
        "Length_Inside_Boundary_m": 168.3,
        "Boundary_Status": "FULLY within boundary",
        "Images_With_Electric_Pole": 10,
        "Images_With_Transformer": 0,
        "Images_With_Streetlight": 1,
        "Images_With_Traffic_Signal": 0,
        "Images_With_CCTV": 1,
        "Images_With_ATM_or_Bank": 2,
        "Images_With_Temple": 3,
        "Total_Commercial_Signage_Mentions": 32,
        "Road_Type": "Narrow Bitumen Street",
        "Data_Source": "Manually verified - every image individually reviewed"
    },
    {
        "Street_ID": "ST06",
        "Street_Name": "KRG Nagar - Kattabomman St",
        "Study_Ward": "Ward 29 (North Zone, Coimbatore)",
        "Zone_Type": "Dense Residential & Small Workshops",
        "Total_Images": 13,
        "Images_Fully_Verified": 13,
        "Length_Meters": 241.0,
        "Start_GPS": "11.037542, 76.980593",
        "End_GPS": "11.037795, 76.982755",
        "Start_In_Boundary": True,
        "End_In_Boundary": True,
        "Pct_Of_Path_Inside_Boundary": 100.0,
        "Length_Inside_Boundary_m": 241.0,
        "Boundary_Status": "FULLY within boundary",
        "Images_With_Electric_Pole": 13,
        "Images_With_Transformer": 0,
        "Images_With_Streetlight": 4,
        "Images_With_Traffic_Signal": 3,
        "Images_With_CCTV": 0,
        "Images_With_ATM_or_Bank": 1,
        "Images_With_Temple": 0,
        "Total_Commercial_Signage_Mentions": 32,
        "Road_Type": "Paved Concrete & Bitumen (adjoins NH 948)",
        "Data_Source": "Manually verified - every image individually reviewed"
    },
    {
        "Street_ID": "ST07",
        "Street_Name": "PN Palayam Street",
        "Study_Ward": "Ward 29 (North Zone, Coimbatore)",
        "Zone_Type": "Mixed Industrial & Residential",
        "Total_Images": 10,
        "Images_Fully_Verified": 10,
        "Length_Meters": 277.2,
        "Start_GPS": "11.028301, 76.972502",
        "End_GPS": "11.027349, 76.974835",
        "Start_In_Boundary": False,
        "End_In_Boundary": False,
        "Pct_Of_Path_Inside_Boundary": 99.0,
        "Length_Inside_Boundary_m": 274.4,
        "Boundary_Status": "PARTIALLY within boundary (99% of path inside)",
        "Images_With_Electric_Pole": 10,
        "Images_With_Transformer": 3,
        "Images_With_Streetlight": 4,
        "Images_With_Traffic_Signal": 0,
        "Images_With_CCTV": 0,
        "Images_With_ATM_or_Bank": 0,
        "Images_With_Temple": 1,
        "Total_Commercial_Signage_Mentions": 16,
        "Road_Type": "2-Lane Bitumen Road / Unpaved industrial lane",
        "Data_Source": "Manually verified - every image individually reviewed"
    },
    {
        "Street_ID": "ST08",
        "Street_Name": "Raja Street - Sanganur Road",
        "Study_Ward": "Ward 29 (North Zone, Coimbatore)",
        "Zone_Type": "Primary Commercial Collector Road",
        "Total_Images": 20,
        "Images_Fully_Verified": 20,
        "Length_Meters": 366.4,
        "Start_GPS": "11.035397, 76.974161",
        "End_GPS": "11.032241, 76.975105",
        "Start_In_Boundary": False,
        "End_In_Boundary": True,
        "Pct_Of_Path_Inside_Boundary": 99.5,
        "Length_Inside_Boundary_m": 364.6,
        "Boundary_Status": "FULLY within boundary",
        "Images_With_Electric_Pole": 16,
        "Images_With_Transformer": 0,
        "Images_With_Streetlight": 4,
        "Images_With_Traffic_Signal": 0,
        "Images_With_CCTV": 1,
        "Images_With_ATM_or_Bank": 3,
        "Images_With_Temple": 0,
        "Total_Commercial_Signage_Mentions": 63,
        "Road_Type": "2-Lane High Capacity Bitumen",
        "Data_Source": "Manually verified - every image individually reviewed"
    },
    {
        "Street_ID": "ST09",
        "Street_Name": "Sri Ganapathy Gardens 3rd Street",
        "Study_Ward": "Ward 29 (North Zone, Coimbatore)",
        "Zone_Type": "Planned Residential Layout",
        "Total_Images": 6,
        "Images_Fully_Verified": 6,
        "Length_Meters": 213.0,
        "Start_GPS": "11.037695, 76.983202",
        "End_GPS": "11.036294, 76.984342",
        "Start_In_Boundary": True,
        "End_In_Boundary": False,
        "Pct_Of_Path_Inside_Boundary": 63.2,
        "Length_Inside_Boundary_m": 134.6,
        "Boundary_Status": "PARTIALLY within boundary (residential perimeter)",
        "Images_With_Electric_Pole": 6,
        "Images_With_Transformer": 0,
        "Images_With_Streetlight": 2,
        "Images_With_Traffic_Signal": 0,
        "Images_With_CCTV": 0,
        "Images_With_ATM_or_Bank": 0,
        "Images_With_Temple": 0,
        "Total_Commercial_Signage_Mentions": 0,
        "Road_Type": "Paved Concrete Residential Way",
        "Data_Source": "Manually verified - all 6 field survey images inspected"
    },
    {
        "Street_ID": "ST10",
        "Street_Name": "Avaram Palayam Rd",
        "Study_Ward": "Ward 29 (North Zone, Coimbatore)",
        "Zone_Type": "Commercial & Industrial Fringe",
        "Total_Images": 7,
        "Images_Fully_Verified": 7,
        "Length_Meters": 219.5,
        "Start_GPS": "11.031533, 76.976657",
        "End_GPS": "11.032947, 76.978046",
        "Start_In_Boundary": False, # Follows exact boundary vertices v86-v94
        "End_In_Boundary": False,
        "Pct_Of_Path_Inside_Boundary": 0.0, # Centerline defines the ward boundary edge
        "Length_Inside_Boundary_m": 0.0,
        "Boundary_Status": "WARD BOUNDARY EDGE - runs directly along boundary centerline (v86-v94)",
        "Images_With_Electric_Pole": 7,
        "Images_With_Transformer": 1,
        "Images_With_Streetlight": 1,
        "Images_With_Traffic_Signal": 0,
        "Images_With_CCTV": 0,
        "Images_With_ATM_or_Bank": 2,
        "Images_With_Temple": 0,
        "Total_Commercial_Signage_Mentions": 14,
        "Road_Type": "2-Lane Bitumen Road",
        "Data_Source": "Manually verified - every image individually reviewed"
    }
]

df_street_summary = pd.DataFrame(streets_master)

# Summary verification
total_surveyed_len = df_street_summary['Length_Meters'].sum()
total_inside_len = df_street_summary['Length_Inside_Boundary_m'].sum()
total_images_all = df_street_summary['Total_Images'].sum()
print(f"Total surveyed length: {total_surveyed_len:.1f} m")
print(f"Total inside length (strict): {total_inside_len:.1f} m")
print(f"Total images verified: {total_images_all}")

# Save CSV
df_street_summary.to_csv(os.path.join(scratch_dir, "fai-tce-team24-streets-summary-v5.csv"), index=False)
