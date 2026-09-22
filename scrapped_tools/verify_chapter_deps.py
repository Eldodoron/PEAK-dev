import re

for filename in ['chapter_boss_magic.snbt', 'culinary_arcane.snbt']:
    filepath = f'minecraft/config/ftbquests/quests/chapters/{filename}'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    defined_ids = set(re.findall(r'id:\s*"([0-9a-fA-F]+)"', content))
    dep_blocks = re.findall(r'dependencies:\s*\[(.*?)\]', content, re.DOTALL)
    broken_deps = []
    for block in dep_blocks:
        deps = re.findall(r'"([0-9a-fA-F]+)"', block)
        for d in deps:
            if d not in defined_ids:
                broken_deps.append(d)
    print(f'{filename}: total quests = {len(defined_ids)}, broken intra-chapter dependencies = {broken_deps}')
