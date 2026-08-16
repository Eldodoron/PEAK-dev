import os
import sys
import subprocess
import json
import re
from pathlib import Path
try:
    import tomllib
except ImportError:
    import tomli as tomllib

repo_root = Path(r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev")
mc_dir = repo_root / "minecraft"
kubejs_dir = mc_dir / "kubejs"

print("=== ADVERSARIAL CHECK 1: AST / TOKEN EQUIVALENCE ON ALL JS FILES ===")
# Get list of all JS files modified in git
res = subprocess.run(["git", "diff", "--name-only", "HEAD", "--", "minecraft/kubejs/"], capture_output=True, text=True)
modified_js = [line.strip() for line in res.stdout.splitlines() if line.strip().endswith(".js")]
print(f"Modified JS files in git: {len(modified_js)}")

def strip_comments(source: str) -> str:
    output = []
    i = 0
    n = len(source)
    while i < n:
        c = source[i]
        if c == "'":
            start = i; i += 1
            while i < n:
                if source[i] == "\\": i += 2
                elif source[i] == "'": i += 1; break
                else: i += 1
            output.append(source[start:i])
        elif c == '"':
            start = i; i += 1
            while i < n:
                if source[i] == "\\": i += 2
                elif source[i] == '"': i += 1; break
                else: i += 1
            output.append(source[start:i])
        elif c == '`':
            start = i; i += 1
            while i < n:
                if source[i] == "\\": i += 2
                elif source[i] == '`': i += 1; break
                else: i += 1
            output.append(source[start:i])
        elif c == '/' and i + 1 < n and source[i + 1] == '/':
            i += 2
            while i < n and source[i] != '\n': i += 1
            if i < n and source[i] == '\n': output.append('\n'); i += 1
        elif c == '/' and i + 1 < n and source[i + 1] == '*':
            i += 2
            while i + 1 < n and not (source[i] == '*' and source[i + 1] == '/'):
                if source[i] == '\n': output.append('\n')
                i += 1
            i += 2
        else:
            output.append(c)
            i += 1
    return "".join(output)

def tokenize(source: str):
    clean = strip_comments(source)
    pat = re.compile(
        r"""(?P<STR>'(\\.|[^\\'])*'|"(\\.|[^\\"])*"|`(\\.|[^\\`])*`) |
            (?P<NUM>\b\d+(\.\d+)?\b) |
            (?P<ID>[a-zA-Z_$][a-zA-Z0-9_$]*) |
            (?P<OP>===|!==|==|!=|<=|>=|=>|\+\+|--|\+=|-=|\*=|/=|&&|\|\||[+\-*/%&|^!=<>?:]+) |
            (?P<PUNCT>[{}()\[\];,.~])""",
        re.VERBOSE,
    )
    return [m.group(0) for m in pat.finditer(clean) if m.group(0)]

all_js_identical = True
for rel_path in modified_js:
    # Get git HEAD version
    head_proc = subprocess.run(["git", "show", f"HEAD:{rel_path}"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    head_tokens = tokenize(head_proc.stdout)
    
    # Get current working copy
    curr_path = repo_root / rel_path
    curr_tokens = tokenize(curr_path.read_text(encoding="utf-8", errors="replace"))
    
    if head_tokens == curr_tokens:
        print(f"  [PASS] {rel_path}: 100% functional token equivalence ({len(curr_tokens)} tokens)")
    else:
        print(f"  [FAIL] {rel_path}: Token mismatch! HEAD={len(head_tokens)} vs CURR={len(curr_tokens)}")
        all_js_identical = False

assert all_js_identical, "Functional code in JS was modified!"

print("\n=== ADVERSARIAL CHECK 2: FTB QUESTS & CHAPTERS INTEGRITY ===")
ftb_lang = mc_dir / "config" / "ftbquests" / "quests" / "lang" / "en_us.snbt"
assert ftb_lang.exists(), "en_us.snbt does not exist!"
lang_lines = ftb_lang.read_text(encoding="utf-8", errors="replace").splitlines()
print(f"en_us.snbt line count: {len(lang_lines)} lines")
assert len(lang_lines) >= 3300, f"Expected >=3300 lines, found {len(lang_lines)}"

chapters_dir = mc_dir / "config" / "ftbquests" / "quests" / "chapters"
chapter_files = list(chapters_dir.glob("*.snbt"))
print(f"Found {len(chapter_files)} chapter .snbt files in config/ftbquests/quests/chapters/:")
for cf in chapter_files:
    c_lines = len(cf.read_text(encoding="utf-8", errors="replace").splitlines())
    print(f"  - {cf.name}: {c_lines} lines")
assert len(chapter_files) > 0, "No chapter files found!"

reward_dir = mc_dir / "config" / "ftbquests" / "quests" / "reward_tables"
reward_files = list(reward_dir.glob("*.snbt")) if reward_dir.exists() else []
print(f"Found {len(reward_files)} reward table .snbt files in reward_tables/")

print("\n=== ADVERSARIAL CHECK 3: CONFIG & DEFAULTCONFIGS TOML/JSON/SNBT VALIDITY ===")
config_dir = mc_dir / "config"
defaultconfigs_dir = mc_dir / "defaultconfigs"

def test_toml_files(directory):
    toml_count = 0
    toml_errors = []
    for tf in directory.rglob("*.toml"):
        toml_count += 1
        try:
            with open(tf, "rb") as f:
                tomllib.load(f)
        except Exception as e:
            toml_errors.append((tf, str(e)))
    return toml_count, toml_errors

c_toml_count, c_toml_errors = test_toml_files(config_dir)
d_toml_count, d_toml_errors = test_toml_files(defaultconfigs_dir)
print(f"config/ TOML files: {c_toml_count} checked, {len(c_toml_errors)} errors")
print(f"defaultconfigs/ TOML files: {d_toml_count} checked, {len(d_toml_errors)} errors")
assert len(c_toml_errors) == 0, f"Broken TOML in config: {c_toml_errors}"
assert len(d_toml_errors) == 0, f"Broken TOML in defaultconfigs: {d_toml_errors}"

print("\n=== ADVERSARIAL CHECK 4: ZERO RESIDUAL AI MATCHES SWEEP ===")
ai_patterns = [
    re.compile(r"(?i)\bantigravity\b"),
    re.compile(r"(?i)\b(chatgpt|openai|claude|anthropic|copilot|gemini)\b"),
    re.compile(r"(?i)\bprompt\s*[0-9]+"),
    re.compile(r"(?i)\bauto-generated\s+by\b"),
    re.compile(r"(?i)\bfixed\s+by\s+antigravity\b"),
    re.compile(r"(?i)\b(per\s+user\s+request|the\s+user\s+wants|the\s+user\s+used|from\s+user\s+prompt|so\s+the\s+user\s+knows)\b"),
    re.compile(r"(?i)\bwait,\s*kubejs\b"),
    re.compile(r"(?i)archivo\s+generado\s+autom[aá]ticamente"),
]
whitelist = [
    re.compile(r"effect\.irons_spellbooks\.antigravity"),
    re.compile(r"irons_spellbooks:antigravity"),
]

scan_extensions = {".js", ".json", ".snbt", ".toml", ".txt", ".md", ".cfg", ".yaml", ".properties", ".mcmeta"}
exclude_dirs = {".git", ".continue", ".agents", "libraries", "logs", "crash-reports", "saves", "cache", "downloads", "scrapped_tools"}

violations = []
for root, dirs, files in os.walk(mc_dir):
    dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith(".")]
    for fname in files:
        ext = Path(fname).suffix.lower()
        if ext in scan_extensions:
            fpath = Path(root) / fname
            try:
                content = fpath.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            for lnum, line in enumerate(content.splitlines(), 1):
                if any(w.search(line) for w in whitelist):
                    continue
                for pat in ai_patterns:
                    m = pat.search(line)
                    if m:
                        violations.append((fpath.relative_to(mc_dir), lnum, m.group(0), line.strip()))

print(f"Total AI sweep violations in runtime minecraft/ files: {len(violations)}")
if violations:
    for v in violations:
        print(f"  - {v[0]}:{v[1]}: matched '{v[2]}' in: {v[3]}")
assert len(violations) == 0, "Found residual AI mentions in runtime files!"
print("ZERO AI residues confirmed across all runtime files!")

print("\n=== ALL ADVERSARIAL CHECKS PASSED WITH 100% INTEGRITY ===")
