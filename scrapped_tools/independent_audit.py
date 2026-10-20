import os
import sys
import re
import subprocess
import json

sys.stdout.reconfigure(encoding='utf-8')

def audit_snbt():
    snbt_path = r'minecraft/config/ftbquests/quests/lang/en_us.snbt'
    print(f"=== Auditing {snbt_path} ===")
    with open(snbt_path, 'r', encoding='utf-8') as f:
        text = f.read()
        lines = text.splitlines(keepends=True)

    print(f"Total lines: {len(lines)}, Total characters: {len(text)}")

    # 1. Surgical check
    surg_matches = []
    for idx, line in enumerate(lines, 1):
        m = re.findall(r'surgic\w*', line, re.IGNORECASE)
        if m:
            surg_matches.append((idx, m, line.strip()))
    print(f"[SNBT] Occurrences of 'surgical'/'surgically': {len(surg_matches)}")

    # 2. Core buzzwords check with broad word boundaries & color code stripping
    core_buzzwords = ['surgical', 'cornerstone', 'unleash', 'meticulous', 'mastery', 'delv', 'embark']
    core_found = []
    for idx, line in enumerate(lines, 1):
        clean = re.sub(r'&[0-9a-fk-orA-FK-OR#]', '', line)
        for w in core_buzzwords:
            m = re.findall(r'\b' + w + r'\w*', clean, re.IGNORECASE)
            if m:
                core_found.append((idx, w, m, line.strip()))
    print(f"[SNBT] Core buzzwords count: {len(core_found)}")
    for cf in core_found:
        print(f"   Line {cf[0]} [{cf[1]}]: {cf[2]} -> {cf[3]}")

    # 3. Literal '& ' check
    amp_space = []
    for idx, line in enumerate(lines, 1):
        if '& ' in line:
            amp_space.append((idx, line.strip()))
    print(f"[SNBT] Literal '& ' violations count: {len(amp_space)}")

    # 4. Invalid formatting code check
    invalid_amp = []
    for idx, line in enumerate(lines, 1):
        for m in re.finditer(r'&([^0-9a-fk-orA-FK-OR#])', line):
            invalid_amp.append((idx, m.group(0), line.strip()))
    print(f"[SNBT] Invalid formatting codes count: {len(invalid_amp)}")

    # 5. Root compound & bracket balance
    stripped = text.strip()
    starts_curly = stripped.startswith('{')
    ends_curly = stripped.endswith('}')
    open_curly = text.count('{')
    close_curly = text.count('}')
    open_square = text.count('[')
    close_square = text.count(']')
    print(f"[SNBT] Root compound starts with '{{': {starts_curly}, ends with '}}': {ends_curly}")
    print(f"[SNBT] Curly balance: {open_curly} open, {close_curly} close (balanced: {open_curly == close_curly})")
    print(f"[SNBT] Square balance: {open_square} open, {close_square} close (balanced: {open_square == close_square})")

    # 6. Check unescaped quotes within double-quoted strings
    quote_errors = []
    for idx, line in enumerate(lines, 1):
        l = line.strip()
        if not l or l == '{' or l == '}':
            continue
        un_escaped = re.sub(r'\\"', '', l)
        q_count = un_escaped.count('"')
        if q_count % 2 != 0:
            quote_errors.append((idx, q_count, l))
    print(f"[SNBT] Lines with unbalanced unescaped quotes: {len(quote_errors)}")

    # 7. Check entire ftbquests directory for surgical
    ftb_dir = r'minecraft/config/ftbquests'
    all_ftb_surg = []
    for root, _, files in os.walk(ftb_dir):
        for f in files:
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='replace') as fp:
                for l_idx, l in enumerate(fp, 1):
                    if re.search(r'\bsurgic', l, re.I):
                        all_ftb_surg.append((p, l_idx, l.strip()))
    print(f"[FTB Quests Dir] Total 'surgic*' in entire directory: {len(all_ftb_surg)}")

def audit_kubejs_scripts():
    print("\n=== Auditing KubeJS Scripts ===")
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
    print(f"Target modified files count: {len(target_files)}")

    # Check 1: surgical / surgically in ANY kubejs file
    all_kubejs_surg = []
    base_kubejs = r'minecraft/kubejs'
    for root, _, files in os.walk(base_kubejs):
        for f in files:
            if f.endswith('.js'):
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8', errors='replace') as fp:
                    for l_idx, l in enumerate(fp, 1):
                        if re.search(r'\bsurgic', l, re.I):
                            all_kubejs_surg.append((p, l_idx, l.strip()))
    print(f"[KubeJS] Total 'surgic*' in all KubeJS files: {len(all_kubejs_surg)}")

    # Check 2: First-person plural ("we", "our") in 27 files
    plural_hits = []
    for tf in target_files:
        if not os.path.exists(tf):
            print(f"WARNING: Target file missing: {tf}")
            continue
        with open(tf, 'r', encoding='utf-8', errors='replace') as fp:
            for l_idx, line in enumerate(fp, 1):
                # Search for whole words \bwe\b or \bour\b
                m = re.findall(r'\b(we|our)\b', line, re.IGNORECASE)
                if m:
                    plural_hits.append((tf, l_idx, m, line.strip()))
    print(f"[Target 27 files] First-person plural ('we'/'our') hits: {len(plural_hits)}")
    for ph in plural_hits:
        print(f"   {ph[0]}:{ph[1]} {ph[2]} -> {ph[3]}")

    # Check 3: Informal self-talk checks in 27 files
    informal_patterns = [
        r'just in case',
        r'feel earned',
        r'they shamble',
        r'died with them',
        r'you can\'t skip',
        r'who knows',
        r'hacky',
        r'todo'
    ]
    informal_hits = []
    for tf in target_files:
        with open(tf, 'r', encoding='utf-8', errors='replace') as fp:
            for l_idx, line in enumerate(fp, 1):
                for pat in informal_patterns:
                    if re.search(pat, line, re.I):
                        informal_hits.append((tf, l_idx, pat, line.strip()))
    print(f"[Target 27 files] Informal developer self-talk hits: {len(informal_hits)}")
    for ih in informal_hits:
        print(f"   {ih[0]}:{ih[1]} [{ih[2]}] -> {ih[3]}")

    # Check 4: Syntax validation via node -c across all 89 files
    passed = 0
    failed = []
    total_js = 0
    for root, _, files in os.walk(base_kubejs):
        for f in files:
            if f.endswith('.js'):
                total_js += 1
                p = os.path.join(root, f)
                r = subprocess.run(['node', '-c', p], capture_output=True, text=True)
                if r.returncode != 0:
                    failed.append((p, r.stderr.strip()))
                else:
                    passed += 1
    print(f"[Syntax Validation] Total .js files tested: {total_js}, Passed: {passed}, Failed: {len(failed)}")
    for fl in failed:
        print(f"   FAILED: {fl[0]} -> {fl[1]}")

def check_dragon_mechanics():
    print("\n=== Checking Stage 5 Dragon Mechanics in startup_scripts/custom_items.js ===")
    p = r'minecraft/kubejs/startup_scripts/custom_items.js'
    if not os.path.exists(p):
        print(f"ERROR: {p} does not exist!")
        return
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
        lines = text.splitlines()

    print(f"Total lines in custom_items.js: {len(lines)}")
    # Print lines 80 to 110 specifically
    for idx in range(80, min(115, len(lines))):
        print(f"Line {idx+1}: {repr(lines[idx])}")

    r = subprocess.run(['git', 'diff', p], capture_output=True, text=True)
    if r.stdout.strip():
        print(f"git diff of {p}:")
        print(r.stdout)
    else:
        print(f"git diff of {p} is EMPTY (unmodified, 100% preserved).")

if __name__ == '__main__':
    audit_snbt()
    audit_kubejs_scripts()
    check_dragon_mechanics()
