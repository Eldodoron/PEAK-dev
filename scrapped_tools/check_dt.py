import json

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\exact_toml_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for fn, m in sorted(data.items()):
    dt = m.get('display_test')
    if dt and dt != 'MATCH_VERSION':
        print(f"{fn} | dt={dt} | mc_side={m.get('mc_dep_side')}")
