import json

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\candidates.json', 'r', encoding='utf-8') as f:
    candidates = json.load(f)

for c in sorted(candidates, key=lambda x: x['filename'].lower()):
    fn = c['filename']
    mid = c.get('mod_id')
    name = c.get('name')
    reasons = '; '.join(c['reasons'])
    has_data = c['has_data']
    data_dirs = ', '.join(c.get('data_dirs', []))
    print(f"[{fn}] ({mid}) '{name}' | DATA: {has_data} ({data_dirs})")
    print(f"   REASONS: {reasons}")
