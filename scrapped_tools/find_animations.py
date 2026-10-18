import os
import zipfile

anims = ['attack_single', 'supernova', 'swim_charge']
for f in os.listdir('minecraft/mods'):
    if f.endswith('.jar'):
        try:
            with zipfile.ZipFile('minecraft/mods/' + f) as z:
                for n in z.namelist():
                    if 'animation' in n and n.endswith('.json'):
                        content = z.read(n).decode('utf-8', errors='ignore')
                        for a in anims:
                            if f'"{a}"' in content:
                                print(f, n, a)
        except:
            pass
