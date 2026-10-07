import zipfile
import os
import json

MODS_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"

mods_to_check = [
    'trade-cycling-neoforge-1.21.1-1.0.18.jar',
    'jauml-neoforge-1.21.1-2.0.0.jar',
    'saturn-mc1.21.1-0.1.5.jar.disabled',
    'DistantHorizons-3.3.2-1.21.1-fabric-neoforge.jar',
    'aero_cam_sync-1.3.1.jar',
    'atmospherics-2.6.5-mc-1.21.1.jar',
    'cloudlayers-1.21.1-1.1.jar',
    'collapsible_groups-neoforge-1.21.1-1.4.2.jar',
    'cosycritters-0.3.2+1.21.1-neoforge.jar',
    'denseflower-1.0.0.jar',
    'enchdesc-neoforge-1.21.1-21.1.10.jar',
    'explosiveenhancement-neoforge-1.21.1-1.1.2.jar',
    'fwa+1.21.1-neoforge-1.2.31.jar',
    'guideme-21.1.17.jar',
    'incrementalmining-1.21.1-1.5.jar.disabled',
    'jeed-1.21-2.3.3.jar',
    'lootr_liason-1.2-neoforge.jar',
    'multiplayerbosses-neoforge-1.21.1-1.0.0.jar',
    'NBTac-NEOFORGE-1.21.1-1.3.10.jar',
    'Nirvana Lib-neoforge-1.21.1-2.2.0.jar',
    'OctoLib-NEOFORGE-0.6.2+1.21.jar',
    'Panoptic-1.08a-NeoForge-1.21.1.jar',
    'particular-1.21.1-NeoForge-1.5.5.jar',
    'ragdoll_reactions-1.21.1-0.7.0.jar.disabled',
    'sable_player_ragdoll-1.21.1-0.7.5.jar.disabled',
    'shine-2.0.1+1.21.1-neoforge.jar',
    'SimplyTooltips-neoforge-0.1.5.jar',
    'towntalk-1.2.0.jar',
    'txnilib-neoforge-1.0.24-1.21.1.jar',
    'uranus-2.4.1-1.21.1-neoforge.jar',
    'yet_another_config_lib_v3-3.8.2+1.21.1-neoforge.jar',
    'Searchables-neoforge-1.21.1-1.0.2.jar',
    'CrashAssistant-neoforge-1.20.6-1.21.4-1.11.9.jar',
    'EvoLoginTimeout-NeoForge-1.21.1-1.0.9.jar',
    'Almanac-1.21.1-2-neoforge-1.5.2.jar',
    'Antique Atlas-1.21.1-8.0.1-NeoForge.jar.disabled',
    'CameraOverhaul-v2.1.1-neoforge+mc[1.21-1.21.1].jar.disabled',
    'BetterThirdPerson-neoforge-1.9.0.jar',
    'smooththirdpersoncamera-26.05.28-mc1.21.1.jar.disabled',
    'smoothswapping-0.9.3.2-1.21.1-neoforge.jar',
    'smoothchunk-1.21-4.1.jar.disabled',
    'super_resolution-neoforge-1.21..1.21.1-0.8.3-alpha.4+opengl.jar.disabled',
    'ToastControl-1.21.1-9.0.1.jar',
    'tooltipoverhaul-neoforge-1.21.1-1.5.1.jar',
    'wits-1.3.0+1.21-neoforge.jar',
    'rhenium-1.0.0+neo.jar',
    'clean_tooltips-1.1-neoforge-1.21.1.jar.disabled',
    'JustEnoughResources-NeoForge-1.21.1-1.6.0.17.jar',
    'JustEnoughProfessions-neoforge-1.21.1-4.0.5.jar',
    'jeiworldgen-neoforge-1.21.1-1.4.1.jar',
    'Perception-NEOFORGE-0.2.1+1.21.1.jar',
    'redirected-neoforge-1.0.0-1.21.1.jar.disabled',
    'reliable_replacer-neoforge-1.21.1-1.7.0.jar.disabled'
]

results = {}

for fn in mods_to_check:
    p = os.path.join(MODS_DIR, fn)
    if not os.path.exists(p):
        continue
    info = {'filename': fn}
    with zipfile.ZipFile(p, 'r') as z:
        names = z.namelist()
        
        # Check neoforge.mods.toml
        toml_content = ""
        if 'META-INF/neoforge.mods.toml' in names:
            toml_content = z.read('META-INF/neoforge.mods.toml').decode('utf-8', errors='ignore')
        elif 'META-INF/mods.toml' in names:
            toml_content = z.read('META-INF/mods.toml').decode('utf-8', errors='ignore')
            
        info['toml_sample'] = toml_content[:300]
        
        # Find mixin files
        mixins = [x for x in names if x.endswith('.mixins.json') or x.endswith('mixin.json')]
        mixin_targets = []
        for mf in mixins:
            try:
                mdata = json.loads(z.read(mf).decode('utf-8', errors='ignore'))
                pkg = mdata.get('package', '')
                mixin_targets.append({
                    'file': mf,
                    'package': pkg,
                    'client': mdata.get('client', []),
                    'server': mdata.get('server', []),
                    'common': mdata.get('mixins', [])
                })
            except:
                pass
        info['mixins'] = mixin_targets
        
        # Check network packets / networking classes
        net_classes = [x for x in names if 'network' in x.lower() or 'packet' in x.lower()]
        info['net_classes_count'] = len(net_classes)
        info['net_classes_sample'] = net_classes[:5]
        
        # Check client classes vs server classes
        client_classes = [x for x in names if 'client' in x.lower()]
        info['client_classes_count'] = len(client_classes)
        
        # Check commands
        cmd_classes = [x for x in names if 'command' in x.lower()]
        info['cmd_classes_count'] = len(cmd_classes)
        
    results[fn] = info

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\ambiguous_audit.json', 'w', encoding='utf-8') as out:
    json.dump(results, out, indent=2)

print(f"Audited {len(results)} ambiguous mods.")
