import os
import re
import zipfile
import json

# Collect all items registered in jars
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

# Add Java registered items in simplymore
for extra in ['exedrill', 'mimicry', 'molten_flare', 'soul_foreseer']:
    all_registered.add(f'simplymore:{extra}')

print(f'Total known valid Simply items: {len(all_registered)}')

# Check all kubejs files
errors_found = []
for root, dirs, files in os.walk('minecraft/kubejs'):
    for f in files:
        if f.endswith('.js'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fl:
                c = fl.read()
            matches = set(re.findall(r'[\'"]((?:simply[a-z_]+|integrated_simply_swords):[a-zA-Z0-9_\/]+)[\'"]', c))
            for m in matches:
                if m not in all_registered:
                    errors_found.append((f, m))

if errors_found:
    print('Found INVALID Simply IDs in KubeJS:')
    for f, m in errors_found:
        print(f'  [{f}] -> {m}')
else:
    print('All Simply IDs in KubeJS are VALID!')
