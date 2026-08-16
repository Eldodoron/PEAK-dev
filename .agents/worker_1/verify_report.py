"""
Comprehensive Verification Script for PEAK Modpack AI Audit Report
Validates existence and line counts of all 94 cited files in the audit report.
"""
import os
import json

ROOT_DIR = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft"

ALL_CITED_FILES = [
    # Category 1: Explicit AI Branding & Agent Attribution
    r"kubejs\server_scripts\00_tags.js",
    r"kubejs\server_scripts\20_fixed_datapacks.js",
    r"kubejs\server_scripts\convert_to_js.py",
    r"kubejs\assets\minecraft\models\block\flowerbed_1.json",
    r"kubejs\assets\minecraft\models\block\flowerbed_2.json",
    r"kubejs\assets\minecraft\models\block\flowerbed_3.json",
    r"kubejs\assets\minecraft\models\block\flowerbed_4.json",
    r"check_client_toml.py",
    r"generate_high_priority_data.py",
    r"scratch\mod_extraction\convert_recipes.py",
    # Category 2: Multi-Prompt Progression Artifacts
    r"kubejs\server_scripts\expert_mode_recipes.js",
    r"kubejs\server_scripts\03_pneumatic_mekanism_gates.js",
    r"kubejs\server_scripts\05_dark_magic_dimensions.js",
    # Category 3: Interactive Dialogue & User Feedback
    r"kubejs\server_scripts\07_draconic_endgame.js",
    r"kubejs\server_scripts\21_fix_illusioner_crash.js",
    r"kubejs\server_scripts\30_remove_create_sa_copper.js",
    r"kubejs\client_scripts\30_hide_create_sa_copper.js",
    r"kubejs\server_scripts\convert_chance.py",
    r"kubejs\server_scripts\clean_suppressor.py",
    r"kubejs\server_scripts\fix_datapacks.py",
    r"kubejs\server_scripts\fix_fluid.py",
    r"kubejs\server_scripts\fix_transitional.py",
    # Category 4: PEAK Expert Mode Progression Suite (Server Scripts)
    r"kubejs\server_scripts\00_recipe_fixer.js",
    r"kubejs\server_scripts\02_create_era_gates.js",
    r"kubejs\server_scripts\04_magic_integration.js",
    r"kubejs\server_scripts\06_enderio_ae2.js",
    r"kubejs\server_scripts\08_reliquary_balance.js",
    r"kubejs\server_scripts\09_custom_loot_tables.js",
    r"kubejs\server_scripts\10_avaritia_final_polish.js",
    r"kubejs\server_scripts\11_end_gating.js",
    r"kubejs\server_scripts\12_admin_commands.js",
    r"kubejs\server_scripts\12_food_buffs.js",
    r"kubejs\server_scripts\13_simply_mythics_loot.js",
    r"kubejs\server_scripts\13a_food_overhaul_farmersdelight.js",
    r"kubejs\server_scripts\13b_food_overhaul_dimensions.js",
    r"kubejs\server_scripts\13c_food_overhaul_creatures.js",
    r"kubejs\server_scripts\13d_food_overhaul_magic.js",
    r"kubejs\server_scripts\13e_food_fixes.js",
    r"kubejs\server_scripts\14_waystone_balance.js",
    r"kubejs\server_scripts\15_loot_nerfs.js",
    r"kubejs\server_scripts\16_recipes_and_balance.js",
    r"kubejs\server_scripts\17_goblin_trades.js",
    r"kubejs\server_scripts\18_boss_duplicator.js",
    r"kubejs\server_scripts\19_mob_gear.js",
    r"kubejs\server_scripts\20_disable_bugged_spells.js",
    r"kubejs\server_scripts\20_disable_bugged_spells_data.js",
    r"kubejs\server_scripts\21_backpack_upgrades.js",
    r"kubejs\server_scripts\22_apotheosis_gear_sets.js",
    r"kubejs\server_scripts\23_fix_illager_weapons.js",
    r"kubejs\server_scripts\23_zenith_saber.js",
    r"kubejs\server_scripts\24_pixie_spawn_limiter.js",
    r"kubejs\server_scripts\25_hardcoded_minibosses.js",
    r"kubejs\server_scripts\26_mob_max_health_fix.js",
    r"kubejs\server_scripts\32_ban_raid_blimp.js",
    r"kubejs\server_scripts\33_remove_vampirism_coatings.js",
    r"kubejs\server_scripts\34_ban_ender_eye.js",
    r"kubejs\server_scripts\41_iaf_loot_buff.js",
    r"kubejs\server_scripts\50_xp_fluids_unification.js",
    r"kubejs\server_scripts\60_dragonforge_materials.js",
    r"kubejs\server_scripts\61_spellbook_assembly.js",
    r"kubejs\server_scripts\apotheosis_auto_tiers.js",
    r"kubejs\server_scripts\dump_ids.js",
    r"kubejs\server_scripts\fix_illusioner_crash.js",
    r"kubejs\server_scripts\nerf_irons_jewelry.js",
    # Category 4 (cont): Client Scripts
    r"kubejs\client_scripts\14_translations.js",
    r"kubejs\client_scripts\32_hide_raid_blimp.js",
    r"kubejs\client_scripts\35_hide_technical_items.js",
    r"kubejs\client_scripts\36_hide_incomplete_items.js",
    r"kubejs\client_scripts\37_hide_banned_and_disabled_items.js",
    r"kubejs\client_scripts\main.js",
    # Category 4 (cont): Startup Scripts
    r"kubejs\startup_scripts\14_waystone_balance.js",
    r"kubejs\startup_scripts\40_iaf_durability_buff.js",
    r"kubejs\startup_scripts\50_avarice_swords_damage.js",
    r"kubejs\startup_scripts\60_spellbook_rebalance.js",
    r"kubejs\startup_scripts\custom_items.js",
    r"kubejs\startup_scripts\fix_malum_watchdog.js",
    r"kubejs\startup_scripts\main.js",
    # Category 5: Root Diagnostic Python Utilities
    r"check_mods.py",
    r"check_shine.py",
    r"check_specific.py",
    r"deep_check.py",
    r"find_recipes.py",
    r"fix_fluids.py",
    r"fix_json.py",
    r"fix_suppressor.py",
    r"fix_syntax.py",
    r"fix_syntax_errors.py",
    r"generate_dummy_recipes.py",
    r"generate_physical_datapack.py",
    r"get_missing_items.py",
    r"replace_missing_items.py",
    r"rewrite_20_fixed_datapacks.py",
    # Category 6: AI-Assisted Narrative & Quest Content
    r"ore_report.md",
    r"config\ftbquests\quests\lang\en_us.snbt"
]

def verify_all_files():
    results = []
    missing = []
    
    for rel in ALL_CITED_FILES:
        abs_path = os.path.join(ROOT_DIR, rel)
        exists = os.path.exists(abs_path)
        line_count = 0
        file_size = 0
        if exists:
            try:
                with open(abs_path, 'r', encoding='utf-8', errors='ignore') as f:
                    line_count = len(f.readlines())
                file_size = os.path.getsize(abs_path)
            except Exception as e:
                pass
        else:
            missing.append(rel)

        results.append({
            "relative_path": rel,
            "absolute_path": abs_path,
            "exists": exists,
            "line_count": line_count,
            "size_bytes": file_size
        })

    print(f"Total files checked: {len(ALL_CITED_FILES)}")
    print(f"Files found: {len(ALL_CITED_FILES) - len(missing)}")
    print(f"Missing files: {len(missing)}")
    
    out_file = os.path.join(r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\.agents\worker_1", "all_files_verification.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    return results

if __name__ == "__main__":
    verify_all_files()
