import os
import json
import zipfile
import re

minecraft_dir = r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft"
mods_dir = os.path.join(minecraft_dir, "mods")

# Search all mod jars for recipes that produce molten_copper, molten_zinc, molten_brass, or brass_ingot
melting_recipes = []

for mod_file in os.listdir(mods_dir):
    if not mod_file.endswith('.jar'):
        continue
    jar_path = os.path.join(mods_dir, mod_file)
    try:
        with zipfile.ZipFile(jar_path, 'r') as z:
            for filename in z.namelist():
                if 'recipes/' in filename and filename.endswith('.json'):
                    try:
                        content = z.read(filename).decode('utf-8', errors='ignore')
                        if any(k in content for k in ['molten_copper', 'molten_zinc', 'molten_brass', 'brass_ingot', 'brass_nugget']):
                            melting_recipes.append({
                                'mod': mod_file,
                                'file': filename,
                                'content': json.loads(content)
                            })
                    except:
                        pass
    except:
        pass

out_file = r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\scrapped_tools\brass_melting_recipes.json"
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(melting_recipes, f, indent=2)

print(f"Found {len(melting_recipes)} recipes related to brass/copper/zinc melting across all mod JARs.")
