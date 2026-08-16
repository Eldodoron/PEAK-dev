import os
import re

WORKSPACE_ROOT = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev"
MC_DIR = os.path.join(WORKSPACE_ROOT, "minecraft")
REPORT_PATH = os.path.join(MC_DIR, "ai_audit_report.md")

with open(REPORT_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Extract Section 5.2 table rows
# | 1 | `kubejs/server_scripts/00_recipe_fixer.js` | 74 | `PEAK EXPERT MODE â€” RECIPE SANITIZER` | Mojibake `â€”`, standardized banner |
js_rows = re.findall(r'\|\s*\d+\s*\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*`?([^`|]+)`?\s*\|', content)

print(f"Found {len(js_rows)} rows in JS Table 5.2")
js_discrepancies = []
for rel_path, reported_lines, header in js_rows:
    p = os.path.join(MC_DIR, rel_path)
    if not os.path.exists(p):
        js_discrepancies.append((rel_path, "FILE_NOT_FOUND", reported_lines, 0))
    else:
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            actual_lines = len(f.readlines())
        # Check if line counts are close or exact (accounting for trailing newline)
        if abs(actual_lines - int(reported_lines)) > 2:
            js_discrepancies.append((rel_path, "LINE_MISMATCH", reported_lines, actual_lines))

print(f"JS discrepancies: {len(js_discrepancies)}")
for d in js_discrepancies:
    print("  ", d)

# Extract Section 6.1 table rows
# | **5.1** | `c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\check_client_toml.py` | 52 |
py_rows = re.findall(r'\|\s*\*\*5\.\d+\*\*\s*\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|', content)
print(f"\nFound {len(py_rows)} rows in Python Table 6.1")
py_discrepancies = []
for full_path, reported_lines in py_rows:
    if not os.path.exists(full_path):
        py_discrepancies.append((full_path, "FILE_NOT_FOUND", reported_lines, 0))
    else:
        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
            actual_lines = len(f.readlines())
        if abs(actual_lines - int(reported_lines)) > 2:
            py_discrepancies.append((full_path, "LINE_MISMATCH", reported_lines, actual_lines))

print(f"Python discrepancies: {len(py_discrepancies)}")
for d in py_discrepancies:
    print("  ", d)
