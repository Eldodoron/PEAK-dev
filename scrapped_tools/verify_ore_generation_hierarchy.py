import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'minecraft', 'kubejs', 'data')
MATERIALS_FILE = os.path.join(BASE_DIR, 'minecraft', 'config', 'almostunified', 'unification', 'materials.json')

def verify_no_bom(file_path):
    with open(file_path, 'rb') as f:
        head = f.read(3)
        if head == b'\xef\xbb\xbf':
            raise AssertionError(f"BOM found in {file_path}")

def verify_json(file_path):
    verify_no_bom(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def run_checks():
    print("=== Starting Ore Generation Hierarchy Verification ===")
    errors = []
    
    # 1. Materials JSON priorities
    try:
        mat_data = verify_json(MATERIALS_FILE)
        priorities = mat_data.get('mod_priorities', [])
        print(f"[OK] materials.json is valid JSON (0 BOM). Contains {len(priorities)} prioritized mods.")
        
        # Verify Create addons are first
        if priorities[0] != 'create':
            errors.append(f"Expected 'create' first in priorities, got '{priorities[0]}'")
        
        # Verify adventure mods are before alltheores
        adv_mods = ['iceandfire', 'alexscaves', 'irons_spellbooks', 'ars_nouveau', 'malum', 'deeperdarker', 'undergarden', 'gobber2']
        ato_idx = priorities.index('alltheores')
        for m in adv_mods:
            if m not in priorities:
                errors.append(f"Adventure mod '{m}' missing from mod_priorities")
            elif priorities.index(m) > ato_idx:
                errors.append(f"Adventure mod '{m}' is positioned after 'alltheores' in mod_priorities")
        print("[OK] Priority hierarchy in materials.json verified: Create Addons -> Adventure Mods -> Fallback Tech (ATO/Mek/IE).")
    except Exception as e:
        errors.append(f"materials.json error: {e}")

    # 2. Suppressed ATO Overworld Biome Modifiers
    ato_suppressed = [
        'zinc_overworld.json', 'lead_overworld.json', 'nickel_overworld.json',
        'osmium_overworld.json', 'tin_overworld.json', 'fluorite_overworld.json',
        'uranium_overworld.json', 'salt_overworld.json', 'silver_overworld.json',
        'sapphire_overworld.json'
    ]
    
    ato_bm_dir = os.path.join(DATA_DIR, 'alltheores', 'neoforge', 'biome_modifier')
    for f in ato_suppressed:
        fp = os.path.join(ato_bm_dir, f)
        if not os.path.exists(fp):
            errors.append(f"Missing ATO biome modifier override: {f}")
            continue
        data = verify_json(fp)
        if data.get('features') != []:
            errors.append(f"ATO biome modifier {f} does not have empty features: {data.get('features')}")
    print(f"[OK] Verified 10 suppressed AllTheOres overworld biome modifiers.")

    # 3. Suppressed ATO Placed Features (count: 0)
    ato_pf_dir = os.path.join(DATA_DIR, 'alltheores', 'worldgen', 'placed_feature')
    ato_pf_suppressed = [
        'ore_zinc_placed.json', 'ore_lead_placed.json', 'ore_nickel_placed.json',
        'ore_osmium_placed.json', 'ore_tin_placed.json', 'ore_fluorite_placed.json',
        'ore_uranium_placed.json', 'ore_salt_placed.json', 'ore_silver_placed.json',
        'ore_sapphire_placed.json'
    ]
    for f in ato_pf_suppressed:
        fp = os.path.join(ato_pf_dir, f)
        if not os.path.exists(fp):
            errors.append(f"Missing ATO placed feature override: {f}")
            continue
        data = verify_json(fp)
        counts = [m.get('count') for m in data.get('placement', []) if m.get('type') == 'minecraft:count']
        if not counts or counts[0] != 0:
            errors.append(f"ATO placed feature {f} count is not 0: {counts}")
    print(f"[OK] Verified 10 suppressed AllTheOres placed features (count = 0).")

    # 4. Active ATO Fallback Placed Features (count > 0)
    ato_pf_active = [
        ('ore_aluminum_placed.json', 3),
        ('ore_cinnabar_placed.json', 2),
        ('ore_iridium_placed.json', 3),
        ('ore_peridot_placed.json', 2),
        ('ore_ruby_placed.json', 2)
    ]
    for f, expected_count in ato_pf_active:
        fp = os.path.join(ato_pf_dir, f)
        data = verify_json(fp)
        counts = [m.get('count') for m in data.get('placement', []) if m.get('type') == 'minecraft:count']
        if not counts or counts[0] != expected_count:
            errors.append(f"ATO active placed feature {f} count is {counts}, expected {expected_count}")
    print(f"[OK] Verified 5 active AllTheOres fallback overworld placed features.")

    # 5. Mekanism Overrides
    mek_bm_fp = os.path.join(DATA_DIR, 'mekanism', 'neoforge', 'biome_modifier', 'lead.json')
    mek_bm_data = verify_json(mek_bm_fp)
    if mek_bm_data.get('features') != []:
        errors.append(f"Mekanism lead biome modifier does not have empty features: {mek_bm_data.get('features')}")
    
    for f in ['ore_lead_normal.json', 'ore_lead_normal_retrogen.json']:
        fp = os.path.join(DATA_DIR, 'mekanism', 'worldgen', 'placed_feature', f)
        data = verify_json(fp)
        counts = [m.get('count') for m in data.get('placement', []) if m.get('type') == 'minecraft:count']
        if not counts or counts[0] != 0:
            errors.append(f"Mekanism placed feature {f} count is not 0: {counts}")
    print(f"[OK] Verified Mekanism lead suppression (biome modifier + placed feature).")

    # 6. Immersive Engineering Overrides
    ie_suppressed = ['bauxite', 'deep_nickel', 'lead', 'nickel', 'silver', 'uranium']
    for ore in ie_suppressed:
        bm_fp = os.path.join(DATA_DIR, 'immersiveengineering', 'neoforge', 'biome_modifier', f"{ore}.json")
        data = verify_json(bm_fp)
        if data.get('features') != []:
            errors.append(f"IE biome modifier {ore} does not have empty features: {data.get('features')}")
        
        pf_fp = os.path.join(DATA_DIR, 'immersiveengineering', 'worldgen', 'placed_feature', f"{ore}.json")
        data = verify_json(pf_fp)
        counts = [m.get('count') for m in data.get('placement', []) if m.get('type') == 'minecraft:count']
        if not counts or counts[0] != 0:
            errors.append(f"IE placed feature {ore} count is not 0: {counts}")
    print(f"[OK] Verified 6 Immersive Engineering suppressed ores (biome modifiers + placed features).")

    # 7. Tier 1 & Tier 2 Active Primary Features
    primary_checks = [
        (os.path.join(DATA_DIR, 'create', 'worldgen', 'placed_feature', 'zinc_ore.json'), 'minecraft:count', 5),
        (os.path.join(DATA_DIR, 'tfmg', 'worldgen', 'placed_feature', 'lead_ore.json'), 'minecraft:count', 3),
        (os.path.join(DATA_DIR, 'tfmg', 'worldgen', 'placed_feature', 'nickel_ore.json'), 'minecraft:count', 3),
        (os.path.join(DATA_DIR, 'tfmg', 'worldgen', 'placed_feature', 'lithium_ore.json'), 'minecraft:count', 2),
        (os.path.join(DATA_DIR, 'iceandfire', 'worldgen', 'placed_feature', 'silver_ore.json'), 'minecraft:count', 10),
        (os.path.join(DATA_DIR, 'iceandfire', 'worldgen', 'placed_feature', 'sapphire_ore.json'), 'minecraft:count', 3),
    ]
    for fp, p_type, expected_val in primary_checks:
        data = verify_json(fp)
        vals = [m.get('count') for m in data.get('placement', []) if m.get('type') == p_type]
        if not vals or vals[0] != expected_val:
            errors.append(f"Primary generator {os.path.basename(fp)} value is {vals}, expected {expected_val}")
    print(f"[OK] Verified active primary generators (Create Zinc, TFMG Lead/Nickel/Lithium, Ice&Fire Silver/Sapphire).")

    # 8. Striated Rock Formations
    for fp in [
        os.path.join(DATA_DIR, 'create', 'worldgen', 'placed_feature', 'striated_ores_overworld.json'),
        os.path.join(DATA_DIR, 'create', 'worldgen', 'placed_feature', 'striated_ores_nether.json'),
        os.path.join(DATA_DIR, 'tfmg', 'worldgen', 'placed_feature', 'tfmg_striated_ores_overworld.json'),
        os.path.join(DATA_DIR, 'tfmg', 'worldgen', 'placed_feature', 'tfmg_striated_ores_nether.json'),
    ]:
        data = verify_json(fp)
        chances = [m.get('chance') for m in data.get('placement', []) if m.get('type') == 'minecraft:rarity_filter']
        if not chances or chances[0] != 30:
            errors.append(f"Striated feature {os.path.basename(fp)} chance is {chances}, expected 30")
    print(f"[OK] Verified Create and TFMG striated rock formations are active (1 in 30 chunks).")

    if errors:
        print("\n[FAIL] Found verification errors:")
        for err in errors:
            print(" -", err)
        return False
    else:
        print("\n=== ALL VERIFICATIONS PASSED CLEANLY (0 ERRORS, 0 BOMS) ===")
        return True

if __name__ == '__main__':
    success = run_checks()
    exit(0 if success else 1)
