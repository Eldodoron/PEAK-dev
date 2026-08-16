import os
import glob
import json

minecraft_dir = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft"

print("--- 1. Python Scripts Audit ---")
py_files = []
for root, dirs, files in os.walk(minecraft_dir):
    for f in files:
        if f.endswith(".py"):
            py_files.append(os.path.relpath(os.path.join(root, f), minecraft_dir))

print(f"Total Python files found in minecraft/: {len(py_files)}")
for p in sorted(py_files):
    print("  -", p)

print("\n--- 2. KubeJS JS Scripts Audit ---")
kubejs_dir = os.path.join(minecraft_dir, "kubejs")
js_files = []
for root, dirs, files in os.walk(kubejs_dir):
    for f in files:
        if f.endswith(".js"):
            js_files.append(os.path.relpath(os.path.join(root, f), minecraft_dir))

print(f"Total JS files found in kubejs/: {len(js_files)}")
for j in sorted(js_files):
    full_path = os.path.join(minecraft_dir, j)
    with open(full_path, "r", encoding="utf-8", errors="ignore") as file:
        lines = len(file.readlines())
    print(f"  - {j} ({lines} lines)")

print("\n--- 3. Empty Dirs Audit ---")
for d in ["patchouli_books", "datapacks", "scripts", "resourcepacks"]:
    dp = os.path.join(minecraft_dir, d)
    if os.path.exists(dp):
        contents = os.listdir(dp)
        print(f"  {d}: exists={os.path.exists(dp)}, contents={contents}")
    else:
        print(f"  {d}: not found")

print("\n--- 4. Config checks ---")
de_cfg = os.path.join(minecraft_dir, "config", "DraconicEvolution.cfg")
print(f"  DraconicEvolution.cfg exists: {os.path.exists(de_cfg)}")
if os.path.exists(de_cfg):
    with open(de_cfg, "r", encoding="utf-8", errors="ignore") as f:
        print("  DE cfg first 10 lines:\n" + "".join(f.readlines()[:10]))

snbt_path = os.path.join(minecraft_dir, "config", "ftbquests", "quests", "lang", "en_us.snbt")
print(f"  en_us.snbt exists: {os.path.exists(snbt_path)}")
if os.path.exists(snbt_path):
    with open(snbt_path, "r", encoding="utf-8", errors="ignore") as f:
        snbt_lines = len(f.readlines())
    print(f"  en_us.snbt total lines: {snbt_lines}")
