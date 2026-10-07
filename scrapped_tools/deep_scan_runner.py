import os
import zipfile
import json
import re

MODS_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"

def inspect_jar_classes(z):
    names = z.namelist()
    class_names = [n for n in names if n.endswith('.class')]
    
    # Check for client vs server references or registration
    client_refs = 0
    server_refs = 0
    network_refs = 0
    command_refs = 0
    
    for cn in class_names[:100]: # Sample up to 100 classes
        try:
            content = z.read(cn)
            if b'net/minecraft/client/' in content:
                client_refs += 1
            if b'net/minecraft/server/' in content:
                server_refs += 1
            if b'net/minecraft/network/' in content:
                network_refs += 1
            if b'net/minecraft/commands/' in content:
                command_refs += 1
        except:
            pass
            
    return {
        'total_classes': len(class_names),
        'client_refs': client_refs,
        'server_refs': server_refs,
        'network_refs': network_refs,
        'command_refs': command_refs
    }

def run_deep_scan():
    files = sorted(os.listdir(MODS_DIR))
    jar_files = [f for f in files if f.endswith('.jar') or '.jar.' in f]
    
    results = {}
    
    for f in jar_files:
        path = os.path.join(MODS_DIR, f)
        if not os.path.isfile(path):
            continue
        try:
            with zipfile.ZipFile(path, 'r') as z:
                names = z.namelist()
                has_data = any(x.startswith('data/') for x in names)
                data_dirs = set()
                if has_data:
                    for x in names:
                        if x.startswith('data/'):
                            parts = x.split('/')
                            if len(parts) > 2:
                                data_dirs.add(parts[2])
                
                # Check manifests
                mod_id = None
                display_name = None
                display_test = None
                dep_side = None
                env = None
                desc = None
                
                if 'META-INF/neoforge.mods.toml' in names:
                    raw = z.read('META-INF/neoforge.mods.toml').decode('utf-8', errors='ignore')
                    # search displayTest
                    m_dt = re.search(r'displayTest\s*=\s*["\']([^"\']+)["\']', raw)
                    if m_dt:
                        display_test = m_dt.group(1)
                    m_id = re.search(r'modId\s*=\s*["\']([^"\']+)["\']', raw)
                    if m_id:
                        mod_id = m_id.group(1)
                    m_dn = re.search(r'displayName\s*=\s*["\']([^"\']+)["\']', raw)
                    if m_dn:
                        display_name = m_dn.group(1)
                    m_desc = re.search(r'description\s*=\s*[\'"]{1,3}([\s\S]*?)[\'"]{1,3}', raw)
                    if m_desc:
                        desc = m_desc.group(1).strip()
                    m_side = re.search(r'side\s*=\s*["\']([^"\']+)["\']', raw)
                    if m_side:
                        dep_side = m_side.group(1)
                elif 'META-INF/mods.toml' in names:
                    raw = z.read('META-INF/mods.toml').decode('utf-8', errors='ignore')
                    m_dt = re.search(r'displayTest\s*=\s*["\']([^"\']+)["\']', raw)
                    if m_dt:
                        display_test = m_dt.group(1)
                    m_id = re.search(r'modId\s*=\s*["\']([^"\']+)["\']', raw)
                    if m_id:
                        mod_id = m_id.group(1)
                    m_dn = re.search(r'displayName\s*=\s*["\']([^"\']+)["\']', raw)
                    if m_dn:
                        display_name = m_dn.group(1)
                    m_desc = re.search(r'description\s*=\s*[\'"]{1,3}([\s\S]*?)[\'"]{1,3}', raw)
                    if m_desc:
                        desc = m_desc.group(1).strip()
                    m_side = re.search(r'side\s*=\s*["\']([^"\']+)["\']', raw)
                    if m_side:
                        dep_side = m_side.group(1)
                
                if 'fabric.mod.json' in names:
                    try:
                        fj = json.loads(z.read('fabric.mod.json').decode('utf-8', errors='ignore'))
                        mod_id = mod_id or fj.get('id')
                        display_name = display_name or fj.get('name')
                        env = fj.get('environment')
                        desc = desc or fj.get('description')
                    except:
                        pass
                
                # Check mixin configs
                mixins = [x for x in names if x.endswith('.mixins.json') or x.endswith('mixin.json')]
                mixin_details = []
                for m in mixins:
                    try:
                        md = json.loads(z.read(m).decode('utf-8', errors='ignore'))
                        mixin_details.append({
                            'name': m,
                            'client': len(md.get('client', [])),
                            'server': len(md.get('server', [])),
                            'common': len(md.get('mixins', []))
                        })
                    except:
                        pass
                
                results[f] = {
                    'filename': f,
                    'mod_id': mod_id,
                    'display_name': display_name,
                    'display_test': display_test,
                    'dep_side': dep_side,
                    'env': env,
                    'has_data': has_data,
                    'data_dirs': sorted(list(data_dirs)),
                    'mixins': mixin_details,
                    'desc': (desc[:150] if desc else '')
                }
        except Exception as e:
            results[f] = {'filename': f, 'error': str(e)}
            
    with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\deep_scan.json', 'w', encoding='utf-8') as out:
        json.dump(results, out, indent=2)
    print(f"Deep scan finished for {len(results)} jars.")

if __name__ == '__main__':
    run_deep_scan()
