import os
import glob

suppressor = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\kubejs\server_scripts\00_recipe_error_suppressor.js"
kubejs_data = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\kubejs\data"

# Find all JSON files in kubejs_data
fixed_ids = set()
for root, dirs, files in os.walk(kubejs_data):
    for f in files:
        if f.endswith('.json'):
            # The path looks like: kubejs/data/<ns>/recipe/<path>.json
            rel_path = os.path.relpath(os.path.join(root, f), kubejs_data).replace('\\', '/')
            parts = rel_path.split('/')
            if len(parts) >= 3:
                ns = parts[0]
                # parts[1] is 'recipe' or 'recipes'
                path = '/'.join(parts[2:]).replace('.json', '')
                fixed_ids.add(f"{ns}:{path}")

with open(suppressor, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
removed = 0
for line in lines:
    stripped = line.strip()
    if stripped.startswith("'") and "'," in stripped:
        recipe_id = stripped.strip("',")
        if recipe_id in fixed_ids:
            removed += 1
            continue  # skip this line
    new_lines.append(line)

with open(suppressor, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Removed {removed} fixed recipes from suppressor script!")
