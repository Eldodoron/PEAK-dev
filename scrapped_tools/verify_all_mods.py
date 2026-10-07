import os
import zipfile
import tomllib
import json

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"
all_files = os.listdir(mods_dir)

print(f"Total files in mods dir: {len(all_files)}")

jars = [f for f in all_files if f.endswith('.jar')]
disabled = [f for f in all_files if f.endswith('.disabled')]
backups = [f for f in all_files if f.endswith('.backup') or f.endswith('.modified')]
others = [f for f in all_files if not f.endswith('.jar') and not f.endswith('.disabled') and not f.endswith('.backup') and not f.endswith('.modified')]

print(f"Active jars: {len(jars)}")
print(f"Disabled files: {len(disabled)}")
print(f"Backup/modified: {len(backups)}")
print(f"Others: {others}")
