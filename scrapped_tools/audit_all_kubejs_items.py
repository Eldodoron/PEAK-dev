import os
import re
import zipfile
import json

# 1. Load ct_dumps
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

print(f'Loaded {len(all_valid_items)} items from CraftTweaker dump')

# 2. Also index items from all installed mod JARs
mods_dir = 'minecraft/mods'
for jar in os.listdir(mods_dir):
    if jar.endswith('.jar'):
        jp = os.path.join(mods_dir, jar)
        try:
            with zipfile.ZipFile(jp) as z:
                # Find modid from neoforge.mods.toml or fabric.mod.json
                for name in z.namelist():
                    if '/models/item/' in name and name.endswith('.json'):
                        parts = name.split('/')
                        modid = parts[1]
                        item_name = os.path.basename(name)[:-5]
                        all_valid_items.add(f'{modid}:{item_name}')
                    elif name.endswith('.json') and '/items/' in name:
                        parts = name.split('/')
                        modid = parts[1]
                        item_name = os.path.basename(name)[:-5]
                        all_valid_items.add(f'{modid}:{item_name}')
                    elif 'lang/en_us.json' in name:
                        try:
                            lang = json.loads(z.read(name).decode('utf-8'))
                            for k in lang:
                                if k.startswith('item.') or k.startswith('block.'):
                                    mod_and_item = k.split('.', 2)
                                    if len(mod_and_item) >= 3:
                                        m_id = mod_and_item[1]
                                        i_id = mod_and_item[2].replace('.', '/')
                                        all_valid_items.add(f'{m_id}:{i_id}')
                        except:
                            pass
        except:
            pass

print(f'Total universe of valid items indexed: {len(all_valid_items)}')

# Add hardcoded vanilla items just in case
vanilla_items = {'minecraft:air', 'minecraft:stone', 'minecraft:iron_ingot', 'minecraft:diamond', 'minecraft:gold_ingot'}
all_valid_items.update(vanilla_items)

# Also add simplymore java registered items
for extra in ['exedrill', 'mimicry', 'molten_flare', 'soul_foreseer']:
    all_valid_items.add(f'simplymore:{extra}')

# 3. Scan all KubeJS scripts
kubejs_dir = 'minecraft/kubejs'
found_issues = {}

for root, dirs, files in os.walk(kubejs_dir):
    for f in files:
        if f.endswith('.js'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as sfile:
                content = sfile.read()
            
            # Find item-like IDs "namespace:path"
            # Exclude tags (starting with #), regexes, URLs, comments
            matches = re.findall(r'[\'"]([a-z0-9_\-\.]+:[a-z0-9_\-\.\/]+)[\'"]', content)
            for m in matches:
                if m.startswith('#') or m.startswith('http') or m.startswith('minecraft:block/') or m.startswith('minecraft:item/'):
                    continue
                # Skip known event or internal namespaces
                if any(m.startswith(prefix) for prefix in [
                    'c:', 'forge:', 'neoforge:', 'tag:', 'apothic_enchanting:gear_sets',
                    'apothic_enchanting:melee', 'apothic_enchanting:ranged', 'apothic_enchanting:overworld',
                    'apothic_enchanting:nether', 'apothic_enchanting:the_end', 'apothic_enchanting:pinnacle',
                    'iceandfire:chest', 'betterdeserttemples:chests', 'tlc:chests'
                ]):
                    continue
                
                # Check if it looks like an item and is unknown
                # Let's filter only modids that are actual item mods
                modid = m.split(':')[0]
                # If modid is simplyswords, simplybows, simplymore, armoroftheages, cataclysm, etc.
                if modid in ['simplyswords', 'simplybows', 'simplymore', 'integrated_simply_swords', 'simplycataclysm', 'armoroftheages']:
                    if m not in all_valid_items:
                        found_issues.setdefault(f, []).append(m)

print('\n=== AUDIT RESULTS FOR SIMPLY & RELATED MODS IN KUBEJS ===')
if found_issues:
    for f, items in found_issues.items():
        print(f'{f}:')
        for it in sorted(set(items)):
            print(f'  - {it}')
else:
    print('ALL Simply & related items in KubeJS are valid!')
