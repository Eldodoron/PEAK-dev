import os
import zipfile
import tomllib

mods_dir = r'C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\mods'
client_mods = []
server_mods = []
unknown_mods = []

for filename in os.listdir(mods_dir):
    if not filename.endswith('.jar'):
        continue
    filepath = os.path.join(mods_dir, filename)
    is_client_only = False
    found_toml = False
    
    try:
        with zipfile.ZipFile(filepath, 'r') as z:
            # Look for neoforge.mods.toml or mods.toml
            toml_path = None
            if 'META-INF/neoforge.mods.toml' in z.namelist():
                toml_path = 'META-INF/neoforge.mods.toml'
            elif 'META-INF/mods.toml' in z.namelist():
                toml_path = 'META-INF/mods.toml'
                
            if toml_path:
                found_toml = True
                with z.open(toml_path) as f:
                    try:
                        data = tomllib.load(f)
                        # Check mods array
                        if 'mods' in data:
                            for mod in data['mods']:
                                # Some mods use displayTest="IGNORE_SERVER_VERSION" or displayTest="IGNORE_ALL_VERSION"
                                # but the most reliable way in new forge is 'side="client"' or checking displayTest
                                if mod.get('displayTest') == 'IGNORE_SERVER_VERSION':
                                    pass # Could be client side, could just be a library
                    except Exception as e:
                        pass
    except Exception as e:
        pass
        
    if not found_toml:
        unknown_mods.append(filename)

# Since TOML parsing for side is unreliable due to different standards, 
# let's just use a heuristic keyword list for obvious client mods.
client_keywords = [
    'oculus', 'rubidium', 'embeddium', 'sodium', 'iris', 'xenon', 'radium', 
    'jei-', 'rei-', 'emi-', 'jade-', 'waila', 'appleskin', 'journeymap', 'xaeros', 
    'cloth-config', 'configured', 'catalogue', 'betterthirdperson', 'dynamiclights',
    'soundphysics', 'ambientsounds', 'presencefootsteps', 'creativecore',
    'defaultoptions', 'controlling', 'searchables', 'mousetweaks', 'inventorysorter',
    'client', 'visual', 'hud', 'gui', 'cam', 'shader', 'menu', 'tooltip'
]

results = []
for filename in os.listdir(mods_dir):
    if not filename.endswith('.jar'):
        continue
    fn_lower = filename.lower()
    is_client = False
    for kw in client_keywords:
        if kw in fn_lower:
            is_client = True
            break
    if is_client:
        results.append(filename)

print('--- POTENTIAL CLIENT MODS ---')
for r in results:
    print(r)

