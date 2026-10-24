import os
import sys
import shutil
import zipfile
import subprocess
import time
import argparse
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

BASE_DEV = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MC_DIR = os.path.join(BASE_DEV, "minecraft")
EXCLUSIONS_FILE = os.path.join(MC_DIR, "server_pack_excluded_mods.txt")
STAGING_DIR = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\ServerPackStaging"
EXPORTS_DIR = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\PackExports"
NEOFORGE_VERSION = "21.1.248"
INSTALLER_SRC = rf"C:\Users\chris\AppData\Roaming\PrismLauncher\libraries\net\neoforged\neoforge\{NEOFORGE_VERSION}\neoforge-{NEOFORGE_VERSION}-installer.jar"

IGNORED_CONFIG_DIRS = {
    "fancymenu",
    "drippyloadingscreen",
    "panoptic",
    "crafttweaker",
    "search_index",
    "fancymenu_data",
    "fancymenu_temp",
    "seamless_world_loading",
    "video_thumbnails"
}

IGNORED_CONFIG_FILES = {
    "panoptic-common.toml",
    "fm_data.db",
    "smoothswapping.json",
    "last_world.fmdata",
    "resourcepack_load_order.json"
}

IGNORED_EXTENSIONS = {".bak", ".tmp", ".log"}

JVM_ARGS_CONTENT = """# PEAK Modpack - Dedicated Server JVM Arguments
# Java 21 LTS Recommended Flags

# Minimum and Maximum RAM allocation
# Recommended: 6GB to 8GB for dedicated servers
-Xms4G
-Xmx8G

# Modern G1GC Garbage Collection Flags (Optimized for Minecraft 1.21.1)
-XX:+UseG1GC
-XX:+ParallelRefProcEnabled
-XX:MaxGCPauseMillis=200
-XX:+UnlockExperimentalVMOptions
-XX:+DisableExplicitGC
-XX:+AlwaysPreTouch
-XX:G1NewSizePercent=30
-XX:G1MaxNewSizePercent=40
-XX:G1ReservePercent=20
-XX:G1HeapWastePercent=5
-XX:G1MixedGCCountTarget=4
-XX:InitiatingHeapOccupancyPercent=15
-XX:G1MixedGCLiveThresholdPercent=90
-XX:G1RSetUpdatingPauseTimePercent=5
-XX:SurvivorRatio=32
-XX:+PerfDisableSharedMem
-XX:MaxTenuringThreshold=1
"""

SERVER_PROPERTIES_CONTENT = """# PEAK Modpack Server Configuration
motd=\\u00A76\\u00A7lPEAK\\u00A7r - \\u00A7eThe Pinnacle of Modpacks\\u00A7r
server-port=25565
allow-flight=true
max-tick-time=120000
view-distance=10
simulation-distance=8
difficulty=hard
enable-command-block=true
network-compression-threshold=256
sync-chunk-writes=false
spawn-protection=0
online-mode=true
max-players=20
pvp=true
enable-rcon=false
white-list=false
broadcast-rcon-to-ops=true
broadcast-console-to-ops=true
enforce-whitelist=false
"""

RUN_BAT_CONTENT = rf"""@echo off
TITLE PEAK Dedicated Server (NeoForge 1.21.1)

echo ========================================================
echo   PEAK Modpack - Dedicated Server Launch Script
echo ========================================================

IF NOT EXIST "libraries\net\neoforged\neoforge\{NEOFORGE_VERSION}\win_args.txt" (
    echo [INFO] First time setup: Installing NeoForge server libraries...
    java -jar neoforge-{NEOFORGE_VERSION}-installer.jar --installServer
    if %errorlevel% neq 0 (
        echo [ERROR] NeoForge installation failed. Please verify Java 21 is installed.
        pause
        exit /b %errorlevel%
    )
)

IF NOT EXIST eula.txt (
    echo eula=false>eula.txt
    echo [NOTICE] eula.txt created. Please open eula.txt, set eula=true, and start the server again.
    pause
    exit /b
)

findstr /i "eula=true" eula.txt >nul
if %errorlevel% neq 0 (
    echo [NOTICE] You must accept the Minecraft EULA by setting eula=true in eula.txt.
    pause
    exit /b
)

echo [INFO] Starting PEAK Server with configured JVM arguments...
java @user_jvm_args.txt @libraries/net/neoforged/neoforge/{NEOFORGE_VERSION}/win_args.txt nogui %*

if %errorlevel% neq 0 (
    echo [SERVER] Server process stopped or encountered an error.
)
pause
"""

RUN_SH_CONTENT = rf"""#!/bin/bash
echo "========================================================"
echo "  PEAK Modpack - Dedicated Server Launch Script (Linux) "
echo "========================================================"

if [ ! -f "libraries/net/neoforged/neoforge/{NEOFORGE_VERSION}/unix_args.txt" ]; then
    echo "[INFO] First time setup: Installing NeoForge server libraries..."
    java -jar neoforge-{NEOFORGE_VERSION}-installer.jar --installServer
    if [ $? -ne 0 ]; then
        echo "[ERROR] NeoForge installation failed. Please verify Java 21 is installed."
        exit 1
    fi
fi

if [ ! -f "eula.txt" ]; then
    echo "eula=false" > eula.txt
    echo "[NOTICE] eula.txt created. Please open eula.txt, set eula=true, and start the server again."
    exit 0
fi

if ! grep -qi "eula=true" eula.txt; then
    echo "[NOTICE] You must accept the Minecraft EULA by setting eula=true in eula.txt."
    exit 0
fi

echo "[INFO] Starting PEAK Server with configured JVM arguments..."
java @user_jvm_args.txt @libraries/net/neoforged/neoforge/{NEOFORGE_VERSION}/unix_args.txt nogui "$@"
"""

def load_exclusions():
    exclusions = set()
    if os.path.exists(EXCLUSIONS_FILE):
        with open(EXCLUSIONS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    exclusions.add(line.lower())
    print(f"Loaded {len(exclusions)} exclusion filenames from {EXCLUSIONS_FILE}")
    return exclusions

def stage_server_pack(version="alpha3"):
    print("========================================================")
    print(f" Staging PEAK Dedicated Server Pack ({version})")
    print(f" Source: {MC_DIR}")
    print(f" Destination: {STAGING_DIR}")
    print("========================================================")

    if os.path.exists(STAGING_DIR):
        print("Cleaning previous staging directory...")
        shutil.rmtree(STAGING_DIR)
    os.makedirs(STAGING_DIR, exist_ok=True)

    exclusions = load_exclusions()

    # 1. Copy Server Mods
    src_mods = os.path.join(MC_DIR, "mods")
    dst_mods = os.path.join(STAGING_DIR, "mods")
    os.makedirs(dst_mods, exist_ok=True)

    all_mods = os.listdir(src_mods)
    copied_mods = 0
    excluded_mods = 0

    for m in sorted(all_mods):
        src_file = os.path.join(src_mods, m)
        if not os.path.isfile(src_file) or not m.endswith(".jar"):
            continue
        if m.lower() in exclusions:
            excluded_mods += 1
            continue
        shutil.copy2(src_file, os.path.join(dst_mods, m))
        copied_mods += 1

    print(f"[MODS] Staged {copied_mods} active server mods (excluded {excluded_mods} client/dev mods).")

    # 2. Copy Config Tree (sanitizing BOMs and skipping client configs)
    src_config = os.path.join(MC_DIR, "config")
    dst_config = os.path.join(STAGING_DIR, "config")

    copied_configs = 0
    for root, dirs, files in os.walk(src_config):
        rel_root = os.path.relpath(root, src_config).replace("\\", "/")
        
        # Skip paxi resourcepacks (keep paxi datapacks)
        if rel_root.startswith("paxi/resourcepacks"):
            dirs.clear()
            continue
        
        # Filter directories
        dirs[:] = [d for d in dirs if d.lower() not in IGNORED_CONFIG_DIRS]

        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in IGNORED_EXTENSIONS or file.lower() in IGNORED_CONFIG_FILES:
                continue

            src_path = os.path.join(root, file)
            target_rel = os.path.relpath(src_path, src_config)
            dst_path = os.path.join(dst_config, target_rel)
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)

            with open(src_path, "rb") as f_in:
                data = f_in.read()
            if data.startswith(b"\xef\xbb\xbf"):
                data = data[3:]
            with open(dst_path, "wb") as f_out:
                f_out.write(data)
            copied_configs += 1

    print(f"[CONFIG] Staged {copied_configs} configuration files (omitted client caches & resource packs).")

    # 3. Copy defaultconfigs
    src_defcfg = os.path.join(MC_DIR, "defaultconfigs")
    dst_defcfg = os.path.join(STAGING_DIR, "defaultconfigs")
    if os.path.exists(src_defcfg):
        shutil.copytree(src_defcfg, dst_defcfg)
        count = sum(len(f) for _, _, f in os.walk(dst_defcfg))
        print(f"[DEFAULTCONFIGS] Staged {count} default configuration files.")

    # 4. Copy KubeJS (server_scripts, startup_scripts, data, config)
    src_kjs = os.path.join(MC_DIR, "kubejs")
    dst_kjs = os.path.join(STAGING_DIR, "kubejs")
    kjs_count = 0
    for sub in ["server_scripts", "startup_scripts", "data", "config"]:
        s_path = os.path.join(src_kjs, sub)
        d_path = os.path.join(dst_kjs, sub)
        if os.path.exists(s_path):
            shutil.copytree(s_path, d_path)
            kjs_count += sum(len(f) for _, _, f in os.walk(d_path))
    print(f"[KUBEJS] Staged {kjs_count} script and data files (server_scripts, startup_scripts, data, config).")

    # 5. Copy datapacks & blueprints if present
    for extra in ["datapacks", "blueprints"]:
        s_extra = os.path.join(MC_DIR, extra)
        d_extra = os.path.join(STAGING_DIR, extra)
        if os.path.exists(s_extra):
            shutil.copytree(s_extra, d_extra)
            extra_count = sum(len(f) for _, _, f in os.walk(d_extra))
            print(f"[{extra.upper()}] Staged {extra_count} files.")

    # 6. Copy NeoForge Installer
    if not os.path.exists(INSTALLER_SRC):
        raise FileNotFoundError(f"NeoForge installer not found at: {INSTALLER_SRC}")
    dst_installer = os.path.join(STAGING_DIR, f"neoforge-{NEOFORGE_VERSION}-installer.jar")
    shutil.copy2(INSTALLER_SRC, dst_installer)
    print(f"[INSTALLER] Staged neoforge-{NEOFORGE_VERSION}-installer.jar ({os.path.getsize(dst_installer) / (1024*1024):.2f} MB).")

    # 7. Pre-install NeoForge Server Libraries
    print(f"[INSTALLER] Running java -jar neoforge-{NEOFORGE_VERSION}-installer.jar --installServer...")
    proc = subprocess.run(["java", "-jar", dst_installer, "--installServer"], cwd=STAGING_DIR, capture_output=True, text=True)
    if proc.returncode != 0:
        print("[ERROR] Installer stdout:", proc.stdout)
        print("[ERROR] Installer stderr:", proc.stderr)
        raise RuntimeError(f"NeoForge installer failed with exit code {proc.returncode}!")
    
    # Clean installer log
    log_file = os.path.join(STAGING_DIR, f"neoforge-{NEOFORGE_VERSION}-installer.jar.log")
    if os.path.exists(log_file):
        os.remove(log_file)
    lib_count = sum(len(f) for _, _, f in os.walk(os.path.join(STAGING_DIR, "libraries")))
    print(f"[LIBRARIES] Pre-installed {lib_count} server library files.")

    # 8. Write runtime files
    with open(os.path.join(STAGING_DIR, "run.bat"), "w", encoding="utf-8") as f:
        f.write(RUN_BAT_CONTENT)

    with open(os.path.join(STAGING_DIR, "run.sh"), "w", encoding="utf-8", newline="\n") as f:
        f.write(RUN_SH_CONTENT)

    with open(os.path.join(STAGING_DIR, "user_jvm_args.txt"), "w", encoding="utf-8") as f:
        f.write(JVM_ARGS_CONTENT)

    with open(os.path.join(STAGING_DIR, "server.properties"), "w", encoding="utf-8") as f:
        f.write(SERVER_PROPERTIES_CONTENT)

    with open(os.path.join(STAGING_DIR, "eula.txt"), "w", encoding="utf-8") as f:
        f.write("eula=false\n")

    print("[BOOTSTRAP] Generated run.bat, run.sh (Unix LF), user_jvm_args.txt, server.properties, eula.txt.")

def compress_and_verify(version="alpha3"):
    output_zip = os.path.join(EXPORTS_DIR, f"Peak-Server-{version}.zip")
    staged_zip = os.path.join(tempfile.gettempdir(), f"Peak-Server-{version}.zip")

    # Purge any test or runtime artifacts from staging
    allowed_dirs = {"blueprints", "config", "datapacks", "defaultconfigs", "kubejs", "libraries", "mods"}
    allowed_files = {"eula.txt", f"neoforge-{NEOFORGE_VERSION}-installer.jar", "run.bat", "run.sh", "server.properties", "user_jvm_args.txt"}
    for item in os.listdir(STAGING_DIR):
        p = os.path.join(STAGING_DIR, item)
        if os.path.isdir(p):
            if item not in allowed_dirs:
                shutil.rmtree(p)
        else:
            if item not in allowed_files:
                os.remove(p)

    print("\n========================================================")
    print(f" Compressing Server Pack: Peak-Server-{version}.zip")
    print(f" Source: {STAGING_DIR}")
    print(f" Output: {output_zip}")
    print("========================================================")

    start_time = time.time()
    file_count = 0

    with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
        for root, dirs, files in os.walk(STAGING_DIR):
            for f in files:
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, STAGING_DIR).replace("\\", "/")
                zout.write(full_path, arcname=rel_path)
                file_count += 1
                if file_count % 100 == 0:
                    sys.stdout.write(f"\rCompressed {file_count} files...")
                    sys.stdout.flush()

    elapsed = time.time() - start_time
    zip_size_mb = os.path.getsize(output_zip) / (1024 * 1024)
    print(f"\nCompression complete in {elapsed:.1f} seconds!")
    print(f"Total Files in ZIP: {file_count} | Size: {zip_size_mb:.2f} MB")

    # Stage copy for browser/temp
    shutil.copy2(output_zip, staged_zip)
    print(f"Staged server pack at: {staged_zip}")

    # Verify integrity
    print("Verifying archive integrity...")
    with zipfile.ZipFile(output_zip, "r") as zver:
        corrupted = zver.testzip()
        if corrupted:
            raise RuntimeError(f"Corrupted entry detected in archive: {corrupted}")
        
        root_items = set(n.split("/")[0] for n in zver.namelist())
        required_roots = {"mods", "config", "defaultconfigs", "kubejs", "libraries", "run.bat", "run.sh", "server.properties", "user_jvm_args.txt", "eula.txt"}
        missing_roots = required_roots - root_items
        if missing_roots:
            raise RuntimeError(f"Missing required root items in archive: {missing_roots}")
        
        # Verify no loose disabled mods
        disabled_jars = [n for n in zver.namelist() if n.endswith(".jar.disabled")]
        if disabled_jars:
            raise RuntimeError(f"Found loose disabled jars in server pack: {disabled_jars}")

        # Verify CraftTweaker is present for alpha3 network parity
        ct_present = any("crafttweaker" in n.lower() for n in zver.namelist())
        assert ct_present, "CraftTweaker must be present in alpha3 server pack for client channel parity!"

        # Verify SeedGen is NOT present
        seedgen_present = any("seedgen" in n.lower() for n in zver.namelist())
        assert not seedgen_present, "Distant Horizons SeedGen must NOT be present in alpha3 server pack!"

        print(f"Integrity test PASSED! Verified root structure: {sorted(list(root_items))}")
        print(f"Server Pack Peak-Server-{version}.zip is 100% verified and ready for production!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PEAK Dedicated Server Pack Builder")
    parser.add_argument("--version", type=str, default="alpha3", help="Target release version string (e.g. alpha3)")
    args = parser.parse_args()

    stage_server_pack(version=args.version)
    compress_and_verify(version=args.version)
