import subprocess
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_files = [
    "minecraft/kubejs/client_scripts/apokinetics_unregister.js",
    "minecraft/kubejs/server_scripts/00_recipe_fixer.js",
    "minecraft/kubejs/server_scripts/02_create_era_gates.js",
    "minecraft/kubejs/server_scripts/04_magic_integration.js",
    "minecraft/kubejs/server_scripts/05_dark_magic_dimensions.js",
    "minecraft/kubejs/server_scripts/06_enderio_ae2.js",
    "minecraft/kubejs/server_scripts/07_draconic_endgame.js",
    "minecraft/kubejs/server_scripts/08_reliquary_balance.js",
    "minecraft/kubejs/server_scripts/09_custom_loot_tables.js",
    "minecraft/kubejs/server_scripts/10_avaritia_final_polish.js",
    "minecraft/kubejs/server_scripts/12_food_buffs.js",
    "minecraft/kubejs/server_scripts/15_loot_nerfs.js",
    "minecraft/kubejs/server_scripts/17_goblin_trades.js",
    "minecraft/kubejs/server_scripts/18_boss_duplicator.js",
    "minecraft/kubejs/server_scripts/20_disable_bugged_spells.js",
    "minecraft/kubejs/server_scripts/22_apotheosis_gear_sets.js",
    "minecraft/kubejs/server_scripts/23_zenith_saber.js",
    "minecraft/kubejs/server_scripts/25_hardcoded_minibosses.js",
    "minecraft/kubejs/server_scripts/27_vampire_pillager.js",
    "minecraft/kubejs/server_scripts/50_xp_fluids_unification.js",
    "minecraft/kubejs/server_scripts/expert_mode_recipes.js",
    "minecraft/kubejs/server_scripts/random_gateways.js",
    "minecraft/kubejs/startup_scripts/40_iaf_durability_buff.js",
    "minecraft/kubejs/startup_scripts/apokinetics_unregister.js",
    "minecraft/kubejs/startup_scripts/block_factory_buffs.js",
    "minecraft/kubejs/startup_scripts/fix_malum_watchdog.js",
    "minecraft/kubejs/startup_scripts/vampillager_entity.js"
]

print("=== Checking Git Diffs of all 27 files ===")

suspicious_changes = []

for tf in target_files:
    r = subprocess.run(['git', 'diff', tf], capture_output=True, encoding='utf-8', errors='replace')
    diff = r.stdout or ""
    if not diff.strip():
        # Check if file is untracked
        print(f"File {tf}: no git diff (might be untracked).")
        continue

    # Inspect added/removed lines
    removed_lines = []
    added_lines = []
    for line in diff.splitlines():
        if line.startswith('---') or line.startswith('+++') or line.startswith('@@'):
            continue
        if line.startswith('-'):
            removed_lines.append(line[1:].strip())
        elif line.startswith('+'):
            added_lines.append(line[1:].strip())

    # Check each removed/added line: is it a comment or console log?
    for rem in removed_lines:
        is_comment = rem.startswith('//') or rem.startswith('/*') or rem.startswith('*')
        is_log = 'console.info' in rem or 'console.error' in rem or 'console.log' in rem
        is_trailing_comment = '//' in rem
        if not (is_comment or is_log or is_trailing_comment):
            suspicious_changes.append((tf, 'REMOVED NON-COMMENT', rem))

    for add in added_lines:
        is_comment = add.startswith('//') or add.startswith('/*') or add.startswith('*')
        is_log = 'console.info' in add or 'console.error' in add or 'console.log' in add
        is_trailing_comment = '//' in add
        if not (is_comment or is_log or is_trailing_comment):
            suspicious_changes.append((tf, 'ADDED NON-COMMENT', add))

print(f"Total suspicious/functional diffs found across 27 files: {len(suspicious_changes)}")
for sc in suspicious_changes:
    print(f"   {sc[0]} [{sc[1]}]: {sc[2]}")
