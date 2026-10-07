import zipfile
import json
import os

MODS_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"

to_inspect = [
    'catalogue-neoforge-1.21.1-1.11.2.jar',
    'configured-neoforge-1.21.1-2.6.3.jar',
    'Loot Beams Refork-neoforge-1.21.1-3.4.7.jar',
    'healight-neoforge-1.21.1-1.0.1.jar',
    'heavier_weapons-1.21.1-NeoForge-1.1.0.jar',
    'aaa_particles-neoforge-1.21.1-2.2.3.jar.disabled',
    'aaa_particles_world-neoforge-1.21.1-2.0.0.jar.disabled',
    'player-animation-lib-forge-2.0.4+1.21.1.jar'
]

for fn in to_inspect:
    p = os.path.join(MODS_DIR, fn)
    print(f"=== {fn} ===")
    with zipfile.ZipFile(p, 'r') as z:
        names = z.namelist()
        # check toml
        for t in ['META-INF/neoforge.mods.toml', 'META-INF/mods.toml', 'fabric.mod.json']:
            if t in names:
                print(f"--- {t} ---")
                print(z.read(t).decode('utf-8', errors='ignore')[:400])
        # check mixins
        mixins = [x for x in names if x.endswith('.mixins.json')]
        for m in mixins:
            print(f"--- mixin: {m} ---")
            print(z.read(m).decode('utf-8', errors='ignore')[:300])
        # sample classes
        classes = [x for x in names if x.endswith('.class')]
        print(f"Total classes: {len(classes)}")
        client_c = [x for x in classes if 'client' in x.lower()]
        net_c = [x for x in classes if 'net' in x.lower() or 'packet' in x.lower()]
        print(f"Client classes: {len(client_c)}, Net classes: {len(net_c)}")
