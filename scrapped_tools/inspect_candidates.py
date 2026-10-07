import json
import zipfile
import os

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\precise_mod_info.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Let's inspect specific mods to see what they are:
inspect_list = [
    'Almanac-1.21.1-2-neoforge-1.5.2.jar',
    'Antique Atlas-1.21.1-8.0.1-NeoForge.jar.disabled',
    'CameraOverhaul-v2.1.1-neoforge+mc[1.21-1.21.1].jar.disabled',
    'CrashAssistant-neoforge-1.20.6-1.21.4-1.11.9.jar',
    'DistantHorizons-3.3.2-1.21.1-fabric-neoforge.jar',
    'Essential_1-5-0-1_neoforge_1-21-1.jar',
    'HealthBars-v21.1.0-1.21.1-NeoForge.jar',
    'Item-Obliterator-NeoForge-MC1.21.1-2.3.0.jar',
    'Ixeris-4.4.1+1.21.1-neoforge.jar',
    'jauml-neoforge-1.21.1-2.0.0.jar',
    'jeiworldgen-neoforge-1.21.1-1.4.1.jar',
    'jupiter-2.3.7-1.21.1-neoforge.jar',
    'JustEnoughProfessions-neoforge-1.21.1-4.0.5.jar',
    'JustEnoughResources-NeoForge-1.21.1-1.6.0.17.jar',
    'LocatorBar-neoforge-1.2.2+1.21.1.jar',
    'Loot Beams Refork-neoforge-1.21.1-3.4.7.jar',
    'miningspeedtooltips-neoforge-1.0.0-1.21.1.jar',
    'OverflowingBars-v21.1.1-1.21.1-NeoForge.jar',
    'ragdoll_reactions-1.21.1-0.7.0.jar.disabled',
    'sable_player_ragdoll-1.21.1-0.7.5.jar.disabled',
    'saturn-mc1.21.1-0.1.5.jar.disabled',
    'sodiumoptionsapi-neoforge-1.0.10-1.21.1.jar.disabled',
    'sodiumoptionsmodcompat-neoforge-1.0.0-1.21.1.jar.disabled',
    'ToastControl-1.21.1-9.0.1.jar',
    'trade-cycling-neoforge-1.21.1-1.0.18.jar',
    'visuality-forge-3.0.0.jar',
    'wits-1.3.0+1.21-neoforge.jar',
    'rhenium-1.0.0+neo.jar',
    'smoothchunk-1.21-4.1.jar.disabled',
    'textureupdatesneo.jar.disabled',
    'txnilib-neoforge-1.0.24-1.21.1.jar.backup',
    'txnilib-neoforge-1.0.24-1.21.1.jar.modified',
    'clean_tooltips-1.1-neoforge-1.21.1.jar.disabled',
    'lambdynamiclights-4.8.8+1.21.1.jar',
    'entity_texture_features_1.21-neoforge-7.1.jar',
    'Perception-NEOFORGE-0.2.1+1.21.1.jar'
]

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"

for fn in inspect_list:
    p = os.path.join(mods_dir, fn)
    if os.path.exists(p):
        m = data.get(fn, {})
        print(f"=== {fn} ===")
        print(f"  ID: {m.get('mod_id')} | Name: {m.get('display_name')}")
        print(f"  Desc: {(m.get('description') or '')[:120]}")
        print(f"  MC Dep Side: {m.get('mc_dep_side')} | Neo Dep Side: {m.get('neoforge_dep_side')} | DT: {m.get('display_test')} | Env: {m.get('fabric_env')}")
        print(f"  Data: {m.get('has_data')} | Dirs: {m.get('data_dirs')}")
        print(f"  Mixins: c={m.get('client_mixins_count')}, s={m.get('server_mixins_count')}, comm={m.get('common_mixins_count')}")
