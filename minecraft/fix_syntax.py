import re

file_path = 'c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/kubejs/server_scripts/00_recipe_error_suppressor.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace '{'id': 'create:andesite_alloy'}' with 'create:andesite_alloy'
content = content.replace("'{'id': '", "'")
content = content.replace("'}'", "'")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed syntax errors.')
