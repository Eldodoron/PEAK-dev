import os
import re
import zipfile
import json

known_items = set()
with open('minecraft/ct_dumps/item.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        line = line.strip()
        if line.startswith('<item:') and line.endswith('>'):
            known_items.add(line[6:-1])

print(f'Known items from ct_dumps: {len(known_items)}')

# Add items from updated jars
for jar in [
    'simplyswords-neoforge-1.70.2-1.21.1.jar',
    'SimplyBows-neoforge-0.1.4-1.21.1.jar',
    'simplymore-neoforge-1.3.0_alpha5+1.21.1.jar',
    'SimplyTooltips-neoforge-0.1.5.jar'
]:
    p = os.path.join('minecraft/mods', jar)
    if os.path.exists(p):
        z = zipfile.ZipFile(p)
        for n in z.namelist():
            if '/models/item/' in n and n.endswith('.json'):
                mod = n.split('/')[1]
                it = os.path.basename(n)[:-5]
                known_items.add(f'{mod}:{it}')
            elif n.endswith('en_us.json'):
                try:
                    d = json.loads(z.read(n).decode('utf-8'))
                    mod = n.split('/')[1]
                    for k in d:
                        if k.startswith(f'item.{mod}.') or k.startswith(f'block.{mod}.'):
                            it = k.split('.', 2)[2].replace('.', '/')
                            known_items.add(f'{mod}:{it}')
                except:
                    pass

print(f'Total known items including new jars: {len(known_items)}')

# Scan all quest chapters & reward tables
quest_dir = 'minecraft/config/ftbquests/quests'
pattern = re.compile(r'id:\s*"([a-zA-Z0-9_\.\-]+:[a-zA-Z0-9_\.\/]+)"')

all_missing = {}
for root, dirs, files in os.walk(quest_dir):
    for f in files:
        if f.endswith('.snbt') and f != 'en_us.snbt':
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as s:
                content = s.read()
                matches = pattern.findall(content)
                for m in matches:
                    if ':' in m:
                        # Exclude non-item types (like entity types, dimensions, or tags if matched)
                        if m.startswith('ftbquests:') or m.startswith('ftbteams:') or m.startswith('minecraft:dimension/'):
                            continue
                        if m not in known_items:
                            if m not in all_missing:
                                all_missing[m] = set()
                            all_missing[m].add(f)

print(f'\nTotal unmatched IDs in quests: {len(all_missing)}')
for item, files in sorted(all_missing.items()):
    print(f'- {item} in {files}')
