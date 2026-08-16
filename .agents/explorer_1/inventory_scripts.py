import os
import re
import json

KUBEJS_DIR = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs"

script_details = []

for root, dirs, files in os.walk(KUBEJS_DIR):
    for f in files:
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, KUBEJS_DIR)
        ext = os.path.splitext(f)[1].lower()
        if ext in ['.js', '.py', '.txt', '.json', '.md']:
            with open(full_path, 'r', encoding='utf-8', errors='replace') as fp:
                content = fp.read()
                lines = content.splitlines()

            # Analyze header comments
            header_lines = []
            for line in lines[:30]:
                if line.strip().startswith('//') or line.strip().startswith('/*') or line.strip().startswith('#') or line.strip() == '':
                    header_lines.append(line)
                else:
                    break

            # Look for specific markers
            has_antigravity = 'antigravity' in content.lower()
            has_prompt = 'prompt' in content.lower()
            has_expert_banner = 'peak expert mode' in content.lower() or '====================' in content
            has_console_log = '[PEAK Expert Mode]' in content or '[peak expert mode]' in content.lower()
            has_mojibake = any(c in content for c in ['â€”', 'Ã¢â‚¬â€', 'Ã¢â€ â€™', 'â€“'])

            script_details.append({
                "file": full_path,
                "rel_path": rel_path,
                "ext": ext,
                "line_count": len(lines),
                "has_antigravity": has_antigravity,
                "has_prompt": has_prompt,
                "has_expert_banner": has_expert_banner,
                "has_console_log": has_console_log,
                "has_mojibake": has_mojibake,
                "header": "\n".join(header_lines[:15])
            })

out_path = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\.agents\explorer_1\script_inventory.json"
with open(out_path, "w", encoding="utf-8") as out_fp:
    json.dump(script_details, out_fp, indent=2)

print(f"Inventoried {len(script_details)} files.")
