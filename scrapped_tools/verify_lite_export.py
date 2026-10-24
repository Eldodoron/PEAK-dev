import zipfile
import json
import os

zip_path = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\PackExports\Peak-Lite-alpha3.zip"
staged_path = os.path.join(os.environ["TEMP"], "Peak-Lite-alpha3.zip")

print("Verifying Lite ZIP at:", zip_path)
print("File size:", os.path.getsize(zip_path), "bytes")
print("Staged ZIP exists:", os.path.exists(staged_path))

with zipfile.ZipFile(zip_path, "r") as z:
    man_raw = z.read("manifest.json")
    assert man_raw[0] == ord("{"), "BOM found in manifest!"
    man = json.loads(man_raw.decode("utf-8"))
    print("Manifest name:", man["name"])
    print("Manifest version:", man["version"])
    print("Manifest author:", man["author"])
    print("Manifest recommended RAM:", man["minecraft"]["recommendedRam"])
    print("Total mod files in manifest:", len(man["files"]))
    assert len(man["files"]) == 385

    file_map = {f["projectID"]: f["fileID"] for f in man["files"]}
    check_mods = {
        "FancyMenu": 367706,
        "Drippy Loading Screen": 511770,
        "Drippy Early Loading Module": 1390924,
        "Konkrete": 410295,
        "Melody": 938643
    }
    for name, pid in check_mods.items():
        assert pid in file_map, f"Missing {name} ({pid})!"
        print(f"  [OK] {name}: projectID={pid}, fileID={file_map[pid]}")

    jars = [n for n in z.namelist() if n.lower().endswith(".jar") or n.lower().endswith(".jar.disabled")]
    assert len(jars) == 0, f"Found loose jars: {jars}"
    print("Loose JARs in overrides: 0")

    fm_entries = [n for n in z.namelist() if "fancymenu" in n.lower() or "drippy" in n.lower()]
    print(f"FancyMenu / Drippy files in overrides: {len(fm_entries)}")

    dh = z.read("overrides/config/DistantHorizons.toml").decode("utf-8")
    assert "lodChunkRenderDistanceRadius = 32" in dh
    print("Distant Horizons radius: 32 [OK]")

    bc = z.read("overrides/config/bettercombat/client.json5").decode("utf-8")
    assert '"firstPersonAnimations": "YES"' in bc
    print("Better Combat first person animations: YES [OK]")

print("\nALL LITE ALPHA3 VERIFICATIONS PASSED SUCCESSFULLY!")
