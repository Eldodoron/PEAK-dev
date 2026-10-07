import zipfile
import os

MODS_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"

to_check = [
    'atmospherics-2.6.5-mc-1.21.1.jar',
    'bigwater-1.2.0-neoforge+mc1.21.1.jar.disabled',
    'fwa+1.21.1-neoforge-1.2.31.jar',
    'NBTac-NEOFORGE-1.21.1-1.3.10.jar',
    'Nirvana Lib-neoforge-1.21.1-2.2.0.jar',
    'OctoLib-NEOFORGE-0.6.2+1.21.jar',
    'Searchables-neoforge-1.21.1-1.0.2.jar',
    'cosycritters-0.3.2+1.21.1-neoforge.jar',
    'denseflower-1.0.0.jar'
]

for fn in to_check:
    p = os.path.join(MODS_DIR, fn)
    print(f"=== {fn} ===")
    with zipfile.ZipFile(p, 'r') as z:
        names = z.namelist()
        for t in ['META-INF/neoforge.mods.toml', 'META-INF/mods.toml', 'fabric.mod.json']:
            if t in names:
                print(f"--- {t} ---")
                print(z.read(t).decode('utf-8', errors='ignore')[:350])
        classes = [x for x in names if x.endswith('.class')]
        print(f"Total classes: {len(classes)}")
        # print sample of non-client classes
        non_client = [x for x in classes if 'client' not in x.lower()]
        print(f"Non-client classes ({len(non_client)}): {non_client[:5]}")
