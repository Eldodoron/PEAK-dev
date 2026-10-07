import os
import shutil
import uuid
import json

BASE_DEV = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev"
BASE_LITE = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-Lite"
DEV_MC = os.path.join(BASE_DEV, "minecraft")
LITE_MC = os.path.join(BASE_LITE, "minecraft")
EXCLUSIONS_FILE = os.path.join(DEV_MC, "peak_lite_excluded_components.txt")

def load_exclusions():
    exclusions = set()
    if os.path.exists(EXCLUSIONS_FILE):
        with open(EXCLUSIONS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    exclusions.add(line.lower())
    print(f"Loaded {len(exclusions)} Lite exclusion filenames.")
    return exclusions

def build_lite_instance():
    print(f"Preparing PEAK Lite instance at: {BASE_LITE}")
    if os.path.exists(BASE_LITE):
        print("Target instance directory already exists. Cleaning up...")
        shutil.rmtree(BASE_LITE)
    os.makedirs(BASE_LITE, exist_ok=True)
    os.makedirs(LITE_MC, exist_ok=True)

    exclusions = load_exclusions()

    # 1. Instance Configuration (instance.cfg)
    dev_cfg_path = os.path.join(BASE_DEV, "instance.cfg")
    lite_cfg_path = os.path.join(BASE_LITE, "instance.cfg")
    if os.path.exists(dev_cfg_path):
        with open(dev_cfg_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open(lite_cfg_path, "w", encoding="utf-8") as f:
            for line in lines:
                if line.startswith("name="):
                    f.write("name=PEAK Lite\n")
                elif line.startswith("uuid="):
                    f.write(f"uuid={uuid.uuid4()}\n")
                elif line.startswith("lastLaunchTime="):
                    f.write("lastLaunchTime=0\n")
                elif line.startswith("lastTimePlayed="):
                    f.write("lastTimePlayed=0\n")
                elif line.startswith("totalTimePlayed="):
                    f.write("totalTimePlayed=0\n")
                elif line.startswith("ExportName="):
                    f.write("ExportName=PEAK-Lite\n")
                else:
                    f.write(line)
        print("Generated instance.cfg for PEAK Lite.")

    # 2. MMC Pack & Patches
    shutil.copy2(os.path.join(BASE_DEV, "mmc-pack.json"), os.path.join(BASE_LITE, "mmc-pack.json"))
    dev_patches = os.path.join(BASE_DEV, "patches")
    if os.path.exists(dev_patches):
        shutil.copytree(dev_patches, os.path.join(BASE_LITE, "patches"))
        print("Copied mmc-pack.json and patches.")

    # 3. Mods (minecraft/mods/)
    dev_mods = os.path.join(DEV_MC, "mods")
    lite_mods = os.path.join(LITE_MC, "mods")
    os.makedirs(lite_mods, exist_ok=True)
    copied_mods = 0
    skipped_mods = 0

    for fname in sorted(os.listdir(dev_mods)):
        fname_lower = fname.lower()
        if not fname.endswith(".jar"):
            skipped_mods += 1
            continue
        if fname_lower in exclusions:
            skipped_mods += 1
            print(f"  [Excluded Visual Mod] {fname}")
            continue

        src_file = os.path.join(dev_mods, fname)
        dst_file = os.path.join(lite_mods, fname)
        shutil.copy2(src_file, dst_file)
        copied_mods += 1

    print(f"Copied {copied_mods} active mods into PEAK Lite (skipped {skipped_mods} visual/disabled files).")

    # 4. Config (minecraft/config/)
    dev_config = os.path.join(DEV_MC, "config")
    lite_config = os.path.join(LITE_MC, "config")
    shutil.copytree(dev_config, lite_config)

    # Filter heavy resource packs in config/paxi/resourcepacks/
    paxi_rp_dir = os.path.join(lite_config, "paxi", "resourcepacks")
    excluded_packs = set()
    if os.path.exists(paxi_rp_dir):
        for fname in os.listdir(paxi_rp_dir):
            if fname.lower() in exclusions:
                excluded_packs.add(fname)
                os.remove(os.path.join(paxi_rp_dir, fname))
                print(f"  [Excluded Resource Pack] {fname}")

    # Update config/paxi/resourcepack_load_order.json
    order_file = os.path.join(lite_config, "paxi", "resourcepack_load_order.json")
    if os.path.exists(order_file):
        try:
            with open(order_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            if "loadOrder" in data:
                data["loadOrder"] = [p for p in data["loadOrder"] if p not in excluded_packs and p.lower() not in exclusions]
            with open(order_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            print("Updated paxi resourcepack load order.")
        except Exception as e:
            print(f"Warning: Failed to update load order: {e}")

    # Remove configs for excluded dev / cosmetic mods
    orphaned_configs = ["spark", "panoptic-common.toml", "smoothswapping.json"]
    for o_cfg in orphaned_configs:
        o_path = os.path.join(lite_config, o_cfg)
        if os.path.exists(o_path):
            if os.path.isdir(o_path):
                shutil.rmtree(o_path)
            else:
                os.remove(o_path)
            print(f"  [Removed Config] {o_cfg}")

    print("Copied and optimized config directory.")

    # 5. DefaultConfigs, KubeJS, DataPacks, Blueprints
    for folder in ["defaultconfigs", "kubejs", "datapacks", "blueprints"]:
        src_dir = os.path.join(DEV_MC, folder)
        dst_dir = os.path.join(LITE_MC, folder)
        if os.path.exists(src_dir):
            shutil.copytree(src_dir, dst_dir)
            print(f"Copied {folder} directory.")

    # 6. Essential Single Files
    single_files = [
        "options.txt",
        "icon.png",
        "paragliderSettings.nbt",
        "patchouli_data.json",
        "servers.dat",
        "servers.essential.dat",
        "ponders_watched.json"
    ]
    for sfile in single_files:
        src = os.path.join(DEV_MC, sfile)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(LITE_MC, sfile))
            print(f"Copied {sfile}")

    print("\n==========================================")
    print("PEAK Lite instance build successfully completed!")
    print(f"Location: {BASE_LITE}")
    print("==========================================")

if __name__ == "__main__":
    build_lite_instance()
