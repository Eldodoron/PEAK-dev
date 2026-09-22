import os
import re
import zipfile

kubejs_dir = r"minecraft/kubejs"
used_sb_items = set()
used_sc_items = set()

for root, dirs, files in os.walk(kubejs_dir):
    for f in files:
        if f.endswith(".js"):
            with open(os.path.join(root, f), "r", encoding="utf-8") as jf:
                content = jf.read()
                matches_sb = re.findall(r'sophisticatedbackpacks:([a-z0-9_]+)', content)
                matches_sc = re.findall(r'sophisticatedcore:([a-z0-9_]+)', content)
                used_sb_items.update(matches_sb)
                used_sc_items.update(matches_sc)

print(f"Total SB IDs referenced in KubeJS: {len(used_sb_items)}")
print(f"Total SC IDs referenced in KubeJS: {len(used_sc_items)}")

sb_jar = r"minecraft/mods/sophisticatedbackpacks-1.21.1-3.26.3.2158.jar"
sc_jar = r"minecraft/mods/sophisticatedcore-1.21.1-1.5.1.2341.jar"

with zipfile.ZipFile(sb_jar) as zf:
    sb_names = " ".join(zf.namelist())

with zipfile.ZipFile(sc_jar) as zf:
    sc_names = " ".join(zf.namelist())

missing_sb = []
for item in sorted(used_sb_items):
    # check in model/item or lang or data
    if f"{item}.json" not in sb_names and f"/{item}/" not in sb_names and item not in sb_names:
        missing_sb.append(item)

missing_sc = []
for item in sorted(used_sc_items):
    if f"{item}.json" not in sc_names and f"/{item}/" not in sc_names and item not in sc_names:
        missing_sc.append(item)

print("\nMissing SB items:", missing_sb)
print("Missing SC items:", missing_sc)
