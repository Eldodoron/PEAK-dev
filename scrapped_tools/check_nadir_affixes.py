import zipfile
import json

with zipfile.ZipFile('minecraft/mods/nadir-1.0.0.jar') as zn, zipfile.ZipFile('minecraft/mods/Apotheosis-1.21.1-8.6.1.jar') as za:
    for n in zn.namelist():
        if 'affixes/' in n and n.endswith('.json'):
            ndata = json.loads(zn.read(n).decode('utf-8'))
            atype = ndata.get('type')
            apoth_path = n.replace('data/nadir/', 'data/apotheosis/')
            if apoth_path in za.namelist():
                adata = json.loads(za.read(apoth_path).decode('utf-8'))
                for k in adata:
                    if k not in ndata and k != 'values':
                        print(f'{n} (type={atype}): missing key "{k}" (apotheosis has: {adata[k]})')
