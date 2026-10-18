import zipfile
import json
import os

KUBEJS_DATA = os.path.abspath('minecraft/kubejs/data')

def setup_directories():
    os.makedirs(os.path.join(KUBEJS_DATA, 'nadir', 'affixes', 'breaker', 'effect'), exist_ok=True)
    os.makedirs(os.path.join(KUBEJS_DATA, 'nadir', 'affixes', 'melee'), exist_ok=True)
    os.makedirs(os.path.join(KUBEJS_DATA, 'nadir', 'rarities'), exist_ok=True)
    os.makedirs(os.path.join(KUBEJS_DATA, 'apothic_compats', 'rarity_override', 'apothic_compats'), exist_ok=True)
    os.makedirs(os.path.join(KUBEJS_DATA, 'irons_apothic', 'rarity_override', 'irons_apothic'), exist_ok=True)

def fix_nadir_affixes():
    print("Fixing Nadir affixes (omnetic.json & executing.json)...")
    with zipfile.ZipFile('minecraft/mods/nadir-1.0.0.jar') as z:
        # 1. Omnetic
        omnetic = json.loads(z.read('data/nadir/affixes/breaker/effect/omnetic.json').decode('utf-8'))
        omnetic['categories'] = ["apotheosis:breaker"]
        out_omnetic = os.path.join(KUBEJS_DATA, 'nadir', 'affixes', 'breaker', 'effect', 'omnetic.json')
        with open(out_omnetic, 'w', encoding='utf-8') as f:
            json.dump(omnetic, f, indent=4)
        print("  -> Wrote", out_omnetic)

        # 2. Executing
        executing = json.loads(z.read('data/nadir/affixes/melee/executing.json').decode('utf-8'))
        executing['categories'] = ["apotheosis:melee_weapon", "apotheosis:trident"]
        out_executing = os.path.join(KUBEJS_DATA, 'nadir', 'affixes', 'melee', 'executing.json')
        with open(out_executing, 'w', encoding='utf-8') as f:
            json.dump(executing, f, indent=4)
        print("  -> Wrote", out_executing)

def fix_nadir_rarities():
    print("Fixing Nadir rarities rules (stellar, divine, esoteric, cataclysmic)...")
    with zipfile.ZipFile('minecraft/mods/nadir-1.0.0.jar') as z:
        for rname in ['stellar', 'divine', 'esoteric', 'cataclysmic']:
            data = json.loads(z.read(f'data/nadir/rarities/{rname}.json').decode('utf-8'))
            old_rules = data.get('rules', [])
            
            # Filter rules: Keep max 5 stat affixes, max 3 basic_effects, max 1 ability affix, and keep select/durability/socket
            new_rules = []
            stat_count = 0
            basic_count = 0
            ability_count = 0
            
            for rule in old_rules:
                rtype = rule.get('type')
                if rtype == 'apotheosis:affix':
                    atype = rule.get('affix_type')
                    if atype == 'stat':
                        if stat_count < 5:
                            new_rules.append(rule)
                            stat_count += 1
                    elif atype == 'basic_effect':
                        if basic_count < 3:
                            new_rules.append(rule)
                            basic_count += 1
                    elif atype == 'ability':
                        if ability_count < 1:
                            new_rules.append(rule)
                            ability_count += 1
                else:
                    new_rules.append(rule)
            
            data['rules'] = new_rules
            out_rarity = os.path.join(KUBEJS_DATA, 'nadir', 'rarities', f'{rname}.json')
            with open(out_rarity, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(f"  -> Wrote {out_rarity} (rules adjusted from {len(old_rules)} to {len(new_rules)})")

def fix_curio_rarity_overrides():
    print("Fixing Apothic Compats curio rarity overrides (14 categories)...")
    curio_overrides_to_add = {
        "nadir:worthless": [
            {
                "type": "apotheosis:socket",
                "min": 0,
                "max": 0
            }
        ],
        "nadir:ancient": [
            {
                "type": "apotheosis:socket",
                "min": 1,
                "max": 1
            }
        ],
        "nadir:forgotten": [
            {
                "type": "apotheosis:socket",
                "min": 1,
                "max": 2
            }
        ],
        "nadir:primal": [
            {
                "type": "apotheosis:socket",
                "min": 1,
                "max": 2
            }
        ],
        "nadir:stellar": [
            {
                "type": "apotheosis:socket",
                "min": 2,
                "max": 2
            }
        ],
        "nadir:divine": [
            {
                "type": "apotheosis:socket",
                "min": 2,
                "max": 2
            }
        ],
        "nadir:esoteric": [
            {
                "type": "apotheosis:socket",
                "min": 2,
                "max": 2
            }
        ],
        "nadir:cataclysmic": [
            {
                "type": "apotheosis:socket",
                "min": 2,
                "max": 2
            }
        ]
    }

    with zipfile.ZipFile('minecraft/mods/apothic_compats-0.2.4.2.jar') as z:
        for n in z.namelist():
            if n.startswith('data/apothic_compats/rarity_override/apothic_compats/') and n.endswith('.json'):
                fname = n.split('/')[-1]
                data = json.loads(z.read(n).decode('utf-8'))
                
                # Add all Nadir overrides to existing overrides
                overrides = data.get('overrides', {})
                for k, v in curio_overrides_to_add.items():
                    overrides[k] = v
                data['overrides'] = overrides
                
                out_path = os.path.join(KUBEJS_DATA, 'apothic_compats', 'rarity_override', 'apothic_compats', fname)
                with open(out_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
                print(f"  -> Wrote {out_path}")

def fix_spellbook_rarity_overrides():
    print("Fixing Iron's Apothic spellbook rarity overrides...")
    with zipfile.ZipFile('minecraft/mods/irons_apothic-2.2.1.jar') as z:
        spellbook_path = 'data/irons_apothic/rarity_override/irons_apothic/spellbook.json'
        data = json.loads(z.read(spellbook_path).decode('utf-8'))
        overrides = data.get('overrides', {})
        
        # Spellbooks have 0 abilities, only stats + basic_effect + sockets
        nadir_spellbook_overrides = {
            "nadir:worthless": [
                { "type": "apotheosis:socket", "min": 0, "max": 0 }
            ],
            "nadir:ancient": [
                { "type": "apotheosis:socket", "min": 1, "max": 2 },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "basic_effect" }
            ],
            "nadir:forgotten": [
                { "type": "apotheosis:socket", "min": 1, "max": 2 },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "basic_effect" }
            ],
            "nadir:primal": [
                { "type": "apotheosis:socket", "min": 2, "max": 2 },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "basic_effect" }
            ],
            "nadir:stellar": [
                { "type": "apotheosis:socket", "min": 2, "max": 3 },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "basic_effect" }
            ],
            "nadir:divine": [
                { "type": "apotheosis:socket", "min": 2, "max": 3 },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "basic_effect" }
            ],
            "nadir:esoteric": [
                { "type": "apotheosis:socket", "min": 3, "max": 3 },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "basic_effect" }
            ],
            "nadir:cataclysmic": [
                { "type": "apotheosis:socket", "min": 3, "max": 3 },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "stat" },
                { "type": "apotheosis:affix", "affix_type": "basic_effect" }
            ]
        }
        for k, v in nadir_spellbook_overrides.items():
            overrides[k] = v
        data['overrides'] = overrides
        out_spellbook = os.path.join(KUBEJS_DATA, 'irons_apothic', 'rarity_override', 'irons_apothic', 'spellbook.json')
        with open(out_spellbook, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"  -> Wrote {out_spellbook}")

if __name__ == '__main__':
    setup_directories()
    fix_nadir_affixes()
    fix_nadir_rarities()
    fix_curio_rarity_overrides()
    fix_spellbook_rarity_overrides()
    print("\nAll Apotheosis & Nadir fixes generated successfully!")
