import os
import zipfile
import tomllib
import json
import re

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"
all_files = sorted([f for f in os.listdir(mods_dir) if f.endswith('.jar') or '.jar.' in f])

results = {}

for fn in all_files:
    p = os.path.join(mods_dir, fn)
    with zipfile.ZipFile(p, 'r') as z:
        names = z.namelist()
        
        has_data = any(n.startswith('data/') for n in names)
        has_assets = any(n.startswith('assets/') for n in names)
        
        # Manifests
        mod_id = None
        display_name = None
        display_test = None
        environment = None
        deps = []
        for t in ['META-INF/neoforge.mods.toml', 'META-INF/mods.toml']:
            if t in names:
                try:
                    data = tomllib.loads(z.read(t).decode('utf-8', errors='ignore'))
                    display_test = data.get('displayTest')
                    mods = data.get('mods', [])
                    if mods and isinstance(mods, list):
                        mod_id = mods[0].get('modId')
                        display_name = mods[0].get('displayName')
                        environment = mods[0].get('environment')
                        if not display_test:
                            display_test = mods[0].get('displayTest')
                    dep_dict = data.get('dependencies', {})
                    for mk, dl in dep_dict.items():
                        if isinstance(dl, list):
                            for d in dl:
                                deps.append({
                                    'modId': d.get('modId'),
                                    'side': d.get('side'),
                                    'type': d.get('type')
                                })
                except:
                    pass
        if 'fabric.mod.json' in names:
            try:
                fj = json.loads(z.read('fabric.mod.json').decode('utf-8', errors='ignore'))
                mod_id = mod_id or fj.get('id')
                display_name = display_name or fj.get('name')
                environment = environment or fj.get('environment')
            except:
                pass
                
        # Mixins
        mixin_configs = [n for n in names if n.endswith('.mixins.json') or (n.endswith('.json') and 'mixin' in n and not n.startswith('assets/'))]
        mixins_client = []
        mixins_server = []
        mixins_common = []
        for mc in mixin_configs:
            try:
                mdata = json.loads(z.read(mc).decode('utf-8', errors='ignore'))
                if isinstance(mdata, dict):
                    pkg = mdata.get('package', '')
                    for c in mdata.get('client', []):
                        mixins_client.append(f"{pkg}.{c}")
                    for s in mdata.get('server', []):
                        mixins_server.append(f"{pkg}.{s}")
                    for com in mdata.get('mixins', []):
                        mixins_common.append(f"{pkg}.{com}")
            except:
                pass
                
        # Packets
        packet_classes = [n for n in names if ('packet' in n.lower() or 'payload' in n.lower() or 'network' in n.lower()) and n.endswith('.class')]
        
        # Client vs server classes count
        classes = [n for n in names if n.endswith('.class')]
        client_classes = [n for n in classes if 'client' in n.lower() or 'render' in n.lower() or 'gui' in n.lower() or 'screen' in n.lower()]
        
        results[fn] = {
            'filename': fn,
            'mod_id': mod_id,
            'name': display_name,
            'display_test': display_test,
            'environment': environment,
            'deps': deps,
            'has_data': has_data,
            'has_assets': has_assets,
            'total_classes': len(classes),
            'client_classes': len(client_classes),
            'mixins_client': len(mixins_client),
            'mixins_server': len(mixins_server),
            'mixins_common': len(mixins_common),
            'packet_classes': len(packet_classes)
        }

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\audit_all_447.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

print(f"Audited {len(results)} files. Written to scrapped_tools/audit_all_447.json")
