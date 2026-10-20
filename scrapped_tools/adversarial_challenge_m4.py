"""
Adversarial Verification Suite for Milestone 4 (Sanitization Verification).
Validates:
1. 'surgic' across minecraft/kubejs and minecraft/config/ftbquests
2. 'Blockbench' in minecraft/kubejs/assets/
3. 'en_us.snbt' and FTB quests buzzwords, literal '& ', invalid formatting codes, and bracket balance
4. 'minecraft/kubejs/' developer self-talk, inner dialogue, first-person plurals, and JS syntax compilation
"""

import os
import re
import json
import subprocess
import sys

def test_surgic(base_dirs):
    print("=== TEST 1: SURGIC (CASE-INSENSITIVE) SEARCH ===")
    total_files = 0
    hits = []
    pattern = re.compile(r'surgic', re.I)
    for d in base_dirs:
        for root, _, files in os.walk(d):
            for f in files:
                total_files += 1
                p = os.path.join(root, f)
                try:
                    with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                        for idx, line in enumerate(fp, 1):
                            if pattern.search(line):
                                hits.append((p, idx, line.strip()))
                except Exception as e:
                    hits.append((p, 0, f"Error reading file: {e}"))
    print(f"Total files scanned across {base_dirs}: {total_files}")
    print(f"Total 'surgic' hits found: {len(hits)}")
    for p, idx, line in hits:
        print(f"  FAILED: {p}:{idx}: {line}")
    return len(hits) == 0, hits

def test_blockbench(assets_dir):
    print("\n=== TEST 2: BLOCKBENCH SEARCH IN ASSETS ===")
    total_json = 0
    bb_hits = []
    made_bb_hits = []
    zanderest_credits = 0
    peak_credits = 0
    json_parse_errors = []

    for root, _, files in os.walk(assets_dir):
        for f in files:
            p = os.path.join(root, f)
            if f.endswith('.json'):
                total_json += 1
                try:
                    with open(p, 'r', encoding='utf-8') as fp:
                        raw = fp.read()
                        if 'made with blockbench' in raw.lower():
                            made_bb_hits.append((p, "Made with Blockbench"))
                        if 'blockbench' in raw.lower():
                            bb_hits.append((p, "Blockbench"))
                        if 'zanderest' in raw:
                            zanderest_credits += 1
                        if '"credit": "PEAK"' in raw or '"credit":"PEAK"' in raw:
                            peak_credits += 1
                        json.loads(raw)
                except Exception as e:
                    json_parse_errors.append((p, str(e)))

    print(f"Total JSON files scanned in assets: {total_json}")
    print(f"Blockbench occurrences: {len(bb_hits)}")
    print(f"'Made with Blockbench' occurrences: {len(made_bb_hits)}")
    print(f"JSON parse errors: {len(json_parse_errors)}")
    print(f"zanderest credits preserved: {zanderest_credits}")
    print(f"PEAK credits preserved: {peak_credits}")

    success = (len(bb_hits) == 0 and len(made_bb_hits) == 0 and len(json_parse_errors) == 0 and zanderest_credits == 25 and peak_credits == 1)
    return success, {
        "bb_hits": bb_hits,
        "made_bb_hits": made_bb_hits,
        "json_parse_errors": json_parse_errors,
        "zanderest_credits": zanderest_credits,
        "peak_credits": peak_credits
    }

def test_ftb_quests(quests_dir):
    print("\n=== TEST 3: FTB QUESTS LOCALIZATION ADVERSARIAL SCAN ===")
    snbt_file = os.path.join(quests_dir, "quests", "lang", "en_us.snbt")
    
    color_code_pattern = re.compile(r'&[0-9a-fk-orA-FK-OR#]')
    core_buzzwords = [
        'surgical', 'delve', 'cornerstone', 'unleash', 'meticulous', 'mastery', 'embark'
    ]
    
    # Exceptions that are genuine in-game item or progression names
    allowed_exceptions = [
        # Example: "The Master's Wand", "Master of the 25 Archetypes"
        "master of", "master's wand"
    ]

    buzzword_hits = []
    literal_amp_hits = []
    invalid_format_hits = []
    
    with open(snbt_file, 'r', encoding='utf-8') as fp:
        raw_snbt = fp.read()
        lines = raw_snbt.splitlines()

    for idx, line in enumerate(lines, 1):
        clean = color_code_pattern.sub('', line)
        for w in core_buzzwords:
            # Match word boundary
            matches = re.finditer(r'\b' + re.escape(w) + r'\w*', clean, re.I)
            for m in matches:
                matched_str = m.group(0).lower()
                # Check if it's mastery or delve or embark etc.
                buzzword_hits.append((idx, matched_str, line.strip()))

        # Check literal '& '
        if '& ' in line:
            literal_amp_hits.append((idx, line.strip()))

        # Check invalid format codes: & followed by something that is not valid code
        # Valid: 0-9, a-f, k-o, r, # (case insensitive)
        for m in re.finditer(r'&(.)', line):
            char = m.group(1)
            if not re.match(r'[0-9a-fk-orA-FK-OR#]', char):
                invalid_format_hits.append((idx, m.group(0), line.strip()))

    # Bracket and structural validation
    stripped = raw_snbt.strip()
    root_valid = stripped.startswith('{') and stripped.endswith('}')
    curly_open = raw_snbt.count('{')
    curly_close = raw_snbt.count('}')
    square_open = raw_snbt.count('[')
    square_close = raw_snbt.count(']')
    brackets_balanced = (curly_open == curly_close and square_open == square_close and curly_open == 1)

    print(f"Total lines in en_us.snbt: {len(lines)}")
    print(f"Core buzzwords found: {len(buzzword_hits)}")
    for h in buzzword_hits:
        print(f"  BUZZWORD: Line {h[0]}: {h[1]} -> {h[2]}")
    print(f"Literal '& ' formatting violations: {len(literal_amp_hits)}")
    for h in literal_amp_hits:
        print(f"  LITERAL_AMP: Line {h[0]}: {h[1]}")
    print(f"Invalid '&<char>' formatting codes: {len(invalid_format_hits)}")
    for h in invalid_format_hits:
        print(f"  INVALID_FORMAT: Line {h[0]}: {h[1]} in {h[2]}")
    print(f"SNBT root compound and bracket balance: {brackets_balanced} (curly: {curly_open}/{curly_close}, square: {square_open}/{square_close})")

    # Also scan all chapters and reward tables for any unexpected text containing buzzwords or literal '& '
    chapter_hits = []
    chapter_amp_hits = []
    for sub in ["chapters", "reward_tables"]:
        sub_dir = os.path.join(quests_dir, "quests", sub)
        if not os.path.exists(sub_dir):
            continue
        for f in os.listdir(sub_dir):
            if f.endswith('.snbt'):
                cp = os.path.join(sub_dir, f)
                with open(cp, 'r', encoding='utf-8') as cfp:
                    for cidx, cline in enumerate(cfp, 1):
                        for w in core_buzzwords:
                            if re.search(r'\b' + re.escape(w) + r'\w*', cline, re.I):
                                chapter_hits.append((f"{sub}/{f}", cidx, cline.strip()))
                        if '& ' in cline:
                            chapter_amp_hits.append((f"{sub}/{f}", cidx, cline.strip()))
    print(f"Quests subfiles scanned (chapters & reward tables). Buzzwords: {len(chapter_hits)}, Literal '& ': {len(chapter_amp_hits)}")
    for ch in chapter_hits:
        print(f"  CHAPTER_HIT: {ch[0]}:{ch[1]}: {ch[2]}")
    for ca in chapter_amp_hits:
        print(f"  CHAPTER_AMP: {ca[0]}:{ca[1]}: {ca[2]}")

    success = (len(buzzword_hits) == 0 and len(literal_amp_hits) == 0 and len(invalid_format_hits) == 0 and brackets_balanced and len(chapter_hits) == 0 and len(chapter_amp_hits) == 0)
    return success, {
        "buzzword_hits": buzzword_hits,
        "literal_amp_hits": literal_amp_hits,
        "invalid_format_hits": invalid_format_hits,
        "brackets_balanced": brackets_balanced,
        "chapter_hits": chapter_hits
    }

def test_kubejs_scripts(kubejs_dir):
    print("\n=== TEST 4: KUBEJS SCRIPTS COMMENT & SYNTAX ADVERSARIAL SCAN ===")
    js_files = []
    for root, _, files in os.walk(kubejs_dir):
        for f in files:
            if f.endswith('.js'):
                js_files.append(os.path.join(root, f))

    plural_hits = []
    inner_monologue_hits = []
    surgic_hits = []
    syntax_errors = []

    # Patterns for first person plural
    # e.g., "we use", "our custom", "we keep", "we add", "we don't", "we've", "we'll"
    plural_pattern = re.compile(r'\b(we\s+(?:use|keep|add|have|can|can\'t|cannot|don\'t|do|are|make|remove|strip|want|need|should|will|replace)|our\s+(?:custom|new|gateway|modpack|system|infrastructure))\b', re.I)

    # Patterns for developer conversational self-talk / inner-dialogue
    monologue_patterns = [
        re.compile(r'\bjust in case\b', re.I),
        re.compile(r'\bit died with them\b', re.I),
        re.compile(r'\bthey shamble\b', re.I),
        re.compile(r'\bshould feel earned\b', re.I),
        re.compile(r'\bYou can\'t skip\b', re.I),
        re.compile(r'\bfor an insane price\b', re.I),
        re.compile(r'\bactually worth crafting\b', re.I)
    ]

    for p in js_files:
        # Check syntax using node -c
        res = subprocess.run(['node', '-c', p], capture_output=True, text=True)
        if res.returncode != 0:
            syntax_errors.append((p, res.stderr.strip()))

        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            for idx, line in enumerate(fp, 1):
                # Ignore third party mod flavor texts or disabled datapacks if known
                rel = os.path.relpath(p, kubejs_dir).replace('\\', '/')
                # Test surgic
                if re.search(r'\bsurgic', line, re.I):
                    surgic_hits.append((rel, idx, line.strip()))
                
                # Test plural aggressively in comments
                if '//' in line or '/*' in line:
                    comment_part = line[line.find('//')+2:] if '//' in line else line
                    # check for standalone 'we' or 'our'
                    m = re.search(r'\b(we|our)\b', comment_part, re.I)
                    if m:
                        if rel == 'server_scripts/20_fixed_datapacks.js' and 'bouncy' in line:
                            continue
                        plural_hits.append((rel, idx, m.group(0), line.strip()))

                # Test monologue
                for pat in monologue_patterns:
                    if pat.search(line):
                        inner_monologue_hits.append((rel, idx, line.strip()))

    print(f"Total .js files scanned: {len(js_files)}")
    print(f"Node.js syntax errors: {len(syntax_errors)}")
    for se in syntax_errors:
        print(f"  SYNTAX_ERROR: {se[0]}: {se[1]}")
    print(f"'surgic' hits in KubeJS: {len(surgic_hits)}")
    for sh in surgic_hits:
        print(f"  SURGIC: {sh[0]}:{sh[1]}: {sh[2]}")
    print(f"First-person plural hits: {len(plural_hits)}")
    for ph in plural_hits:
        print(f"  PLURAL: {ph[0]}:{ph[1]}: '{ph[2]}' in: {ph[3]}")
    print(f"Inner monologue / editorializing hits: {len(inner_monologue_hits)}")
    for mh in inner_monologue_hits:
        print(f"  MONOLOGUE: {mh[0]}:{mh[1]}: {mh[2]}")

    success = (len(syntax_errors) == 0 and len(surgic_hits) == 0 and len(plural_hits) == 0 and len(inner_monologue_hits) == 0)
    return success, {
        "syntax_errors": syntax_errors,
        "surgic_hits": surgic_hits,
        "plural_hits": plural_hits,
        "inner_monologue_hits": inner_monologue_hits,
        "total_files": len(js_files)
    }

def main():
    base_kubejs = r'minecraft/kubejs'
    base_quests = r'minecraft/config/ftbquests'
    base_assets = r'minecraft/kubejs/assets'

    t1_pass, t1_res = test_surgic([base_kubejs, base_quests])
    t2_pass, t2_res = test_blockbench(base_assets)
    t3_pass, t3_res = test_ftb_quests(base_quests)
    t4_pass, t4_res = test_kubejs_scripts(base_kubejs)

    print("\n===============================")
    print("FINAL CHALLENGE SUMMARY VERDICT")
    print("===============================")
    print(f"Test 1 (Surgic zero-occurrence): {'PASS' if t1_pass else 'FAIL'}")
    print(f"Test 2 (Blockbench metadata removal & JSON): {'PASS' if t2_pass else 'FAIL'}")
    print(f"Test 3 (FTB Quests tone, buzzwords, & formatting): {'PASS' if t3_pass else 'FAIL'}")
    print(f"Test 4 (KubeJS plurals, comments, & compilation): {'PASS' if t4_pass else 'FAIL'}")

    all_pass = t1_pass and t2_pass and t3_pass and t4_pass
    print(f"OVERALL VERDICT: {'APPROVE' if all_pass else 'REQUEST_CHANGES'}")
    if not all_pass:
        sys.exit(1)

if __name__ == '__main__':
    main()
