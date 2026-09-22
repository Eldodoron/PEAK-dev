import zipfile

with zipfile.ZipFile("minecraft/mods/create-enchantment-industry-2.5.4.jar") as zf:
    for n in zf.namelist():
        if "mods.toml" in n:
            print("=== CEI 2.5.4 toml ===")
            content = zf.read(n).decode('utf-8', errors='ignore')
            for line in content.splitlines():
                if "dependencies" in line or "modId" in line or "versionRange" in line or "type" in line:
                    print(line)

with zipfile.ZipFile("minecraft/mods/create-integrated-farming-1.4.2.jar") as zf:
    for n in zf.namelist():
        if "mods.toml" in n:
            print("\n=== Integrated Farming 1.4.2 toml ===")
            content = zf.read(n).decode('utf-8', errors='ignore')
            for line in content.splitlines():
                if "dependencies" in line or "modId" in line or "versionRange" in line or "type" in line:
                    print(line)
