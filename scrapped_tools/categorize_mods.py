import json
import os

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\deep_audit.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

no_data = [x for x in data if not x.get('has_data')]
print(f'Total mods: {len(data)}')
print(f'Mods without data folder: {len(no_data)}')

for x in sorted(no_data, key=lambda k: k['filename'].lower()):
    print(f"{x['filename']} | id: {x.get('mod_id')} | name: {x.get('name')}")
