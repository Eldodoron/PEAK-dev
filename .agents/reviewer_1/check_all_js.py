import os
import re

minecraft_dir = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft"

# Let's inspect all JS files in kubejs
js_files = []
for root, dirs, files in os.walk(os.path.join(minecraft_dir, "kubejs")):
    for file in files:
        if file.endswith(".js"):
            full_p = os.path.join(root, file)
            rel_p = os.path.relpath(full_p, minecraft_dir).replace("\\", "/")
            with open(full_p, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
            js_files.append({
                "rel_path": rel_p,
                "line_count": len(lines),
                "first_few": [l.strip() for l in lines[:5] if l.strip()]
            })

js_files.sort(key=lambda x: x["rel_path"])
print(f"Total JS files: {len(js_files)}")
for item in js_files:
    print(f"{item['rel_path']}: {item['line_count']} lines | Header: {item['first_few'][:2]}")
