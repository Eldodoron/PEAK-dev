import os
import zipfile

mods_dir = r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods'
for fname in os.listdir(mods_dir):
    if fname.endswith('.jar'):
        p = os.path.join(mods_dir, fname)
        try:
            with zipfile.ZipFile(p, 'r') as z:
                for name in z.namelist():
                    if name.endswith('.mcfunction'):
                        content = z.read(name).decode('utf-8', errors='ignore')
                        if 'scoreboard' in content and '@e' in content:
                            print(f"Mod: {fname} -> {name}")
                            # print first 3 matching lines
                            for l in content.splitlines():
                                if 'scoreboard' in l and '@e' in l:
                                    print("   ", l[:120])
        except:
            pass
