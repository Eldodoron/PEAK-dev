import json
import zipfile
import os

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\deep_scan.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Known server-side or both mods that might look like client or UI or optimization:
KNOWN_SERVER_OR_BOTH = {
    'modernfix', 'ferritecore', 'lithium', 'krypton_fnp', 'noisiumed', 'spark', 'servercore',
    'fastsuite', 'recipeessentials', 'structureessentials', 'paxi', 'polymorph', 'netherportalfix',
    'letmedespawn', 'packetfixer', 'logprot', 'memguard', 'leaky', 'cupboard', 'placebo',
    'smartbrainlib', 'rhino', 'kubejs', 'morejs', 'curios', 'caelus', 'cloth_config',
    'jei', 'jade', 'appleskin', 'paraglider', 'lootr', 'lootr_liason', 'item_obliterator',
    'chunky', 'crafttweaker', 'octolib', 'resourcefullib', 'puzzleslib', 'cerbonsapi',
    'lionfishapi', 'mru', 'panoptic', 'playeranimator', 'citadel', 'geckolib', 'azurelib',
    'architectury', 'neoforge', 'minecraft', 'patchouli', 'solcarrot', 'someassemblyrequired',
    'sophisticatedbackpacks', 'sophisticatedcore', 'supplementaries', 'farmersdelight',
    'apotheosis', 'apothicattributes', 'apothicenchanting', 'apothicspawners', 'mekanism',
    'immersiveengineering', 'draconic_evolution', 'cataclysm', 'twilightforest', 'undergarden',
    'aether', 'aquaculture', 'alexsmobs', 'artifacts', 'waystones', 'dungeons_arise',
    'incendium', 'nullscape', 'irons_spellbooks', 'mutantmonsters', 'illageandspillage',
    'takesapillage', 'rottencreatures', 'whisperwoods', 'born_in_chaos_v1', 'boss_rifts',
    'sable', 'sabledestructive', 'treephysics', 'fallingtree', 'trading_floor', 'towntalk',
    'unusualend', 'variantsandventures', 'villagesandpillages', 'village_n_pillage_remake',
    'yagm', 'trimeffects', 'multiplayerbosses', 'plagatesummon', 'mobspropertiesrandomness',
    'easyanvils', 'explorerscompass', 'naturescompass', 'buildingwands', 'evologintimeout',
    'gateways', 'gobber2', 'goodending', 'ida', 'iss', 'illagerinvasion', 'mynethersdelight',
    'necronomicon', 'nirvana_lib', 'prickle', 'remnant_bosses', 'royal_variations',
    'simplycataclysm', 'simplyentityequipment', 'simplymore', 'simplyswords', 'smooth_steps',
    'structurify', 'structurize', 'tfmg', 'the_beyond', 'tlc', 'traveloptics', 'twilightdelight',
    'uranus', 'vampire_spells_addon', 'vampiricageing', 'vampirism_integrations', 'waystonessable',
    'wind_spellbooks', 'wizard_samurai', 'createdragonsplus', 'bomd', 'brandons_core',
    'codechickenlib', 'dndesires', 'dungeonsarisesevenseas', 'kjscauto', 'kubejs_curios',
    'kubejs_enderio', 'kubejs_rarity', 'kubejsarsnouveau', 'kubejsdelight', 'libertyvillagers',
    'almanac', 'antiqueatlas', 'autotag', 'badpackets', 'betterarcheology', 'bettercombat',
    'betterdungeons', 'betterfortresses', 'betterjungletemples', 'bettermineshafts',
    'betteroceanmonuments', 'betterstrongholds', 'betterwitchhuts', 'bloodmagic', 'borealis',
    'cataclysmic_combat', 'celestial_artifacts', 'celestial_core', 'corpse', 'corpse_curios',
    'create', 'create_central_kitchen', 'create_connected', 'create_dragons_armor',
    'create_dragon_lib', 'create_enchantment_industry', 'create_extra_casing', 'create_new_age',
    'create_optical', 'create_sa', 'createaddition', 'creeperoverhaul', 'crittersandcompanions',
    'cullleaves', 'curios_continuation', 'daily_rewards', 'darkutils', 'dawn', 'death_knell',
    'deep_dark_regrowth', 'deeperdarker', 'dimdoors', 'dummmmmmy', 'eidolon', 'eldritch_end',
    'embers', 'enchantinginfuser', 'ends_delight', 'enhancedcelestials', 'enigmaticlegacy',
    'entity_collision_fps_fix', 'eureka', 'experiencebugfix', 'extragolems', 'factory_blocks',
    'farmersstructures', 'fastip', 'ftbchunks', 'ftblibrary', 'ftbquests', 'ftbteams',
    'ftbxmodcompat', 'fusion', 'graveyard', 'graveyard_biomes', 'gtceu', 'handcrafted',
    'iceandfire', 'integrateddynamics', 'ironchest', 'ironfurnaces', 'itemphysic',
    'justhammers', 'lootr', 'majruszsdifficulty', 'majruszlibrary', 'mcwdoors', 'mcwfences',
    'mcwfurnitures', 'mcwlights', 'mcwpaintings', 'mcwpaths', 'mcwroofs', 'mcwstairs',
    'mcwswindows', 'mysticalagriculture', 'mysticalagradditions', 'observable', 'pneumaticcraft',
    'quark', 'reliquary', 'silentgear', 'silentlib', 'thermal', 'thermal_expansion',
    'thermal_foundation', 'valkyrienskies', 'vintageimprovements'
}

candidates = []
for fn, m in sorted(data.items()):
    mid = (m.get('mod_id') or '').lower()
    # Check if disabled / backup / modified
    is_special = fn.endswith('.disabled') or fn.endswith('.backup') or fn.endswith('.modified')
    
    # Check indicators
    reasons = []
    
    # 1. Manifest side or env
    if m.get('env') == 'client':
        reasons.append("fabric.mod.json environment = client")
    if m.get('dep_side') == 'CLIENT':
        reasons.append("neoforge dependency side = CLIENT")
    if m.get('display_test') in ('IGNORE_ALL_VERSION', 'NONE'):
        reasons.append(f"displayTest = {m.get('display_test')}")
        
    # 2. Check keywords in filename or modid or display name
    name_lower = (m.get('display_name') or '').lower()
    desc_lower = (m.get('desc') or '').lower()
    fn_lower = fn.lower()
    
    client_keywords = [
        'sodium', 'iris', 'oculus', 'embeddium', 'rubidium', 'immediatelyfast', 'badoptimization',
        'dynamic-fps', 'culling', 'entityculling', 'moreculling', 'rhenium', 'super_resolution',
        'smoothchunk', 'smooththirdperson', 'betterthirdperson', 'cameraoverhaul', 'freecam',
        'etf', 'emf', 'entity_texture_features', 'entity_model_features', 'visuality',
        'notenoughanimations', 'skinlayers', 'skin_layers', 'waveycapes', 'eatinganimation',
        'chatheads', 'chat_heads', 'fallingleaves', 'particle', 'simplefog', 'cirrus',
        'sounds-', 'presencefootsteps', 'auditory', 'soundphysics', 'dynamicmusic',
        'controlling', 'mousetweaks', 'cursor', 'tooltip', 'overflowingbars', 'healthbars',
        'locatorbar', 'recipe_book', 'toast', 'cherished', 'configured', 'catalogue',
        'searchables', 'cleantooltip', 'miningspeedtooltips', 'wits', 'trade_cycling',
        'justenoughbeacons', 'justenoughprofessions', 'jeiworldgen', 'essential',
        'crashassistant', 'resourcify', 'nowheel', 'textureupdates', 'smoothswapping',
        'punchy', 'cinematic_respawn', 'ragdoll', 'shine', 'yet_another_config_lib',
        'reeses', 'sodiumoptions', 'saturn'
    ]
    
    matched_kw = [kw for kw in client_keywords if kw in fn_lower or kw in mid or kw in name_lower]
    if matched_kw:
        reasons.append(f"Matched keywords: {', '.join(matched_kw)}")
        
    # 3. Check data folder
    if not m.get('has_data') and not reasons and mid not in KNOWN_SERVER_OR_BOTH:
        reasons.append("No data folder and not in known server list")
        
    if reasons:
        candidates.append({
            'filename': fn,
            'mod_id': mid,
            'name': m.get('display_name'),
            'reasons': reasons,
            'has_data': m.get('has_data'),
            'data_dirs': m.get('data_dirs', []),
            'desc': m.get('desc', '')[:100]
        })

print(f"Found {len(candidates)} potential client or special candidates.")
with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\candidates.json', 'w', encoding='utf-8') as out:
    json.dump(candidates, out, indent=2)
