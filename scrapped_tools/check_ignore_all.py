import json

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\deep_scan.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total scanned: {len(data)}")

# Let's inspect display_test == 'IGNORE_ALL_VERSION'
ignore_all = [v for v in data.values() if v.get('display_test') in ('IGNORE_ALL_VERSION', 'NONE')]
print(f"Mods with IGNORE_ALL_VERSION or NONE: {len(ignore_all)}")
for v in ignore_all:
    print(f"  {v['filename']} | id: {v.get('mod_id')} | name: {v.get('display_name')} | has_data: {v.get('has_data')}")
