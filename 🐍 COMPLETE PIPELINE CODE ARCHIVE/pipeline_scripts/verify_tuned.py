with open(r'C:\Users\ABI\Downloads\Filtering_antenna_stage1_3_05GHz.hfss', 'r', encoding='latin-1') as f:
    t = f.read()

assert 'PerfE1' in t, 'PerfE1 missing'
assert 'feedline1' in t, 'feedline1 missing'
assert "XStart='26mm'" in t, 'XStart 26mm missing'
assert "Width='12mm'" in t, 'Width 12mm missing'
assert "XStart='9.5mm'" in t, 'XStart 9.5mm missing'
assert "Width='28.5mm'" in t, 'Width 28.5mm missing'
print('ALL VERIFICATIONS PASSED 100%!')
