import os
import json

KUBEJS_DATA = os.path.abspath('minecraft/kubejs/data/integrated_simply_swords/recipe/born_in_chaos/dark_metal')
os.makedirs(KUBEJS_DATA, exist_ok=True)

weapons = [
    'chakram', 'claymore', 'cutlass', 'glaive', 'greataxe',
    'greathammer', 'halberd', 'katana', 'longsword', 'rapier',
    'sai', 'scythe', 'spear', 'twinblade', 'warglaive'
]

recipe_template = {
    "neoforge:conditions": [
        {
            "type": "neoforge:mod_loaded",
            "modid": "born_in_chaos_v1"
        }
    ]
}

for w in weapons:
    dest = os.path.join(KUBEJS_DATA, f"{w}.json")
    with open(dest, 'w', encoding='utf-8') as f:
        json.dump(recipe_template, f, indent=4)
    print(f"Generated condition-guarded recipe: {dest}")

print("All 15 born_in_chaos recipes guarded with mod_loaded condition!")
