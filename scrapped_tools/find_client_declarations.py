import os
import zipfile
import json
import re

MODS_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"

def inspect_all_fabric_and_neoforge():
    results = []
    for f in sorted(os.listdir(MODS_DIR)):
        if not (f.endswith('.jar') or '.jar.' in f):
            continue
        p = os.path.join(MODS_DIR, f)
        if not os.path.isfile(p):
            continue
            
        with zipfile.ZipFile(p, 'r') as z:
            names = z.namelist()
            entry = {'file': f, 'fabric_client_only': False, 'neoforge_client_only': False}
            
            if 'fabric.mod.json' in names:
                try:
                    fj = json.loads(z.read('fabric.mod.json').decode('utf-8', errors='ignore'))
                    if fj.get('environment') == 'client':
                        entry['fabric_client_only'] = True
                    ep = fj.get('entrypoints', {})
                    if 'client' in ep and 'main' not in ep and 'server' not in ep:
                        entry['fabric_entrypoint_client_only'] = True
                except:
                    pass
                    
            if 'META-INF/neoforge.mods.toml' in names:
                try:
                    txt = z.read('META-INF/neoforge.mods.toml').decode('utf-8', errors='ignore')
                    # check if any dependency on minecraft has side="CLIENT"
                    if re.search(r'\[\[dependencies\.[^\]]+\]\][\s\S]*?modId\s*=\s*["\']minecraft["\'][\s\S]*?side\s*=\s*["\']CLIENT["\']', txt):
                        entry['neoforge_client_only'] = True
                except:
                    pass
                    
            results.append(entry)
            
    return results

res = inspect_all_fabric_and_neoforge()
for r in res:
    if r.get('fabric_client_only') or r.get('fabric_entrypoint_client_only') or r.get('neoforge_client_only'):
        print(r)
