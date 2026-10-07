import os
import zipfile
import tomllib
import json

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"
disabled = [f for f in os.listdir(mods_dir) if f.endswith('.disabled')]

for f in sorted(disabled):
    path = os.path.join(mods_dir, f)
    mod_id = "unknown"
    mod_name = "unknown"
    client_side = None
    side = None
    with zipfile.ZipFile(path, 'r') as z:
        names = z.namelist()
        has_data = any(n.startswith("data/") for n in names)
        for toml in ["META-INF/neoforge.mods.toml", "META-INF/mods.toml"]:
            if toml in names:
                try:
                    p = tomllib.loads(z.read(toml).decode('utf-8', errors='ignore'))
                    mods = p.get("mods", [])
                    if mods:
                        mod_id = mods[0].get("modId")
                        mod_name = mods[0].get("displayName")
                    side = p.get("displayTest")
                    deps = p.get("dependencies", {})
                    for mid, dl in deps.items():
                        for d in dl:
                            if d.get("side") == "CLIENT":
                                client_side = "dep_client"
                except:
                    pass
        if "fabric.mod.json" in names:
            try:
                p = json.loads(z.read("fabric.mod.json").decode('utf-8', errors='ignore'))
                mod_id = p.get("id", mod_id)
                mod_name = p.get("name", mod_name)
                env = p.get("environment")
                if env:
                    client_side = env
            except:
                pass
    print(f"{f} | id: {mod_id} | name: {mod_name} | displayTest: {side} | client_side: {client_side} | has_data: {has_data}")
