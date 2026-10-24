import os
import sys
import json
import zipfile
import shutil
import re

sys.stdout.reconfigure(encoding="utf-8")

BASE_DEV = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_LITE = os.path.abspath(os.path.join(BASE_DEV, "..", "PEAK-Lite"))
DEV_MC = os.path.join(BASE_DEV, "minecraft")
LITE_MC = os.path.join(BASE_LITE, "minecraft")

PACK_EXPORTS_DIR = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\PackExports"
ALPHA1_ZIP = os.path.join(PACK_EXPORTS_DIR, "Peak-alpha1.zip")

TEMP_DIR = os.environ.get("TEMP", r"C:\Users\chris\AppData\Local\Temp")

REMOVED_PIDS_DEV = {
    682567,   # Easy Anvils
    1470821,  # AnvilCore
    281849    # PneumaticCraft: Repressurized
}

DEAD_PIDS = {1277910}

UPDATED_FILES = {
    1040076: 9128508,  # IceAndFire Community Edition -> 2.1.4
    1559657: 9099698,  # Yet Another Gravestone [YAGM] -> 0.1.5
    1676741: 9228021,  # Spatial GUI -> 1.8
    1327508: 9257162,  # Tooltip Overhaul -> 2.0.7
    967617: 9021968,   # EntityJS -> 1.5.2
    1368368: 8616457,  # Evolution of Entities -> 1.9
    1487841: 9165847,  # Better Combat - Heavier Weapons -> 1.2.0
    568563: 9188408,   # Entity Texture Features -> 7.2.6
    844662: 9188526,   # Entity Model Features -> 3.3.12
    1605113: 9205847,  # EMF Compat Core -> 2.3.2
    1605147: 9190768   # EMF Compat Better Combat -> 2.1.1
}

INJECTED_CF_MODS = [
    {"projectID": 367706, "fileID": 9002957, "required": True},  # FancyMenu (3.9.14 NeoForge 1.21.1)
    {"projectID": 511770, "fileID": 8552907, "required": True},  # Drippy Loading Screen (3.1.5 NeoForge 1.21.1)
    {"projectID": 1390924, "fileID": 8552908, "required": True}, # Drippy Early Loading Module (3.1.5 NeoForge 1.21.1)
    {"projectID": 410295, "fileID": 5453385, "required": True},  # Konkrete (1.9.9 NeoForge 1.21.1)
    {"projectID": 938643, "fileID": 5453382, "required": True},  # Melody (1.0.10 NeoForge 1.21.1)
]

LITE_EXCLUDED_PIDS = {
    # 239197, # CraftTweaker: Retained in Lite alpha3 for Essential server compatibility; exclude in alpha4 across both editions
    513689,   # Smooth Swapping
    1182393,  # Cosy Critters & Creepy Crawlies
    393442,   # LambDynamicLights
    1494094,  # Shine: VFX
    1552769,  # Diamond's Cloud Layers
    1413643,  # Foxified Dense Flowers
    1150640,  # Loot Beams: Refork
    1374153,  # Punchy! - First person animations
    1493725,  # ATMOSPHERICS
    1036246,  # Explosive Enhancement: Reforged
    985426,   # Particle Core
    1452982,  # Fancy World Animations
    1676741,  # Spatial GUI
    361579,   # spark
    433760,   # Not Enough Animations
    1620784,  # Panoptic
    704256,   # Visuality: Reforged
    1164411,  # Nirvana Library
    1219053,  # Particular Reforged
    1112793,  # Perception
    909375    # WITS (What Is This Structure?)
}

IGNORED_EXTENSIONS = {".bak", ".tmp", ".log"}
IGNORED_CONFIG_DIRS = {"panoptic", "crafttweaker", "search_index"}
IGNORED_CONFIG_FILES = {"panoptic-common.toml", "fm_data.db"}
IGNORED_FANCYMENU_DATA_DIRS = {"fancymenu_temp", "seamless_world_loading", "video_thumbnails"}
IGNORED_FANCYMENU_DATA_FILES = {"last_world.fmdata"}

VANILLA_KEYBINDS = {
    "key_key.attack",
    "key_key.use",
    "key_key.forward",
    "key_key.left",
    "key_key.back",
    "key_key.right",
    "key_key.jump",
    "key_key.sneak",
    "key_key.sprint",
    "key_key.drop",
    "key_key.inventory",
    "key_key.chat",
    "key_key.playerlist",
    "key_key.pickItem",
    "key_key.command",
    "key_key.socialInteractions",
    "key_key.screenshot",
    "key_key.togglePerspective",
    "key_key.smoothCamera",
    "key_key.fullscreen",
    "key_key.spectatorOutlines",
    "key_key.swapOffhand",
    "key_key.saveToolbarActivator",
    "key_key.loadToolbarActivator",
    "key_key.advancements",
    "key_key.hotbar.1",
    "key_key.hotbar.2",
    "key_key.hotbar.3",
    "key_key.hotbar.4",
    "key_key.hotbar.5",
    "key_key.hotbar.6",
    "key_key.hotbar.7",
    "key_key.hotbar.8",
    "key_key.hotbar.9"
}

def collect_overrides(mc_dir, is_lite=False):
    """Walks override folders and collects file entries, stripping BOMs and preventing loose jars."""
    entries = {}
    override_folders = ["config", "defaultconfigs", "kubejs", "fancymenu_data"]
    for folder in override_folders:
        folder_path = os.path.join(mc_dir, folder)
        if not os.path.isdir(folder_path):
            continue

        for root, dirs, files in os.walk(folder_path):
            if folder == "config":
                dirs[:] = [d for d in dirs if d.lower() not in IGNORED_CONFIG_DIRS]
            elif folder == "fancymenu_data":
                dirs[:] = [d for d in dirs if d.lower() not in IGNORED_FANCYMENU_DATA_DIRS]

            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in IGNORED_EXTENSIONS:
                    continue
                if folder == "config" and file.lower() in IGNORED_CONFIG_FILES:
                    continue
                if folder == "fancymenu_data" and file.lower() in IGNORED_FANCYMENU_DATA_FILES:
                    continue
                if file.lower().endswith(".jar") or file.lower().endswith(".jar.disabled"):
                    raise RuntimeError(f"FATAL: Loose JAR found in overrides: {file} at {root}")

                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, mc_dir)
                entry_name = ("overrides/" + rel_path.replace("\\", "/")).strip()

                with open(abs_path, "rb") as f_in:
                    content = f_in.read()

                if content.startswith(b"\xef\xbb\xbf"):
                    content = content[3:]

                # For Lite, ensure DistantHorizons lodChunkRenderDistanceRadius is 32
                if is_lite and entry_name == "overrides/config/DistantHorizons.toml":
                    text = content.decode("utf-8", errors="replace")
                    text = re.sub(r"lodChunkRenderDistanceRadius\s*=\s*\d+", "lodChunkRenderDistanceRadius = 32", text)
                    content = text.encode("utf-8")

                # For Lite, turn on Better Combat weapon swing animations in first person
                if is_lite and entry_name == "overrides/config/bettercombat/client.json5":
                    text = content.decode("utf-8", errors="replace")
                    text = re.sub(r'"firstPersonAnimations"\s*:\s*"[^"]*"', '"firstPersonAnimations": "YES"', text)
                    content = text.encode("utf-8")

                # Enforce FancyMenu modpack lock mode and suppress welcome screen in exported packs
                if entry_name == "overrides/config/fancymenu/options.txt":
                    text = content.decode("utf-8", errors="replace")
                    text = re.sub(r"B:modpack_mode\s*=\s*'[a-zA-Z]+';", "B:modpack_mode = 'true';", text)
                    text = re.sub(r"B:show_welcome_screen\s*=\s*'[a-zA-Z]+';", "B:show_welcome_screen = 'false';", text)
                    content = text.encode("utf-8")

                entries[entry_name] = content

    options_path = os.path.join(mc_dir, "options.txt")
    if os.path.isfile(options_path):
        with open(options_path, "rb") as f_in:
            opt_content = f_in.read()
        if opt_content.startswith(b"\xef\xbb\xbf"):
            opt_content = opt_content[3:]
        # Strip common vanilla player keybinds so developer controls are never exported,
        # allowing Minecraft to initialize standard defaults and preserve player keybinds on updates.
        opt_text = opt_content.decode("utf-8", errors="replace")
        clean_lines = []
        for line in opt_text.splitlines():
            line_clean = line.strip()
            key_name = line_clean.split(":", 1)[0].strip() if ":" in line_clean else ""
            if key_name in VANILLA_KEYBINDS:
                continue
            clean_lines.append(line)
        entries["overrides/options.txt"] = ("\n".join(clean_lines) + "\n").encode("utf-8")

    return entries

def build_dev_pack(version="alpha3"):
    dev_out_zip = os.path.join(PACK_EXPORTS_DIR, f"Peak-{version}.zip")
    dev_staged_zip = os.path.join(TEMP_DIR, f"Peak-{version}.zip")
    print("\n========================================================")
    print(f" Building CurseForge Export: Peak-{version}.zip")
    print("========================================================")

    assert os.path.isfile(ALPHA1_ZIP), f"Alpha 1 reference ZIP not found: {ALPHA1_ZIP}"
    with zipfile.ZipFile(ALPHA1_ZIP, "r") as zalpha1:
        raw_manifest = zalpha1.read("manifest.json").decode("utf-8-sig")
        manifest_data = json.loads(raw_manifest)
        raw_modlist = zalpha1.read("modlist.html").decode("utf-8-sig")
        logo_bytes = zalpha1.read("profileImage/logo_square_preview.png")

    manifest_data["name"] = "Peak"
    manifest_data["version"] = version
    manifest_data["author"] = "eldodoron"
    if "minecraft" in manifest_data:
        manifest_data["minecraft"]["recommendedRam"] = 7520
        manifest_data["minecraft"]["modLoaders"] = [{"id": "neoforge-21.1.248", "primary": True}]

    original_files = manifest_data.get("files", [])
    filtered_files = []
    for f in original_files:
        pid = f.get("projectID")
        if pid in REMOVED_PIDS_DEV or pid in DEAD_PIDS:
            continue
        if pid in UPDATED_FILES:
            f = dict(f)
            f["fileID"] = UPDATED_FILES[pid]
        filtered_files.append(f)

    manifest_data["files"] = filtered_files
    existing_pids = {f["projectID"] for f in filtered_files}
    for mod in INJECTED_CF_MODS:
        if mod["projectID"] not in existing_pids:
            filtered_files.append(dict(mod))
    manifest_data["files"] = filtered_files
    print(f"Manifest mods: {len(original_files)} -> {len(filtered_files)} (removed {len(original_files) - len(filtered_files) + len(INJECTED_CF_MODS)}, added {len(INJECTED_CF_MODS)} CF mods)")
    assert len(filtered_files) == 407, f"Expected 407 mods for Dev {version}, got {len(filtered_files)}"

    manifest_bytes = json.dumps(manifest_data, indent=2).encode("utf-8")
    assert manifest_bytes[0] == ord("{"), "Manifest must start with '{'"

    # Filter modlist.html to remove easy-anvils, anvilcore, and pneumaticcraft
    modlist_lines = raw_modlist.splitlines()
    filtered_modlist_lines = []
    for line in modlist_lines:
        lower = line.lower()
        if "easy-anvils" in lower or "anvilcore" in lower or "pneumaticcraft" in lower:
            continue
        filtered_modlist_lines.append(line)

    injected_html_entries = [
        '<li><a href="https://www.curseforge.com/minecraft/mc-mods/fancymenu">FancyMenu (by Keksuccino)</a></li>',
        '<li><a href="https://www.curseforge.com/minecraft/mc-mods/drippy-loading-screen">Drippy Loading Screen (by Keksuccino)</a></li>',
        '<li><a href="https://www.curseforge.com/minecraft/mc-mods/drippy-early-loading-module">Drippy Early Loading Module (by Keksuccino)</a></li>',
        '<li><a href="https://www.curseforge.com/minecraft/mc-mods/konkrete">Konkrete (by Keksuccino)</a></li>',
        '<li><a href="https://www.curseforge.com/minecraft/mc-mods/melody">Melody (by Keksuccino)</a></li>'
    ]
    if filtered_modlist_lines and filtered_modlist_lines[-1].strip() == "</ul>":
        filtered_modlist_lines = filtered_modlist_lines[:-1] + injected_html_entries + ["</ul>"]
    else:
        filtered_modlist_lines.extend(injected_html_entries)
    filtered_modlist = "\n".join(filtered_modlist_lines).encode("utf-8")

    # Collect overrides from DEV_MC
    print("Collecting overrides from PEAK-dev...")
    overrides = collect_overrides(DEV_MC, is_lite=False)
    print(f"Collected {len(overrides)} override files.")

    # Write DEV ZIP
    temp_zip = dev_out_zip + ".tmp"
    with zipfile.ZipFile(temp_zip, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        zout.writestr("manifest.json", manifest_bytes)
        zout.writestr("modlist.html", filtered_modlist)
        zout.writestr("profileImage/logo_square_preview.png", logo_bytes)
        for name, content in overrides.items():
            zout.writestr(name, content)

    if os.path.exists(dev_out_zip):
        os.remove(dev_out_zip)
    shutil.move(temp_zip, dev_out_zip)
    print(f"Export ZIP written to: {dev_out_zip} ({os.path.getsize(dev_out_zip) / (1024*1024):.2f} MB)")

    # Stage for browser agent
    shutil.copy2(dev_out_zip, dev_staged_zip)
    print(f"Staged ZIP for browser agent at: {dev_staged_zip}")

    # Validate
    with zipfile.ZipFile(dev_out_zip, "r") as zver:
        man_raw = zver.read("manifest.json")
        assert man_raw[0] == ord("{")
        man = json.loads(man_raw.decode("utf-8"))
        assert man["name"] == "Peak"
        assert man["version"] == version
        assert man["author"] == "eldodoron"
        assert man["minecraft"]["modLoaders"][0]["id"] == "neoforge-21.1.248"
        assert len(man["files"]) == 407
        dev_pids = {f["projectID"] for f in man["files"]}
        for mod in INJECTED_CF_MODS:
            assert mod["projectID"] in dev_pids, f"Missing injected mod PID {mod['projectID']} in Dev manifest!"
        jars = [n for n in zver.namelist() if n.endswith(".jar") or n.endswith(".jar.disabled")]
        assert len(jars) == 0, f"Found loose jars: {jars}"
    print(f"Dev {version} Package Verified Successfully!")

    return manifest_data, filtered_modlist_lines, logo_bytes

def build_lite_pack(dev_manifest, dev_modlist_lines, logo_bytes, version="alpha3"):
    lite_out_zip = os.path.join(PACK_EXPORTS_DIR, f"Peak-Lite-{version}.zip")
    lite_staged_zip = os.path.join(TEMP_DIR, f"Peak-Lite-{version}.zip")
    print("\n========================================================")
    print(f" Building CurseForge Export: Peak-Lite-{version}.zip")
    print("========================================================")

    lite_manifest = dict(dev_manifest)
    lite_manifest["name"] = "Peak Lite"
    lite_manifest["version"] = version
    lite_manifest["author"] = "eldodoron"
    if "minecraft" in lite_manifest:
        lite_manifest["minecraft"]["recommendedRam"] = 6348
        lite_manifest["minecraft"]["modLoaders"] = [{"id": "neoforge-21.1.248", "primary": True}]

    dev_files = dev_manifest.get("files", [])
    lite_files = [
        f for f in dev_files
        if f.get("projectID") not in LITE_EXCLUDED_PIDS and f.get("projectID") not in DEAD_PIDS
    ]
    lite_manifest["files"] = lite_files
    print(f"Manifest mods: {len(dev_files)} -> {len(lite_files)} (removed {len(dev_files) - len(lite_files)})")
    assert len(lite_files) == 386, f"Expected 386 mods for Lite {version}, got {len(lite_files)}"

    manifest_bytes = json.dumps(lite_manifest, indent=2).encode("utf-8")
    assert manifest_bytes[0] == ord("{"), "Manifest must start with '{'"

    # Modlist filter for Lite
    inst_path = r"C:\Users\chris\curseforge\minecraft\Instances\Peak (Dev)\minecraftinstance.json"
    with open(inst_path, "r", encoding="utf-8") as f:
        inst_data = json.load(f)

    excluded_slugs = set()
    for addon in inst_data.get("installedAddons", []):
        if addon.get("addonID") in LITE_EXCLUDED_PIDS:
            url = addon.get("webSiteURL", "")
            if url:
                slug = url.rstrip("/").split("/")[-1].lower()
                excluded_slugs.add(slug)

    filtered_modlist_lines = []
    removed_modlist_count = 0
    for line in dev_modlist_lines:
        lower = line.lower()
        is_excluded = False
        if line.strip().startswith("<li>"):
            for slug in excluded_slugs:
                if f"/{slug}\"" in lower or f"/{slug}/" in lower:
                    is_excluded = True
                    break
        if is_excluded:
            removed_modlist_count += 1
        else:
            filtered_modlist_lines.append(line)

    filtered_modlist = "\n".join(filtered_modlist_lines).encode("utf-8")
    print(f"Modlist lines: {len(dev_modlist_lines)} -> {len(filtered_modlist_lines)} (removed {removed_modlist_count})")

    # Collect overrides from LITE_MC
    print("Collecting overrides from PEAK-Lite...")
    overrides = collect_overrides(LITE_MC, is_lite=True)
    print(f"Collected {len(overrides)} override files for Lite.")

    # Write LITE ZIP
    temp_zip = lite_out_zip + ".tmp"
    with zipfile.ZipFile(temp_zip, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        zout.writestr("manifest.json", manifest_bytes)
        zout.writestr("modlist.html", filtered_modlist)
        zout.writestr("profileImage/logo_square_preview.png", logo_bytes)
        for name, content in overrides.items():
            zout.writestr(name, content)

    if os.path.exists(lite_out_zip):
        os.remove(lite_out_zip)
    shutil.move(temp_zip, lite_out_zip)
    print(f"Export ZIP written to: {lite_out_zip} ({os.path.getsize(lite_out_zip) / (1024*1024):.2f} MB)")

    # Stage for browser agent
    shutil.copy2(lite_out_zip, lite_staged_zip)
    print(f"Staged ZIP for browser agent at: {lite_staged_zip}")

    # Validate
    with zipfile.ZipFile(lite_out_zip, "r") as zver:
        man_raw = zver.read("manifest.json")
        assert man_raw[0] == ord("{")
        man = json.loads(man_raw.decode("utf-8"))
        assert man["name"] == "Peak Lite"
        assert man["version"] == version
        assert man["author"] == "eldodoron"
        assert man["minecraft"]["modLoaders"][0]["id"] == "neoforge-21.1.248"
        assert len(man["files"]) == 386
        lite_pids = {f["projectID"] for f in man["files"]}
        for mod in INJECTED_CF_MODS:
            assert mod["projectID"] in lite_pids, f"Missing injected mod PID {mod['projectID']} in Lite manifest!"
        assert man["minecraft"]["recommendedRam"] == 6348, "Recommended RAM for Lite must be 6348!"
        jars = [n for n in zver.namelist() if n.endswith(".jar") or n.endswith(".jar.disabled")]
        assert len(jars) == 0, f"Found loose jars: {jars}"
        dh_raw = zver.read("overrides/config/DistantHorizons.toml").decode("utf-8")
        assert "lodChunkRenderDistanceRadius = 32" in dh_raw, "DH radius in Lite is not 32!"
        bc_raw = zver.read("overrides/config/bettercombat/client.json5").decode("utf-8")
        assert '"firstPersonAnimations": "YES"' in bc_raw, "Better Combat first person animations not enabled in Lite!"
    print(f"Lite {version} Package Verified Successfully (Including DistantHorizons = 32 and Better Combat Animations = YES)!")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="CurseForge export builder")
    parser.add_argument("--version", type=str, default="alpha3", help="Target release version string (e.g. alpha3)")
    parser.add_argument("--lite", action="store_true", help="Also build PEAK Lite export")
    parser.add_argument("--only-lite", action="store_true", help="Build PEAK Lite export")
    args = parser.parse_args()

    dev_manifest, dev_modlist_lines, logo_bytes = build_dev_pack(version=args.version)
    if args.lite or args.only_lite:
        build_lite_pack(dev_manifest, dev_modlist_lines, logo_bytes, version=args.version)
