import os
import zipfile
import tomllib
import re

mods_dir = r'C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\mods'

# List from user prompt
user_list = '''
aero_cam_sync-1.3.1.jar
catalogue-neoforge-1.21.1-1.11.2.jar
configured-neoforge-1.21.1-2.6.3.jar
fastboot-1.21.x-v1.3neo.jar
guideme-21.1.16.jar
SimplyTooltips-neoforge-0.1.3.jar
textureupdatesneo.jar
'''

client_mods = []

for filename in os.listdir(mods_dir):
    if not filename.endswith('.jar'):
        continue
        
    filepath = os.path.join(mods_dir, filename)
    try:
        with zipfile.ZipFile(filepath, 'r') as z:
            toml_path = None
            if 'META-INF/neoforge.mods.toml' in z.namelist():
                toml_path = 'META-INF/neoforge.mods.toml'
            elif 'META-INF/mods.toml' in z.namelist():
                toml_path = 'META-INF/mods.toml'
                
            if toml_path:
                with z.open(toml_path) as f:
                    try:
                        data = tomllib.load(f)
                        if 'mods' in data:
                            for mod in data['mods']:
                                display_test = mod.get('displayTest', '')
                                if display_test in ['IGNORE_SERVER_VERSION', 'IGNORE_ALL_VERSION']:
                                    client_mods.append(filename)
                                    break
                    except Exception as e:
                        pass
    except Exception as e:
        pass

print('Client-side only mods based on TOML displayTest (IGNORE_SERVER_VERSION):')
for m in sorted(client_mods):
    print(m)

