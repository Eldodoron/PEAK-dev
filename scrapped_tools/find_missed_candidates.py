import json
import sys
sys.path.append('.')
from scrapped_tools.audit_curated_excluded import EXCLUDED_FILENAMES

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\audit_all_447.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total files in data: {len(data)}")
print(f"Prior excluded: {len(EXCLUDED_FILENAMES)}")

# Let's check which files have client-only indicators but are NOT in EXCLUDED_FILENAMES:
candidates_not_excluded = []
for fn, info in data.items():
    if fn in EXCLUDED_FILENAMES:
        continue
    # check conditions
    is_cand = False
    reasons = []
    
    if info['environment'] == 'client':
        is_cand = True
        reasons.append("environment=client")
        
    for d in info['deps']:
        if d.get('modId') in ['minecraft', 'neoforge'] and d.get('side') == 'CLIENT':
            is_cand = True
            reasons.append(f"{d.get('modId')} side=CLIENT")
            
    if info['mixins_client'] > 0 and info['mixins_server'] == 0 and info['mixins_common'] == 0 and not info['has_data']:
        is_cand = True
        reasons.append(f"purely client mixins ({info['mixins_client']}) and no data")

    if info['display_test'] in ['IGNORE_ALL_VERSION', 'IGNORE_SERVER_VERSION', 'NONE'] and not info['has_data'] and info['total_classes'] > 0 and info['client_classes'] == info['total_classes']:
        is_cand = True
        reasons.append(f"display_test={info['display_test']} and 100% client classes")

    if is_cand:
        candidates_not_excluded.append((fn, reasons, info))

print(f"\nCandidates NOT in prior excluded list: {len(candidates_not_excluded)}")
for fn, reasons, info in candidates_not_excluded:
    print(f"  {fn} ({info['name']}): {', '.join(reasons)}")
