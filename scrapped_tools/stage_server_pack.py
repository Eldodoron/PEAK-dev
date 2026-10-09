import os
import shutil

source_mc = r"minecraft"
dest_staging = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\ServerPackStaging"
excluded_file = r"minecraft\server_pack_excluded_mods.txt"

print(f"Starting Server Pack Staging (Step 1)...")
print(f"Source: {os.path.abspath(source_mc)}")
print(f"Destination: {dest_staging}")

# Clean existing staging dir if present
if os.path.exists(dest_staging):
    shutil.rmtree(dest_staging)
os.makedirs(dest_staging, exist_ok=True)

# 1. Parse excluded mods
with open(excluded_file, "r", encoding="utf-8") as f:
    excluded_mods = set(line.strip() for line in f if line.strip() and not line.startswith("#"))
print(f"Loaded {len(excluded_mods)} excluded mod filenames from {excluded_file}")

# 2. Copy Mods
source_mods = os.path.join(source_mc, "mods")
dest_mods = os.path.join(dest_staging, "mods")
os.makedirs(dest_mods, exist_ok=True)

all_mod_files = os.listdir(source_mods)
copied_mods = 0
skipped_excluded = 0
skipped_disabled = 0

for m in sorted(all_mod_files):
    src_file = os.path.join(source_mods, m)
    if not os.path.isfile(src_file):
        continue
    if not m.endswith(".jar"):
        # disabled or backup files
        skipped_disabled += 1
        continue
    if m in excluded_mods:
        skipped_excluded += 1
        continue
    shutil.copy2(src_file, os.path.join(dest_mods, m))
    copied_mods += 1

print(f"[MODS] Copied: {copied_mods} active server mods | Excluded: {skipped_excluded} client mods | Skipped: {skipped_disabled} disabled/backups")

# 3. Copy Config (excluding paxi/resourcepacks and client caches)
source_config = os.path.join(source_mc, "config")
dest_config = os.path.join(dest_staging, "config")

def copy_config_tree(src, dst):
    for root, dirs, files in os.walk(src):
        rel = os.path.relpath(root, src)
        # Skip paxi resourcepacks
        if rel.replace("\\", "/").startswith("paxi/resourcepacks"):
            continue
        # Skip iris/sodium shaderpacks or client caches
        if rel.replace("\\", "/").startswith("fancymenu") or rel.replace("\\", "/").startswith("drippyloadingscreen"):
            continue
        target_dir = os.path.join(dst, rel) if rel != "." else dst
        os.makedirs(target_dir, exist_ok=True)
        for f in files:
            shutil.copy2(os.path.join(root, f), os.path.join(target_dir, f))

copy_config_tree(source_config, dest_config)
config_file_count = sum(len(files) for _, _, files in os.walk(dest_config))
print(f"[CONFIG] Staged {config_file_count} configuration files (omitted paxi/resourcepacks)")

# 4. Copy defaultconfigs
source_defcfg = os.path.join(source_mc, "defaultconfigs")
dest_defcfg = os.path.join(dest_staging, "defaultconfigs")
if os.path.exists(source_defcfg):
    shutil.copytree(source_defcfg, dest_defcfg)
    defcfg_count = sum(len(files) for _, _, files in os.walk(dest_defcfg))
    print(f"[DEFAULTCONFIGS] Staged {defcfg_count} default configuration files")

# 5. Copy kubejs (server_scripts, startup_scripts, data, config)
source_kjs = os.path.join(source_mc, "kubejs")
dest_kjs = os.path.join(dest_staging, "kubejs")
for sub in ["server_scripts", "startup_scripts", "data", "config"]:
    s_path = os.path.join(source_kjs, sub)
    d_path = os.path.join(dest_kjs, sub)
    if os.path.exists(s_path):
        shutil.copytree(s_path, d_path)
kjs_count = sum(len(files) for _, _, files in os.walk(dest_kjs))
print(f"[KUBEJS] Staged {kjs_count} script and data files (server_scripts, startup_scripts, data, config)")

# Calculate total size
total_size = sum(os.path.getsize(os.path.join(dirpath, filename)) for dirpath, _, filenames in os.walk(dest_staging) for filename in filenames)
print(f"\nStep 1 Complete! Staging directory ready at:\n{dest_staging}")
print(f"Total Staged Files: {copied_mods + config_file_count + kjs_count} | Total Size: {total_size / (1024*1024):.2f} MB")
