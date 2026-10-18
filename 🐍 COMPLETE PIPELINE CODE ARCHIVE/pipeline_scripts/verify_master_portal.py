import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'D:\farm ai\urban_digital_twin_portal.html', 'r', encoding='utf-8') as f:
    text = f.read()

tabs = ['triview', 'gis', 'buildings', 'ocr', 'passports', 'scorecards', 'copilot', 'municipal', 'aws', 'vlm', 'export']
all_ok = True
for t in tabs:
    has_tab = f'id="tab_{t}"' in text
    has_pane = f'id="pane_{t}"' in text
    print(f"Tab {t:12s} -> Button: {has_tab} | Pane: {has_pane}")
    if not (has_tab and has_pane):
        all_ok = False

print("\nAll 11 modules verified in Master Platform:", all_ok)
