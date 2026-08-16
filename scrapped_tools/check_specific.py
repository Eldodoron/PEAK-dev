import zipfile
import tomllib
import os

jars = [
    'bigwater-1.2.0-neoforge+mc1.21.1.jar',
    'CrashAssistant-neoforge-1.20.6-1.21.4-1.11.9.jar',
    'fwa+1.21.1-neoforge-1.2.31.jar',
    'healight-neoforge-1.21.1-1.0.1.jar',
    'particle_core-0.3.3+1.21+neoforge.jar',
    'particular-1.21.1-NeoForge-1.5.5.jar',
    'Perception-NEOFORGE-0.2.1+1.21.1.jar',
    'punchy-2.6.2-neoforge-1.21.1.jar',
    'sounds-2.4.22+lts+1.21.1-neoforge.jar'
]

base_dir = r'C:\Users\wamb9\Desktop\Server_Mods_PEAK'

for jar in jars:
    path = os.path.join(base_dir, jar)
    if not os.path.exists(path):
        continue
    try:
        with zipfile.ZipFile(path, 'r') as z:
            toml_path = None
            if 'META-INF/neoforge.mods.toml' in z.namelist():
                toml_path = 'META-INF/neoforge.mods.toml'
            elif 'META-INF/mods.toml' in z.namelist():
                toml_path = 'META-INF/mods.toml'
                
            if toml_path:
                with z.open(toml_path) as f:
                    try:
                        data = tomllib.load(f)
                        if 'mods' in data and len(data['mods']) > 0:
                            mod = data['mods'][0]
                            print(f"{jar}: displayTest = {mod.get('displayTest', 'NONE')}")
                    except:
                        pass
    except:
        pass
