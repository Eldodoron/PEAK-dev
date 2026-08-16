import os
import re
import json

log_file = "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/errors2.txt"
data_dir = "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/kubejs/data"

dummy_recipe = {
  "type": "minecraft:crafting_shapeless",
  "category": "misc",
  "ingredients": [{"item": "minecraft:barrier"}],
  "result": {"id": "minecraft:barrier", "count": 1}
}

dummy_loot_table = {
  "type": "minecraft:empty"
}

# A simple valid predicate condition
dummy_predicate = {
  "condition": "minecraft:inverted",
  "term": {
    "condition": "minecraft:killed_by_player"
  }
}

count = 0
with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        # Pattern 1: RecipeManager parsing error
        m1 = re.search(r"Parsing error loading recipe ([a-z0-9_.-]+:[a-z0-9_./-]+):", line)
        if m1:
            modid, path = m1.group(1).split(':', 1)
            target = os.path.join(data_dir, modid, "recipe", f"{path}.json")
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, 'w') as out: json.dump(dummy_recipe, out, indent=2)
            count += 1
            continue
            
        # Pattern 2: LootDataType (Loot Table or Predicate)
        m2 = re.search(r"Couldn't parse element ResourceKey\[minecraft:root / minecraft:(loot_table|predicate)\]:([a-z0-9_.-]+:[a-z0-9_./-]+)", line)
        if m2:
            dtype = m2.group(1)
            modid, path = m2.group(2).split(':', 1)
            target = os.path.join(data_dir, modid, dtype, f"{path}.json")
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, 'w') as out:
                if dtype == "loot_table":
                    json.dump(dummy_loot_table, out, indent=2)
                else:
                    json.dump(dummy_predicate, out, indent=2)
            count += 1
            continue

print(f"Generated {count} dummy files from RecipeManager/LootDataType.")
