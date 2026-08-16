import json
import os

with open(r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\.agents\explorer_1\script_inventory.json", "r", encoding="utf-8") as f:
    scripts = json.load(f)

js_py_scripts = [s for s in scripts if s['ext'] in ['.js', '.py']]

output_lines = [f"Total JS/PY scripts: {len(js_py_scripts)}\n", "=== JS & PY SCRIPTS BREAKDOWN ===\n"]

for s in sorted(js_py_scripts, key=lambda x: x['rel_path']):
    flags = []
    if s['has_antigravity']: flags.append("ANTIGRAVITY")
    if s['has_prompt']: flags.append("PROMPT_REF")
    if s['has_expert_banner']: flags.append("PEAK_BANNER")
    if s['has_console_log']: flags.append("CONSOLE_LOG")
    if s['has_mojibake']: flags.append("MOJIBAKE")
    
    flag_str = ", ".join(flags) if flags else "none"
    output_lines.append(f"\n[{s['rel_path']}] ({s['line_count']} lines) -> Flags: [{flag_str}]")
    if s['header']:
        hl = [l for l in s['header'].splitlines() if l.strip()][:6]
        for l in hl:
            output_lines.append(f"    {l}")

with open(r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\.agents\explorer_1\script_summary.txt", "w", encoding="utf-8") as out_f:
    out_f.write("\n".join(output_lines))

print(f"Summary written to script_summary.txt for {len(js_py_scripts)} scripts.")
