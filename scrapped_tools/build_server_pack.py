import os
import shutil
import zipfile

BASE_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev"
MC_DIR = os.path.join(BASE_DIR, "minecraft")
EXCLUSIONS_FILE = os.path.join(MC_DIR, "server_pack_excluded_mods.txt")
OUTPUT_ZIP = os.path.join(BASE_DIR, "PEAK_Server_Pack.zip")
TEMP_SERVER_DIR = os.path.join(BASE_DIR, "server_pack_temp")

def load_exclusions():
    exclusions = set()
    if os.path.exists(EXCLUSIONS_FILE):
        with open(EXCLUSIONS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    exclusions.add(line.lower())
    print(f"Loaded {len(exclusions)} exclusion filenames.")
    return exclusions

def build_server_pack():
    if os.path.exists(TEMP_SERVER_DIR):
        shutil.rmtree(TEMP_SERVER_DIR)
    os.makedirs(TEMP_SERVER_DIR, exist_ok=True)

    exclusions = load_exclusions()

    # 1. Process Mods
    mods_src = os.path.join(MC_DIR, "mods")
    mods_dest = os.path.join(TEMP_SERVER_DIR, "mods")
    os.makedirs(mods_dest, exist_ok=True)

    copied_mods = 0
    skipped_mods = 0

    for fname in os.listdir(mods_src):
        fname_lower = fname.lower()
        # Only include active .jar files (not .disabled, .backup, .modified)
        if not fname.endswith(".jar"):
            skipped_mods += 1
            continue
        if fname_lower in exclusions:
            skipped_mods += 1
            continue

        src_path = os.path.join(mods_src, fname)
        dest_path = os.path.join(mods_dest, fname)
        shutil.copy2(src_path, dest_path)
        copied_mods += 1

    print(f"Copied {copied_mods} active server mods (skipped {skipped_mods} client/disabled/artifact files).")

    # 2. Process Config
    config_src = os.path.join(MC_DIR, "config")
    config_dest = os.path.join(TEMP_SERVER_DIR, "config")
    if os.path.exists(config_src):
        shutil.copytree(config_src, config_dest, dirs_exist_ok=True)
        print("Copied config directory.")

    # 3. Process DefaultConfigs
    defconfig_src = os.path.join(MC_DIR, "defaultconfigs")
    defconfig_dest = os.path.join(TEMP_SERVER_DIR, "defaultconfigs")
    if os.path.exists(defconfig_src):
        shutil.copytree(defconfig_src, defconfig_dest, dirs_exist_ok=True)
        print("Copied defaultconfigs directory.")

    # 4. Process KubeJS
    kubejs_src = os.path.join(MC_DIR, "kubejs")
    kubejs_dest = os.path.join(TEMP_SERVER_DIR, "kubejs")
    if os.path.exists(kubejs_src):
        shutil.copytree(kubejs_src, kubejs_dest, dirs_exist_ok=True)
        print("Copied kubejs directory.")

    # 5. Process DataPacks
    datapacks_src = os.path.join(MC_DIR, "datapacks")
    datapacks_dest = os.path.join(TEMP_SERVER_DIR, "datapacks")
    if os.path.exists(datapacks_src):
        shutil.copytree(datapacks_src, datapacks_dest, dirs_exist_ok=True)
        print("Copied datapacks directory.")

    # 6. Process Blueprints
    blueprints_src = os.path.join(MC_DIR, "blueprints")
    blueprints_dest = os.path.join(TEMP_SERVER_DIR, "blueprints")
    if os.path.exists(blueprints_src):
        shutil.copytree(blueprints_src, blueprints_dest, dirs_exist_ok=True)
        print("Copied blueprints directory.")

    # 7. Add user_jvm_args.txt
    jvm_args_content = (
        "-Xms8G -Xmx8G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=100 "
        "-XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch "
        "-XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=16m "
        "-XX:G1ReservePercent=15 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 "
        "-XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 "
        "-XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=8\n"
    )
    with open(os.path.join(TEMP_SERVER_DIR, "user_jvm_args.txt"), "w", encoding="utf-8") as f:
        f.write(jvm_args_content)

    # 6. Create ZIP archive
    print(f"Creating ZIP archive at {OUTPUT_ZIP}...")
    if os.path.exists(OUTPUT_ZIP):
        os.remove(OUTPUT_ZIP)

    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(TEMP_SERVER_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, TEMP_SERVER_DIR)
                zipf.write(file_path, rel_path)

    zip_size_mb = os.path.getsize(OUTPUT_ZIP) / (1024 * 1024)
    print(f"Server pack successfully created! Archive size: {zip_size_mb:.2f} MB")

if __name__ == "__main__":
    build_server_pack()
