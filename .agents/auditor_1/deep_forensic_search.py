import os
import re

WORKSPACE_ROOT = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev"
MC_DIR = os.path.join(WORKSPACE_ROOT, "minecraft")

PATTERNS = [
    r"chatgpt",
    r"openai",
    r"claude",
    r"antigravity",
    r"copilot",
    r"auto-generated",
    r"generado autom[áa]ticamente",
    r"user request",
    r"per user",
    r"user prompt",
    r"prompt \d",
    r"handled in prompt",
    r"ai generated",
    r"ai-generated"
]

results = {}

for root, dirs, files in os.walk(MC_DIR):
    # skip .jar files / binary files
    for f in files:
        if f.endswith((".js", ".py", ".json", ".toml", ".cfg", ".md", ".txt", ".snbt", ".yaml", ".yml")):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, MC_DIR)
            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as file_obj:
                    for line_num, line in enumerate(file_obj, 1):
                        for pattern in PATTERNS:
                            if re.search(pattern, line, re.IGNORECASE):
                                if rel_path not in results:
                                    results[rel_path] = []
                                results[rel_path].append({
                                    "line": line_num,
                                    "pattern": pattern,
                                    "text": line.strip()
                                })
            except Exception as e:
                pass

print(f"Total files with AI indicators found: {len(results)}")
for path, matches in results.items():
    print(f"\n--- {path} ({len(matches)} matches) ---")
    for m in matches[:5]: # show first 5 matches per file
        print(f"  Line {m['line']} [{m['pattern']}]: {m['text'][:100]}")
