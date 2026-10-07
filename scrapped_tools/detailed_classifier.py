import os
import zipfile
import re
import json

MODS_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"

def parse_full_toml(content):
    # Split content by sections
    sections = []
    current_header = ""
    current_lines = []
    for line in content.splitlines():
        line_clean = line.strip()
        if line_clean.startswith('[') and line_clean.endswith(']'):
            if current_lines or current_header:
                sections.append((current_header, current_lines))
            current_header = line_clean
            current_lines = []
        else:
            current_lines.append(line)
    if current_lines or current_header:
        sections.append((current_header, current_lines))
        
    mods = []
    deps = []
    
    for header, lines in sections:
        header_clean = header.strip('[]').strip()
        data = {}
        for l in lines:
            l_strip = l.strip()
            if not l_strip or l_strip.startswith('#'):
                continue
            if '=' in l_strip:
                k, v = l_strip.split('=', 1)
                k = k.strip()
                v = v.split('#')[0].strip().strip('"').strip("'")
                data[k] = v
        if header_clean == 'mods':
            mods.append(data)
        elif header_clean.startswith('dependencies.'):
            data['_target'] = header_clean.split('.', 1)[1]
            deps.append(data)
            
    return mods, deps

def analyze_mod(filepath):
    fn = os.path.basename(filepath)
    info = {
        'filename': fn,
        'is_disabled': fn.endswith('.disabled'),
        'is_backup': fn.endswith('.backup') or fn.endswith('.modified'),
        'mod_id': None,
        'display_name': None,
        'description': '',
        'display_test': None,
        'mc_dep_side': None,
        'neoforge_dep_side': None,
        'fabric_env': None,
        'mixins': [],
        'client_mixins_count': 0,
        'server_mixins_count': 0,
        'common_mixins_count': 0,
        'has_data': False,
        'data_dirs': [],
        'has_assets': False,
        'class_count': 0,
        'client_class_refs': 0,
        'server_class_refs': 0
    }
    
    with zipfile.ZipFile(filepath, 'r') as z:
        namelist = z.namelist()
        info['class_count'] = len([x for x in namelist if x.endswith('.class')])
        
        # Data
        data_files = [x for x in namelist if x.startswith('data/')]
        if data_files:
            info['has_data'] = True
            subdirs = set()
            for df in data_files:
                parts = df.split('/')
                if len(parts) > 2:
                    subdirs.add(parts[2])
            info['data_dirs'] = sorted(list(subdirs))
            
        info['has_assets'] = any(x.startswith('assets/') for x in namelist)
        
        # Manifests
        manifest_text = None
        if 'META-INF/neoforge.mods.toml' in namelist:
            manifest_text = z.read('META-INF/neoforge.mods.toml').decode('utf-8', errors='ignore')
        elif 'META-INF/mods.toml' in namelist:
            manifest_text = z.read('META-INF/mods.toml').decode('utf-8', errors='ignore')
            
        if manifest_text:
            mods, deps = parse_full_toml(manifest_text)
            if mods:
                info['mod_id'] = mods[0].get('modId')
                info['display_name'] = mods[0].get('displayName')
                info['display_test'] = mods[0].get('displayTest')
                info['description'] = mods[0].get('description', '')
            for d in deps:
                target_mod = d.get('modId')
                side = d.get('side')
                if target_mod == 'minecraft':
                    info['mc_dep_side'] = side
                elif target_mod == 'neoforge':
                    info['neoforge_dep_side'] = side
                    
        if 'fabric.mod.json' in namelist:
            try:
                fj = json.loads(z.read('fabric.mod.json').decode('utf-8', errors='ignore'))
                info['mod_id'] = info['mod_id'] or fj.get('id')
                info['display_name'] = info['display_name'] or fj.get('name')
                info['fabric_env'] = fj.get('environment')
                if not info['description']:
                    info['description'] = str(fj.get('description', ''))
            except:
                pass
                
        # Mixins
        mixin_files = [x for x in namelist if x.endswith('.mixins.json') or x.endswith('mixin.json')]
        for mf in mixin_files:
            try:
                mdata = json.loads(z.read(mf).decode('utf-8', errors='ignore'))
                c_cnt = len(mdata.get('client', []))
                s_cnt = len(mdata.get('server', []))
                m_cnt = len(mdata.get('mixins', []))
                info['client_mixins_count'] += c_cnt
                info['server_mixins_count'] += s_cnt
                info['common_mixins_count'] += m_cnt
                info['mixins'].append({
                    'file': mf,
                    'client': c_cnt,
                    'server': s_cnt,
                    'common': m_cnt
                })
            except:
                pass
                
    return info

def run():
    all_info = {}
    for f in sorted(os.listdir(MODS_DIR)):
        if not (f.endswith('.jar') or '.jar.' in f):
            continue
        p = os.path.join(MODS_DIR, f)
        if os.path.isfile(p):
            try:
                all_info[f] = analyze_mod(p)
            except Exception as e:
                all_info[f] = {'filename': f, 'error': str(e)}
                
    with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\precise_mod_info.json', 'w', encoding='utf-8') as out:
        json.dump(all_info, out, indent=2)
    print(f"Precise analysis complete for {len(all_info)} mods.")

if __name__ == '__main__':
    run()
