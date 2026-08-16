import os
filepath = r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\kubejs\server_scripts\20_fixed_datapacks.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('"fluid":', '"id":')
content = content.replace('"fluidTag":', '"tag":')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed fluid and fluidTag keys!")
