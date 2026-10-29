import re

with open('minecraft/kubejs/server_scripts/67_allthemodium_expansion.js', 'r', encoding='utf-8') as f:
    text = f.read()

items = re.findall(r"['\"]([a-z0-9_]+:[a-z0-9_]+)['\"]", text)

with open('minecraft/ct_dumps/item.txt', 'r', encoding='utf-8') as f:
    item_dump = set(line.strip() for line in f)

with open('minecraft/ct_dumps/fluid.txt', 'r', encoding='utf-8') as f:
    fluid_dump = set(line.strip() for line in f)

missing = []
for it in set(items):
    item_str = f'<item:{it}>'
    fluid_str = f'<fluid:{it}>'
    if item_str not in item_dump and fluid_str not in fluid_dump:
        missing.append(it)

if missing:
    print('WARNING: Missing IDs in dump:', missing)
else:
    print(f'VERIFIED: All {len(set(items))} item and fluid IDs in 67_allthemodium_expansion.js are 100% valid registry entries!')
