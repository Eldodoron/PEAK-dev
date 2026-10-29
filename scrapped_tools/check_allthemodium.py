import os
import re
import json
import zipfile
from collections import defaultdict

def main():
    root = os.path.abspath(".")
    minecraft_dir = os.path.join(root, "minecraft")
    item_dump = os.path.join(minecraft_dir, "ct_dumps", "item.txt")
    
    # 1. Load all allthemodium items
    atm_items = set()
    with open(item_dump, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"<item:(allthemodium:[^>]+)>", line)
            if m:
                atm_items.add(m.group(1))

    print(f"Total AllTheModium items found in dump: {len(atm_items)}")

    # 2. Inspect allthemodium jar recipes
    atm_jar_path = os.path.join(minecraft_dir, "mods", "allthemodium-3.0.1_mc_1.21.1.jar")
    jar_recipes_out = defaultdict(list)
    jar_recipes_in = defaultdict(list)
    tconstruct_recipes = []
    
    with zipfile.ZipFile(atm_jar_path, 'r') as z:
        for name in z.namelist():
            if name.startswith("data/allthemodium/recipe/") and name.endswith(".json"):
                data = json.loads(z.read(name).decode('utf-8'))
                conds = data.get("neoforge:conditions", [])
                is_tcon = any(c.get("modid") == "tconstruct" for c in conds)
                
                # result / output
                result = data.get("result") or data.get("output")
                res_id = None
                if isinstance(result, str):
                    res_id = result
                elif isinstance(result, dict):
                    res_id = result.get("id") or result.get("item")
                
                if is_tcon:
                    tconstruct_recipes.append((name, res_id, data))
                else:
                    if res_id:
                        jar_recipes_out[res_id].append(name)
                        
                # inputs/ingredients
                # Traverse JSON to find all strings matching allthemodium:
                content_str = json.dumps(data)
                for item in atm_items:
                    if f'"{item}"' in content_str:
                        if is_tcon:
                            pass
                        else:
                            jar_recipes_in[item].append(name)

    print(f"Active jar recipes producing items: {len(jar_recipes_out)} unique items")
    print(f"TConstruct-conditioned recipes disabled: {len(tconstruct_recipes)}")

    # 3. Inspect KubeJS server scripts
    kjs_dir = os.path.join(minecraft_dir, "kubejs", "server_scripts")
    kjs_recipes_out = defaultdict(list)
    kjs_recipes_in = defaultdict(list)
    kjs_removals = defaultdict(list)

    for dirpath, _, filenames in os.walk(kjs_dir):
        for fname in filenames:
            if fname.endswith(".js"):
                fpath = os.path.join(dirpath, fname)
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                for idx, line in enumerate(lines, 1):
                    # Check removals
                    for item in atm_items:
                        if item in line:
                            if "event.remove" in line or "remove({" in line or "output:" in line:
                                kjs_removals[item].append(f"{fname}:{idx}")
                            # rough check for recipes
                            if any(k in line for k in ["event.shaped", "event.shapeless", "event.recipes", ".crushing", ".mixing", ".deploying", ".sequenced_assembly"]):
                                # Is it output or input?
                                kjs_recipes_in[item].append(f"{fname}:{idx}")

    # 4. Also check backpack_allthemodium_upgrade jar
    bp_jar = os.path.join(minecraft_dir, "mods", "backpack_allthemodium_upgrade-2.4.jar")
    bp_recipes_out = defaultdict(list)
    bp_recipes_in = defaultdict(list)
    if os.path.exists(bp_jar):
        with zipfile.ZipFile(bp_jar, 'r') as z:
            for name in z.namelist():
                if name.endswith(".json") and "recipe" in name:
                    try:
                        content = z.read(name).decode('utf-8')
                        for item in atm_items:
                            if f'"{item}"' in content:
                                bp_recipes_in[item].append(f"backpack_jar:{name}")
                    except Exception:
                        pass

    # 5. Check all items and categorize
    missing_recipe = []
    missing_use = []
    both_missing = []

    # Known natural/drop sources
    natural_sources = {
        'allthemodium:allthemodium_ore': 'Worldgen (Deepslate/Mountain biomes / Mining dim)',
        'allthemodium:allthemodium_slate_ore': 'Worldgen (Deepslate)',
        'allthemodium:vibranium_ore': 'Worldgen (Nether / Other dim)',
        'allthemodium:other_vibranium_ore': 'Worldgen (The Other dim)',
        'allthemodium:unobtainium_ore': 'Worldgen (The End highlands)',
        'allthemodium:raw_allthemodium': 'Mined from allthemodium_ore',
        'allthemodium:raw_vibranium': 'Mined from vibranium_ore',
        'allthemodium:raw_unobtainium': 'Mined from unobtainium_ore',
        'allthemodium:piglich_heart': 'Dropped by Piglich (The Other)',
        'allthemodium:ancient_dirt': 'Worldgen in The Mining Dimension / The Other',
        'allthemodium:ancient_stone': 'Worldgen in Ancient biomes',
        'allthemodium:ancient_grass': 'Worldgen in Ancient biomes',
        'allthemodium:ancient_podzol': 'Worldgen in Ancient biomes',
        'allthemodium:ancient_log_0': 'Ancient Trees in Ancient biomes',
        'allthemodium:ancient_log_1': 'Ancient Trees in Ancient biomes',
        'allthemodium:ancient_log_2': 'Ancient Trees in Ancient biomes',
        'allthemodium:ancient_leaves': 'Ancient Trees in Ancient biomes',
        'allthemodium:ancient_leaves_bottom': 'Ancient Trees in Ancient biomes',
        'allthemodium:ancient_sapling': 'Ancient Leaves drop',
        'allthemodium:ancient_fern': 'Ancient foliage',
        'allthemodium:ancient_herb': 'Ancient foliage',
        'allthemodium:ancient_soulberries': 'Ancient foliage',
        'allthemodium:demonic_log': 'Demonic Trees (The Other)',
        'allthemodium:demonic_leaves': 'Demonic Trees (The Other)',
        'allthemodium:demonic_leaves_bottom': 'Demonic Trees (The Other)',
        'allthemodium:demonic_sapling': 'Demonic Leaves drop',
        'allthemodium:demonic_herb': 'Demonic foliage',
        'allthemodium:soul_log': 'Soul Trees (The Other)',
        'allthemodium:soul_log_0': 'Soul Trees (The Other)',
        'allthemodium:soul_log_1': 'Soul Trees (The Other)',
        'allthemodium:soul_log_2': 'Soul Trees (The Other)',
        'allthemodium:soul_leaves': 'Soul Trees (The Other)',
        'allthemodium:soul_leaves_bottom': 'Soul Trees (The Other)',
        'allthemodium:soul_sapling': 'Soul Leaves drop',
        'allthemodium:soul_herb': 'Soul foliage',
        'allthemodium:soul_lava_bucket': 'Soul Lava source in The Other',
        'allthemodium:suspicious_clay': 'Archeology in Ancient/Other structures',
        'allthemodium:suspicious_soul_sand': 'Archeology in Ancient/Other structures',
        'allthemodium:allthemodium_upgrade_smithing_template': 'Loot in Ancient/Other / Sus clay',
        'allthemodium:vibranium_upgrade_smithing_template': 'Loot in The Other',
        'allthemodium:unobtainium_upgrade_smithing_template': 'Loot in The Other / Piglich pyramid',
    }

    # Known equipment uses (wearable, weapon, tool, food, functional block)
    innate_uses = {
        'allthemodium:allthemodium_sword': 'Weapon (Indestructible, high damage)',
        'allthemodium:allthemodium_pickaxe': 'Tool (Can mine Vibranium)',
        'allthemodium:allthemodium_axe': 'Tool (High efficiency axe)',
        'allthemodium:allthemodium_shovel': 'Tool (High efficiency shovel)',
        'allthemodium:allthemodium_hoe': 'Tool (High efficiency hoe)',
        'allthemodium:allthemodium_helmet': 'Armor (No drowning, buffs)',
        'allthemodium:allthemodium_chestplate': 'Armor',
        'allthemodium:allthemodium_leggings': 'Armor',
        'allthemodium:allthemodium_boots': 'Armor (No fall damage, step assist)',
        'allthemodium:allthemodium_bow': 'Ranged Weapon',
        'allthemodium:allthemodium_mace': 'Heavy Weapon',
        'allthemodium:allthemodium_apple': 'Food (OP buffs)',
        'allthemodium:allthemodium_carrot': 'Food (OP buffs)',
        'allthemodium:allthemodium_source_jar': 'Ars Nouveau / Source storage block',
        'allthemodium:teleport_pad': 'Portal block (Dimension teleporter)',
        
        'allthemodium:vibranium_sword': 'Weapon',
        'allthemodium:vibranium_pickaxe': 'Tool (Can mine Unobtainium)',
        'allthemodium:vibranium_axe': 'Tool',
        'allthemodium:vibranium_shovel': 'Tool',
        'allthemodium:vibranium_hoe': 'Tool',
        'allthemodium:vibranium_helmet': 'Armor',
        'allthemodium:vibranium_chestplate': 'Armor',
        'allthemodium:vibranium_leggings': 'Armor',
        'allthemodium:vibranium_boots': 'Armor',
        'allthemodium:vibranium_shield': 'Shield (Indestructible)',
        'allthemodium:vibranium_mace': 'Heavy Weapon',

        'allthemodium:unobtainium_sword': 'Weapon',
        'allthemodium:unobtainium_pickaxe': 'Tool',
        'allthemodium:unobtainium_axe': 'Tool',
        'allthemodium:unobtainium_shovel': 'Tool',
        'allthemodium:unobtainium_hoe': 'Tool',
        'allthemodium:unobtainium_helmet': 'Armor',
        'allthemodium:unobtainium_chestplate': 'Armor',
        'allthemodium:unobtainium_leggings': 'Armor',
        'allthemodium:unobtainium_boots': 'Armor',
        'allthemodium:unobtainium_crossbow': 'Ranged Weapon',
        'allthemodium:unobtainium_mace': 'Heavy Weapon',

        'allthemodium:alloy_sword': 'Ultimate Weapon',
        'allthemodium:alloy_pick': 'Ultimate Pickaxe (3x3 / instant / indestructible)',
        'allthemodium:alloy_axe': 'Ultimate Axe',
        'allthemodium:alloy_shovel': 'Ultimate Shovel',
        'allthemodium:alloy_paxel': 'Ultimate Paxel (All-in-one)',
        'allthemodium:alloy_trident': 'Ultimate Trident',
    }

    print("\n================== FULL AUDIT ==================")
    for item in sorted(atm_items):
        recipes_out = jar_recipes_out.get(item, [])
        recipes_in = jar_recipes_in.get(item, []) + bp_recipes_in.get(item, [])
        nat = natural_sources.get(item)
        innate = innate_uses.get(item)
        
        has_recipe = bool(recipes_out or nat)
        has_use = bool(recipes_in or innate or item in kjs_recipes_in)

        status_rec = "OK" if has_recipe else "NO RECIPE/SOURCE"
        status_use = "OK" if has_use else "NO RECIPE USE"

        if not has_recipe and not has_use:
            both_missing.append(item)
        elif not has_recipe:
            missing_recipe.append(item)
        elif not has_use:
            missing_use.append(item)

    print(f"\n--- ITEMS MISSING RECIPE / OBTAIN METHOD ({len(missing_recipe)}) ---")
    for it in missing_recipe:
        print(f"  {it}")

    print(f"\n--- ITEMS MISSING USES ({len(missing_use)}) ---")
    for it in missing_use:
        print(f"  {it}")

    print(f"\n--- ITEMS MISSING BOTH RECIPE AND USES ({len(both_missing)}) ---")
    for it in both_missing:
        print(f"  {it}")

if __name__ == '__main__':
    main()
