import re
import json

log_files = [
    "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/errors.txt",
    "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/errors2.txt"
]
output_js = "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/kubejs/server_scripts/01_high_priority_data_override.js"

broken_paths = set()

for log_file in log_files:
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Pattern 1: RecipeManager
                m1 = re.search(r"Parsing error loading recipe ([a-z0-9_.-]+):([a-z0-9_./-]+)", line)
                if m1:
                    modid = m1.group(1)
                    path = m1.group(2)
                    broken_paths.add(f"{modid}:recipe/{path}")
                    continue
                    
                # Pattern 2: LootDataType (loot_table, predicate)
                m2 = re.search(r"Couldn't parse element ResourceKey\[minecraft:root / minecraft:(loot_table|predicate)\]:([a-z0-9_.-]+):([a-z0-9_./-]+)", line)
                if m2:
                    dtype = m2.group(1)
                    modid = m2.group(2)
                    path = m2.group(3)
                    broken_paths.add(f"{modid}:{dtype}/{path}")
                    continue
                    
                # Pattern 3: KubeRecipe.java "Failed to parse recipe"
                m3 = re.search(r"Failed to parse recipe '([^']+)'", line)
                if m3:
                    full_id = m3.group(1)
                    if '[' in full_id:
                        full_id = full_id.split('[')[0]
                    if ':' in full_id:
                        modid, path = full_id.split(':', 1)
                        broken_paths.add(f"{modid}:recipe/{path}")
                    continue
    except Exception as e:
        print(f"Error reading {log_file}: {e}")

with open(output_js, 'w', encoding='utf-8') as out:
    out.write("// Archivo generado automáticamente para sobrescribir JSONs rotos de los mods.\n")
    out.write("ServerEvents.highPriorityData(event => {\n")
    
    out.write("    const dummyRecipe = {\n")
    out.write("        type: 'minecraft:crafting_shapeless',\n")
    out.write("        category: 'misc',\n")
    out.write("        ingredients: [{ item: 'minecraft:barrier' }],\n")
    out.write("        result: { id: 'minecraft:barrier', count: 1 }\n")
    out.write("    };\n\n")
    
    out.write("    const dummyLootTable = { type: 'minecraft:empty' };\n\n")
    
    out.write("    const dummyPredicate = {\n")
    out.write("        condition: 'minecraft:inverted',\n")
    out.write("        term: { condition: 'minecraft:killed_by_player' }\n")
    out.write("    };\n\n")
    
    for full_path in sorted(list(broken_paths)):
        if ':recipe/' in full_path:
            out.write(f"    event.addJson('{full_path}', dummyRecipe);\n")
        elif ':loot_table/' in full_path:
            out.write(f"    event.addJson('{full_path}', dummyLootTable);\n")
        elif ':predicate/' in full_path:
            out.write(f"    event.addJson('{full_path}', dummyPredicate);\n")
            
    out.write("});\n")

print(f"Generated KubeJS High Priority Data script with {len(broken_paths)} overrides.")
