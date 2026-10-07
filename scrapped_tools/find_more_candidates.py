import json
import sys
sys.path.append('.')
from scrapped_tools.audit_curated_excluded import EXCLUDED_FILENAMES

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\audit_all_447.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find all mods not in EXCLUDED_FILENAMES with no data and no server mixins
candidates = []
for fn, info in sorted(data.items()):
    if fn in EXCLUDED_FILENAMES:
        continue
    if not info['has_data'] and info['mixins_server'] == 0:
        candidates.append((fn, info))

print(f"Total candidates with no data and no server mixins: {len(candidates)}")
for fn, info in candidates:
    print(f"{fn} | id: {info['mod_id']} | name: {info['name']} | c_mixins: {info['mixins_client']}, com_mixins: {info['mixins_common']}, pkts: {info['packet_classes']}")
