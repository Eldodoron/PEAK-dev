import os
import zipfile
import tomllib
import json
import re

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"
all_files = sorted([f for f in os.listdir(mods_dir) if f.endswith('.jar') or '.jar.' in f])

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\audit_curated_excluded.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Load currently excluded list
from scrapped_tools.audit_curated_excluded import EXCLUDED_FILENAMES

print(f"Total jar files to check: {len(all_files)}")
print(f"Currently excluded: {len(EXCLUDED_FILENAMES)}")

# Let's inspect the remaining 375 mods!
remaining = [f for f in all_files if f not in EXCLUDED_FILENAMES]
print(f"Remaining mods to check: {len(remaining)}")

flagged = []

for fn in remaining:
    p = os.path.join(mods_dir, fn)
    info = {
        'filename': fn,
        'reasons': []
    }
    
    with zipfile.ZipFile(p, 'r') as z:
        names = z.namelist()
        
        has_data = any(n.startswith('data/') for n in names)
        has_assets = any(n.startswith('assets/') for n in names)
        
        # Check toml
        display_test = None
        environment = None
        dep_sides = []
        for t in ['META-INF/neoforge.mods.toml', 'META-INF/mods.toml']:
            if t in names:
                try:
                    data = tomllib.loads(z.read(t).decode('utf-8', errors='ignore'))
                    display_test = data.get('displayTest')
                    mods = data.get('mods', [])
                    if mods and isinstance(mods, list):
                        environment = mods[0].get('environment')
                    deps = data.get('dependencies', {})
                    for mk, dl in deps.items():
                        if isinstance(dl, list):
                            for d in dl:
                                if d.get('side') == 'CLIENT':
                                    dep_sides.append(f"{d.get('modId')}:CLIENT")
                except:
                    pass
                    
        # Check fabric
        fabric_env = None
        if 'fabric.mod.json' in names:
            try:
                fj = json.loads(z.read('fabric.mod.json').decode('utf-8', errors='ignore'))
                fabric_env = fj.get('environment')
            except:
                pass
                
        # Check mixins
        mixins_configs = [n for n in names if n.endswith('.mixins.json') or (n.endswith('.json') and 'mixin' in n and not n.startswith('assets/'))]
        all_client_mixins = True
        has_any_mixins = False
        mixin_details = []
        for mc in mixins_configs:
            try:
                mdata = json.loads(z.read(mc).decode('utf-8', errors='ignore'))
                if isinstance(mdata, dict):
                    c = mdata.get('client', [])
                    s = mdata.get('server', [])
                    com = mdata.get('mixins', [])
                    if c or s or com:
                        has_any_mixins = True
                    if s:
                        all_client_mixins = False
                    if com:
                        # Check if package or mixin names imply client
                        pkg = mdata.get('package', '')
                        if not ('client' in pkg.lower()):
                            # check if any common mixin doesn't contain 'client'
                            for cm in com:
                                if 'client' not in cm.lower() and 'gui' not in cm.lower() and 'render' not in cm.lower():
                                    all_client_mixins = False
                    mixin_details.append({'config': mc, 'c': len(c), 's': len(s), 'com': len(com)})
            except:
                pass

        # Check classes for client vs common
        classes = [n for n in names if n.endswith('.class')]
        client_classes = [n for n in classes if 'client' in n.lower() or 'render' in n.lower() or 'gui' in n.lower() or 'screen' in n.lower()]
        
        # Reasons to flag:
        if display_test in ['IGNORE_ALL_VERSION', 'IGNORE_SERVER_VERSION']:
            info['reasons'].append(f"displayTest={display_test}")
        if environment == 'client' or fabric_env == 'client':
            info['reasons'].append(f"env=client (toml:{environment}, fab:{fabric_env})")
        if dep_sides:
            info['reasons'].append(f"deps_client={dep_sides}")
        if has_any_mixins and all_client_mixins and not has_data:
            info['reasons'].append(f"mixins_purely_client (mixins={mixin_details})")
        if not has_data and len(client_classes) > 0 and len(client_classes) == len(classes):
            info['reasons'].append("100% client classes and no data/")

        # Keyword checks in filename
        for kw in ['hud', 'tooltip', 'gui', 'render', 'camera', 'anim', 'visual', 'particle', 'sound', 'chat', 'optic', 'blur', 'menu', 'screen', 'font', 'model']:
            if kw in fn.lower() and not has_data:
                info['reasons'].append(f"keyword '{kw}' in filename and no data/")
                break

    if info['reasons']:
        flagged.append(info)

print(f"\nFound {len(flagged)} potentially client-only mods among remaining {len(remaining)} mods:")
for item in flagged:
    print(f"  {item['filename']}: {', '.join(item['reasons'])}")
