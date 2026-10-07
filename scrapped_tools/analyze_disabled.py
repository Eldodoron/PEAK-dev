import os
import zipfile
import tomllib
import json

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"
disabled = [f for f in os.listdir(mods_dir) if f.endswith('.disabled')]

def analyze_jar(path):
    info = {"displayTest": None, "environment": None, "mixins": [], "has_client_mixin": False, "has_server_mixin": False, "has_data": False, "has_assets": False, "has_net_minecraft_client": False, "has_packets": False, "client_only_dep": False}
    try:
        with zipfile.ZipFile(path, 'r') as z:
            names = z.namelist()
            info["has_data"] = any(n.startswith("data/") for n in names)
            info["has_assets"] = any(n.startswith("assets/") for n in names)
            info["has_net_minecraft_client"] = any("net/minecraft/client" in n for n in names)
            info["has_packets"] = any("packet" in n.lower() or "payload" in n.lower() or "network" in n.lower() for n in names)
            
            # check neoforge.mods.toml
            for toml_path in ["META-INF/neoforge.mods.toml", "META-INF/mods.toml"]:
                if toml_path in names:
                    data = z.read(toml_path)
                    try:
                        parsed = tomllib.loads(data.decode('utf-8', errors='ignore'))
                        info["displayTest"] = parsed.get("displayTest")
                        mods = parsed.get("mods", [])
                        if mods:
                            info["environment"] = mods[0].get("environment")
                        # check dependencies
                        deps = parsed.get("dependencies", {})
                        for mod_id, dlist in deps.items():
                            for d in dlist:
                                if d.get("side") == "CLIENT":
                                    info["client_only_dep"] = True
                    except Exception as e:
                        info["toml_err"] = str(e)
            
            if "fabric.mod.json" in names:
                try:
                    f_data = json.loads(z.read("fabric.mod.json").decode('utf-8', errors='ignore'))
                    info["fabric_environment"] = f_data.get("environment")
                except:
                    pass

            for n in names:
                if n.endswith(".mixins.json") or (n.endswith(".json") and "mixin" in n):
                    try:
                        m_data = json.loads(z.read(n).decode('utf-8', errors='ignore'))
                        if isinstance(m_data, dict):
                            client_m = m_data.get("client", [])
                            server_m = m_data.get("server", [])
                            mixins = m_data.get("mixins", [])
                            if client_m:
                                info["has_client_mixin"] = True
                            if server_m:
                                info["has_server_mixin"] = True
                            info["mixins"].append(n)
                    except:
                        pass
    except Exception as e:
        info["error"] = str(e)
    return info

for f in sorted(disabled):
    path = os.path.join(mods_dir, f)
    res = analyze_jar(path)
    print(f"=== {f} ===")
    print(f"  displayTest: {res.get('displayTest')}, env: {res.get('environment')}, fab_env: {res.get('fabric_environment')}")
    print(f"  has_data: {res['has_data']}, has_assets: {res['has_assets']}")
    print(f"  has_client_mixin: {res['has_client_mixin']}, has_server_mixin: {res['has_server_mixin']}, mixins: {res['mixins']}")
    print(f"  has_client_classes: {res['has_net_minecraft_client']}")
