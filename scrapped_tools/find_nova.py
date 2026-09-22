import os
import zipfile

mods_dir = r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods'
found = False
for fname in os.listdir(mods_dir):
    if fname.endswith('.jar'):
        p = os.path.join(mods_dir, fname)
        try:
            with zipfile.ZipFile(p, 'r') as z:
                names = z.namelist()
                if any('nova_structures' in n for n in names):
                    print(f"Found in mod: {fname}")
                    found = True
        except:
            pass

if not found:
    print("Not found in any active mod jar!")
