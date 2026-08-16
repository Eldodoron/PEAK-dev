import os
import re
import json

WORKSPACE_ROOT = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev"
MC_DIR = os.path.join(WORKSPACE_ROOT, "minecraft")

PATTERNS = {
    "explicit_ai": re.compile(r"chatgpt|openai|claude|antigravity|copilot", re.I),
    "auto_generated": re.compile(r"auto-generated|generado autom[áa]ticamente", re.I),
    "prompt_residue": re.compile(r"prompt \d|handled in prompt|user prompt|per user request|user wants to", re.I)
}

IGNORED_DIRS = {"logs", "crash-reports", ".cache", "saves", "mods", ".mixin.out"}

results = {}

for root, dirs, files in os.walk(MC_DIR):
    dirs[:] = [d for d in dirs if d.lower() not in IGNORED_DIRS]
    for f in files:
        if f.endswith((".js", ".py", ".json", ".toml", ".cfg", ".md", ".txt", ".snbt", ".yaml", ".yml")):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, MC_DIR)
            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as file_obj:
                    for line_num, line in enumerate(file_obj, 1):
                        for cat, pat in PATTERNS.items():
                            if pat.search(line):
                                if rel_path not in results:
                                    results[rel_path] = []
                                results[rel_path].append({
                                    "line": line_num,
                                    "category": cat,
                                    "text": line.strip()
                                })
            except Exception:
                pass

print(f"Total matching files found: {len(results)}")
for path, matches in sorted(results.items()):
    print(f"\n[{path}] ({len(matches)} occurrences)")
    for m in matches[:3]:
        print(f"  L{m['line']} ({m['category']}): {m['text'][:120]}")

out_path = os.path.join(WORKSPACE_ROOT, ".agents", "auditor_1", "fast_scan_results.json")
with open(out_path, "w", encoding="utf-8") as out_f:
    json.dump(results, out_f, indent=2)
print(f"\nWritten to {out_path}")
