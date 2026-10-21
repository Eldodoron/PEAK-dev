import glob
import re
import zipfile

print("--- XP-like fluids ---")
with open("minecraft/ct_dumps/fluid.txt", encoding="utf-8") as fh:
    for line in fh:
        if re.search(r"xp|exp|liquid_", line):
            print(line.strip())

print("--- Avaritia shaped_table recipes with empty slots ---")
for jar in glob.glob("minecraft/mods/*varitia*.jar"):
    z = zipfile.ZipFile(jar)
    shown = 0
    for name in z.namelist():
        if name.startswith("data/avaritia/recipe/") and name.endswith(".json"):
            text = z.read(name).decode("utf-8")
            if "shaped_table" in text and '" ' in text:
                print(jar, name)
                print(text[:700])
                shown += 1
                if shown >= 1:
                    break

print("--- Infusing ingredient tag ---")
z = zipfile.ZipFile("minecraft/mods/create-enchantment-industry-2.5.0-preview-alpha1.jar")
for name in z.namelist():
    if "infusing/ingredients" in name:
        print(name)
        print(z.read(name).decode()[:600])
