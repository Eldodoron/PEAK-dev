import zipfile
import json
import os
import glob

print("--- APOTHIC ENCHANTING STATS ---")
with zipfile.ZipFile("minecraft/mods/ApothicEnchanting-1.21.1-1.6.0.jar") as z:
    for name in sorted(z.namelist()):
        if name.startswith("data/apothic_enchanting/enchanting_stats/") and name.endswith(".json"):
            data = json.loads(z.read(name).decode("utf-8"))
            fname = os.path.basename(name)
            print(f"{fname}: {data}")

print("\n--- APOTHIC ENCHANTING RECIPES FOR SHELVES ---")
with zipfile.ZipFile("minecraft/mods/ApothicEnchanting-1.21.1-1.6.0.jar") as z:
    for name in sorted(z.namelist()):
        if name.startswith("data/apothic_enchanting/recipe/") and name.endswith(".json"):
            if "shelf" in name:
                data = json.loads(z.read(name).decode("utf-8"))
                fname = os.path.basename(name)
                print(f"\n{fname}:")
                print(json.dumps(data, indent=2))
