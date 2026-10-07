import os
import zipfile
import tomllib
import json

MODS_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"

results = {}

for f in sorted(os.listdir(MODS_DIR)):
    if not (f.endswith('.jar') or '.jar.' in f):
        continue
    p = os.path.join(MODS_DIR, f)
    if not os.path.isfile(p):
        continue
        
    info = {
        'filename': f,
        'mod_id': None,
        'display_name': None,
        'display_test': None,
        'description': '',
        'mc_dep_side': None,
        'neoforge_dep_side': None,
        'all_deps': [],
        'has_toml': False,
        'has_fabric': False,
        'fabric_env': None
    }
    
    with zipfile.ZipFile(p, 'r') as z:
        names = z.namelist()
        toml_content = None
        if 'META-INF/neoforge.mods.toml' in names:
            toml_content = z.read('META-INF/neoforge.mods.toml').decode('utf-8', errors='ignore')
        elif 'META-INF/mods.toml' in names:
            toml_content = z.read('META-INF/mods.toml').decode('utf-8', errors='ignore')
            
        if toml_content:
            info['has_toml'] = True
            try:
                data = tomllib.loads(toml_content)
                mods = data.get('mods', [])
                if mods and isinstance(mods, list):
                    info['mod_id'] = mods[0].get('modId')
                    info['display_name'] = mods[0].get('displayName')
                    info['display_test'] = mods[0].get('displayTest')
                    info['description'] = mods[0].get('description', '')
                    
                deps_dict = data.get('dependencies', {})
                # dependencies is usually a dict of modId -> list of dep dicts
                for mod_key, dep_list in deps_dict.items():
                    if isinstance(dep_list, list):
                        for dep in dep_list:
                            dep_id = dep.get('modId')
                            dep_side = dep.get('side')
                            info['all_deps'].append({'target': dep_id, 'side': dep_side, 'type': dep.get('type')})
                            if dep_id == 'minecraft':
                                info['mc_dep_side'] = dep_side
                            elif dep_id == 'neoforge':
                                info['neoforge_dep_side'] = dep_side
            except Exception as e:
                info['toml_error'] = str(e)
                
        if 'fabric.mod.json' in names:
            info['has_fabric'] = True
            try:
                fj = json.loads(z.read('fabric.mod.json').decode('utf-8', errors='ignore'))
                info['mod_id'] = info['mod_id'] or fj.get('id')
                info['display_name'] = info['display_name'] or fj.get('name')
                info['fabric_env'] = fj.get('environment')
                if not info['description']:
                    info['description'] = str(fj.get('description', ''))
            except:
                pass
                
    results[f] = info

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\exact_toml_data.json', 'w', encoding='utf-8') as out:
    json.dump(results, out, indent=2)

print(f"Parsed {len(results)} jars with tomllib.")
