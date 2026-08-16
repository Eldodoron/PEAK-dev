import os
import re

scripts_dir = 'c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/kubejs/server_scripts/'

# Fix 13b_food_overhaul_dimensions.js
path = os.path.join(scripts_dir, '13b_food_overhaul_dimensions.js')
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in [718, 719, 724, 725]:
    if not lines[i].startswith('//'):
        lines[i] = '// ' + lines[i]
with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

# Fix expert_mode_recipes.js
path = os.path.join(scripts_dir, 'expert_mode_recipes.js')
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in [248, 249, 254, 255]:
    if not lines[i].startswith('//'):
        lines[i] = '// ' + lines[i]
with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

# Fix 00_recipe_error_suppressor.js
path = os.path.join(scripts_dir, '00_recipe_error_suppressor.js')
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(len(lines)):
    if "{'id':" in lines[i]:
        lines[i] = re.sub(r"'(\d+x) \{'id': '(.*?)'\}", r"'\1 \2'", lines[i])
        
with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

# Fix 20_fixed_datapacks.js (molten tags)
path = os.path.join(scripts_dir, '20_fixed_datapacks.js')
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("Fluid.of('c:molten_andesite_alloy'", "Fluid.of('createmetalwork:molten_andesite_alloy'")
    lines[i] = lines[i].replace("Fluid.of('c:molten_brass'", "Fluid.of('createmetalwork:molten_brass'")
    lines[i] = lines[i].replace("Fluid.of('c:molten_copper'", "Fluid.of('createmetalwork:molten_copper'")
    lines[i] = lines[i].replace("Fluid.of('c:molten_gold'", "Fluid.of('createmetalwork:molten_gold'")
    lines[i] = lines[i].replace("Fluid.of('c:molten_iron'", "Fluid.of('createmetalwork:molten_iron'")
    lines[i] = lines[i].replace("Fluid.of('c:molten_zinc'", "Fluid.of('createmetalwork:molten_zinc'")
with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Syntax errors fixed!')
