import os
import re

file_path = 'c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/kubejs/server_scripts/20_fixed_datapacks.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix base: {'id': ...} to base: {'item': ...}
content = re.sub(r'"base":\s*\{"id":', '"base": {"item":', content)
content = re.sub(r'"template":\s*\{"id":', '"template": {"item":', content)
content = re.sub(r'"result":\s*\{"count":\s*1,\s*"id":', '"result": {"id":', content)

# Fix Fluid.of('#...') to Fluid.of('...')
content = re.sub(r'Fluid\.of\([\'"]#(.*?)([\'"])', r"Fluid.of('\1'", content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
