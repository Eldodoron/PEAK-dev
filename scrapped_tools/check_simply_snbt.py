import re
import zipfile
import json
import os

simply_jars = [
    ('simplyswords', 'simplyswords-neoforge-1.70.2-1.21.1.jar'),
    ('simplybows', 'SimplyBows-neoforge-0.1.4-1.21.1.jar'),
    ('simplymore', 'simplymore-neoforge-1.3.0_alpha5+1.21.1.jar'),
    ('integrated_simply_swords', 'integrated_simply_swords-1.4.0+1.21.1-neoforge.jar'),
    ('simplycataclysm', 'simplycataclysm-1.0.2+1.21.1+neoforge.jar')
]

all_registered = set()

for modid, jar in simply_jars:
    p = os.path.join('minecraft/mods', jar)
    if not os.path.exists(p):
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
                        all_registered.add(f'{modid}:{name}')
                    elif k.startswith(f'block.{modid}.'):
                        name = k[len(f'block.{modid}.'):].replace('.', '/')
                        all_registered.add(f'{modid}:{name}')
            except:
                pass
    # Check models/items
    for n in z.namelist():
        if '/models/item/' in n and n.endswith('.json'):
            mod = n.split('/')[1]
            it = os.path.basename(n)[:-5]
            all_registered.add(f'{mod}:{it}')
        elif '/items/' in n and n.endswith('.json'):
            mod = n.split('/')[1]
            it = os.path.basename(n)[:-5]
            all_registered.add(f'{mod}:{it}')
        elif '/models/block/' in n and n.endswith('.json'):
            mod = n.split('/')[1]
            it = os.path.basename(n)[:-5]
            all_registered.add(f'{mod}:{it}')

# Add Java registered items that might lack a direct model json
for extra in ['exedrill', 'mimicry', 'molten_flare', 'soul_foreseer']:
    all_registered.add(f'simplymore:{extra}')

chapters = ['simply_swords.snbt', 'simply_forge.snbt', 'simply_crossmod.snbt', 'simply_bows.snbt', 'simply_more.snbt']

for c in chapters:
    fp = f'minecraft/config/ftbquests/quests/chapters/{c}'
    with open(fp, 'r', encoding='utf-8') as f:
        t = f.read()
    items = re.findall(r'"((?:simply[a-z_]+|integrated_simply_swords):[a-zA-Z0-9_\/]+)"', t)
    unique_items = set(items)
    missing = [i for i in unique_items if i not in all_registered]
    print(f'Chapter: {c} | Total items: {len(items)} | Unique: {len(unique_items)}')
    if missing:
        print(f'  --> MISSING in {c}: {missing}')
    else:
        print(f'  --> All items VALID!')

# Check reward tables as well
rewards = [
    'peak_supplies_simply_common.snbt',
    'peak_supplies_simply_rare.snbt',
    'peak_supplies_simply_mythic.snbt'
]
for r in rewards:
    fp = f'minecraft/config/ftbquests/quests/reward_tables/{r}'
    with open(fp, 'r', encoding='utf-8') as f:
        t = f.read()
    items = re.findall(r'"((?:simply[a-z_]+|integrated_simply_swords):[a-zA-Z0-9_\/]+)"', t)
    unique_items = set(items)
    missing = [i for i in unique_items if i not in all_registered]
    print(f'Reward Table: {r} | Total items: {len(items)} | Unique: {len(unique_items)}')
    if missing:
        print(f'  --> MISSING in {r}: {missing}')
    else:
        print(f'  --> All items VALID!')
