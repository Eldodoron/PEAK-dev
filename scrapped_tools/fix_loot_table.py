import zipfile
import json
import os

jar_path = 'minecraft/mods/create_structures_overhaul-1.4.0-neoforge-1.21.1.jar'
entry_path = 'data/create_structures_overhaul/loot_table/nether_forpost.json'

with zipfile.ZipFile(jar_path) as z:
    raw = z.read(entry_path).decode('utf-8')

lines = raw.splitlines()
# Line 283 (0-indexed 282) is '                    "weight": 1,'
# Line 284 (0-indexed 283) is '                    ]'
lines[282] = '                    "weight": 1'
del lines[283]

fixed_content = '\n'.join(lines)
data = json.loads(fixed_content)
print(f"Successfully loaded and validated JSON! Pools: {len(data['pools'])}, Entries: {len(data['pools'][0]['entries'])}")

out_dir = os.path.abspath('minecraft/kubejs/data/create_structures_overhaul/loot_table')
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, 'nether_forpost.json')

with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print(f"Wrote sanitized loot table to: {out_file}")
