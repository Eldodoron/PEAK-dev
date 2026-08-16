import re

files = [
    '07_draconic_endgame.js', '10_avaritia_final_polish.js', 
    '13a_food_overhaul_farmersdelight.js', '12_food_buffs.js', 
    '13d_food_overhaul_magic.js', '13b_food_overhaul_dimensions.js', 
    '21_backpack_upgrades.js'
]

missing_items = set()

with open('c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/logs/latest.log', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if any(script in line for script in files) and ('ERROR' in line or 'Failed' in line):
            m1 = re.search(r'Unknown registry key in ResourceKey\[.*?(item|fluid)\]: ([a-zA-Z0-9_:-]+)', line)
            if m1:
                missing_items.add(m1.group(2))
            
            m2 = re.search(r'Failed to read ([a-zA-Z0-9_:-]+) \(left', line)
            if m2:
                missing_items.add(m2.group(1))

            m3 = re.search(r'No key tag in MapLike\[\{"item":"(.*?)"\}\]', line)
            if m3:
                missing_items.add(m3.group(1))

print('Missing Items/Fluids identified:')
for item in missing_items:
    print(item)
