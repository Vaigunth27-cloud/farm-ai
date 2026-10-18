"""
==========================================================================
Generate 5 HFSS project files for the CP Filtering Patch Antenna
==========================================================================
Based on paper: "Compact Broadband Circularly Polarized Filtering Patch 
Antenna With Multi-Element Coupling Structure"

Source file: Filtering_antenna_v15_final.hfss (resonates at 3.5 GHz)
Target: 3.05 GHz with circular polarization

The paper's Figure 4 shows 4 evolution stages:
  Ant I:   Bare patch + GND/U-slot/feed (no stubs, no parasitics, no slot)
  Ant II:  Patch + L-stubs (Stub A + Stub B) 
  Ant III: Patch + L-stubs + 4 parasitic patches
  Ant IV:  Patch + L-stubs + 4 parasitics + patch slot (full design)

Plus: Stage 5 = Full design frequency-tuned to 3.05 GHz

==========================================================================
V15 GEOMETRY MAPPING (from analysis)
==========================================================================
STACK-UP (origin at bottom-left corner, NOT centered):
  z=0:     Feed line copper (feedline1..feedline8)
  z=0..1:  Lower FR4 substrate (fr4bottom, 60x60x1mm)
  z=1:     Ground plane with U-slot (feedline = 60x60 sheet, minus feedline9+10+11)
  z=1..7:  Air gap (Box1, 60x60x6mm)
  z=7..7.8: Upper FR4 substrate (fr4upper, 60x60x0.8mm)
  z=7:     y-parasitic patches (Rectangle1, Rectangle2)
  z=7.8:   Main patch, x-parasitics, stubs, slot (Rectangle5 etc.)

PART IDENTIFICATION:
  Main Patch:     Rectangle5  (13.8, 14.1, 7.8) W=32.5 H=31.4
  Patch Slot:     Rectangle8  (17.3, 21.8, 7.8) W=25 H=1 -> subtracted from R5
  
  Stub B (left):  Rectangle9  (15, 7.8, 7.8) W=35 H=4  [horizontal arm l4]
                  Rectangle13 (10, 26.3, 7.8) W=3 H=25  [vertical arm l3, w3=3??]
                  + Rectangle10,11,12 [corner details]
  
  Stub A (right): Rectangle14 (10, 48.3, 7.8) W=31 H=3  [horizontal arm l5]
                  + Rectangle15,16 [corner details]
  
  y-Parasitics:   Rectangle1 (0, 4, 7) W=5.8 H=38.8   [left, at z=7]
                  Rectangle2 (54.2, 17.2, 7) W=5.8 H=38.8 [right, at z=7]
  
  x-Parasitics:   Rectangle3 (18.5, 0, 7.8) W=39 H=5.8  [bottom]
                  Rectangle4 (2.5, 54.2, 7.8) W=39 H=5.8 [top]
  
  Slot cutouts:   Rectangle6 (13.8, 14.1, 7.8) W=0.8 H=10  -> subtracted from R5
                  Rectangle7 (45.5, 14.1, 7.8) W=0.8 H=10  -> subtracted from R5

  Ground plane:   feedline (0,0,1) 60x60 sheet with U-slot subtracted
  U-slot:         feedline9  (35.5, 20.75, 1) W=2.5 H=19 [vertical lc3 arm]
                  feedline10 (28, 20.75, 1) W=10 H=2.5   [horizontal lc2 bar]
                  feedline11 (13, 37.25, 1) W=25 H=2.5    [long lc1 arm]
  
  Feed segments:  feedline1 (58.3, 29, 0) W=1.7 H=2 [SMA jog, lg7]
                  feedline2 (43, 28.2, 0) W=15.3 H=3.6 [lg6, wg1]
                  feedline3 (41, 26.9, 0) W=2 H=6 [lg4, wg3]
                  feedline4 (33, 28.2, 0) W=8 H=3.6 [lg5, wg1]
                  feedline5 (31, 26.9, 0) W=2 H=6 [lg3, wg3]
                  feedline6 (28.5, 28.1, 0) W=2.5 H=3.6 [lg2?]
                  feedline7 (25.5, 27.5, 0) W=3 H=5 [wg2]
                  feedline8 (19.3, 28.2, 0) W=6.2 H=3.6 [lg1, wg1]
  
  Port:           Rectangle17 (60, 29, 0) W=2 H=1 on X-axis [lumped port]
  
  Radiation box:  Box2 (-30,-30,-30) 120x120x67.8

BOUNDARY CONDITIONS:
  PerfE1 (Perfect E): Objects(58, 487, 166, 178, 190, 202, 226, 325, 399)
    58  = feedline (GND plane)
    487 = feedline1 complex (united feed segments)
    166 = Rectangle1 (y-parasitic left)
    178 = Rectangle2 (y-parasitic right)
    190 = Rectangle3 (x-parasitic bottom)
    202 = Rectangle4 (x-parasitic top)
    226 = Rectangle5 (main patch)
    325 = Rectangle9 complex (Stub B)
    399 = Rectangle13 complex (Rectangle13+14+15+16 = Stub A area)
  Rad1: Objects(691) = Box2
  Port 1: Objects(719) = Rectangle17

==========================================================================
FREQUENCY SCALING: 3.5 GHz -> 3.05 GHz
==========================================================================
Scale factor K = 3.5 / 3.05 = 1.1475

All resonant dimensions scale by K:
  - Main patch: l7*K, l8*K
  - Patch slot: ls*K, ws*K  
  - L-stub arms: l3*K, l4*K, l5*K, l6*K
  - Parasitic patches: l1*K, l2*K (w1, w2 stay same for coupling)
  - U-slot: lc1*K, lc2*K, lc3*K
  - Feed line lengths: scale by K (widths stay same for impedance)

NOTE: The substrate (60x60mm) and overall board size stay FIXED.
Offsets (d1-d7, t1-t3) need recalculation to keep elements centered.
"""

import re
import os
import copy

# ---- Configuration ----
INPUT_FILE = r'C:\Users\ABI\.gemini\antigravity\scratch\Filtering_antenna_v15_final.hfss'
OUTPUT_DIR = r'C:\Users\ABI\Downloads'

# Scale factor for 3.05 GHz
K = 3.5 / 3.05  # = 1.1475

# Read the original HFSS file
with open(INPUT_FILE, 'r', encoding='latin-1') as f:
    original_text = f.read()


def replace_rect_param(text, op_id, param_name, new_value):
    """Replace a specific parameter in a Rectangle/Box operation identified by its ID."""
    # Find the operation block with this ID
    pattern = rf"(OperationType='(?:Rectangle|Box)'\s+ID={op_id}\s+.*?\$begin '(?:Rectangle|Box)Parameters'.*?{param_name}=')[^']*(')"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        text = text[:match.start(1)] + match.group(1) + new_value + match.group(2) + text[match.end(2):]
        return text
    return text


def replace_param_near_id(text, op_id, param_name, new_value):
    """Replace parameter value near a specific operation ID."""
    pos = text.find(f"ID={op_id}")
    if pos == -1:
        return text
    # Search within next 500 chars for the parameter
    search_region = text[pos:pos+500]
    param_pattern = f"{param_name}='[^']*'"
    match = re.search(param_pattern, search_region)
    if match:
        new_param = f"{param_name}='{new_value}'"
        start = pos + match.start()
        end = pos + match.end()
        text = text[:start] + new_param + text[end:]
    return text


def clear_solutions(text):
    """Clear cached solution data so HFSS re-solves."""
    text = re.sub(r"\$begin 'Solutions'.*?\$end 'Solutions'", 
                  "$begin 'Solutions'\n\t\t$end 'Solutions'", text, flags=re.DOTALL)
    return text


# ============================================================
# Identify all operation IDs from the original file
# ============================================================
# We need the operation IDs for each part's CreateRectangle/CreateBox
# Let's extract them:

def get_op_id(text, part_name):
    """Get the first Rectangle/Box operation ID for a named part."""
    pat = re.escape(part_name)
    part_match = re.search(
        r"\$begin 'GeometryPart'\s+\$begin 'Attributes'\s+Name='" + pat + r"'.*?\$end 'GeometryPart'",
        text, re.DOTALL
    )
    if part_match:
        part_text = part_match.group(0)
        id_match = re.search(r"OperationType='(?:Rectangle|Box)'\s+ID=(\d+)", part_text)
        if id_match:
            return int(id_match.group(1))
    return None

# Get all operation IDs
op_ids = {}
for part in ['fr4bottom', 'feedline', 'Box1', 'fr4upper', 'patch',
             'Rectangle1', 'Rectangle2', 'Rectangle3', 'Rectangle4', 'Rectangle5',
             'Rectangle6', 'Rectangle7', 'Rectangle8', 'Rectangle9', 
             'Rectangle10', 'Rectangle11', 'Rectangle12', 'Rectangle13',
             'Rectangle14', 'Rectangle15', 'Rectangle16', 'Rectangle17',
             'feedline1', 'feedline2', 'feedline3', 'feedline4', 'feedline5',
             'feedline6', 'feedline7', 'feedline8', 'feedline9',
             'feedline10', 'feedline11', 'Box2']:
    oid = get_op_id(original_text, part)
    if oid:
        op_ids[part] = oid
        
print("Operation IDs found:")
for name, oid in sorted(op_ids.items(), key=lambda x: x[1]):
    print(f"  {name}: ID={oid}")


# ============================================================
# Helper: Remove parts by suppressing their operations
# ============================================================
def suppress_part(text, part_name):
    """Suppress a part by setting IsSuppressed=true on all its operations."""
    pat = re.escape(part_name)
    part_match = re.search(
        r"\$begin 'GeometryPart'\s+\$begin 'Attributes'\s+Name='" + pat + r"'.*?\$end 'GeometryPart'",
        text, re.DOTALL
    )
    if part_match:
        part_text = part_match.group(0)
        new_part = part_text.replace("IsSuppressed=false", "IsSuppressed=true")
        text = text.replace(part_text, new_part)
    return text


def remove_from_perfe(text, body_id):
    """Remove a body ID from PerfE1 boundary Objects list."""
    # Find PerfE1 Objects line
    match = re.search(r"(Objects\([^)]*" + str(body_id) + r"[^)]*\))", text)
    if match:
        old_objs = match.group(1)
        # Remove the body_id from the list
        new_objs = old_objs.replace(f", {body_id}", "").replace(f"{body_id}, ", "").replace(f"{body_id}", "")
        if new_objs == "Objects()":
            # Don't create empty objects
            pass
        text = text.replace(old_objs, new_objs)
    return text


# ============================================================
# STAGE 1: Bare Patch (Ant. I)
# ============================================================
# Keep: fr4bottom, feedline (GND+U-slot), Box1, fr4upper, patch,
#       Rectangle5 (main patch), feedline1-8 (feed), feedline9-11 (U-slot),
#       Rectangle17 (port), Box2 (radiation)
# Remove: Rectangle1,2 (y-parasitics), Rectangle3,4 (x-parasitics),
#         Rectangle6,7,8 (slot cutouts from patch),
#         Rectangle9-16 (stubs)

print("\n=== GENERATING STAGE 1: Bare Patch ===")
stage1 = original_text

# Suppress parasitic patches
for p in ['Rectangle1', 'Rectangle2', 'Rectangle3', 'Rectangle4']:
    stage1 = suppress_part(stage1, p)

# Suppress stubs
for p in ['Rectangle9', 'Rectangle10', 'Rectangle11', 'Rectangle12',
          'Rectangle13', 'Rectangle14', 'Rectangle15', 'Rectangle16']:
    stage1 = suppress_part(stage1, p)

# Suppress slot cutouts from patch
for p in ['Rectangle6', 'Rectangle7', 'Rectangle8']:
    stage1 = suppress_part(stage1, p)

stage1 = clear_solutions(stage1)

# Save
stage1_file = os.path.join(OUTPUT_DIR, 'Stage1_Bare_Patch.hfss')
with open(stage1_file, 'w', encoding='latin-1') as f:
    f.write(stage1)
print(f"  Saved: {stage1_file}")


# ============================================================
# STAGE 2: Patch + L-Stubs (Ant. II)
# ============================================================
# Add back stubs (Rectangle9-16), keep patch without slot
print("\n=== GENERATING STAGE 2: Patch + L-Stubs ===")
stage2 = original_text

# Suppress parasitic patches
for p in ['Rectangle1', 'Rectangle2', 'Rectangle3', 'Rectangle4']:
    stage2 = suppress_part(stage2, p)

# Suppress slot cutouts from patch
for p in ['Rectangle6', 'Rectangle7', 'Rectangle8']:
    stage2 = suppress_part(stage2, p)

stage2 = clear_solutions(stage2)

stage2_file = os.path.join(OUTPUT_DIR, 'Stage2_Patch_Stubs.hfss')
with open(stage2_file, 'w', encoding='latin-1') as f:
    f.write(stage2)
print(f"  Saved: {stage2_file}")


# ============================================================
# STAGE 3: Patch + L-Stubs + Parasitics (Ant. III)
# ============================================================
# Add back parasitics, still no patch slot
print("\n=== GENERATING STAGE 3: Patch + Stubs + Parasitics ===")
stage3 = original_text

# Suppress slot cutouts from patch only
for p in ['Rectangle6', 'Rectangle7', 'Rectangle8']:
    stage3 = suppress_part(stage3, p)

stage3 = clear_solutions(stage3)

stage3_file = os.path.join(OUTPUT_DIR, 'Stage3_Patch_Stubs_Parasitics.hfss')
with open(stage3_file, 'w', encoding='latin-1') as f:
    f.write(stage3)
print(f"  Saved: {stage3_file}")


# ============================================================
# STAGE 4: Full Design at Original Frequency (Ant. IV)
# ============================================================
# Everything enabled (this IS the v15 original, just with cleared solutions)
print("\n=== GENERATING STAGE 4: Full Design (original freq) ===")
stage4 = clear_solutions(original_text)

stage4_file = os.path.join(OUTPUT_DIR, 'Stage4_Full_Original_Freq.hfss')
with open(stage4_file, 'w', encoding='latin-1') as f:
    f.write(stage4)
print(f"  Saved: {stage4_file}")


# ============================================================
# STAGE 5: Full Design TUNED to 3.05 GHz
# ============================================================
print("\n=== GENERATING STAGE 5: Full Design Tuned to 3.05 GHz ===")
stage5 = original_text

# --- Scale Main Patch (Rectangle5) ---
# Original: XStart=13.8, YStart=14.1, Width=32.5 (l8), Height=31.4 (l7)
# Center: X=13.8+32.5/2=30.05, Y=14.1+31.4/2=29.8
l8_new = round(32.5 * K, 1)  # 37.3
l7_new = round(31.4 * K, 1)  # 36.0
x_center = 30.05
y_center = 29.8
xs_new = round(x_center - l8_new/2, 2)  # 11.4
ys_new = round(y_center - l7_new/2, 2)  # 11.8

stage5 = replace_param_near_id(stage5, op_ids['Rectangle5'], 'XStart', f'{xs_new}mm')
stage5 = replace_param_near_id(stage5, op_ids['Rectangle5'], 'YStart', f'{ys_new}mm')
stage5 = replace_param_near_id(stage5, op_ids['Rectangle5'], 'Width', f'{l8_new}mm')
stage5 = replace_param_near_id(stage5, op_ids['Rectangle5'], 'Height', f'{l7_new}mm')
print(f"  Patch: ({xs_new}, {ys_new}) W={l8_new} H={l7_new}")

# --- Scale Patch Slot (Rectangle8) ---
# Original: XStart=17.3, YStart=21.8, Width=25 (ls), Height=1 (ws)
# Center: X=17.3+25/2=29.8, Y=21.8+1/2=22.3
ls_new = round(25 * K, 1)  # 28.7
ws_new = round(1 * K, 1)   # 1.1
xs_slot = round(29.8 - ls_new/2, 2)
ys_slot = round(22.3 - ws_new/2, 2)

stage5 = replace_param_near_id(stage5, op_ids['Rectangle8'], 'XStart', f'{xs_slot}mm')
stage5 = replace_param_near_id(stage5, op_ids['Rectangle8'], 'YStart', f'{ys_slot}mm')
stage5 = replace_param_near_id(stage5, op_ids['Rectangle8'], 'Width', f'{ls_new}mm')
stage5 = replace_param_near_id(stage5, op_ids['Rectangle8'], 'Height', f'{ws_new}mm')
print(f"  Slot: ({xs_slot}, {ys_slot}) W={ls_new} H={ws_new}")

# --- Scale Slot Cutouts (Rectangle6, Rectangle7) ---
# Rectangle6: (13.8, 14.1) W=0.8 H=10 -> scale H
r6_h = round(10 * K, 1)
stage5 = replace_param_near_id(stage5, op_ids['Rectangle6'], 'XStart', f'{xs_new}mm')
stage5 = replace_param_near_id(stage5, op_ids['Rectangle6'], 'YStart', f'{ys_new}mm')
stage5 = replace_param_near_id(stage5, op_ids['Rectangle6'], 'Height', f'{r6_h}mm')
# Rectangle7: (45.5, 14.1) W=0.8 H=10 -> scale H, adjust X
r7_xs = round(xs_new + l8_new - 0.8, 2)
stage5 = replace_param_near_id(stage5, op_ids['Rectangle7'], 'XStart', f'{r7_xs}mm')
stage5 = replace_param_near_id(stage5, op_ids['Rectangle7'], 'YStart', f'{ys_new}mm')
stage5 = replace_param_near_id(stage5, op_ids['Rectangle7'], 'Height', f'{r6_h}mm')
print(f"  Slot cutouts scaled to H={r6_h}")

# --- Scale Stub B ---
# Rectangle9 (horiz arm): (15, 7.8) W=35 H=4 -> l4=23.5->27.0, w4=1.5->1.7
# Rectangle11 (vert arm): (48.5, 7.8) W=1.5 H=23.5 -> l3=35->40.2
# Rectangle13 (vert arm2): (10, 26.3) W=3 H=25 -> scale
l4_new = round(23.5 * K, 1)  # 27.0
l3_new = round(35 * K, 1)    # 40.2

# Stub B horizontal arm
r9_w = round(l4_new, 1)
r9_xs = round(xs_new + l8_new - l4_new - 2.6*K, 1)  # adjust d3 offset
stage5 = replace_param_near_id(stage5, op_ids['Rectangle9'], 'Width', f'{r9_w}mm')

# Stub B vertical arm (Rectangle11)
r11_h = round(l3_new, 1)
stage5 = replace_param_near_id(stage5, op_ids['Rectangle11'], 'Height', f'{r11_h}mm')

# --- Scale Stub A ---
# Rectangle14 (horiz arm): (10, 48.3) W=31 H=3 -> l5=25->28.7
l5_new = round(25 * K, 1)  # 28.7
l6_new = round(31 * K, 1)  # 35.6

# Rectangle13 (vert arm): (10, 26.3) W=3 H=25 -> l6=31->35.6
r13_h = round(l6_new, 1)
stage5 = replace_param_near_id(stage5, op_ids['Rectangle13'], 'Height', f'{r13_h}mm')

# Rectangle14 horizontal arm
r14_w = round(l5_new, 1)
stage5 = replace_param_near_id(stage5, op_ids['Rectangle14'], 'Width', f'{r14_w}mm')
print(f"  Stub A: l5={l5_new}, l6={r13_h}")
print(f"  Stub B: l4={r9_w}, l3={r11_h}")

# --- Scale y-Parasitic Patches ---
# Rectangle1: (0, 4) W=5.8 H=38.8 -> l1=39->44.8, w1=5.8 (keep)
l1_new = round(39 * K, 1)  # 44.8
stage5 = replace_param_near_id(stage5, op_ids['Rectangle1'], 'Height', f'{l1_new}mm')
# Rectangle2: (54.2, 17.2) same scaling
stage5 = replace_param_near_id(stage5, op_ids['Rectangle2'], 'Height', f'{l1_new}mm')
# Adjust YStart for Rectangle2 to keep it within board
r2_ys = round(60 - l1_new - 4, 1)
stage5 = replace_param_near_id(stage5, op_ids['Rectangle2'], 'YStart', f'{r2_ys}mm')
print(f"  y-Parasitics: l1={l1_new}")

# --- Scale x-Parasitic Patches ---
# Rectangle3: (18.5, 0) W=39 H=5.8 -> l2=38.8->44.5
l2_new = round(38.8 * K, 1)  # 44.5
stage5 = replace_param_near_id(stage5, op_ids['Rectangle3'], 'Width', f'{l2_new}mm')
# Adjust XStart to center
r3_xs = round(30 - l2_new/2, 1)
stage5 = replace_param_near_id(stage5, op_ids['Rectangle3'], 'XStart', f'{r3_xs}mm')
# Rectangle4: (2.5, 54.2) W=39 H=5.8
stage5 = replace_param_near_id(stage5, op_ids['Rectangle4'], 'Width', f'{l2_new}mm')
r4_xs = round(30 - l2_new/2, 1)
stage5 = replace_param_near_id(stage5, op_ids['Rectangle4'], 'XStart', f'{r4_xs}mm')
print(f"  x-Parasitics: l2={l2_new}")

# --- Scale U-Slot ---
# feedline9 (lc3 arm): (35.5, 20.75, 1) W=2.5 H=19
lc2_new = round(19 * K, 1)  # 21.8
lc3_new = round(25 * K, 1)  # 28.7
lc1_new = round(10 * K, 1)  # 11.5

# feedline9: vertical arm lc3
stage5 = replace_param_near_id(stage5, op_ids['feedline9'], 'Height', f'{lc2_new}mm')
# Adjust YStart to keep U-slot centered on feed
r9_ys = round(30 - lc2_new/2, 2)
stage5 = replace_param_near_id(stage5, op_ids['feedline9'], 'YStart', f'{r9_ys}mm')

# feedline10 (horizontal bar): W=10 -> lc1
stage5 = replace_param_near_id(stage5, op_ids['feedline10'], 'Width', f'{lc1_new}mm')
# Adjust XStart
r10_xs = round(35.5 + 2.5 - lc1_new, 1)  # keep right edge aligned
stage5 = replace_param_near_id(stage5, op_ids['feedline10'], 'XStart', f'{r10_xs}mm')

# feedline11 (long arm): W=25 -> lc3
stage5 = replace_param_near_id(stage5, op_ids['feedline11'], 'Width', f'{lc3_new}mm')
# Adjust XStart
r11_xs = round(38 - lc3_new, 1)  # keep right edge at x=38
stage5 = replace_param_near_id(stage5, op_ids['feedline11'], 'XStart', f'{r11_xs}mm')

print(f"  U-Slot: lc1={lc1_new}, lc2={lc2_new}, lc3={lc3_new}")

# --- Update Analysis Setup frequency ---
stage5 = stage5.replace("Frequency='3GHz'", "Frequency='3.05GHz'")

stage5 = clear_solutions(stage5)

stage5_file = os.path.join(OUTPUT_DIR, 'Stage5_Full_3_05GHz.hfss')
with open(stage5_file, 'w', encoding='latin-1') as f:
    f.write(stage5)
print(f"  Saved: {stage5_file}")


# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*60)
print("ALL 5 FILES GENERATED SUCCESSFULLY!")
print("="*60)
print(f"\n  1. {os.path.join(OUTPUT_DIR, 'Stage1_Bare_Patch.hfss')}")
print(f"  2. {os.path.join(OUTPUT_DIR, 'Stage2_Patch_Stubs.hfss')}")
print(f"  3. {os.path.join(OUTPUT_DIR, 'Stage3_Patch_Stubs_Parasitics.hfss')}")
print(f"  4. {os.path.join(OUTPUT_DIR, 'Stage4_Full_Original_Freq.hfss')}")
print(f"  5. {os.path.join(OUTPUT_DIR, 'Stage5_Full_3_05GHz.hfss')}")
print("\nOpen each in HFSS and run Setup1 -> Analyze to see results.")
print("Compare S11 and Axial Ratio plots across stages.")
