import os
import zipfile

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"

files_to_check = [
    'aaa_particles-neoforge-1.21.1-2.2.3.jar.disabled',
    'aaa_particles_world-neoforge-1.21.1-2.0.0.jar.disabled',
    'ragdoll_reactions-1.21.1-0.7.0.jar.disabled',
    'sable_player_ragdoll-1.21.1-0.7.5.jar.disabled',
    'redirected-neoforge-1.0.0-1.21.1.jar.disabled',
    'reliable_replacer-neoforge-1.21.1-1.7.0.jar.disabled',
    'incrementalmining-1.21.1-1.5.jar.disabled',
    'textureupdatesneo.jar.disabled'
]

for f in files_to_check:
    print(f"\n==================== {f} ====================")
    path = os.path.join(mods_dir, f)
    with zipfile.ZipFile(path, 'r') as z:
        names = z.namelist()
        for toml in ["META-INF/neoforge.mods.toml", "META-INF/mods.toml", "fabric.mod.json"]:
            if toml in names:
                print(f"--- {toml} ---")
                print(z.read(toml).decode('utf-8', errors='ignore')[:1000])
        # list some classes
        classes = [n for n in names if n.endswith('.class')]
        print(f"Total classes: {len(classes)}")
        print("Sample classes:", classes[:10])
