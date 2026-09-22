import zipfile
import json

jar_path = r"minecraft/mods/create-enchantment-industry-2.5.4.jar"

with zipfile.ZipFile(jar_path) as zf:
    names = zf.namelist()
    targets = [
        "super_experience_nugget",
        "experience",
        "experience_cake",
        "experience_cake_base",
        "experience_hatch"
    ]
    print(f"Checking {jar_path}...")
    for t in targets:
        matches = [n for n in names if t in n]
        print(f"  Target '{t}': {len(matches)} matches (e.g. {matches[:2]})")
