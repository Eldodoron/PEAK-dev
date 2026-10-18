import zipfile
import json
import os

KUBEJS_DATA = os.path.abspath('minecraft/kubejs/data')

def setup_dirs():
    os.makedirs(os.path.join(KUBEJS_DATA, 'apotheosis', 'rarity_override', 'apotheosis'), exist_ok=True)
    os.makedirs(os.path.join(KUBEJS_DATA, 'irons_apothic', 'rarity_override', 'irons_apothic'), exist_ok=True)
    os.makedirs(os.path.join(KUBEJS_DATA, 'nadir', 'rarities'), exist_ok=True)

def generate_shears_override():
    # Read vanilla shears.json
    with zipfile.ZipFile('minecraft/mods/Apotheosis-1.21.1-8.6.1.jar') as z:
        data = json.loads(z.read('data/apotheosis/rarity_override/apotheosis/shears.json').decode('utf-8'))
    
    # Add Nadir tiers (shears have no abilities)
    data['overrides']['nadir:worthless'] = []
    for r in ['nadir:ancient', 'nadir:forgotten', 'nadir:primal']:
        data['overrides'][r] = [
            {"type": "apotheosis:socket", "min": 1, "max": 1},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:durability", "min": 0.25, "max": 0.55}
        ]
    for r in ['nadir:stellar', 'nadir:divine', 'nadir:esoteric', 'nadir:cataclysmic']:
        data['overrides'][r] = [
            {"type": "apotheosis:socket", "min": 1, "max": 2},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {
                "type": "apotheosis:select",
                "chance": 0.6,
                "if_false": {
                    "type": "apotheosis:component",
                    "components": {
                        "!apotheosis:durability_bonus": {},
                        "minecraft:unbreakable": {}
                    }
                },
                "if_true": {
                    "type": "apotheosis:durability",
                    "min": 0.8,
                    "max": 1.0
                }
            }
        ]
    
    dest = os.path.join(KUBEJS_DATA, 'apotheosis', 'rarity_override', 'apotheosis', 'shears.json')
    with open(dest, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print("Wrote:", dest)

def generate_breaker_override():
    # Breaker: has 5 stats, 2 basic effects, 0 abilities
    dest = os.path.join(KUBEJS_DATA, 'apotheosis', 'rarity_override', 'apotheosis', 'breaker.json')
    data = {
        "type": "apotheosis:rarity_override",
        "category": "apotheosis:breaker",
        "overrides": {
            "nadir:worthless": [
                {"type": "apotheosis:socket", "min": 0, "max": 0}
            ],
            "nadir:ancient": [
                {"type": "apotheosis:socket", "min": 1, "max": 1},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "basic_effect"},
                {"type": "apotheosis:durability", "min": 0.2, "max": 0.4}
            ],
            "nadir:forgotten": [
                {"type": "apotheosis:socket", "min": 1, "max": 2},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "basic_effect"},
                {"type": "apotheosis:durability", "min": 0.3, "max": 0.5}
            ],
            "nadir:primal": [
                {"type": "apotheosis:socket", "min": 2, "max": 2},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "basic_effect"},
                {"type": "apotheosis:durability", "min": 0.4, "max": 0.6}
            ]
        }
    }
    for r in ['nadir:stellar', 'nadir:divine', 'nadir:esoteric', 'nadir:cataclysmic']:
        data['overrides'][r] = [
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "basic_effect"},
            {"type": "apotheosis:affix", "affix_type": "basic_effect"},
            {
                "type": "apotheosis:select",
                "chance": 0.95,
                "if_false": {"type": "apotheosis:socket", "min": 6, "max": 6},
                "if_true": {"type": "apotheosis:socket", "min": 3, "max": 5}
            },
            {
                "type": "apotheosis:select",
                "chance": 0.6,
                "if_false": {
                    "type": "apotheosis:component",
                    "components": {
                        "!apotheosis:durability_bonus": {},
                        "minecraft:unbreakable": {}
                    }
                },
                "if_true": {"type": "apotheosis:durability", "min": 0.8, "max": 1.0}
            }
        ]
    with open(dest, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print("Wrote:", dest)

def generate_shield_override():
    # Shield: has 4 stats, 0 basic effects, 0 abilities
    dest = os.path.join(KUBEJS_DATA, 'apotheosis', 'rarity_override', 'apotheosis', 'shield.json')
    data = {
        "type": "apotheosis:rarity_override",
        "category": "apotheosis:shield",
        "overrides": {
            "nadir:worthless": [
                {"type": "apotheosis:socket", "min": 0, "max": 0}
            ],
            "nadir:ancient": [
                {"type": "apotheosis:socket", "min": 1, "max": 1},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:durability", "min": 0.2, "max": 0.4}
            ],
            "nadir:forgotten": [
                {"type": "apotheosis:socket", "min": 1, "max": 2},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:durability", "min": 0.3, "max": 0.5}
            ],
            "nadir:primal": [
                {"type": "apotheosis:socket", "min": 2, "max": 2},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:durability", "min": 0.4, "max": 0.6}
            ]
        }
    }
    for r in ['nadir:stellar', 'nadir:divine', 'nadir:esoteric', 'nadir:cataclysmic']:
        data['overrides'][r] = [
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {
                "type": "apotheosis:select",
                "chance": 0.95,
                "if_false": {"type": "apotheosis:socket", "min": 6, "max": 6},
                "if_true": {"type": "apotheosis:socket", "min": 3, "max": 5}
            },
            {
                "type": "apotheosis:select",
                "chance": 0.6,
                "if_false": {
                    "type": "apotheosis:component",
                    "components": {
                        "!apotheosis:durability_bonus": {},
                        "minecraft:unbreakable": {}
                    }
                },
                "if_true": {"type": "apotheosis:durability", "min": 0.8, "max": 1.0}
            }
        ]
    with open(dest, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print("Wrote:", dest)

def generate_bow_override():
    # Bow: has 9 stats, 0 basic effects, 1 ability (prosperous)
    dest = os.path.join(KUBEJS_DATA, 'apotheosis', 'rarity_override', 'apotheosis', 'bow.json')
    data = {
        "type": "apotheosis:rarity_override",
        "category": "apotheosis:bow",
        "overrides": {
            "nadir:worthless": [
                {"type": "apotheosis:socket", "min": 0, "max": 0}
            ],
            "nadir:ancient": [
                {"type": "apotheosis:socket", "min": 1, "max": 1},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "ability"},
                {"type": "apotheosis:durability", "min": 0.2, "max": 0.4}
            ],
            "nadir:forgotten": [
                {"type": "apotheosis:socket", "min": 1, "max": 2},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "ability"},
                {"type": "apotheosis:durability", "min": 0.3, "max": 0.5}
            ],
            "nadir:primal": [
                {"type": "apotheosis:socket", "min": 2, "max": 2},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "ability"},
                {"type": "apotheosis:durability", "min": 0.4, "max": 0.6}
            ]
        }
    }
    for r in ['nadir:stellar', 'nadir:divine', 'nadir:esoteric', 'nadir:cataclysmic']:
        data['overrides'][r] = [
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "stat"},
            {"type": "apotheosis:affix", "affix_type": "ability"},
            {
                "type": "apotheosis:select",
                "chance": 0.95,
                "if_false": {"type": "apotheosis:socket", "min": 6, "max": 6},
                "if_true": {"type": "apotheosis:socket", "min": 3, "max": 5}
            },
            {
                "type": "apotheosis:select",
                "chance": 0.6,
                "if_false": {
                    "type": "apotheosis:component",
                    "components": {
                        "!apotheosis:durability_bonus": {},
                        "minecraft:unbreakable": {}
                    }
                },
                "if_true": {"type": "apotheosis:durability", "min": 0.8, "max": 1.0}
            }
        ]
    with open(dest, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print("Wrote:", dest)

def generate_irons_apothic_overrides():
    # 1. Staff
    with zipfile.ZipFile('minecraft/mods/irons_apothic-2.2.1.jar') as z:
        staff_data = json.loads(z.read('data/irons_apothic/rarity_override/irons_apothic/staff.json').decode('utf-8'))
    
    # Staves have no Nadir affixes, so grant pure bonus sockets for Nadir tiers
    staff_data['overrides']['nadir:worthless'] = []
    staff_data['overrides']['nadir:ancient'] = [{"type": "apotheosis:socket", "min": 1, "max": 2}]
    staff_data['overrides']['nadir:forgotten'] = [{"type": "apotheosis:socket", "min": 2, "max": 2}]
    staff_data['overrides']['nadir:primal'] = [{"type": "apotheosis:socket", "min": 2, "max": 3}]
    staff_data['overrides']['nadir:stellar'] = [{"type": "apotheosis:socket", "min": 3, "max": 4}]
    staff_data['overrides']['nadir:divine'] = [{"type": "apotheosis:socket", "min": 3, "max": 4}]
    staff_data['overrides']['nadir:esoteric'] = [{"type": "apotheosis:socket", "min": 4, "max": 4}]
    staff_data['overrides']['nadir:cataclysmic'] = [{"type": "apotheosis:socket", "min": 4, "max": 5}]

    dest_staff = os.path.join(KUBEJS_DATA, 'irons_apothic', 'rarity_override', 'irons_apothic', 'staff.json')
    with open(dest_staff, 'w', encoding='utf-8') as f:
        json.dump(staff_data, f, indent=4)
    print("Wrote:", dest_staff)

    # 2. Spellbook
    with zipfile.ZipFile('minecraft/mods/irons_apothic-2.2.1.jar') as z:
        spellbook_data = json.loads(z.read('data/irons_apothic/rarity_override/irons_apothic/spellbook.json').decode('utf-8'))
    
    # Spellbooks have no Nadir affixes, so grant bonus sockets for Nadir tiers
    spellbook_data['overrides']['nadir:worthless'] = []
    spellbook_data['overrides']['nadir:ancient'] = [{"type": "apotheosis:socket", "min": 1, "max": 2}]
    spellbook_data['overrides']['nadir:forgotten'] = [{"type": "apotheosis:socket", "min": 2, "max": 2}]
    spellbook_data['overrides']['nadir:primal'] = [{"type": "apotheosis:socket", "min": 2, "max": 3}]
    spellbook_data['overrides']['nadir:stellar'] = [{"type": "apotheosis:socket", "min": 3, "max": 3}]
    spellbook_data['overrides']['nadir:divine'] = [{"type": "apotheosis:socket", "min": 3, "max": 4}]
    spellbook_data['overrides']['nadir:esoteric'] = [{"type": "apotheosis:socket", "min": 3, "max": 4}]
    spellbook_data['overrides']['nadir:cataclysmic'] = [{"type": "apotheosis:socket", "min": 4, "max": 4}]

    dest_spellbook = os.path.join(KUBEJS_DATA, 'irons_apothic', 'rarity_override', 'irons_apothic', 'spellbook.json')
    with open(dest_spellbook, 'w', encoding='utf-8') as f:
        json.dump(spellbook_data, f, indent=4)
    print("Wrote:", dest_spellbook)

def update_generic_nadir_rarities():
    # Update default rules in cataclysmic, esoteric, divine, stellar
    # Standard gear that uses default rules: Armor (helmet, chestplate, leggings, boots) and Melee weapons (swords, tridents)
    # Armor and melee weapons all have at least: 5 STAT, 1 BASIC_EFFECT, 1 ABILITY
    with zipfile.ZipFile('minecraft/mods/nadir-1.0.0.jar') as z:
        for rname in ['cataclysmic', 'esoteric', 'divine', 'stellar']:
            data = json.loads(z.read(f'data/nadir/rarities/{rname}.json').decode('utf-8'))
            new_rules = [
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "stat"},
                {"type": "apotheosis:affix", "affix_type": "basic_effect"},
                {"type": "apotheosis:affix", "affix_type": "ability"},
                {
                    "type": "apotheosis:select",
                    "chance": 0.95,
                    "if_false": {"type": "apotheosis:socket", "min": 6, "max": 6},
                    "if_true": {"type": "apotheosis:socket", "min": 3, "max": 5}
                },
                {
                    "type": "apotheosis:select",
                    "chance": 0.6,
                    "if_false": {
                        "type": "apotheosis:component",
                        "components": {
                            "!apotheosis:durability_bonus": {},
                            "minecraft:unbreakable": {}
                        }
                    },
                    "if_true": {"type": "apotheosis:durability", "min": 0.8, "max": 1.0}
                }
            ]
            data['rules'] = new_rules
            dest = os.path.join(KUBEJS_DATA, 'nadir', 'rarities', f'{rname}.json')
            with open(dest, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print("Wrote:", dest)

if __name__ == '__main__':
    setup_dirs()
    generate_shears_override()
    generate_breaker_override()
    generate_shield_override()
    generate_bow_override()
    generate_irons_apothic_overrides()
    update_generic_nadir_rarities()
    print("Full Apotheosis & Nadir perfection overrides completed successfully!")
