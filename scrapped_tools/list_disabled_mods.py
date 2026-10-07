import os
import zipfile
import tomllib
import json

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"
all_files = os.listdir(mods_dir)
disabled = [f for f in all_files if f.endswith('.disabled')]

print(f"Total disabled files: {len(disabled)}")
for i, f in enumerate(sorted(disabled), 1):
    print(f"{i:2d}. {f}")
