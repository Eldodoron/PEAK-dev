import zipfile
import json
import os
from collections import defaultdict

# Let's inspect all affixes across Apotheosis, Apothic Compats, and Nadir
mods = ['Apotheosis-1.21.1-8.6.1.jar', 'apothic_compats-0.2.4.2.jar', 'nadir-1.0.0.jar', 'irons_apothic-2.2.1.jar', 'fallen_gems_affixes-1.21.1-1.0.0.jar']

affixes_by_category_rarity_type = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

for mod in mods:
    path = os.path.join('minecraft/mods', mod)
    if not os.path.exists(path): continue
    with zipfile.ZipFile(path) as z:
        for n in z.namelist():
            if 'affixes/' in n and n.endswith('.json'):
                try:
                    data = json.loads(z.read(n).decode('utf-8'))
                    affix_id = n.split('affixes/')[1].replace('.json', '')
                    definition = data.get('definition', {})
                    affix_type = definition.get('affix_type', 'unknown').upper()
                    
                    # categories
                    cats = data.get('categories') or data.get('types') or []
                    if isinstance(cats, str): cats = [cats]
                    
                    # values: rarities supported
                    values = data.get('values', {})
                    rarities = list(values.keys())
                    
                    for cat in cats:
                        for r in rarities:
                            affixes_by_category_rarity_type[cat][r][affix_type].append(affix_id)
                except Exception as e:
                    pass

print("=== CHECKING CURIO CATEGORIES ===")
curio_cats = ['apothic_compats:belt', 'apothic_compats:necklace', 'apothic_compats:head', 'apothic_compats:ring']
nadir_rarities = ['nadir:worthless', 'nadir:ancient', 'nadir:cataclysmic', 'nadir:divine', 'nadir:esoteric', 'nadir:forgotten', 'nadir:primal', 'nadir:stellar']

for cat in curio_cats:
    print(f"\nCategory: {cat}")
    for r in nadir_rarities:
        stats = affixes_by_category_rarity_type[cat][r]['STAT']
        abilities = affixes_by_category_rarity_type[cat][r]['ABILITY']
        print(f"  {r}: STAT={len(stats)}, ABILITY={len(abilities)}")

print("\n=== CHECKING ARMOR & BREAKER CATEGORIES ===")
gear_cats = ['apotheosis:breaker', 'apotheosis:helmet', 'apotheosis:chestplate', 'apotheosis:leggings', 'apotheosis:boots']
for cat in gear_cats:
    print(f"\nCategory: {cat}")
    for r in nadir_rarities:
        stats = affixes_by_category_rarity_type[cat][r]['STAT']
        abilities = affixes_by_category_rarity_type[cat][r]['ABILITY']
        print(f"  {r}: STAT={len(stats)}, ABILITY={len(abilities)}")
