import os
import zipfile
import tomllib

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"
client_side_mods = {}
for f in os.listdir(mods_dir):
    if not (f.endswith('.jar') or '.jar.' in f): continue
    with zipfile.ZipFile(os.path.join(mods_dir, f)) as z:
        for t in ['META-INF/neoforge.mods.toml', 'META-INF/mods.toml']:
            if t in z.namelist():
                try:
                    data = tomllib.loads(z.read(t).decode('utf-8', errors='ignore'))
                    deps = data.get('dependencies', {})
                    for mk, dl in deps.items():
                        if isinstance(dl, list):
                            for d in dl:
                                if d.get('modId') in ['minecraft', 'neoforge', 'forge'] and d.get('side') == 'CLIENT':
                                    client_side_mods[f] = f"{d.get('modId')} side=CLIENT"
                except:
                    pass
print(f"Total mods declaring minecraft/neoforge side=CLIENT: {len(client_side_mods)}")
for f, s in sorted(client_side_mods.items()):
    print(f"  {f}: {s}")
