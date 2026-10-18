import os
import openpyxl
import pandas as pd

excel_path = r"C:\Users\ABI\.gemini\antigravity\scratch\fai-tce-team24-urban-dataset-v3-corrected.xlsx"
wb = openpyxl.load_workbook(excel_path)

print("Sheet names:", wb.sheetnames)

df_s = pd.read_excel(excel_path, sheet_name="Street_Summary")
df_i = pd.read_excel(excel_path, sheet_name="Image_Intelligence")
df_a = pd.read_excel(excel_path, sheet_name="Urban_Asset_Inventory")
df_p = pd.read_excel(excel_path, sheet_name="Pole_Asset_Inventory")
df_b = pd.read_excel(excel_path, sheet_name="Ward29_Boundary_Metadata")

print("\n--- SUMMARY OF SHEETS ---")
print(f"1. Street_Summary: {len(df_s)} streets")
print(f"2. Image_Intelligence: {len(df_i)} surveyed image frames")
print(f"3. Urban_Asset_Inventory: {len(df_a)} total cataloged assets")
print(f"4. Pole_Asset_Inventory: {len(df_p)} anchor pole locations")
print(f"5. Ward29_Boundary_Metadata: {len(df_b)} boundary record")

print("\n--- CHECKING AGGREGATION INTEGRITY ---")
img_agg = df_i.groupby('Street_ID').agg(
    imgs=('Image_ID', 'count'),
    poles=('Electric_Poles', 'sum'),
    lights=('Streetlights', 'sum'),
    signs=('Commercial_Signs', 'sum')
).reset_index()

merged = pd.merge(df_s, img_agg, on='Street_ID')
for idx, r in merged.iterrows():
    m_img = r['Total_Images'] == r['imgs']
    m_pol = r['Poles_Count'] == r['poles']
    m_lgt = r['Streetlights_Count'] == r['lights']
    m_sgn = r['Signboards_Count'] == r['signs']
    all_ok = m_img and m_pol and m_lgt and m_sgn
    print(f"Street {r['Street_ID']} ({r['Street_Name'][:20]}): Exact Match = {all_ok} (Imgs:{r['Total_Images']} Poles:{r['Poles_Count']} Lights:{r['Streetlights_Count']} Signs:{r['Signboards_Count']})")

print("\n--- TOTAL VERIFICATION ---")
print(f"Total Road Length: {df_s['Length_Meters'].sum():.1f} meters ({df_s['Length_Meters'].sum()/1000.0:.2f} km)")
print(f"Total Images: {df_s['Total_Images'].sum()} (matches images sheet: {len(df_i) == df_s['Total_Images'].sum()})")
print(f"Total Poles: {df_s['Poles_Count'].sum()} (matches poles count in assets: {(df_a['Asset_Type'] == 'Electric Utility Pole').sum() == df_s['Poles_Count'].sum()})")
print(f"Total Streetlights: {df_s['Streetlights_Count'].sum()} (matches lights count in assets: {(df_a['Asset_Type'] == 'Municipal Streetlight Fixture').sum() == df_s['Streetlights_Count'].sum()})")
print(f"Total Signboards: {df_s['Signboards_Count'].sum()} (matches signs count in assets: {(df_a['Asset_Type'] == 'Commercial Signboard / Fascia').sum() == df_s['Signboards_Count'].sum()})")
print(f"Total Cataloged Assets: {len(df_a)} == {df_s['Poles_Count'].sum() + df_s['Streetlights_Count'].sum() + df_s['Signboards_Count'].sum()}")
