import os
import json
import zipfile

minecraft_dir = r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft"
mods_dir = os.path.join(minecraft_dir, "mods")

recipes = []

for mod_file in os.listdir(mods_dir):
    if not mod_file.endswith('.jar'):
        continue
    jar_path = os.path.join(mods_dir, mod_file)
    try:
        with zipfile.ZipFile(jar_path, 'r') as z:
            for filename in z.namelist():
                if ('/recipe/' in filename or '/recipes/' in filename) and filename.endswith('.json'):
                    try:
                        content = z.read(filename).decode('utf-8', errors='ignore')
                        if any(k in content for k in ['molten_copper', 'molten_zinc', 'molten_brass', 'brass_ingot', 'copper_ingot', 'zinc_ingot']):
                            data = json.loads(content)
                            rtype = data.get('type', '')
                            if 'create:mixing' in rtype or 'create:compacting' in rtype or 'melting' in rtype or 'smeltery' in rtype or 'casting' in rtype:
                                recipes.append({
                                    'mod': mod_file,
                                    'file': filename,
                                    'type': rtype,
                                    'data': data
                                })
                    except:
                        pass
    except:
        pass

print(f"Found {len(recipes)} mixing/compacting/melting recipes matching criteria.")
for r in recipes:
    print(f"\nMOD: {r['mod']} | FILE: {r['file']}")
    print(f"  Type: {r['type']}")
    print(f"  Data: {json.dumps(r['data'], indent=2)}")
