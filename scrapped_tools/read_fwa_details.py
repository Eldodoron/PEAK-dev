import zipfile
jar_path = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods\fwa+1.21.1-neoforge-1.2.31.jar"
with zipfile.ZipFile(jar_path) as zf:
    for name in zf.namelist():
        if "mods.toml" in name:
            lines = zf.read(name).decode('utf-8', errors='ignore').splitlines()
            for i, l in enumerate(lines):
                if "displayName" in l or "description" in l or "modId" in l:
                    print(f"{i}: {l}")
