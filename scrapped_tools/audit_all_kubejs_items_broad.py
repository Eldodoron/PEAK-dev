import os
import re
import zipfile
import json

all_valid_items = set()
if os.path.exists('minecraft/ct_dumps/item.txt'):
    with open('minecraft/ct_dumps/item.txt', 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if line:
                m = re.search(r'<item:([^>]+)>', line)
                if m:
                    all_valid_items.add(m.group(1))
                else:
                    all_valid_items.add(line)

mods_dir = 'minecraft/mods'
for jar in os.listdir(mods_dir):
    if jar.endswith('.jar'):
        jp = os.path.join(mods_dir, jar)
        try:
            with zipfile.ZipFile(jp) as z:
                for name in z.namelist():
                    if ('/models/item/' in name or '/items/' in name) and name.endswith('.json'):
                        parts = name.split('/')
                        modid = parts[1]
                        item_name = os.path.basename(name)[:-5]
                        all_valid_items.add(f'{modid}:{item_name}')
                    elif 'lang/en_us.json' in name:
                        try:
                            lang = json.loads(z.read(name).decode('utf-8'))
                            for k in lang:
                                if k.startswith('item.') or k.startswith('block.'):
                                    parts = k.split('.', 2)
                                    if len(parts) >= 3:
                                        all_valid_items.add(f'{parts[1]}:{parts[2].replace(".", "/")}')
                        except:
                            pass
        except:
            pass

vanilla_items = {'minecraft:air', 'minecraft:stone', 'minecraft:iron_ingot', 'minecraft:diamond', 'minecraft:gold_ingot'}
all_valid_items.update(vanilla_items)

for extra in ['exedrill', 'mimicry', 'molten_flare', 'soul_foreseer']:
    all_valid_items.add(f'simplymore:{extra}')

kubejs_dir = 'minecraft/kubejs'
found_issues = {}

ignored_namespaces = {
    'minecraft', 'forge', 'c', 'neoforge', 'tag', 'apothic_enchanting', 'curios',
    'kubejs', 'levelz', 'puffish_skills', 'item', 'block', 'entity', 'fluid',
    'dimension', 'biome', 'structure', 'sound', 'enchantment', 'effect', 'attribute'
}

for root, dirs, files in os.walk(kubejs_dir):
    for f in files:
        if f.endswith('.js'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as sfile:
                content = sfile.read()
            
            matches = re.findall(r'[\'"]([a-z0-9_\-\.]+:[a-z0-9_\-\.\/]+)[\'"]', content)
            for m in matches:
                if m.startswith('#') or m.startswith('http') or m.startswith('minecraft:'):
                    continue
                modid = m.split(':')[0]
                if modid in ignored_namespaces:
                    continue
                if any(m.startswith(prefix) for prefix in [
                    'iceandfire:chest', 'betterdeserttemples:chests', 'tlc:chests',
                    'cataclysm:chest', 'dungeons_arise:chest'
                ]):
                    continue
                # If modid is an actual mod, let's see if the item is known
                if m not in all_valid_items:
                    found_issues.setdefault(f, []).append(m)

print('\n=== AUDIT RESULTS ACROSS ALL MODS IN KUBEJS ===')
for f, items in sorted(found_issues.items()):
    unique_items = sorted(set(items))
    print(f'{f}:')
    for it in unique_items:
        print(f'  - {it}')
