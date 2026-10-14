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

DEV_OUT_ZIP = os.path.join(PACK_EXPORTS_DIR, "Peak-alpha2.zip")
LITE_OUT_ZIP = os.path.join(PACK_EXPORTS_DIR, "Peak-Lite-alpha2.zip")

TEMP_DIR = os.environ.get("TEMP", r"C:\Users\chris\AppData\Local\Temp")
DEV_STAGED_ZIP = os.path.join(TEMP_DIR, "Peak-alpha2.zip")
LITE_STAGED_ZIP = os.path.join(TEMP_DIR, "Peak-Lite-alpha2.zip")

REMOVED_PIDS_DEV = {
    682567,   # Easy Anvils
    1470821   # AnvilCore
}

DEAD_PIDS = {1277910}

UPDATED_FILES = {
    1040076: 9128508,  # IceAndFire Community Edition -> 2.1.4
    1559657: 9099698   # Yet Another Gravestone [YAGM] -> 0.1.5
}

LITE_EXCLUDED_PIDS = {
    239197,   # CraftTweaker
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
IGNORED_CONFIG_FILES = {"panoptic-common.toml", "smoothswapping.json"}

def collect_overrides(mc_dir, is_lite=False):
    """Walks override folders and collects file entries, stripping BOMs and preventing loose jars."""
    entries = {}
    override_folders = ["config", "defaultconfigs", "kubejs"]
    for folder in override_folders:
        folder_path = os.path.join(mc_dir, folder)
        if not os.path.isdir(folder_path):
            continue

        for root, dirs, files in os.walk(folder_path):
            if folder == "config":
                dirs[:] = [d for d in dirs if d.lower() not in IGNORED_CONFIG_DIRS]

            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in IGNORED_EXTENSIONS:
                    continue
                if folder == "config" and file.lower() in IGNORED_CONFIG_FILES:
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

                entries[entry_name] = content

    options_path = os.path.join(mc_dir, "options.txt")
    if os.path.isfile(options_path):
        with open(options_path, "rb") as f_in:
            opt_content = f_in.read()
        if opt_content.startswith(b"\xef\xbb\xbf"):
            opt_content = opt_content[3:]
        entries["overrides/options.txt"] = opt_content

    return entries

def build_dev_pack():
    print("\n========================================================")
    print(" Building CurseForge Export: Peak-alpha2.zip")
    print("========================================================")

    assert os.path.isfile(ALPHA1_ZIP), f"Alpha 1 reference ZIP not found: {ALPHA1_ZIP}"
    with zipfile.ZipFile(ALPHA1_ZIP, "r") as zalpha1:
        raw_manifest = zalpha1.read("manifest.json").decode("utf-8-sig")
        manifest_data = json.loads(raw_manifest)
        raw_modlist = zalpha1.read("modlist.html").decode("utf-8-sig")
        logo_bytes = zalpha1.read("profileImage/logo_square_preview.png")

    manifest_data["name"] = "Peak"
    manifest_data["version"] = "alpha2"
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
    print(f"Manifest mods: {len(original_files)} -> {len(filtered_files)} (removed {len(original_files) - len(filtered_files)})")
    assert len(filtered_files) == 403, f"Expected 403 mods for Dev Alpha 2, got {len(filtered_files)}"

    manifest_bytes = json.dumps(manifest_data, indent=2).encode("utf-8")
    assert manifest_bytes[0] == ord("{"), "Manifest must start with '{'"

    # Filter modlist.html to remove easy-anvils and anvilcore
    modlist_lines = raw_modlist.splitlines()
    filtered_modlist_lines = []
    for line in modlist_lines:
        lower = line.lower()
        if "easy-anvils" in lower or "anvilcore" in lower:
            continue
        filtered_modlist_lines.append(line)
    filtered_modlist = "\n".join(filtered_modlist_lines).encode("utf-8")

    # Collect overrides from DEV_MC
    print("Collecting overrides from PEAK-dev...")
    overrides = collect_overrides(DEV_MC, is_lite=False)
    print(f"Collected {len(overrides)} override files.")

    # Write DEV ZIP
    temp_zip = DEV_OUT_ZIP + ".tmp"
    with zipfile.ZipFile(temp_zip, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        zout.writestr("manifest.json", manifest_bytes)
        zout.writestr("modlist.html", filtered_modlist)
        zout.writestr("profileImage/logo_square_preview.png", logo_bytes)
        for name, content in overrides.items():
            zout.writestr(name, content)

    if os.path.exists(DEV_OUT_ZIP):
        os.remove(DEV_OUT_ZIP)
    shutil.move(temp_zip, DEV_OUT_ZIP)
    print(f"Export ZIP written to: {DEV_OUT_ZIP} ({os.path.getsize(DEV_OUT_ZIP) / (1024*1024):.2f} MB)")

    # Stage for browser agent
    shutil.copy2(DEV_OUT_ZIP, DEV_STAGED_ZIP)
    print(f"Staged ZIP for browser agent at: {DEV_STAGED_ZIP}")

    # Validate
    with zipfile.ZipFile(DEV_OUT_ZIP, "r") as zver:
        man_raw = zver.read("manifest.json")
        assert man_raw[0] == ord("{")
        man = json.loads(man_raw.decode("utf-8"))
        assert man["name"] == "Peak"
        assert man["version"] == "alpha2"
        assert man["author"] == "eldodoron"
        assert man["minecraft"]["modLoaders"][0]["id"] == "neoforge-21.1.248"
        assert len(man["files"]) == 403
        jars = [n for n in zver.namelist() if n.endswith(".jar") or n.endswith(".jar.disabled")]
        assert len(jars) == 0, f"Found loose jars: {jars}"
    print("Dev Alpha 2 Package Verified Successfully!")

    return manifest_data, filtered_modlist_lines, logo_bytes

def build_lite_pack(dev_manifest, dev_modlist_lines, logo_bytes):
    print("\n========================================================")
    print(" Building CurseForge Export: Peak-Lite-alpha2.zip")
    print("========================================================")

    lite_manifest = dict(dev_manifest)
    lite_manifest["name"] = "Peak Lite"
    lite_manifest["version"] = "alpha2"
    lite_manifest["author"] = "eldodoron"
    if "minecraft" in lite_manifest:
        lite_manifest["minecraft"]["recommendedRam"] = 6144
        lite_manifest["minecraft"]["modLoaders"] = [{"id": "neoforge-21.1.248", "primary": True}]

    dev_files = dev_manifest.get("files", [])
    lite_files = [
        f for f in dev_files
        if f.get("projectID") not in LITE_EXCLUDED_PIDS and f.get("projectID") not in DEAD_PIDS
    ]
    lite_manifest["files"] = lite_files
    print(f"Manifest mods: {len(dev_files)} -> {len(lite_files)} (removed {len(dev_files) - len(lite_files)})")
    assert len(lite_files) == 381, f"Expected 381 mods for Lite Alpha 2, got {len(lite_files)}"

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
    temp_zip = LITE_OUT_ZIP + ".tmp"
    with zipfile.ZipFile(temp_zip, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        zout.writestr("manifest.json", manifest_bytes)
        zout.writestr("modlist.html", filtered_modlist)
        zout.writestr("profileImage/logo_square_preview.png", logo_bytes)
        for name, content in overrides.items():
            zout.writestr(name, content)

    if os.path.exists(LITE_OUT_ZIP):
        os.remove(LITE_OUT_ZIP)
    shutil.move(temp_zip, LITE_OUT_ZIP)
    print(f"Export ZIP written to: {LITE_OUT_ZIP} ({os.path.getsize(LITE_OUT_ZIP) / (1024*1024):.2f} MB)")

    # Stage for browser agent
    shutil.copy2(LITE_OUT_ZIP, LITE_STAGED_ZIP)
    print(f"Staged ZIP for browser agent at: {LITE_STAGED_ZIP}")

    # Validate
    with zipfile.ZipFile(LITE_OUT_ZIP, "r") as zver:
        man_raw = zver.read("manifest.json")
        assert man_raw[0] == ord("{")
        man = json.loads(man_raw.decode("utf-8"))
        assert man["name"] == "Peak Lite"
        assert man["version"] == "alpha2"
        assert man["author"] == "eldodoron"
        assert man["minecraft"]["modLoaders"][0]["id"] == "neoforge-21.1.248"
        assert len(man["files"]) == 381
        jars = [n for n in zver.namelist() if n.endswith(".jar") or n.endswith(".jar.disabled")]
        assert len(jars) == 0, f"Found loose jars: {jars}"
        dh_raw = zver.read("overrides/config/DistantHorizons.toml").decode("utf-8")
        assert "lodChunkRenderDistanceRadius = 32" in dh_raw, "DH radius in Lite is not 32!"
    print("Lite Alpha 2 Package Verified Successfully (Including DistantHorizons = 32)!")

if __name__ == "__main__":
    dev_manifest, dev_modlist_lines, logo_bytes = build_dev_pack()
    build_lite_pack(dev_manifest, dev_modlist_lines, logo_bytes)
