import os
import re

WORKSPACE_ROOT = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev"
MC_DIR = os.path.join(WORKSPACE_ROOT, "minecraft")
REPORT_PATH = os.path.join(MC_DIR, "ai_audit_report.md")

with open(REPORT_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Extract Table 5.2 rows
# Format: | 1 | `kubejs/server_scripts/00_recipe_fixer.js` | 74 | `PEAK EXPERT MODE â€” RECIPE SANITIZER` | Mojibake `â€”`, standardized banner |
matches = re.findall(r'\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*`?([^`|]+)`?\s*\|\s*([^|]+)\|', content)

print(f"Total entries in Section 5.2 table: {len(matches)}")
all_exist = True
header_matches = 0
for idx, rel_path, lines, header, notes in matches:
    p = os.path.join(MC_DIR, rel_path.strip())
    if not os.path.exists(p):
        print(f"[FAIL] Missing file: {rel_path}")
        all_exist = False
    else:
        # Check if file has header or content
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            fc = f.read()
        # Clean header search term
        h_clean = header.strip().split("â")[0].split("Ã")[0].split("—")[0].strip()
        if h_clean and h_clean.lower() in fc.lower():
            header_matches += 1
        else:
            # Check if partial words match
            words = [w for w in h_clean.split() if len(w) > 3]
            if words and any(w.lower() in fc.lower() for w in words):
                header_matches += 1
            else:
                print(f"[WARN] Header '{header.strip()}' not found in {rel_path}")

print(f"All 64 JS files exist on disk: {all_exist}")
print(f"Headers matching content on disk: {header_matches}/{len(matches)}")
