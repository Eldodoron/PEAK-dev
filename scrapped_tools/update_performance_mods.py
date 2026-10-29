import os
import sys
import hashlib
import urllib.request
import json
import re

DEV_DIR = r"C:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev"
MODS_DIR = os.path.join(DEV_DIR, "minecraft", "mods")
INDEX_DIR = os.path.join(MODS_DIR, ".index")
REG_FILE = os.path.join(DEV_DIR, "scrapped_tools", "curseforge_mod_registry.json")

PERF_MODS = [
    {
        "name": "More Culling",
        "old_file": "moreculling-neoforge-1.21.1-1.0.7.jar",
        "new_file": "moreculling-neoforge-1.21.1-1.0.10.jar",
        "url": "https://cdn.modrinth.com/data/51shyZVL/versions/5M4T2FfG/moreculling-neoforge-1.21.1-1.0.10.jar",
        "version": "1.0.10",
        "version_id": "5M4T2FfG",
        "pw_file": "moreculling.pw.toml",
        "mod_id": "moreculling",
        "project_id": 630104,
        "file_id": 8833217
    },
    {
        "name": "ImmediatelyFast",
        "old_file": "ImmediatelyFast-NeoForge-1.6.11+1.21.1.jar",
        "new_file": "ImmediatelyFast-NeoForge-1.6.15+1.21.1.jar",
        "url": "https://cdn.modrinth.com/data/5ZwdcRci/versions/EJzmEPZV/ImmediatelyFast-NeoForge-1.6.15%2B1.21.1.jar",
        "version": "1.6.15+1.21.1",
        "version_id": "EJzmEPZV",
        "pw_file": "immediatelyfast.pw.toml",
        "mod_id": "immediatelyfast",
        "project_id": 686911,
        "file_id": 9165518
    },
    {
        "name": "ModernFix",
        "old_file": "modernfix-neoforge-5.27.20+mc1.21.1.jar",
        "new_file": "modernfix-neoforge-5.27.27+mc1.21.1.jar",
        "url": "https://cdn.modrinth.com/data/nmDcB62a/versions/ZDZENbHH/modernfix-neoforge-5.27.27%2Bmc1.21.1.jar",
        "version": "5.27.27+mc1.21.1",
        "version_id": "ZDZENbHH",
        "pw_file": "modernfix.pw.toml",
        "mod_id": "modernfix",
        "project_id": 790626,
        "file_id": 9309399
    },
    {
        "name": "Lithium",
        "old_file": "lithium-neoforge-0.15.3+mc1.21.1.jar",
        "new_file": "lithium-neoforge-0.15.4+mc1.21.1.jar",
        "url": "https://cdn.modrinth.com/data/gvQqBUqZ/versions/DDUrRVCA/lithium-neoforge-0.15.4%2Bmc1.21.1.jar",
        "version": "0.15.4+mc1.21.1",
        "version_id": "DDUrRVCA",
        "pw_file": "lithium.pw.toml",
        "mod_id": "lithium",
        "project_id": 360438,
        "file_id": 8330365
    },
    {
        "name": "Dynamic FPS",
        "old_file": "dynamic-fps-3.7.7+minecraft-1.21.0-neoforge.jar",
        "new_file": "dynamic-fps-3.11.4+minecraft-1.21.0-neoforge.jar",
        "url": "https://cdn.modrinth.com/data/LQ3K71Q1/versions/T238FZpQ/dynamic-fps-3.11.4%2Bminecraft-1.21.0-neoforge.jar",
        "version": "3.11.4",
        "version_id": "T238FZpQ",
        "pw_file": "dynamic-fps.pw.toml",
        "mod_id": "dynamic_fps",
        "project_id": 335493,
        "file_id": 7546938
    },
    {
        "name": "ServerCore",
        "old_file": "servercore-neoforge-1.5.17+1.21.1.jar",
        "new_file": "servercore-neoforge-1.5.19+1.21.1.jar",
        "url": "https://cdn.modrinth.com/data/4WWQxlQP/versions/6N9hXiRa/servercore-neoforge-1.5.19%2B1.21.1.jar",
        "version": "1.5.19+1.21.1",
        "version_id": "6N9hXiRa",
        "pw_file": "servercore.pw.toml",
        "mod_id": "servercore",
        "project_id": 550579,
        "file_id": 8312220
    },
    {
        "name": "C2ME",
        "old_file": "c2me-neoforge-mc1.21.1-0.4.0-alpha.0.122.jar",
        "new_file": "c2me-neoforge-mc1.21.1-0.4.0-alpha.0.124.jar",
        "url": "https://cdn.modrinth.com/data/COlSi5iR/versions/VACgDPOc/c2me-neoforge-mc1.21.1-0.4.0-alpha.0.124.jar",
        "version": "0.4.0-alpha.0.124+1.21.1",
        "version_id": "VACgDPOc",
        "pw_file": "c2me-neoforge.pw.toml",
        "mod_id": "c2me",
        "project_id": 533097,
        "file_id": 8896937
    }
]

def get_hashes(path):
    h_sha1 = hashlib.sha1()
    h_sha512 = hashlib.sha512()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h_sha1.update(chunk)
            h_sha512.update(chunk)
    return h_sha1.hexdigest(), h_sha512.hexdigest()

def main():
    print("=== Step 1: Downloading & Validating New Mod Versions ===")
    downloads = {}
    for item in PERF_MODS:
        dest = os.path.join(MODS_DIR, item["new_file"])
        temp_dest = dest + ".tmp"
        print(f"Downloading {item['new_file']}...")
        req = urllib.request.Request(item["url"], headers={"User-Agent": "PEAKModpack/1.0"})
        with urllib.request.urlopen(req) as resp, open(temp_dest, "wb") as f:
            f.write(resp.read())
        
        sha1_val, sha512_val = get_hashes(temp_dest)
        file_size = os.path.getsize(temp_dest)
        print(f"  Downloaded: {item['new_file']} ({file_size} bytes)")
        print(f"    SHA1:   {sha1_val}")
        print(f"    SHA512: {sha512_val}")
        downloads[item["new_file"]] = {
            "temp_path": temp_dest,
            "final_path": dest,
            "sha1": sha1_val,
            "sha512": sha512_val,
            "size": file_size,
            "item": item
        }

    print("\n=== Step 2: Replacing Old Mod JARs in mods/ ===")
    for item in PERF_MODS:
        old_path = os.path.join(MODS_DIR, item["old_file"])
        d = downloads[item["new_file"]]
        
        if os.path.exists(d["final_path"]):
            os.remove(d["final_path"])
        os.rename(d["temp_path"], d["final_path"])
        print(f"  + Added: {item['new_file']}")
        
        if os.path.exists(old_path) and item["old_file"] != item["new_file"]:
            os.remove(old_path)
            print(f"  - Removed: {item['old_file']}")

    print("\n=== Step 3: Updating Packwiz .index metadata ===")
    for item in PERF_MODS:
        pw_path = os.path.join(INDEX_DIR, item["pw_file"])
        if os.path.isfile(pw_path):
            with open(pw_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            d = downloads[item["new_file"]]
            
            # Replace filename
            content = content.replace(f"filename = '{item['old_file']}'", f"filename = '{item['new_file']}'")
            
            # Check hash format
            if "hash-format = 'sha512'" in content:
                content = re.sub(r"hash = '[a-f0-9]+'", f"hash = '{d['sha512']}'", content)
            else:
                content = re.sub(r"hash = '[a-f0-9]+'", f"hash = '{d['sha1']}'", content)
            
            # Update url and version if present
            content = content.replace(item["old_file"], item["new_file"])
            if item.get("version_id"):
                content = re.sub(r"version = '[A-Za-z0-9]+'", f"version = '{item['version_id']}'", content)
                content = re.sub(r"versions/[A-Za-z0-9]+/", f"versions/{item['version_id']}/", content)
            
            with open(pw_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  Updated: {item['pw_file']}")
        else:
            print(f"  Warning: .pw.toml not found for {item['pw_file']}")

    print("\n=== Step 4: Updating CurseForge Master Registry ===")
    if os.path.isfile(REG_FILE):
        with open(REG_FILE, "r", encoding="utf-8") as f:
            reg = json.load(f)
        
        for item in PERF_MODS:
            d = downloads[item["new_file"]]
            old_meta = reg.get(item["old_file"], {})
            
            new_meta = {
                "filename": item["new_file"],
                "projectID": old_meta.get("projectID", item["project_id"]),
                "fileID": item.get("file_id", old_meta.get("fileID", 0)),
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
            print(f"  Registry updated: {item['new_file']} (projectID={new_meta['projectID']}, fileID={new_meta['fileID']})")
        
        sorted_reg = {k: reg[k] for k in sorted(reg.keys())}
        with open(REG_FILE, "w", encoding="utf-8") as f:
            json.dump(sorted_reg, f, indent=2)

    print("\n=== Step 5: Verifying Mod Counts & Invariants ===")
    dev_jars = [f for f in os.listdir(MODS_DIR) if f.endswith(".jar")]
    dev_disabled = [f for f in os.listdir(MODS_DIR) if f.endswith(".disabled")]
    print(f"  Active mods count: {len(dev_jars)} (Target: 411)")
    print(f"  Disabled mods count: {len(dev_disabled)} (Target: 42)")
    assert len(dev_jars) == 411, f"Expected 411 active jars, found {len(dev_jars)}"
    assert len(dev_disabled) == 42, f"Expected 42 disabled jars, found {len(dev_disabled)}"

    print("\nALL 7 PERFORMANCE MODS UPDATED AND VERIFIED SUCCESSFULLY.")

if __name__ == "__main__":
    main()
