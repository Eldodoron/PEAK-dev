import glob
import json
import os
import re
import subprocess
import sys
import zipfile

from PIL import Image

ROOT = "minecraft"
SCRIPT = f"{ROOT}/kubejs/server_scripts/66_bookshelf_overhaul.js"
STARTUP = f"{ROOT}/kubejs/startup_scripts/bookshelf_tomes.js"
STATS = f"{ROOT}/kubejs/data/apothic_enchanting/enchanting_stats/wisewood_bookshelf.json"
TEX_DIR = f"{ROOT}/kubejs/assets/kubejs/textures/item"
problems = []


def load_dump(name, kind):
    ids = set()
    with open(f"{ROOT}/ct_dumps/{name}", encoding="utf-8") as fh:
        for line in fh:
            m = re.match(rf"<{kind}:([^>]+)>", line.strip())
            if m:
                ids.add(m.group(1))
    return ids


items = load_dump("item.txt", "item")
fluids = load_dump("fluid.txt", "fluid")
tomes = {"stonebook", "melonbook", "beebook", "hellbook", "seabook", "deepbook", "sculkbook", "endbook", "enchanted_brass_cube", "enchanted_precision_mechanism"}

# 1. JS syntax check
for path in (SCRIPT, STARTUP, f"{ROOT}/kubejs/server_scripts/05_dark_magic_dimensions.js"):
    result = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    status = "OK" if result.returncode == 0 else "FAIL"
    print(f"[syntax] {path}: {status}")
    if result.returncode != 0:
        problems.append(f"syntax {path}: {result.stderr.strip()[:300]}")

# 2. Item and fluid ids referenced in the recipe script
text = open(SCRIPT, encoding="utf-8").read()
quoted = set(re.findall(r"'([a-z0-9_]+:[a-z0-9_/]+)'", text))
fluid_ids = set(re.findall(r"fluid: '([^']+)'", text)) | set(re.findall(r"Fluid\.of\('([^']+)'", text))
skip_prefixes = ("kubejs:tome/", "kubejs:shelf/", "kubejs:infusion/", "kubejs:filling/",
                 "kubejs:crafting/", "apokinetics:", "apotheosis:purity",
                 "kubejs:sequenced_assembly/", "apothic_enchanting:infusion/",
                 "irons_spellbooks:filling/", "create_enchantment_industry:sequenced_assembly/",
                 "create:", "farmersdelight:", "ars_nouveau:enchanting", "avaritia:shaped",
                 "apothic_enchanting:infusion", "neoforge:")
for ident in sorted(quoted):
    if ident in fluid_ids:
        continue
    ns, name = ident.split(":", 1)
    if ns == "kubejs" and name in tomes:
        continue
    if any(ident.startswith(p) for p in skip_prefixes) and ident not in items:
        # allow recipe types / ids; real items are re-checked below
        if ident in items:
            continue
        if ident.startswith(("create:", "farmersdelight:", "ars_nouveau:", "avaritia:", "neoforge:")) and ident not in items:
            if ident in ("create:compacting", "create:mixing", "create:filling", "create:deploying",
                         "create:sequenced_assembly", "farmersdelight:cooking",
                         "ars_nouveau:enchanting_apparatus", "avaritia:shaped_table", "neoforge:single", "neoforge:tag"):
                continue
        if ident.startswith(("kubejs:", "apothic_enchanting:infusion", "irons_spellbooks:filling",
                             "apokinetics:", "apotheosis:purity",
                             "create_enchantment_industry:sequenced_assembly")):
            continue
    if ident in ("create_enchantment_industry:infusing/ingredients",):
        continue
    if ident not in items:
        problems.append(f"unknown item id: {ident}")
        print(f"[item] MISSING {ident}")
for fid in sorted(fluid_ids):
    ok = fid in fluids or fid == "create_wizardry:mana"
    print(f"[fluid] {fid}: {'OK' if ok else 'MISSING'}")
    if not ok:
        problems.append(f"unknown fluid id: {fid}")

# create_wizardry mana fluid check inside jar (not guaranteed in dump)
for jar in glob.glob(f"{ROOT}/mods/create_wizardry*.jar"):
    z = zipfile.ZipFile(jar)
    names = " ".join(z.namelist())
    print("[fluid] create_wizardry:mana present in jar assets:", "mana" in names)

# 3. Textures
for tome in sorted(tomes):
    p = f"{TEX_DIR}/{tome}.png"
    if not os.path.exists(p):
        problems.append(f"missing texture {p}")
        continue
    size = Image.open(p).size
    print(f"[texture] {tome}: {size}")
    if size != (16, 16):
        problems.append(f"bad texture size {tome}: {size}")

# 4. JSON validity and BOM
for p in (STATS,):
    raw = open(p, "rb").read()
    print(f"[json] {p}: BOM={raw.startswith(b'\xef\xbb\xbf')}")
    json.loads(raw.decode("utf-8"))
    if raw.startswith(b"\xef\xbb\xbf"):
        problems.append(f"BOM in {p}")

# 5. Other sources already defining Wisewood stats
for jar in glob.glob(f"{ROOT}/mods/*.jar"):
    try:
        z = zipfile.ZipFile(jar)
    except Exception:
        continue
    for name in z.namelist():
        if "enchanting_stats/" in name and name.endswith(".json"):
            try:
                body = z.read(name).decode("utf-8")
            except Exception:
                continue
            if "wisewood" in body:
                print(f"[stats] other definition: {jar} {name}")
                problems.append(f"duplicate wisewood stats in {jar}:{name}")

# 6. Ban-list words in new files
for p in (SCRIPT, STARTUP):
    body = open(p, encoding="utf-8").read().lower()
    for word in ("surgical", "seamless", "meticulous", "antigravity", "delve"):
        if word in body:
            problems.append(f"banned word '{word}' in {p}")

print("\nPROBLEMS:", problems if problems else "none")
sys.exit(1 if problems else 0)
