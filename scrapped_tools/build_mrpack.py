import os
import hashlib
import json
import urllib.request
import zipfile
import time
import shutil

instance_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft"
output_mrpack = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\PackExports\Peak-alpha1.mrpack"
temp_mrpack = os.path.join(os.environ.get("TEMP", r"C:\Users\chris\AppData\Local\Temp"), "Peak-alpha1.mrpack")

print("Starting MRPack Build for PEAK Alpha 1...")
start_time = time.time()

# 1. Read server pack exclusions for environment tagging
excluded_file = os.path.join(instance_dir, "server_pack_excluded_mods.txt")
client_only_mods = set()
if os.path.exists(excluded_file):
    with open(excluded_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                client_only_mods.add(line)
print(f"Loaded {len(client_only_mods)} client-only mod filenames for environment tagging.")

# 2. Hash all active jar mods
mods_dir = os.path.join(instance_dir, "mods")
all_jars = sorted([f for f in os.listdir(mods_dir) if f.endswith(".jar")])
print(f"Hashing {len(all_jars)} mod JARs...")

file_hashes = {}
for j in all_jars:
    p = os.path.join(mods_dir, j)
    with open(p, "rb") as f:
        data = f.read()
        file_hashes[j] = {
            "path": p,
            "filename": j,
            "sha1": hashlib.sha1(data).hexdigest(),
            "sha512": hashlib.sha512(data).hexdigest(),
            "size": len(data)
        }

# 3. Query Modrinth API in batches
sha1_to_filename = {v["sha1"]: k for k, v in file_hashes.items()}
all_sha1s = list(sha1_to_filename.keys())

found_on_modrinth = {}
batch_size = 100

print("Querying Modrinth API for mod hashes...")
for i in range(0, len(all_sha1s), batch_size):
    batch = all_sha1s[i:i + batch_size]
    req_data = json.dumps({"hashes": batch, "algorithm": "sha1"}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.modrinth.com/v2/version_files",
        data=req_data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "PEAK-Modpack-Builder/1.0 (contact@modrinth.com)"
        }
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        found_on_modrinth.update(res)

print(f"Modrinth hash check complete:")
print(f"  Hosted on Modrinth: {len(found_on_modrinth)} / {len(all_jars)}")
print(f"  Packaged as overrides: {len(all_jars) - len(found_on_modrinth)} / {len(all_jars)}")

# 4. Construct modrinth.index.json
index_files = []
override_jars = []

for filename, info in file_hashes.items():
    h_sha1 = info["sha1"]
    h_sha512 = info["sha512"]
    
    # Determine environment
    if filename in client_only_mods:
        env = {"client": "required", "server": "unsupported"}
    else:
        env = {"client": "required", "server": "required"}
        
    if h_sha1 in found_on_modrinth:
        modrinth_version = found_on_modrinth[h_sha1]
        # Locate matching file inside version
        matching_file = None
        for mf in modrinth_version.get("files", []):
            if mf.get("hashes", {}).get("sha1") == h_sha1:
                matching_file = mf
                break
        if matching_file and matching_file.get("url"):
            index_files.append({
                "path": f"mods/{filename}",
                "hashes": {
                    "sha1": h_sha1,
                    "sha512": h_sha512
                },
                "env": env,
                "downloads": [matching_file["url"]],
                "fileSize": info["size"]
            })
            continue

    # Fallback to override if not found or missing download URL
    override_jars.append(info)

index_data = {
    "formatVersion": 1,
    "game": "minecraft",
    "versionId": "alpha1",
    "name": "Peak (Dev)",
    "summary": "A non-linear Ultra optimized Modpack built around Create automation, Magic systems, and Tons of custom content to explore!",
    "files": index_files,
    "dependencies": {
        "minecraft": "1.21.1",
        "neoforge": "21.1.240"
    }
}

# 5. Build .mrpack ZIP archive
os.makedirs(os.path.dirname(output_mrpack), exist_ok=True)
print(f"Writing MRPack archive: {output_mrpack}...")

with zipfile.ZipFile(output_mrpack, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
    # A. modrinth.index.json at root
    index_json_bytes = json.dumps(index_data, indent=2).encode("utf-8")
    assert index_json_bytes[0] == ord("{")
    zout.writestr("modrinth.index.json", index_json_bytes)
    
    # B. Override mod JARs
    for oj in override_jars:
        arcname = f"overrides/mods/{oj['filename']}"
        zout.write(oj["path"], arcname=arcname)
        
    # C. Config, Defaultconfigs, KubeJS, Options
    for sub in ["config", "defaultconfigs", "kubejs"]:
        sub_dir = os.path.join(instance_dir, sub)
        if os.path.isdir(sub_dir):
            for root, dirs, files in os.walk(sub_dir):
                for f in files:
                    full_p = os.path.join(root, f)
                    rel_p = os.path.relpath(full_p, instance_dir).replace("\\", "/")
                    zout.write(full_p, arcname=f"overrides/{rel_p}")
                    
    # Options.txt
    opt_file = os.path.join(instance_dir, "options.txt")
    if os.path.isfile(opt_file):
        zout.write(opt_file, arcname="overrides/options.txt")

elapsed = time.time() - start_time
size_mb = os.path.getsize(output_mrpack) / (1024 * 1024)
print(f"MRPack successfully built in {elapsed:.1f}s!")
print(f"Size: {size_mb:.2f} MB")
print(f"Index files (CDN downloads): {len(index_files)}")
print(f"Override JARs bundled: {len(override_jars)}")

# 6. Verify integrity
with zipfile.ZipFile(output_mrpack, "r") as zver:
    corrupt = zver.testzip()
    if corrupt:
        raise RuntimeError(f"Corrupt file in archive: {corrupt}")
    root_items = set(n.split("/")[0] for n in zver.namelist())
    print("Archive integrity verified! Root items:", sorted(list(root_items)))

# 7. Copy to Temp for browser upload
print(f"Staging copy to {temp_mrpack}...")
shutil.copy2(output_mrpack, temp_mrpack)
print("Staging complete!")
