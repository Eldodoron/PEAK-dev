import urllib.request
import os
import zipfile

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

mods_dir = os.path.abspath(r"minecraft/mods")

downloads = [
    {
        "name": "BadOptimizations-2.4.1-1.21.1.jar",
        "url": "https://edge.forgecdn.net/files/7338/300/BadOptimizations-2.4.1-1.21.1.jar"
    },
    {
        "name": "noisiumed-3.0.6-neoforge-1.21.1.jar",
        "url": "https://edge.forgecdn.net/files/8475/257/noisiumed-3.0.6-neoforge-1.21.1.jar"
    },
    {
        "name": "dynamic-fps-3.7.7+minecraft-1.21.0-neoforge.jar",
        "url": "https://edge.forgecdn.net/files/5959/826/dynamic-fps-3.7.7%2bminecraft-1.21.0-neoforge.jar"
    }
]

print(f"Target directory: {mods_dir}")

for item in downloads:
    target_path = os.path.join(mods_dir, item["name"])
    print(f"Downloading {item['name']} from {item['url']}...")
    req = urllib.request.Request(item["url"], headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    with open(target_path, "wb") as f:
        f.write(data)
    
    if zipfile.is_zipfile(target_path):
        zf = zipfile.ZipFile(target_path)
        print(f"  SUCCESS: {item['name']} verified valid ZIP ({len(data)} bytes, {len(zf.namelist())} files inside)")
    else:
        print(f"  ERROR: {item['name']} is NOT a valid zip file!")
