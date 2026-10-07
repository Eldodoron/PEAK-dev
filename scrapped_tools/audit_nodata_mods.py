import os
import zipfile
import tomllib
import json
import sys
sys.path.append('.')
from scrapped_tools.audit_curated_excluded import EXCLUDED_FILENAMES

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"
all_files = sorted([f for f in os.listdir(mods_dir) if f.endswith('.jar') or '.jar.' in f])

nodata_included = []

for fn in all_files:
    if fn in EXCLUDED_FILENAMES:
        continue
    p = os.path.join(mods_dir, fn)
    with zipfile.ZipFile(p, 'r') as z:
        names = z.namelist()
        has_data = any(n.startswith('data/') for n in names)
        if not has_data:
            # Let's inspect what this mod has
            classes = [n for n in names if n.endswith('.class')]
            client_classes = [n for n in classes if 'client' in n.lower() or 'render' in n.lower() or 'gui' in n.lower()]
            mixins = [n for n in names if n.endswith('.mixins.json') or (n.endswith('.json') and 'mixin' in n and not n.startswith('assets/'))]
            
            # Check toml display name and description
            dname = None
            desc = None
            for t in ['META-INF/neoforge.mods.toml', 'META-INF/mods.toml']:
                if t in names:
                    try:
                        td = tomllib.loads(z.read(t).decode('utf-8', errors='ignore'))
                        mods = td.get('mods', [])
                        if mods:
                            dname = mods[0].get('displayName')
                            desc = mods[0].get('description')
                    except:
                        pass
            if 'fabric.mod.json' in names:
                try:
                    fd = json.loads(z.read('fabric.mod.json').decode('utf-8', errors='ignore'))
                    dname = dname or fd.get('name')
                    desc = desc or fd.get('description')
                except:
                    pass
                    
            nodata_included.append({
                'filename': fn,
                'name': dname,
                'desc': (desc or '')[:100].replace('\n', ' '),
                'classes_count': len(classes),
                'client_classes_count': len(client_classes),
                'mixins': mixins
            })

print(f"Total mods without data/ currently included: {len(nodata_included)}")
for item in nodata_included:
    ratio = f"{item['client_classes_count']}/{item['classes_count']}"
    print(f"  {item['filename']} | {item['name']} | classes: {ratio} | mixins: {len(item['mixins'])} | desc: {item['desc']}")
