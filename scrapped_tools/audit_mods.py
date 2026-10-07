import os
import zipfile
import re
import json

MODS_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"

def parse_toml_simple(content):
    res = {}
    current_section = None
    mods = []
    current_mod = {}
    
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('[[mods]]'):
            if current_mod:
                mods.append(current_mod)
            current_mod = {}
            current_section = 'mods'
            continue
        elif line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1].strip()
            continue
        
        if '=' in line:
            parts = line.split('=', 1)
            key = parts[0].strip()
            val = parts[1].strip().strip('"').strip("'")
            if current_section == 'mods':
                current_mod[key] = val
            elif current_section is None:
                res[key] = val
            else:
                if current_section not in res:
                    res[current_section] = {}
                if isinstance(res[current_section], dict):
                    res[current_section][key] = val
    if current_mod:
        mods.append(current_mod)
    res['mods'] = mods
    return res

def scan_mods():
    entries = []
    files = sorted(os.listdir(MODS_DIR))
    print(f"Total files in mods dir: {len(files)}")
    
    for f in files:
        if not (f.endswith('.jar') or '.jar.' in f):
            continue
        path = os.path.join(MODS_DIR, f)
        if not os.path.isfile(path):
            continue
        
        info = {
            'filename': f,
            'is_disabled': f.endswith('.disabled'),
            'is_backup': f.endswith('.backup') or f.endswith('.modified'),
            'mod_id': None,
            'name': None,
            'display_test': None,
            'side': None,
            'environment': None,
            'has_data': False,
            'has_assets': False,
            'data_dirs': [],
            'has_neoforge_toml': False,
            'has_forge_toml': False,
            'has_fabric_json': False,
            'description': None,
            'file_list_sample': []
        }
        
        try:
            with zipfile.ZipFile(path, 'r') as z:
                namelist = z.namelist()
                data_files = [x for x in namelist if x.startswith('data/')]
                info['has_data'] = len(data_files) > 0
                if info['has_data']:
                    subdirs = set()
                    for df in data_files:
                        parts = df.split('/')
                        if len(parts) > 2:
                            subdirs.add(parts[2])
                    info['data_dirs'] = sorted(list(subdirs))
                
                info['has_assets'] = any(x.startswith('assets/') for x in namelist)
                
                if 'META-INF/neoforge.mods.toml' in namelist:
                    info['has_neoforge_toml'] = True
                    try:
                        content = z.read('META-INF/neoforge.mods.toml').decode('utf-8', errors='ignore')
                        parsed = parse_toml_simple(content)
                        if parsed.get('mods'):
                            m = parsed['mods'][0]
                            info['mod_id'] = m.get('modId')
                            info['name'] = m.get('displayName')
                            info['display_test'] = m.get('displayTest')
                            info['side'] = m.get('side')
                            info['description'] = m.get('description', '')[:100]
                    except Exception as e:
                        pass
                elif 'META-INF/mods.toml' in namelist:
                    info['has_forge_toml'] = True
                    try:
                        content = z.read('META-INF/mods.toml').decode('utf-8', errors='ignore')
                        parsed = parse_toml_simple(content)
                        if parsed.get('mods'):
                            m = parsed['mods'][0]
                            info['mod_id'] = m.get('modId')
                            info['name'] = m.get('displayName')
                            info['display_test'] = m.get('displayTest')
                            info['side'] = m.get('side')
                            info['description'] = m.get('description', '')[:100]
                    except Exception as e:
                        pass
                
                if 'fabric.mod.json' in namelist:
                    info['has_fabric_json'] = True
                    try:
                        content = z.read('fabric.mod.json').decode('utf-8', errors='ignore')
                        f_json = json.loads(content)
                        info['mod_id'] = info['mod_id'] or f_json.get('id')
                        info['name'] = info['name'] or f_json.get('name')
                        info['environment'] = f_json.get('environment')
                        if not info['description']:
                            info['description'] = str(f_json.get('description', ''))[:100]
                    except Exception as e:
                        pass
                        
        except Exception as e:
            info['error'] = str(e)
            
        entries.append(info)
        
    with open(r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\mods_audit_data.json", 'w', encoding='utf-8') as out:
        json.dump(entries, out, indent=2)
    print(f"Scanned {len(entries)} mods. Output written to mods_audit_data.json.")

if __name__ == '__main__':
    scan_mods()
