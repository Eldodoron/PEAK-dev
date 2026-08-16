import os
import re
import json

KUBEJS_DIR = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs"

comments_by_file = {}

for root, dirs, files in os.walk(KUBEJS_DIR):
    for f in files:
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, KUBEJS_DIR)
        ext = os.path.splitext(f)[1].lower()
        if ext in ['.js', '.py', '.txt']:
            with open(full_path, 'r', encoding='utf-8', errors='replace') as fp:
                lines = fp.readlines()
            
            file_comments = []
            for i, line in enumerate(lines, 1):
                stripped = line.strip()
                if stripped.startswith('//') or stripped.startswith('#') or stripped.startswith('/*') or stripped.startswith('*'):
                    file_comments.append((i, stripped))
            
            if file_comments:
                comments_by_file[rel_path] = file_comments

# Let's search for interesting patterns in comments
suspicious_patterns = [
    (r"antigravity", "Explicit AI Name (Antigravity)"),
    (r"prompt\s*\d*", "Prompt Iteration Reference"),
    (r"user", "User Reference / Agent Dialogue"),
    (r"fixed by", "Attribution"),
    (r"auto-generated", "Auto-generation Notice"),
    (r"emergency fix", "AI Emergency Intervention"),
    (r"handled in", "Cross-prompt/Task Reference"),
    (r"refined in", "Cross-prompt/Task Reference"),
    (r"defined in prompt", "Prompt Reference"),
    (r"peak expert mode", "Standardized AI Modpack Architecture"),
    (r"â€”|Ã¢â‚¬â€|Ã¢â€ â€™|â†’", "UTF-8 Mojibake in Comments"),
    (r"this script", "Descriptive LLM Script Preface"),
]

categorized_findings = {}

for rel_path, comments in comments_by_file.items():
    file_findings = []
    for line_num, text in comments:
        matched_cats = []
        for pat, cat_name in suspicious_patterns:
            if re.search(pat, text, re.IGNORECASE):
                matched_cats.append(cat_name)
        if matched_cats:
            file_findings.append({
                "line": line_num,
                "text": text,
                "categories": matched_cats
            })
    if file_findings:
        categorized_findings[rel_path] = file_findings

out_json = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\.agents\explorer_1\detailed_findings.json"
with open(out_json, "w", encoding="utf-8") as out_fp:
    json.dump(categorized_findings, out_fp, indent=2)

print(f"Extracted findings from {len(categorized_findings)} files.")
