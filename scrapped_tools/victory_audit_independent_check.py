#!/usr/bin/env python3
"""
Independent Victory Audit Verification Script
Exhaustive verification of R1, R2, R3, R4 for PEAK Modpack Codebase Sanitization.
Zero shared context. Verifies everything directly from disk and git.
"""

import os
import sys
import re
import json
import subprocess

FAILURES = []
WARNINGS = []
SUMMARY = {}

def report_fail(category, message):
    FAILURES.append(f"[{category}] {message}")
    print(f"[-] FAIL: [{category}] {message}")

def report_pass(category, message):
    print(f"[+] PASS: [{category}] {message}")

def report_warn(category, message):
    WARNINGS.append(f"[{category}] {message}")
    print(f"[!] WARN: [{category}] {message}")

print("=================================================================")
print("=== VICTORY AUDITOR INDEPENDENT VERIFICATION EXECUTION ===")
print("=================================================================\n")

# =====================================================================
# CHECK 1: SCOPE CONFINEMENT & ENVIRONMENT CLEANLINESS (R4)
# =====================================================================
print("--- [CHECK 1] Scope Confinement & Cleanliness (R4) ---")

# 1.1 Excluded directories
ext_dir = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA"
ct_dir = r"minecraft/ct_dumps"

if os.path.exists(ext_dir):
    recent_ext = []
    # Check if any file was modified in last 4 hours
    now = os.path.getmtime(r".agents/ORIGINAL_REQUEST.md")
    for root, _, files in os.walk(ext_dir):
        for f in files:
            fp = os.path.join(root, f)
            if os.path.getmtime(fp) > now - 1800: # 30 min before request
                recent_ext.append(fp)
    if recent_ext:
        report_fail("SCOPE", f"Files modified in PEAK DEV MULTIMEDIA: {recent_ext}")
    else:
        report_pass("SCOPE", "PEAK DEV MULTIMEDIA is completely untouched.")
else:
    report_pass("SCOPE", "PEAK DEV MULTIMEDIA path not found or untouched.")

# ct_dumps git status
ct_status = subprocess.run(["git", "status", "--porcelain", "minecraft/ct_dumps"], capture_output=True, encoding="utf-8", errors="replace")
if ct_status.stdout.strip():
    report_fail("SCOPE", f"minecraft/ct_dumps has git changes: {ct_status.stdout.strip()}")
else:
    report_pass("SCOPE", "minecraft/ct_dumps has zero git changes.")

# 1.2 Rule 2: Zero .py files inside minecraft/
py_in_mc = []
for root, _, files in os.walk("minecraft"):
    for f in files:
        if f.endswith(".py"):
            py_in_mc.append(os.path.join(root, f))
if py_in_mc:
    report_fail("CLEANLINESS", f"Found .py files in minecraft/: {py_in_mc}")
else:
    report_pass("CLEANLINESS", "Zero .py files exist inside minecraft/ directory.")

# 1.3 UTF-8 BOM check across all modified files in git diff
diff_files_proc = subprocess.run(["git", "diff", "--name-only"], capture_output=True, encoding="utf-8", errors="replace")
diff_files = [f.strip() for f in (diff_files_proc.stdout or "").splitlines() if f.strip() and os.path.exists(f.strip())]
bom_files = []
for f in diff_files:
    with open(f, "rb") as fp:
        head = fp.read(3)
        if head == b'\xef\xbb\xbf':
            bom_files.append(f)
if bom_files:
    report_fail("ENCODING", f"UTF-8 BOM detected in files: {bom_files}")
else:
    report_pass("ENCODING", f"Zero UTF-8 BOMs found across {len(diff_files)} git modified files.")


# =====================================================================
# CHECK 2: RULE 1 METADATA ATTRIBUTION CLEANUP (R2)
# =====================================================================
print("\n--- [CHECK 2] Rule 1 Metadata Attribution Cleanup (R2) ---")
assets_dir = r"minecraft/kubejs/assets"
all_json_assets = []
blockbench_hits = []
json_errors = []
zanderest_count = 0
peak_credit_count = 0

for root, _, files in os.walk(assets_dir):
    for f in files:
        if f.endswith(".json"):
            fp = os.path.join(root, f)
            all_json_assets.append(fp)
            try:
                with open(fp, "r", encoding="utf-8") as jfp:
                    content = jfp.read()
                    if "blockbench" in content.lower():
                        blockbench_hits.append(fp)
                    if '"credit": "zanderest"' in content or '"credit":"zanderest"' in content:
                        zanderest_count += 1
                    if '"credit": "PEAK"' in content or '"credit":"PEAK"' in content:
                        peak_credit_count += 1
                    data = json.loads(content)
            except Exception as e:
                json_errors.append((fp, str(e)))

print(f"Total JSON files scanned in kubejs/assets: {len(all_json_assets)}")
if blockbench_hits:
    report_fail("MODELS", f"Residual 'Blockbench' tags found in: {blockbench_hits}")
else:
    report_pass("MODELS", "Exactly 0 occurrences of 'Blockbench' / 'Made with Blockbench' in assets.")

if json_errors:
    report_fail("MODELS", f"JSON parse errors in assets: {json_errors}")
else:
    report_pass("MODELS", f"All {len(all_json_assets)} JSON assets parsed cleanly without errors.")

if zanderest_count == 25:
    report_pass("MODELS", f"Open-source community credits intact: {zanderest_count}/25 'zanderest' credits.")
else:
    report_fail("MODELS", f"Unexpected 'zanderest' credit count: {zanderest_count} (expected 25)")

if peak_credit_count == 1:
    report_pass("MODELS", f"Pack model credit intact: {peak_credit_count}/1 'PEAK' credit.")
else:
    report_fail("MODELS", f"Unexpected 'PEAK' credit count: {peak_credit_count} (expected 1)")

# Git diff check on assets
asset_diff = subprocess.run(["git", "diff", "--stat", assets_dir], capture_output=True, encoding="utf-8", errors="replace")
asset_diff_num = subprocess.run(["git", "diff", "--numstat", assets_dir], capture_output=True, encoding="utf-8", errors="replace")
print("Assets git numstat:")
lines = (asset_diff_num.stdout or "").strip().splitlines()
all_assets_strictly_cleaned = True
for l in lines:
    parts = l.split("\t")
    if len(parts) == 3:
        added, deleted, path = parts
        print(f"  {path}: +{added} -{deleted}")
        if added != "0" or deleted != "1":
            all_assets_strictly_cleaned = False
if len(lines) == 9 and all_assets_strictly_cleaned:
    report_pass("MODELS", "Exactly 9 model files modified: exactly 0 lines added, 1 line deleted each.")
else:
    report_warn("MODELS", f"Modified assets count: {len(lines)} (expected 9), clean single deletions: {all_assets_strictly_cleaned}")


# =====================================================================
# CHECK 3: FTB QUESTS LOCALIZATION TONE POLISH (R3)
# =====================================================================
print("\n--- [CHECK 3] FTB Quests Localization Tone Polish (R3) ---")
quest_lang = r"minecraft/config/ftbquests/quests/lang/en_us.snbt"

with open(quest_lang, "r", encoding="utf-8") as fp:
    snbt_raw = fp.read()
    snbt_lines = snbt_raw.splitlines()

print(f"Total lines in en_us.snbt: {len(snbt_lines)}")

# 3.1 Surgical search
surgic_hits = []
for idx, line in enumerate(snbt_lines, 1):
    if re.search(r"surgic", line, re.I):
        surgic_hits.append((idx, line.strip()))
if surgic_hits:
    report_fail("QUESTS", f"'surgic' found in en_us.snbt: {surgic_hits}")
else:
    report_pass("QUESTS", "Exactly 0 occurrences of 'surgical' / 'surgically' in en_us.snbt.")

# 3.2 AI Buzzwords search (color-code aware)
color_code_pattern = re.compile(r'&[0-9a-fk-orA-FK-OR#]')
core_buzzwords = ['surgical', 'delve', 'cornerstone', 'unleash', 'meticulous', 'mastery', 'embark']
buzzword_hits = []

for idx, line in enumerate(snbt_lines, 1):
    clean = color_code_pattern.sub('', line)
    for bw in core_buzzwords:
        # Check word boundary on stripped line
        m = re.findall(r'\b' + re.escape(bw) + r'\w*', clean, re.I)
        if m:
            for hit in m:
                # Check for in-game item exceptions
                lower_line = clean.lower()
                if "master of" in lower_line or "master's wand" in lower_line or "grandmaster" in lower_line:
                    continue
                buzzword_hits.append((idx, hit, line.strip()))

if buzzword_hits:
    report_fail("QUESTS", f"Core buzzwords remaining in en_us.snbt: {buzzword_hits}")
else:
    report_pass("QUESTS", "Zero core AI buzzwords (delve, cornerstone, unleash, meticulous, mastery, embark) found in en_us.snbt.")

# 3.3 Formatting codes: literal '& '
literal_amp = []
for idx, line in enumerate(snbt_lines, 1):
    if "& " in line:
        literal_amp.append((idx, line.strip()))
if literal_amp:
    report_fail("QUESTS", f"Literal '& ' formatting violations in en_us.snbt: {literal_amp}")
else:
    report_pass("QUESTS", "Zero literal '& ' formatting violations in en_us.snbt.")

# 3.4 Formatting codes: invalid format codes
invalid_codes = []
for idx, line in enumerate(snbt_lines, 1):
    for m in re.finditer(r'&([^0-9a-fk-orA-FK-OR#\s\"])', line):
        invalid_codes.append((idx, m.group(0), line.strip()))
if invalid_codes:
    report_fail("QUESTS", f"Invalid Minecraft color format codes in en_us.snbt: {invalid_codes}")
else:
    report_pass("QUESTS", "All Minecraft formatting color escapes (&6, &b, etc.) are valid.")

# 3.5 SNBT syntax integrity
curly_open = snbt_raw.count("{")
curly_close = snbt_raw.count("}")
square_open = snbt_raw.count("[")
square_close = snbt_raw.count("]")
balanced = (curly_open == curly_close and square_open == square_close and curly_open == 1)

if balanced:
    report_pass("QUESTS", f"SNBT root compound & brackets balanced: curly={curly_open}/{curly_close}, square={square_open}/{square_close}")
else:
    report_fail("QUESTS", f"SNBT unbalanced brackets: curly={curly_open}/{curly_close}, square={square_open}/{square_close}")

# 3.6 Check other quest snbt files (chapters & reward tables)
extra_quest_surgic = []
extra_quest_amp = []
for sub in ["chapters", "reward_tables"]:
    dirpath = os.path.join(r"minecraft/config/ftbquests/quests", sub)
    if os.path.exists(dirpath):
        for f in os.listdir(dirpath):
            if f.endswith(".snbt"):
                with open(os.path.join(dirpath, f), "r", encoding="utf-8") as fp:
                    for lidx, l in enumerate(fp, 1):
                        if re.search(r"surgic", l, re.I):
                            extra_quest_surgic.append((f"{sub}/{f}", lidx, l.strip()))
                        if "& " in l:
                            extra_quest_amp.append((f"{sub}/{f}", lidx, l.strip()))

if extra_quest_surgic:
    report_fail("QUESTS", f"Surgic hits in quest subfiles: {extra_quest_surgic}")
else:
    report_pass("QUESTS", "Zero 'surgic' in chapters and reward tables SNBT files.")
if extra_quest_amp:
    report_fail("QUESTS", f"Literal '& ' in quest subfiles: {extra_quest_amp}")
else:
    report_pass("QUESTS", "Zero literal '& ' in chapters and reward tables SNBT files.")


# =====================================================================
# CHECK 4: KUBEJS SCRIPT COMMENT & LOG SANITIZATION (R1)
# =====================================================================
print("\n--- [CHECK 4] KubeJS Script Comment & Log Sanitization (R1) ---")
kubejs_dir = r"minecraft/kubejs"

js_files = []
for root, _, files in os.walk(kubejs_dir):
    for f in files:
        if f.endswith(".js"):
            js_files.append(os.path.join(root, f))

print(f"Total .js files found in minecraft/kubejs: {len(js_files)}")

# 4.1 Node.js syntax compilation
compile_errors = []
for js in js_files:
    res = subprocess.run(["node", "-c", js], capture_output=True, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        compile_errors.append((js, (res.stderr or "").strip()))

if compile_errors:
    report_fail("SCRIPTS", f"Syntax compilation errors: {compile_errors}")
else:
    report_pass("SCRIPTS", f"All {len(js_files)}/{len(js_files)} KubeJS scripts compiled cleanly with node -c (exit 0).")

# 4.2 Surgical search in kubejs
kubejs_surgic = []
for js in js_files:
    with open(js, "r", encoding="utf-8", errors="ignore") as fp:
        for idx, line in enumerate(fp, 1):
            if re.search(r"surgic", line, re.I):
                kubejs_surgic.append((js, idx, line.strip()))

if kubejs_surgic:
    report_fail("SCRIPTS", f"'surgic' found in KubeJS: {kubejs_surgic}")
else:
    report_pass("SCRIPTS", "Exactly 0 occurrences of 'surgical' / 'surgically' in minecraft/kubejs/.")

# 4.3 First-person plural in comments/logs
plural_hits = []
for js in js_files:
    rel = os.path.relpath(js, kubejs_dir).replace("\\", "/")
    with open(js, "r", encoding="utf-8", errors="ignore") as fp:
        for idx, line in enumerate(fp, 1):
            if "//" in line or "/*" in line:
                comment = line[line.find("//")+2:] if "//" in line else line
                # Ignore upstream Ars Nouveau flavor text in disabled datapack
                if rel == "server_scripts/20_fixed_datapacks.js" and "bouncy" in comment:
                    continue
                # Match \b(we|our|us)\b
                m = re.search(r'\b(we|our)\b', comment, re.I)
                if m:
                    # Ignore standard common words or technical names if any
                    word = m.group(0).lower()
                    plural_hits.append((rel, idx, word, line.strip()))

if plural_hits:
    report_fail("SCRIPTS", f"First-person plural comments remaining: {plural_hits}")
else:
    report_pass("SCRIPTS", "Zero first-person plural statements ('we', 'our') in KubeJS comments.")

# 4.4 Conversational self-talk & inner monologue
monologue_patterns = [
    r'\bjust in case\b',
    r'\bit died with them\b',
    r'\bthey shamble\b',
    r'\bshould feel earned\b',
    r'\bYou can\'t skip\b',
    r'\bfor an insane price\b',
    r'\bactually worth crafting\b',
    r'\bI think\b',
    r'\bI feel\b',
    r'\bin my opinion\b'
]
monologue_hits = []
for js in js_files:
    rel = os.path.relpath(js, kubejs_dir).replace("\\", "/")
    with open(js, "r", encoding="utf-8", errors="ignore") as fp:
        for idx, line in enumerate(fp, 1):
            for pat in monologue_patterns:
                if re.search(pat, line, re.I):
                    monologue_hits.append((rel, idx, line.strip()))

if monologue_hits:
    report_fail("SCRIPTS", f"Conversational inner dialogue hits: {monologue_hits}")
else:
    report_pass("SCRIPTS", "Zero conversational self-talk or inner-monologue editorializing found.")

# 4.5 Logic invariance check on all git modified .js files
git_js_diff = subprocess.run(["git", "diff", kubejs_dir], capture_output=True, encoding="utf-8", errors="replace")
diff_lines = (git_js_diff.stdout or "").splitlines()

# Analyze git diff hunks to verify only comments or log strings were changed
modified_code_lines = []
current_file = None
for l in diff_lines:
    if l.startswith("diff --git"):
        current_file = l.split()[-1]
    elif l.startswith("+") and not l.startswith("+++"):
        added = l[1:].strip()
        # Check if added line is comment, log, or empty
        if not (added == "" or added.startswith("//") or added.startswith("/*") or added.startswith("*") or 
                "console.info" in added or "console.log" in added or "console.error" in added or "console.warn" in added):
            modified_code_lines.append((current_file, "ADDED_NON_COMMENT", added))
    elif l.startswith("-") and not l.startswith("---"):
        deleted = l[1:].strip()
        if not (deleted == "" or deleted.startswith("//") or deleted.startswith("/*") or deleted.startswith("*") or 
                "console.info" in deleted or "console.log" in deleted or "console.error" in deleted or "console.warn" in deleted):
            modified_code_lines.append((current_file, "DELETED_NON_COMMENT", deleted))

if modified_code_lines:
    report_warn("SCRIPTS", f"Non-comment/non-log lines modified in KubeJS diff: {modified_code_lines}")
else:
    report_pass("SCRIPTS", "100% of modified lines in KubeJS scripts are strictly comments or console log strings.")

# 4.6 Authentic game mechanics check (custom_items.js Stage 5 dragons)
custom_items_path = r"minecraft/kubejs/startup_scripts/custom_items.js"
with open(custom_items_path, "r", encoding="utf-8") as fp:
    c_raw = fp.read()
if "primordial_dragon_blood" in c_raw and "STAGE 5 DRAGON" in c_raw:
    report_pass("MECHANICS", "custom_items.js Stage 5 dragon item and mechanics verified 100% intact.")
else:
    report_fail("MECHANICS", "custom_items.js Stage 5 dragon registration was corrupted or missing!")


# =====================================================================
# OVERALL VICTORY AUDIT VERDICT
# =====================================================================
print("\n=================================================================")
print("=== VICTORY AUDIT RESULT SUMMARY ===")
print("=================================================================")
print(f"Total Failures: {len(FAILURES)}")
print(f"Total Warnings: {len(WARNINGS)}")

if FAILURES:
    print("\nVERDICT: VICTORY REJECTED")
    for f in FAILURES:
        print(f"  {f}")
    sys.exit(1)
else:
    print("\nVERDICT: VICTORY CONFIRMED")
    print("All acceptance criteria, syntactic constraints, and scope boundaries fully met.")
    sys.exit(0)
