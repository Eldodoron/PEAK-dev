import os
import sys
import json
import zipfile
import shutil

sys.stdout.reconfigure(encoding="utf-8")

BASE_DEV = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_LITE = os.path.abspath(os.path.join(BASE_DEV, "..", "PEAK-Lite"))
DEV_MC = os.path.join(BASE_DEV, "minecraft")
LITE_MC = os.path.join(BASE_LITE, "minecraft")
MASTER_ZIP = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\PackExports\Peak-alpha1.zip"
OUT_ZIP = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\PackExports\Peak-Lite-alpha1.zip"
TEMP_ZIP = os.path.join(os.environ.get("TEMP", r"C:\Users\chris\AppData\Local\Temp"), "Peak-Lite-alpha1.zip")

EXCLUDED_PIDS = {
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

DEAD_PIDS = {1277910}

def build_lite_pack():
    print("==================================================")
    print(" Building CurseForge Export: Peak-Lite-alpha1.zip ")
    print("==================================================")

    assert os.path.isfile(MASTER_ZIP), f"Master ZIP not found: {MASTER_ZIP}"
    assert os.path.isdir(LITE_MC), f"Lite minecraft directory not found: {LITE_MC}"

    # 1. Read master manifest and modlist from Peak-alpha1.zip
    with zipfile.ZipFile(MASTER_ZIP, "r") as zmaster:
        raw_manifest = zmaster.read("manifest.json").decode("utf-8-sig")
        manifest_data = json.loads(raw_manifest)
        raw_modlist = zmaster.read("modlist.html").decode("utf-8-sig")
        logo_bytes = zmaster.read("profileImage/logo_square_preview.png")

    # 2. Update manifest metadata
    manifest_data["name"] = "Peak Lite"
    manifest_data["version"] = "alpha1"
    manifest_data["author"] = "eldodoron"
    if "minecraft" in manifest_data:
        manifest_data["minecraft"]["recommendedRam"] = 6348

    original_files = manifest_data.get("files", [])
    filtered_files = [
        f for f in original_files
        if f.get("projectID") not in EXCLUDED_PIDS and f.get("projectID") not in DEAD_PIDS
    ]
    manifest_data["files"] = filtered_files
    print(f"Manifest mods: {len(original_files)} -> {len(filtered_files)} (removed {len(original_files) - len(filtered_files)})")
    assert len(filtered_files) == 383, f"Expected 383 mods, got {len(filtered_files)}"

    manifest_bytes = json.dumps(manifest_data, indent=2).encode("utf-8")
    assert manifest_bytes[0] == ord("{"), "Manifest must start with '{' (no BOM)"

    # 3. Filter modlist.html
    # Extract slugs for the excluded mods from Peak (Dev) minecraftinstance.json
    inst_path = r"C:\Users\chris\curseforge\minecraft\Instances\Peak (Dev)\minecraftinstance.json"
    with open(inst_path, "r", encoding="utf-8") as f:
        inst_data = json.load(f)

    excluded_slugs = set()
    for addon in inst_data.get("installedAddons", []):
        if addon.get("addonID") in EXCLUDED_PIDS:
            url = addon.get("webSiteURL", "")
            if url:
                slug = url.rstrip("/").split("/")[-1].lower()
                excluded_slugs.add(slug)

    modlist_lines = raw_modlist.splitlines()
    filtered_modlist_lines = []
    removed_modlist_count = 0
    for line in modlist_lines:
        lower_line = line.lower()
        is_excluded = False
        if line.strip().startswith("<li>"):
            for slug in excluded_slugs:
                if f"/{slug}\"" in lower_line or f"/{slug}/" in lower_line:
                    is_excluded = True
                    break
        if is_excluded:
            removed_modlist_count += 1
        else:
            filtered_modlist_lines.append(line)

    filtered_modlist = "\n".join(filtered_modlist_lines).encode("utf-8")
    print(f"Modlist lines: {len(modlist_lines)} -> {len(filtered_modlist_lines)} (removed {removed_modlist_count} entries)")

    # 4. Create ZIP
    os.makedirs(os.path.dirname(OUT_ZIP), exist_ok=True)
    temp_working_zip = OUT_ZIP + ".tmp"

    with zipfile.ZipFile(temp_working_zip, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        # Write root files
        zout.writestr("manifest.json", manifest_bytes)
        zout.writestr("modlist.html", filtered_modlist)
        zout.writestr("profileImage/logo_square_preview.png", logo_bytes)

        # Write overrides
        override_folders = ["config", "defaultconfigs", "kubejs"]
        for folder in override_folders:
            folder_path = os.path.join(LITE_MC, folder)
            if not os.path.isdir(folder_path):
                print(f"Warning: override folder {folder} not found at {folder_path}")
                continue

            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    ext = os.path.splitext(file)[1].lower()
                    if ext in {".bak", ".tmp", ".log"}:
                        continue
                    if file.lower().endswith(".jar") or file.lower().endswith(".jar.disabled"):
                        raise RuntimeError(f"FATAL: Loose JAR found in overrides: {file}")

                    abs_file = os.path.join(root, file)
                    rel_to_mc = os.path.relpath(abs_file, LITE_MC)
                    zip_entry_name = ("overrides/" + rel_to_mc.replace("\\", "/")).strip()

                    with open(abs_file, "rb") as f_in:
                        content = f_in.read()

                    # Strip BOM if present
                    if content.startswith(b"\xef\xbb\xbf"):
                        content = content[3:]

                    zout.writestr(zip_entry_name, content)

        # Write options.txt
        options_path = os.path.join(LITE_MC, "options.txt")
        if os.path.isfile(options_path):
            with open(options_path, "rb") as f_in:
                opt_content = f_in.read()
            if opt_content.startswith(b"\xef\xbb\xbf"):
                opt_content = opt_content[3:]
            zout.writestr("overrides/options.txt", opt_content)

    if os.path.exists(OUT_ZIP):
        os.remove(OUT_ZIP)
    shutil.move(temp_working_zip, OUT_ZIP)
    print(f"Export ZIP written to: {OUT_ZIP} ({os.path.getsize(OUT_ZIP) / (1024*1024):.2f} MB)")

    # 5. Staging for browser agent
    shutil.copy2(OUT_ZIP, TEMP_ZIP)
    print(f"Staged ZIP for browser agent at: {TEMP_ZIP}")

    # 6. Post-build validation
    print("\n--- Running Invariant Validations ---")
    with zipfile.ZipFile(OUT_ZIP, "r") as zver:
        man_raw = zver.read("manifest.json")
        assert man_raw[0] == ord("{"), "Invariant Violation: manifest.json does not start with '{'"
        man_json = json.loads(man_raw.decode("utf-8"))
        assert man_json["name"] == "Peak Lite"
        assert man_json["author"] == "eldodoron"
        assert len(man_json["files"]) == 383
        jars = [n for n in zver.namelist() if n.endswith(".jar") or n.endswith(".jar.disabled")]
        assert len(jars) == 0, f"Invariant Violation: loose JARs found: {jars}"

    print("All Invariants Verified Successfully (No BOM, Zero Loose JARs, Pure UTF-8, 383 mods)!")

if __name__ == "__main__":
    build_lite_pack()
