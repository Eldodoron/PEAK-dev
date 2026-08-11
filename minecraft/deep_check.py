import os
import zipfile
import tomllib
import json

mods_dir = r'C:\Users\wamb9\Desktop\Server_Mods_PEAK'

suspect_keywords = [
    'client', 'visual', 'hud', 'gui ', 'menu', 'tooltip', 'render', 'animation',
    'sound', 'particle', 'shader', 'bloom', 'lighting', 'camera', 'minimap',
    'map', 'crosshair', 'keybind', 'music', 'texture', 'model', 'physics', 'ragdoll'
]

results = []

for filename in os.listdir(mods_dir):
    if not filename.endswith('.jar'):
        continue
    filepath = os.path.join(mods_dir, filename)
    
    mod_info = {'file': filename, 'name': 'Unknown', 'desc': '', 'is_suspect': False, 'suspect_reasons': []}
    
    try:
        with zipfile.ZipFile(filepath, 'r') as z:
            toml_path = None
            if 'META-INF/neoforge.mods.toml' in z.namelist():
                toml_path = 'META-INF/neoforge.mods.toml'
            elif 'META-INF/mods.toml' in z.namelist():
                toml_path = 'META-INF/mods.toml'
                
            if toml_path:
                with z.open(toml_path) as f:
                    try:
                        data = tomllib.load(f)
                        if 'mods' in data and len(data['mods']) > 0:
                            mod = data['mods'][0]
                            mod_info['name'] = mod.get('displayName', filename)
                            mod_info['desc'] = mod.get('description', '').lower()
                            
                            # Check description
                            for kw in suspect_keywords:
                                if kw in mod_info['desc']:
                                    mod_info['is_suspect'] = True
                                    mod_info['suspect_reasons'].append(kw)
                            
                            # Check name
                            name_lower = mod_info['name'].lower()
                            for kw in suspect_keywords:
                                if kw in name_lower:
                                    mod_info['is_suspect'] = True
                                    mod_info['suspect_reasons'].append(kw + ' (in name)')
                                    
                    except Exception as e:
                        pass
    except Exception as e:
        pass

    if mod_info['is_suspect']:
        results.append(mod_info)

with open('suspect_mods.txt', 'w', encoding='utf-8') as out:
    for r in results:
        reasons = set(r['suspect_reasons'])
        out.write(f"File: {r['file']}\nName: {r['name']}\nReasons: {', '.join(reasons)}\nDesc Snippet: {r['desc'][:100]}...\n-------------------\n")

print(f"Found {len(results)} suspect mods. Saved to suspect_mods.txt")
