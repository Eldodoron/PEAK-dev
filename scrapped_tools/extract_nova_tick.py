import zipfile

jar_path = r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods\dungeons-and-taverns-v4.4.4 [NeoForge].jar'
with zipfile.ZipFile(jar_path, 'r') as z:
    for name in z.namelist():
        if 'nova_structures' in name and name.endswith('.mcfunction'):
            print(name)
            if 'tick' in name:
                print("--- CONTENT OF " + name + " ---")
                print(z.read(name).decode('utf-8', errors='ignore'))
