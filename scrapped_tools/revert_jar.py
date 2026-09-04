import zipfile, os

def unfix_jar(jar_path):
    if not os.path.exists(jar_path):
        print('Missing:', jar_path)
        return
    temp_path = jar_path + '.tmp'
    with zipfile.ZipFile(jar_path, 'r') as zin, zipfile.ZipFile(temp_path, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename == 'pack.mcmeta':
                broken = '''{
  "pack": {
    "description": {
      "text": "${mod_id} resources"
    },
    "pack_format": ${pack_format_number}
}
}'''
                zout.writestr(item, broken)
            else:
                zout.writestr(item, zin.read(item.filename))
    os.replace(temp_path, jar_path)
    print('Reverted', jar_path)

unfix_jar(r'c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev beta1\minecraft\mods\kubejsarsnouveau-1.3.2.jar')
unfix_jar(r'c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\mods\kubejsarsnouveau-1.3.2.jar')
