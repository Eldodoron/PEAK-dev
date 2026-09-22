import os
import re

ct_items = set()
with open('minecraft/ct_dumps/item.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            # CraftTweaker items might look like <item:minecraft:dirt> or minecraft:dirt
            m = re.search(r'<item:([^>]+)>', line)
            if m:
                ct_items.add(m.group(1))
            else:
                ct_items.add(line)

print(f'Loaded {len(ct_items)} items from CraftTweaker dump')

with open('minecraft/kubejs/server_scripts/22_apotheosis_gear_sets.js', 'r', encoding='utf-8') as f:
    c = f.read()

items = re.findall(r'"id":\s*"([^"]+)"', c)
print(f'Found {len(items)} item IDs in 22_apotheosis_gear_sets.js')

for item in set(items):
    if item not in ct_items:
        print(f'  UNKNOWN ITEM in 22_apotheosis_gear_sets.js: {item}')
