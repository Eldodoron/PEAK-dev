import os
import glob
import re
import json

minecraft_dir = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft"

# 1. Find all JS files
js_files = []
for root, dirs, files in os.walk(os.path.join(minecraft_dir, "kubejs")):
    for file in files:
        if file.endswith(".js"):
            js_files.append(os.path.relpath(os.path.join(root, file), minecraft_dir))

# 2. Find all Python files across minecraft/
py_files = []
for root, dirs, files in os.walk(minecraft_dir):
    for file in files:
        if file.endswith(".py"):
            py_files.append(os.path.relpath(os.path.join(root, file), minecraft_dir))

# 3. Find all flowerbed models
model_files = []
models_dir = os.path.join(minecraft_dir, "kubejs", "assets", "minecraft", "models", "block")
if os.path.exists(models_dir):
    for file in os.listdir(models_dir):
        if "flowerbed" in file:
            model_files.append(os.path.relpath(os.path.join(models_dir, file), minecraft_dir))

# 4. Check quests file and ore report
snbt_path = os.path.join(minecraft_dir, "config", "ftbquests", "quests", "lang", "en_us.snbt")
ore_report_path = os.path.join(minecraft_dir, "ore_report.md")

snbt_lines = 0
if os.path.exists(snbt_path):
    with open(snbt_path, "r", encoding="utf-8", errors="ignore") as f:
        snbt_lines = len(f.readlines())

ore_report_lines = 0
if os.path.exists(ore_report_path):
    with open(ore_report_path, "r", encoding="utf-8", errors="ignore") as f:
        ore_report_lines = len(f.readlines())

print(f"JS Files count in kubejs: {len(js_files)}")
print(f"PY Files count in minecraft: {len(py_files)}")
print("Python files found:")
for p in sorted(py_files):
    print(f"  - {p}")

print(f"Flowerbed model files: {model_files}")
print(f"snbt lines: {snbt_lines}")
print(f"ore_report.md lines: {ore_report_lines}")
