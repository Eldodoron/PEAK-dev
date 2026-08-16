import os
import re
import json
import shutil

log_files = [
    "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/errors.txt",
    "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/errors2.txt"
]

pack_dir = "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/global_packs/required_data/recipe_error_fixer"
data_dir = os.path.join(pack_dir, "data")
broken_script = "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/kubejs/server_scripts/01_high_priority_data_override.js"

# 1. Clean up KubeJS broken script
if os.path.exists(broken_script):
    os.remove(broken_script)

# 2. Setup datapack directory
if os.path.exists(pack_dir):
    shutil.rmtree(pack_dir)
os.makedirs(pack_dir, exist_ok=True)

# 3. Write pack.mcmeta (pack_format 48 is for 1.21.1)
with open(os.path.join(pack_dir, "pack.mcmeta"), 'w') as f:
    json.dump({
        "pack": {
            "pack_format": 48,
            "description": "Fixes broken mod recipes and loot tables by overriding them with valid dummies"
        }
    }, f, indent=2)

dummy_recipe = {
  "type": "minecraft:crafting_shapeless",
  "category": "misc",
  "ingredients": [{"item": "minecraft:barrier"}],
  "result": {"id": "minecraft:barrier", "count": 1}
}

dummy_loot_table = {
  "type": "minecraft:empty"
}

dummy_predicate = {
  "condition": "minecraft:inverted",
  "term": {
    "condition": "minecraft:killed_by_player"
  }
}

broken_paths = set()
for log_file in log_files:
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            for line in f:
                m1 = re.search(r"Parsing error loading recipe ([a-z0-9_.-]+):([a-z0-9_./-]+)", line)
                if m1:
                    broken_paths.add((m1.group(1), "recipe", m1.group(2)))
                    continue
                    
                m2 = re.search(r"Couldn't parse element ResourceKey\[minecraft:root / minecraft:(loot_table|predicate)\]:([a-z0-9_.-]+):([a-z0-9_./-]+)", line)
                if m2:
                    broken_paths.add((m2.group(2), m2.group(1), m2.group(3)))
                    continue
                    
                m3 = re.search(r"Failed to parse recipe '([^']+)'", line)
                if m3:
                    full_id = m3.group(1).split('[')[0]
                    if ':' in full_id:
                        modid, path = full_id.split(':', 1)
                        broken_paths.add((modid, "recipe", path))
                    continue
    except Exception as e:
        print(f"Error reading {log_file}: {e}")

# 4. Generate the files in the global datapack
for modid, dtype, path in broken_paths:
    target = os.path.join(data_dir, modid, dtype, f"{path}.json")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, 'w') as out:
        if dtype == "recipe":
            json.dump(dummy_recipe, out, indent=2)
        elif dtype == "loot_table":
            json.dump(dummy_loot_table, out, indent=2)
        else:
            json.dump(dummy_predicate, out, indent=2)

print(f"Generated physical datapack with {len(broken_paths)} override JSONs at {pack_dir}.")
