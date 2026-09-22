import os
import zipfile

mods_dir = 'minecraft/mods'
optimization_suite = []

for f in os.listdir(mods_dir):
    if not f.endswith('.jar'):
        continue
    p = os.path.join(mods_dir, f)
    try:
        with zipfile.ZipFile(p) as z:
            mod_name = f
            desc = ""
            modid = ""
            if 'META-INF/neoforge.mods.toml' in z.namelist():
                txt = z.read('META-INF/neoforge.mods.toml').decode('utf-8', errors='ignore')
                for line in txt.splitlines():
                    if line.strip().startswith('modId='):
                        modid = line.split('=')[1].strip().strip('"\'')
                    elif line.strip().startswith('displayName='):
                        mod_name = line.split('=')[1].strip().strip('"\'')
                    elif line.strip().startswith('description='):
                        desc = line.split('=', 1)[1].strip().strip('\'" ')
            elif 'META-INF/mods.toml' in z.namelist():
                txt = z.read('META-INF/mods.toml').decode('utf-8', errors='ignore')
                for line in txt.splitlines():
                    if line.strip().startswith('modId='):
                        modid = line.split('=')[1].strip().strip('"\'')
                    elif line.strip().startswith('displayName='):
                        mod_name = line.split('=')[1].strip().strip('"\'')
            elif 'fabric.mod.json' in z.namelist():
                import json
                fj = json.loads(z.read('fabric.mod.json').decode('utf-8', errors='ignore'))
                modid = fj.get('id', '')
                mod_name = fj.get('name', f)
                desc = fj.get('description', '')

            # Check if this mod is related to performance/optimization/memory/culling
            keywords = ['opti', 'cull', 'memory', 'leak', 'faster', 'speed', 'fps', 'performance', 'cache', 'lag', 'render', 'tps', 'chunk']
            combo = f"{modid} {mod_name} {desc} {f}".lower()
            if any(k in combo for k in keywords):
                optimization_suite.append((f, modid, mod_name))
    except Exception as e:
        pass

print(f"Total optimization-related mods detected: {len(optimization_suite)}")
for jar, mid, name in sorted(optimization_suite, key=lambda x: x[1]):
    print(f"  [{mid}] {name} ({jar})")
