import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\Users\chris\curseforge\minecraft\Instances\Peak (Dev)\minecraftinstance.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

excluded_names = {
    "CraftTweaker-neoforge-1.21.1-21.0.38.jar",
    "Loot Beams Refork-neoforge-1.21.1-3.4.7.jar",
    "Nirvana Lib-neoforge-1.21.1-2.2.0.jar",
    "Panoptic-1.08a-NeoForge-1.21.1.jar",
    "Perception-NEOFORGE-0.2.1+1.21.1.jar",
    "atmospherics-2.6.5-mc-1.21.1.jar",
    "cloudlayers-1.21.1-1.1.jar",
    "cosycritters-0.3.2+1.21.1-neoforge.jar",
    "denseflower-1.0.0.jar",
    "explosiveenhancement-neoforge-1.21.1-1.1.2.jar",
    "fwa+1.21.1-neoforge-1.2.31.jar",
    "lambdynamiclights-4.8.8+1.21.1.jar",
    "notenoughanimations-neoforge-1.12.3-mc1.21.1.jar",
    "particle_core-0.3.3+1.21+neoforge.jar",
    "particular-1.21.1-NeoForge-1.5.5.jar",
    "punchy-2.6.2-neoforge-1.21.1.jar",
    "shine-2.0.1+1.21.1-neoforge.jar",
    "smoothswapping-0.9.3.2-1.21.1-neoforge.jar",
    "spark-1.10.124-neoforge.jar",
    "spatial-gui-1.6+1.21.1-neoforge.jar",
    "visuality-forge-3.0.0.jar",
    "wits-1.3.0+1.21-neoforge.jar"
}

addons = data.get("installedAddons", [])
excluded_pids = {}
for a in addons:
    fn = a.get("fileNameOnDisk") or a.get("installedFile", {}).get("fileName")
    if fn in excluded_names:
        excluded_pids[a["addonID"]] = {
            "name": a.get("name"),
            "fileID": a["installedFile"]["id"],
            "fileName": fn
        }
        print(f"Excluded: {a.get('name')} (PID: {a['addonID']}, FID: {a['installedFile']['id']})")

print(f"\nTotal excluded found in minecraftinstance.json: {len(excluded_pids)} / {len(excluded_names)}")
missing = excluded_names - set(v["fileName"] for v in excluded_pids.values())
if missing:
    print(f"Missing from mapping: {missing}")
