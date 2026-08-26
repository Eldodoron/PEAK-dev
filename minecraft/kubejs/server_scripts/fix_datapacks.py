import os
import zipfile
import json
import glob

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"
kubejs_data = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\kubejs\data"
suppressor = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\kubejs\server_scripts\00_recipe_error_suppressor.js"

# 1. Read broken recipes
broken = []
with open(suppressor, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith("'") and "'," in line:
            recipe_id = line.strip("',")
            broken.append(recipe_id)

def fix_json(obj):
    if isinstance(obj, dict):
        # Fix fluid_stack
        if obj.get("type") == "fluid_stack" or obj.get("type") == "neoforge:single":
            new_obj = {}
            if "fluid" in obj:
                new_obj["fluid"] = obj["fluid"]
            elif "id" in obj:
                new_obj["fluid"] = obj["id"]
            
            if "amount" in obj:
                new_obj["amount"] = obj["amount"]
            return new_obj
        
        # Fix transitionalItem -> transitional_item
        if "transitionalItem" in obj:
            obj["transitional_item"] = obj.pop("transitionalItem")
            
        for k, v in obj.items():
            obj[k] = fix_json(v)
    elif isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = fix_json(obj[i])
    return obj

# 2. Scan all jars
jars = glob.glob(os.path.join(mods_dir, "*.jar"))

extracted_count = 0
for jar in jars:
    try:
        with zipfile.ZipFile(jar, 'r') as z:
            namelist = z.namelist()
            for recipe_id in broken:
                if ":" not in recipe_id: continue
                ns, path = recipe_id.split(":", 1)
                
                # Check for recipes/ or recipe/
                possible_paths = [
                    f"data/{ns}/recipes/{path}.json",
                    f"data/{ns}/recipe/{path}.json"
                ]
                
                for p in possible_paths:
                    if p in namelist:
                        # Extract and fix
                        data = z.read(p)
                        try:
                            json_obj = json.loads(data)
                            fixed_obj = fix_json(json_obj)
                            
                            # Write to kubejs/data
                            out_path = os.path.join(kubejs_data, p.replace("data/", ""))
                            os.makedirs(os.path.dirname(out_path), exist_ok=True)
                            with open(out_path, 'w', encoding='utf-8') as out_f:
                                json.dump(fixed_obj, out_f, indent=2)
                            extracted_count += 1
                            print(f"Fixed {recipe_id} from {os.path.basename(jar)}")
                        except json.JSONDecodeError:
                            print(f"Failed to parse JSON for {p}")
    except Exception as e:
        pass

print(f"Extracted and fixed {extracted_count} datapack recipes!")
