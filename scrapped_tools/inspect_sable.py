import zipfile

def inspect(path):
    with zipfile.ZipFile(path) as zf:
        print(f"=== {path} ===")
        for n in zf.namelist():
            if "mods.toml" in n:
                print(zf.read(n).decode('utf-8', errors='ignore'))

inspect("minecraft/mods/sable-neoforge-1.21.1-1.2.2.jar")
inspect("minecraft/mods/sabledestructive-1.7.2.jar")
