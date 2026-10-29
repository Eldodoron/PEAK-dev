import os
import sys
import hashlib
import urllib.request
import json

DEV_DIR = r"C:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev"
MODS_DIR = os.path.join(DEV_DIR, "minecraft", "mods")
INDEX_DIR = os.path.join(MODS_DIR, ".index")
REG_FILE = os.path.join(DEV_DIR, "scrapped_tools", "curseforge_mod_registry.json")

MODS_TO_UPDATE = [
    {
        "name": "Create: Enchantment Industry",
        "old_file": "create-enchantment-industry-2.5.0-preview-alpha1.jar",
        "new_file": "create-enchantment-industry-2.5.4b.jar",
        "url": "https://cdn.modrinth.com/data/JWGBpFUP/versions/L6VSDdC4/create-enchantment-industry-2.5.4b.jar",
        "version": "2.5.4b",
        "pw_file": "create-enchantment-industry.pw.toml",
        "mod_id": "create_enchantment_industry",
        "project_id": 688768
    },
    {
        "name": "Create: Integrated Farming",
        "old_file": "create-integrated-farming-1.4.1c.jar",
        "new_file": "create-integrated-farming-1.4.3.jar",
        "url": "https://cdn.modrinth.com/data/9k1pAsfR/versions/EWfVwbHy/create-integrated-farming-1.4.3.jar",
        "version": "1.4.3",
        "pw_file": "create-integrated-farming.pw.toml",
        "mod_id": "create_integrated_farming",
        "project_id": 1249131
    },
    {
        "name": "Ender's Delight",
        "old_file": "endersdelight-1.3.0.jar",
        "new_file": "endersdelight-1.3.1.jar",
        "url": "https://cdn.modrinth.com/data/2uEhdGKt/versions/5S67w5gs/endersdelight-1.3.1.jar",
        "version": "1.3.1",
        "pw_file": "enders-delight.pw.toml",
        "mod_id": "endersdelight",
        "project_id": 827163
    }
]

def sha1sum(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def main():
    print("=== Step 1: Downloading & Validating New Mod Versions ===")
    downloads = {}
    for item in MODS_TO_UPDATE:
        dest = os.path.join(MODS_DIR, item["new_file"])
        temp_dest = dest + ".tmp"
        print(f"Downloading {item['new_file']}...")
        req = urllib.request.Request(item["url"], headers={"User-Agent": "ModpackResearcher/1.0"})
        with urllib.request.urlopen(req) as resp, open(temp_dest, "wb") as f:
            f.write(resp.read())
        
        file_sha1 = sha1sum(temp_dest)
        file_size = os.path.getsize(temp_dest)
        print(f"  Downloaded: {item['new_file']} ({file_size} bytes, sha1: {file_sha1})")
        downloads[item["new_file"]] = {
            "temp_path": temp_dest,
            "final_path": dest,
            "sha1": file_sha1,
            "size": file_size,
            "item": item
        }

    print("\n=== Step 2: Replacing Old Mod JARs ===")
    for item in MODS_TO_UPDATE:
        old_path = os.path.join(MODS_DIR, item["old_file"])
        d = downloads[item["new_file"]]
        
        # Move temp to final
        if os.path.exists(d["final_path"]):
            os.remove(d["final_path"])
        os.rename(d["temp_path"], d["final_path"])
        print(f"  + Added: {item['new_file']}")
        
        if os.path.exists(old_path) and item["old_file"] != item["new_file"]:
            os.remove(old_path)
            print(f"  - Removed: {item['old_file']}")

    print("\n=== Step 3: Updating Packwiz .index metadata ===")
    for item in MODS_TO_UPDATE:
        pw_path = os.path.join(INDEX_DIR, item["pw_file"])
        if os.path.isfile(pw_path):
            with open(pw_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            d = downloads[item["new_file"]]
            # Update filename
            content = content.replace(f"filename = '{item['old_file']}'", f"filename = '{item['new_file']}'")
            # Update hash
            import re
            content = re.sub(r"hash = '[a-f0-9]+'", f"hash = '{d['sha1']}'", content)
            
            with open(pw_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  Updated: {item['pw_file']}")

    print("\n=== Step 4: Updating CurseForge Master Registry ===")
    if os.path.isfile(REG_FILE):
        with open(REG_FILE, "r", encoding="utf-8") as f:
            reg = json.load(f)
        
        for item in MODS_TO_UPDATE:
            d = downloads[item["new_file"]]
            old_meta = reg.get(item["old_file"], {})
            
            new_meta = {
                "filename": item["new_file"],
                "projectID": old_meta.get("projectID", item["project_id"]),
                "fileID": old_meta.get("fileID", 0),
                "name": old_meta.get("name", item["name"]),
                "authors": old_meta.get("authors", ["Mod Author"]),
                "url": old_meta.get("url", f"https://www.curseforge.com/projects/{item['project_id']}"),
                "mod_ids": [item["mod_id"]],
                "mod_version": item["version"],
                "sha1": d["sha1"],
                "size": d["size"],
                "client_side_only": old_meta.get("client_side_only", False),
                "lite_excluded": old_meta.get("lite_excluded", False),
                "has_mandatory_network_channels": old_meta.get("has_mandatory_network_channels", False)
            }
            if item["old_file"] in reg:
                del reg[item["old_file"]]
            reg[item["new_file"]] = new_meta
            print(f"  Registry updated for {item['new_file']}")
        
        sorted_reg = {k: reg[k] for k in sorted(reg.keys())}
        with open(REG_FILE, "w", encoding="utf-8") as f:
            json.dump(sorted_reg, f, indent=2)

    print("\n=== Step 5: Verifying Mod Counts & Integrity ===")
    dev_jars = [f for f in os.listdir(MODS_DIR) if f.endswith(".jar")]
    dev_disabled = [f for f in os.listdir(MODS_DIR) if f.endswith(".disabled")]
    print(f"  Active mods count: {len(dev_jars)} (Target: 411)")
    print(f"  Disabled mods count: {len(dev_disabled)} (Target: 42)")
    assert len(dev_jars) == 411, f"Expected 411 active jars, found {len(dev_jars)}"
    assert len(dev_disabled) == 42, f"Expected 42 disabled jars, found {len(dev_disabled)}"

    print("\nALL GATED CREATE MOD UPDATES COMPLETED SUCCESSFULLY.")

if __name__ == "__main__":
    main()
