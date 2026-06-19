import zipfile

with zipfile.ZipFile('minecraft/mods/lithostitched-1.7.9-neoforge-21.1.jar', 'r') as z:
    for info in z.infolist():
        if info.filename == 'pack.mcmeta':
            print(f'--- {info.file_size} bytes ---')
            print(z.read(info).decode('utf-8'))
