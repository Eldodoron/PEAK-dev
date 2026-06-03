import os

scripts_dir = 'c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/kubejs/server_scripts/'

# Fix 00_recipe_error_suppressor.js
path = os.path.join(scripts_dir, '00_recipe_error_suppressor.js')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace("Fluid.of('#c:crude_oil'", "Fluid.of('createdieselgenerators:crude_oil'")
text = text.replace("Fluid.of('#c:plantoil'", "Fluid.of('createdieselgenerators:plant_oil'")
text = text.replace("Fluid.of('#c:ethanol'", "Fluid.of('createdieselgenerators:ethanol'")
with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

# Fix 20_fixed_datapacks.js
path = os.path.join(scripts_dir, '20_fixed_datapacks.js')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace("Fluid.of('c:molten_netherite'", "Fluid.of('createmetalwork:molten_netherite'")
with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixed fluids!')
