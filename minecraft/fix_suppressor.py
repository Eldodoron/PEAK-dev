import os

scripts_dir = 'c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/kubejs/server_scripts/'
path = os.path.join(scripts_dir, '00_recipe_error_suppressor.js')
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(len(lines)):
    if "{'id': '" in lines[i]:
        lines[i] = lines[i].replace("{'id': '", "")
with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Fixed id syntax in suppressor script!')
