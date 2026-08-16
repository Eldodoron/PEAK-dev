import os
import re

minecraft_dir = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft"

target_dirs = [
    os.path.join(minecraft_dir, "kubejs"),
    os.path.join(minecraft_dir, "config"),
    os.path.join(minecraft_dir, "defaultconfigs"),
    os.path.join(minecraft_dir, "global_packs"),
    os.path.join(minecraft_dir, "scratch")
]

keywords = [
    r"\bchatgpt\b",
    r"\bclaude\b",
    r"\bopenai\b",
    r"\bantigravity\b",
    r"\bcopilot\b",
    r"\bai[- ]generated\b",
    r"\bauto[- ]generated\b",
    r"\bllm\b",
    r"\bprompt\s*\d+\b",
    r"per user request",
    r"user prompt"
]

compiled = [(kw, re.compile(kw, re.IGNORECASE)) for kw in keywords]

# Search root files
root_files = [os.path.join(minecraft_dir, f) for f in os.listdir(minecraft_dir) if os.path.isfile(os.path.join(minecraft_dir, f))]

all_files = list(root_files)
for d in target_dirs:
    if os.path.exists(d):
        for root, _, files in os.walk(d):
            for f in files:
                ext = os.path.splitext(f)[1].lower()
                if ext in {".js", ".py", ".json", ".toml", ".cfg", ".snbt", ".md", ".txt", ".json5", ".yaml", ".yml"}:
                    all_files.append(os.path.join(root, f))

print(f"Scanning {len(all_files)} files...")
matches = []

for full_p in all_files:
    rel_p = os.path.relpath(full_p, minecraft_dir)
    try:
        with open(full_p, "r", encoding="utf-8", errors="ignore") as f:
            for line_no, line in enumerate(f, 1):
                for kw_str, kw_re in compiled:
                    if kw_re.search(line):
                        matches.append({
                            "file": rel_p,
                            "line": line_no,
                            "kw": kw_str,
                            "snippet": line.strip()
                        })
    except Exception as e:
        pass

print(f"Total matches found: {len(matches)}")
files_matched = {}
for m in matches:
    files_matched.setdefault(m["file"], []).append(m)

for f, mlist in sorted(files_matched.items()):
    print(f"\n--- {f} ({len(mlist)} matches) ---")
    for m in mlist:
        print(f"  L{m['line']} [{m['kw']}]: {m['snippet'][:120]}")
