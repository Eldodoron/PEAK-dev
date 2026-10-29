import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'minecraft', 'kubejs', 'data')
MATERIALS_FILE = os.path.join(BASE_DIR, 'minecraft', 'config', 'almostunified', 'unification', 'materials.json')

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def write_json_clean(file_path, data):
    ensure_dir(os.path.dirname(file_path))
    content = json.dumps(data, indent=2) + '\n'
    with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    # Verify no BOM
    with open(file_path, 'rb') as f:
        head = f.read(3)
        if head == b'\xef\xbb\xbf':
            raise ValueError(f"BOM detected in {file_path}")
    print(f"Wrote: {os.path.relpath(file_path, BASE_DIR)}")

def update_materials_priorities():
    with open(MATERIALS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    expected_order = [
        # Tier 1: Create & Create Addons
        "create",
        "simulated",
        "create_enchantment_industry",
        "create_wizardry",
        "tfmg",
        "create_new_age",
        "createdieselgenerators",
        "create_factory",
        "createmetalwork",
        "create_sa",
        "create_confectionery",
        "create_central_kitchen",
        "dndesires",
        "create_dragons_plus",
        "apokinetics",
        "northstar",
        "mek_x_star",
        "minecraft",
        # Tier 2: Adventure & Magic Mods
        "iceandfire",
        "alexscaves",
        "irons_spellbooks",
        "ars_nouveau",
        "malum",
        "deeperdarker",
        "undergarden",
        "gobber2",
        # Tier 3 & Fallback Tech Mods
        "alltheores",
        "mekanism",
        "immersiveengineering",
        "enderio",
        "allthemodium"
    ]
    
    data['mod_priorities'] = expected_order
    write_json_clean(MATERIALS_FILE, data)

def apply_ato_overrides():
    ato_bm_dir = os.path.join(DATA_DIR, 'alltheores', 'neoforge', 'biome_modifier')
    ato_pf_dir = os.path.join(DATA_DIR, 'alltheores', 'worldgen', 'placed_feature')
    
    # Overworld duplicate ores to suppress in ATO
    suppressed_ato = [
        ("zinc_overworld.json", "ore_zinc_placed.json"),
        ("lead_overworld.json", "ore_lead_placed.json"),
        ("nickel_overworld.json", "ore_nickel_placed.json"),
        ("osmium_overworld.json", "ore_osmium_placed.json"),
        ("tin_overworld.json", "ore_tin_placed.json"),
        ("fluorite_overworld.json", "ore_fluorite_placed.json"),
        ("uranium_overworld.json", "ore_uranium_placed.json"),
        ("salt_overworld.json", "ore_salt_placed.json"),
        ("silver_overworld.json", "ore_silver_placed.json"),
        ("sapphire_overworld.json", "ore_sapphire_placed.json")
    ]
    
    empty_bm = {
        "type": "neoforge:add_features",
        "biomes": "#c:is_overworld",
        "features": [],
        "step": "underground_ores"
    }
    
    for bm_name, pf_name in suppressed_ato:
        bm_path = os.path.join(ato_bm_dir, bm_name)
        write_json_clean(bm_path, empty_bm)
        
        pf_path = os.path.join(ato_pf_dir, pf_name)
        if os.path.exists(pf_path):
            with open(pf_path, 'r', encoding='utf-8') as f:
                pf_data = json.load(f)
            
            # Update count in placement modifiers to 0
            for modifier in pf_data.get('placement', []):
                if modifier.get('type') == 'minecraft:count':
                    modifier['count'] = 0
            
            write_json_clean(pf_path, pf_data)
        else:
            # Create placed feature override with count 0
            base_feature_name = pf_name.replace('.json', '')
            pf_data = {
                "feature": f"alltheores:{base_feature_name}",
                "placement": [
                    {
                        "type": "minecraft:count",
                        "count": 0
                    }
                ]
            }
            write_json_clean(pf_path, pf_data)

def apply_mekanism_overrides():
    mek_bm_dir = os.path.join(DATA_DIR, 'mekanism', 'neoforge', 'biome_modifier')
    mek_pf_dir = os.path.join(DATA_DIR, 'mekanism', 'worldgen', 'placed_feature')
    
    # Suppress Mekanism lead
    lead_bm = {
        "type": "neoforge:add_features",
        "biomes": "#mekanism:spawn_ores",
        "features": [],
        "step": "underground_ores"
    }
    write_json_clean(os.path.join(mek_bm_dir, 'lead.json'), lead_bm)
    
    lead_pf = {
        "feature": "mekanism:ore_lead_normal",
        "placement": [
            {
                "type": "minecraft:count",
                "count": 0
            }
        ]
    }
    write_json_clean(os.path.join(mek_pf_dir, 'ore_lead_normal.json'), lead_pf)
    write_json_clean(os.path.join(mek_pf_dir, 'ore_lead_normal_retrogen.json'), lead_pf)

def apply_immersive_engineering_overrides():
    ie_bm_dir = os.path.join(DATA_DIR, 'immersiveengineering', 'neoforge', 'biome_modifier')
    ie_pf_dir = os.path.join(DATA_DIR, 'immersiveengineering', 'worldgen', 'placed_feature')
    
    suppressed_ie = [
        "bauxite",
        "deep_nickel",
        "lead",
        "nickel",
        "silver",
        "uranium"
    ]
    
    empty_bm = {
        "type": "neoforge:add_features",
        "biomes": "#minecraft:is_overworld",
        "features": [],
        "step": "underground_ores"
    }
    
    for ore in suppressed_ie:
        write_json_clean(os.path.join(ie_bm_dir, f"{ore}.json"), empty_bm)
        
        pf_data = {
            "feature": f"immersiveengineering:{ore}",
            "placement": [
                {
                    "type": "minecraft:count",
                    "count": 0
                }
            ]
        }
        write_json_clean(os.path.join(ie_pf_dir, f"{ore}.json"), pf_data)

if __name__ == '__main__':
    print("Applying ore generation unification overrides...")
    update_materials_priorities()
    apply_ato_overrides()
    apply_mekanism_overrides()
    apply_immersive_engineering_overrides()
    print("Done!")
