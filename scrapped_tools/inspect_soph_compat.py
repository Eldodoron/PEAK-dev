import zipfile

jar_path = r"minecraft/mods/create_sophback_compat-1.0.jar"
with zipfile.ZipFile(jar_path) as zf:
    print("Files in create_sophback_compat:")
    for n in zf.namelist():
        print(" ", n)
        if "mods.toml" in n or "mixins.json" in n:
            print("--- Content ---")
            print(zf.read(n).decode('utf-8', errors='ignore'))
