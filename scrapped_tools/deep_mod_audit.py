import os
import zipfile
import re
import json

MODS_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"

def parse_toml(content):
    res = {}
    current_section = None
    mods = []
    current_mod = {}
    dependencies = []
    current_dep = {}
    
    for raw_line in content.splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('[[mods]]'):
            if current_mod:
                mods.append(current_mod)
            current_mod = {}
            current_section = 'mods'
            continue
        elif line.startswith('[[dependencies.'):
            if current_dep:
                dependencies.append(current_dep)
            dep_key = line.split('.')[1].rstrip(']').strip()
            current_dep = {'target': dep_key}
            current_section = 'dependency'
            continue
        elif line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1].strip()
            continue
        
        if '=' in line:
            parts = line.split('=', 1)
            key = parts[0].strip()
            val = parts[1].split('#')[0].strip().strip('"').strip("'")
            if current_section == 'mods':
                current_mod[key] = val
            elif current_section == 'dependency':
                current_dep[key] = val
            elif current_section is None:
                res[key] = val
            else:
                if current_section not in res:
                    res[current_section] = {}
                if isinstance(res[current_section], dict):
                    res[current_section][key] = val
    if current_mod:
        mods.append(current_mod)
    if current_dep:
        dependencies.append(current_dep)
    res['mods'] = mods
    res['dependencies'] = dependencies
    return res

def analyze_all():
    results = []
    files = sorted(os.listdir(MODS_DIR))
    
    for f in files:
        if not (f.endswith('.jar') or '.jar.' in f):
            continue
        path = os.path.join(MODS_DIR, f)
        if not os.path.isfile(path):
            continue
            
        entry = {
            'filename': f,
            'is_disabled': f.endswith('.disabled'),
            'is_backup': f.endswith('.backup') or f.endswith('.modified'),
            'mod_id': None,
            'name': None,
            'display_test': None,
            'client_side_only': False,
            'environment': None,
            'mixins': [],
            'has_data': False,
            'data_types': [],
            'dependencies': [],
            'description': '',
            'has_client_mixins_only': False,
            'classes_count': 0
        }
        
        try:
            with zipfile.ZipFile(path, 'r') as z:
                names = z.namelist()
                entry['classes_count'] = len([n for n in names if n.endswith('.class')])
                
                # Check data/
                data_files = [n for n in names if n.startswith('data/')]
                if data_files:
                    entry['has_data'] = True
                    types = set()
                    for df in data_files:
                        parts = df.split('/')
                        if len(parts) > 2:
                            types.add(parts[2])
                    entry['data_types'] = sorted(list(types))
                
                # Check mixins
                mixin_files = [n for n in names if n.endswith('.mixins.json') or n.endswith('mixin.json')]
                has_server_or_common_mixins = False
                has_client_mixins = False
                for mf in mixin_files:
                    try:
                        m_data = json.loads(z.read(mf).decode('utf-8', errors='ignore'))
                        mix_info = {'file': mf}
                        if 'mixins' in m_data and m_data['mixins']:
                            mix_info['mixins'] = len(m_data['mixins'])
                            has_server_or_common_mixins = True
                        if 'client' in m_data and m_data['client']:
                            mix_info['client'] = len(m_data['client'])
                            has_client_mixins = True
                        if 'server' in m_data and m_data['server']:
                            mix_info['server'] = len(m_data['server'])
                            has_server_or_common_mixins = True
                        entry['mixins'].append(mix_info)
                    except:
                        pass
                
                if has_client_mixins and not has_server_or_common_mixins:
                    entry['has_client_mixins_only'] = True
                
                # Check manifests
                if 'META-INF/neoforge.mods.toml' in names:
                    raw = z.read('META-INF/neoforge.mods.toml').decode('utf-8', errors='ignore')
                    p = parse_toml(raw)
                    if p.get('mods'):
                        entry['mod_id'] = p['mods'][0].get('modId')
                        entry['name'] = p['mods'][0].get('displayName')
                        entry['display_test'] = p['mods'][0].get('displayTest')
                        entry['description'] = p['mods'][0].get('description', '')
                    entry['dependencies'] = p.get('dependencies', [])
                elif 'META-INF/mods.toml' in names:
                    raw = z.read('META-INF/mods.toml').decode('utf-8', errors='ignore')
                    p = parse_toml(raw)
                    if p.get('mods'):
                        entry['mod_id'] = p['mods'][0].get('modId')
                        entry['name'] = p['mods'][0].get('displayName')
                        entry['display_test'] = p['mods'][0].get('displayTest')
                        entry['description'] = p['mods'][0].get('description', '')
                    entry['dependencies'] = p.get('dependencies', [])
                    
                if 'fabric.mod.json' in names:
                    try:
                        f_data = json.loads(z.read('fabric.mod.json').decode('utf-8', errors='ignore'))
                        entry['mod_id'] = entry['mod_id'] or f_data.get('id')
                        entry['name'] = entry['name'] or f_data.get('name')
                        entry['environment'] = f_data.get('environment')
                        if not entry['description']:
                            entry['description'] = str(f_data.get('description', ''))
                    except:
                        pass
                        
        except Exception as e:
            entry['error'] = str(e)
            
        results.append(entry)
        
    with open(r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\deep_audit.json", 'w', encoding='utf-8') as out:
        json.dump(results, out, indent=2)
    print(f"Deep audit complete for {len(results)} mods.")

if __name__ == '__main__':
    analyze_all()
