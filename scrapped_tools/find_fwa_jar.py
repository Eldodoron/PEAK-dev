import os
import zipfile

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"

for fname in os.listdir(mods_dir):
    if not fname.endswith(".jar"):
        continue
    fpath = os.path.join(mods_dir, fname)
    try:
        with zipfile.ZipFile(fpath, 'r') as zf:
            names = zf.namelist()
            if "fwa.mixins.json" in names:
                print(f"FOUND fwa.mixins.json in: {fname}")
            for item in names:
                if "mods.toml" in item:
                    try:
                        content = zf.read(item).decode('utf-8', errors='ignore')
                        if 'modId="fwa"' in content or 'modId = "fwa"' in content or 'modId = \'fwa\'' in content:
                            print(f"FOUND modId fwa in: {fname}")
                            for line in content.splitlines()[:25]:
                                print("  ", line)
                    except Exception:
                        pass
    except Exception:
        pass
