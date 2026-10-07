import os
import zipfile
import tomllib
import json
import sys
sys.path.append('.')
from scrapped_tools.audit_curated_excluded import EXCLUDED_FILENAMES

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"
all_files = sorted([f for f in os.listdir(mods_dir) if f.endswith('.jar') or '.jar.' in f])

# Add the two missed mods to excluded
full_excluded = set(EXCLUDED_FILENAMES.keys())
full_excluded.add('Loot Beams Refork-neoforge-1.21.1-3.4.7.jar')
full_excluded.add('Nirvana Lib-neoforge-1.21.1-2.2.0.jar')

remaining = [f for f in all_files if f not in full_excluded]
print(f"Remaining mods to thoroughly scrutinize: {len(remaining)}")

# For each remaining mod, let's inspect:
# 1. Does it have any server-side classes?
# 2. Does it have any client-only classes (net/minecraft/client) called in main class?
# 3. Does it have Mixins targeting net/minecraft/client only?

suspicious = []
for fn in remaining:
    p = os.path.join(mods_dir, fn)
    with zipfile.ZipFile(p, 'r') as z:
        names = z.namelist()
        classes = [n for n in names if n.endswith('.class')]
        has_data = any(n.startswith('data/') for n in names)
        
        # Check if there is any mixin
        mixin_files = [n for n in names if n.endswith('.mixins.json') or (n.endswith('.json') and 'mixin' in n and not n.startswith('assets/'))]
        targets = []
        for mf in mixin_files:
            try:
                mdata = json.loads(z.read(mf).decode('utf-8', errors='ignore'))
                if isinstance(mdata, dict):
                    pkg = mdata.get('package', '')
                    for m in mdata.get('mixins', []) + mdata.get('client', []):
                        targets.append(f"{pkg}.{m}")
            except:
                pass
                
        # If all mixins contain 'client', 'gui', 'render', 'hud', 'screen'
        if targets:
            all_client_targets = True
            for t in targets:
                t_low = t.lower()
                if not any(k in t_low for k in ['client', 'gui', 'render', 'hud', 'screen', 'tooltip']):
                    all_client_targets = False
            if all_client_targets and not has_data:
                suspicious.append((fn, 'all_mixins_client_like', targets))

print(f"\nSuspicious mods found: {len(suspicious)}")
for fn, reason, details in suspicious:
    print(f"  {fn} ({reason}): {details[:3]}")
