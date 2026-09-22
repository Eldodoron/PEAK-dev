import os
import urllib.request
import zipfile

HEADERS = {'User-Agent': 'PEAK/1.0'}
mods_dir = os.path.abspath("minecraft/mods")

swaps = [
    {
        "old_file": "create-enchantment-industry-2.5.4.jar",
        "new_name": "create-enchantment-industry-2.5.0-preview-alpha1.jar",
        "url": "https://cdn.modrinth.com/data/JWGBpFUP/versions/8XedJhwv/create-enchantment-industry-2.5.0-preview-alpha1.jar"
    },
    {
        "old_file": "create-integrated-farming-1.4.2.jar",
        "new_name": "create-integrated-farming-1.4.1c.jar",
        "url": "https://cdn.modrinth.com/data/9k1pAsfR/versions/zF7BFx6A/create-integrated-farming-1.4.1c.jar"
    }
]

for item in swaps:
    old_p = os.path.join(mods_dir, item["old_file"])
    new_p = os.path.join(mods_dir, item["new_name"])
    
    print(f"Downloading {item['new_name']}...")
    req = urllib.request.Request(item["url"], headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    with open(new_p, "wb") as f:
        f.write(data)
    
    if zipfile.is_zipfile(new_p):
        print(f"  VERIFIED: {item['new_name']} is valid ({len(data)} bytes).")
        if os.path.exists(old_p):
            os.remove(old_p)
            print(f"  REMOVED old conflicting jar: {item['old_file']}")
    else:
        print(f"  ERROR: {item['new_name']} download failed or corrupted!")
