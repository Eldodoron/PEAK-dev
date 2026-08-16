import os
import re

minecraft_dir = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft"

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

compiled = [re.compile(kw, re.IGNORECASE) for kw in keywords]

matches = []
ignored_exts = {".jar", ".png", ".jpg", ".ogg", ".zip", ".dll", ".dat", ".nbt", ".marker"}
ignored_dirs = {"mods", "logs", "crash-reports", "saves", "temp_jar", "temp_alexscaves", "temp_litho", "tmp_bc", "tmp_bfb", "tmp_cei", "tmp_cna", "tmp_irons", ".mixin.out"}

for root, dirs, files in os.walk(minecraft_dir):
    # filter ignored dirs
    dirs[:] = [d for d in dirs if d not in ignored_dirs and not d.startswith(".")]
    
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        if ext in ignored_exts or f.endswith(".log"):
            continue
        full_p = os.path.join(root, f)
        rel_p = os.path.relpath(full_p, minecraft_dir)
        try:
            with open(full_p, "r", encoding="utf-8", errors="ignore") as file_obj:
                for line_no, line in enumerate(file_obj, 1):
                    for kw_re in compiled:
                        if kw_re.search(line):
                            matches.append({
                                "file": rel_p,
                                "line": line_no,
                                "pattern": kw_re.pattern,
                                "content": line.strip()
                            })
        except Exception as e:
            pass

print(f"Total keyword matches: {len(matches)}")
# Group by file
files_matched = {}
for m in matches:
    files_matched.setdefault(m["file"], []).append(m)

for f, mlist in sorted(files_matched.items()):
    print(f"\n--- {f} ({len(mlist)} matches) ---")
    for m in mlist[:5]:
        print(f"  L{m['line']}: [{m['pattern']}] {m['content'][:100]}")
    if len(mlist) > 5:
        print(f"  ... and {len(mlist)-5} more")
