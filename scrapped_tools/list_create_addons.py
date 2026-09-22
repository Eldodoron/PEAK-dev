import os
import zipfile

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"
create_mods = []

for fname in os.listdir(mods_dir):
    if not fname.endswith(".jar"):
        continue
    fpath = os.path.join(mods_dir, fname)
    is_create = "create" in fname.lower()
    mod_id = ""
    version = ""
    display_name = ""
    try:
        with zipfile.ZipFile(fpath, 'r') as zf:
            for item in zf.namelist():
                if "mods.toml" in item:
                    content = zf.read(item).decode('utf-8', errors='ignore')
                    if "modId" in content:
                        for line in content.splitlines():
                            line_s = line.strip()
                            if line_s.startswith("modId") and not mod_id:
                                mod_id = line_s.split("=")[-1].strip().strip('"').strip("'")
                            if line_s.startswith("version") and not version:
                                version = line_s.split("=")[-1].strip().strip('"').strip("'")
                            if line_s.startswith("displayName") and not display_name:
                                display_name = line_s.split("=")[-1].strip().strip('"').strip("'")
                    if "create" in content.lower() or "create" in fname.lower():
                        is_create = True
    except Exception:
        pass
    if is_create:
        create_mods.append((fname, mod_id, version, display_name))

print(f"Total Create-related mods found: {len(create_mods)}")
for fname, mid, ver, dname in sorted(create_mods):
    print(f"JAR: {fname} | ID: {mid} | Ver: {ver} | Name: {dname}")
