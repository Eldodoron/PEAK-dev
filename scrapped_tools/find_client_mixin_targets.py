import os
import zipfile
import json
import re

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"
all_files = sorted([f for f in os.listdir(mods_dir) if f.endswith('.jar') or '.jar.' in f])

import sys
sys.path.append('.')
from scrapped_tools.audit_curated_excluded import EXCLUDED_FILENAMES

known_excluded = set(EXCLUDED_FILENAMES.keys())
known_excluded.add('Loot Beams Refork-neoforge-1.21.1-3.4.7.jar')
known_excluded.add('Nirvana Lib-neoforge-1.21.1-2.2.0.jar')
known_excluded.add('apothiccombat-1.2.1.jar')

# Scan all remaining mods for mixins targeting client classes
client_targeting_mods = []

for fn in all_files:
    if fn in known_excluded:
        continue
    p = os.path.join(mods_dir, fn)
    with zipfile.ZipFile(p, 'r') as z:
        names = z.namelist()
        has_data = any(n.startswith('data/') for n in names)
        
        # Read mixin classes and look for targets
        mixin_classes = [n for n in names if 'mixin' in n.lower() and n.endswith('.class')]
        if not mixin_classes:
            continue
            
        all_targets = set()
        for mc in mixin_classes:
            try:
                raw = z.read(mc)
                # search for strings resembling class names (L...;)
                # Or regex for Minecraft / mod class targets
                found = re.findall(b'L(net/minecraft/[a-zA-Z0-9/_$]+);', raw)
                for f in found:
                    all_targets.add(f.decode('utf-8', errors='ignore'))
                found_bc = re.findall(b'L(net/bettercombat/[a-zA-Z0-9/_$]+);', raw)
                for f in found_bc:
                    all_targets.add(f.decode('utf-8', errors='ignore'))
            except:
                pass
                
        # If all detected targets are client classes
        if all_targets:
            client_targets = [t for t in all_targets if '/client/' in t]
            non_client_targets = [t for t in all_targets if '/client/' not in t]
            if len(client_targets) > 0 and len(non_client_targets) == 0 and not has_data:
                client_targeting_mods.append((fn, client_targets))

print(f"Found {len(client_targeting_mods)} mods with ONLY client targets and NO data/:")
for fn, targets in client_targeting_mods:
    print(f"  {fn} -> {targets[:5]}")
