import os
import re
import zipfile
import json

simply_jars = [
    ('simplyswords', 'simplyswords-neoforge-1.70.2-1.21.1.jar'),
    ('simplybows', 'SimplyBows-neoforge-0.1.4-1.21.1.jar'),
    ('simplymore', 'simplymore-neoforge-1.3.0_alpha5+1.21.1.jar'),
    ('integrated_simply_swords', 'integrated_simply_swords-1.4.0+1.21.1-neoforge.jar'),
    ('simplycataclysm', 'simplycataclysm-1.0.2+1.21.1+neoforge.jar')
]

registered_items = set()

# Inspect JAR registries directly
for modid, jar in simply_jars:
    p = os.path.join('minecraft/mods', jar)
    if not os.path.exists(p):
        print(f"WARNING: Jar {jar} not found!")
        continue
    z = zipfile.ZipFile(p)
    # Check language file
    for lang_name in [f'assets/{modid}/lang/en_us.json', f'assets/{modid}/lang/en_US.json']:
        if lang_name in z.namelist():
            try:
                lang = json.loads(z.read(lang_name).decode('utf-8'))
                for k in lang:
                    if k.startswith(f'item.{modid}.'):
                        name = k[len(f'item.{modid}.'):].replace('.', '/')
                        registered_items.add(f'{modid}:{name}')
                    elif k.startswith(f'block.{modid}.'):
                        name = k[len(f'block.{modid}.'):].replace('.', '/')
                        registered_items.add(f'{modid}:{name}')
            except Exception as e:
                print(f'Lang error in {jar}: {e}')
    # Check models and assets
    for n in z.namelist():
        if n.startswith(f'assets/{modid}/models/item/') and n.endswith('.json'):
            sub = n[len(f'assets/{modid}/models/item/'):-5]
            registered_items.add(f'{modid}:{sub}')
        elif n.startswith(f'assets/{modid}/items/') and n.endswith('.json'):
            sub = n[len(f'assets/{modid}/items/'):-5]
            registered_items.add(f'{modid}:{sub}')
        elif n.startswith(f'assets/{modid}/models/block/') and n.endswith('.json'):
            sub = n[len(f'assets/{modid}/models/block/'):-5]
            registered_items.add(f'{modid}:{sub}')

print(f'Total known registered items across simply mods: {len(registered_items)}')

# Scan FTB Quests
quest_dirs = [
    'minecraft/config/ftbquests/quests/chapters',
    'minecraft/config/ftbquests/quests/reward_tables'
]

referenced_items = {}
pattern = re.compile(r'"((?:simplyswords|simplybows|simplymore|integrated_simply_swords|simplycataclysm):[a-zA-Z0-9_\/]+)"')

for qd in quest_dirs:
    for f in os.listdir(qd):
        if f.endswith('.snbt'):
            fp = os.path.join(qd, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as s:
                content = s.read()
                matches = pattern.findall(content)
                for m in matches:
                    if m not in referenced_items:
                        referenced_items[m] = []
                    referenced_items[m].append(f)

print(f'Total unique Simply items referenced in quests: {len(referenced_items)}')

broken = []
for item_id, files in sorted(referenced_items.items()):
    if item_id not in registered_items:
        broken.append((item_id, set(files)))

if broken:
    print(f'\nFOUND {len(broken)} POTENTIALLY BROKEN ITEM IDs:')
    for item_id, files in broken:
        print(f'- {item_id} in {files}')
else:
    print('\nALL Simply item IDs referenced in FTB Quests are 100% VALID!')
