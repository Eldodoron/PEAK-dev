import zipfile
import tomllib

jarPath = r'C:\Users\wamb9\Desktop\Server_Mods_PEAK\shine-2.0.1+1.21.1-neoforge.jar'
with zipfile.ZipFile(jarPath, 'r') as z:
    for name in z.namelist():
        if name.endswith('neoforge.mods.toml') or name.endswith('mods.toml') or name.endswith('fabric.mod.json'):
            print(f'--- {name} ---')
            print(z.read(name).decode('utf-8'))
