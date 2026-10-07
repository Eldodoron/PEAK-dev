import json
import os
import zipfile
import re

MODS_DIR = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\precise_mod_info.json', 'r', encoding='utf-8') as f:
    mods_info = json.load(f)

# Let's write rules to evaluate every mod
def evaluate_mod(fn, m):
    # Returns (is_excluded_from_server, reason, category)
    
    # 0. Backup / modified duplicates
    if fn.endswith('.backup') or fn.endswith('.modified'):
        return True, "Backup/development artifact", "Backup / Duplicate"
        
    # 1. Obvious rendering & shaders
    name = (m.get('display_name') or '').lower()
    desc = (m.get('description') or '').lower()
    mid = (m.get('mod_id') or '').lower()
    fn_lower = fn.lower()
    
    # Shaders / Sodium ecosystem
    if any(k in fn_lower for k in ['sodium', 'iris', 'oculus', 'embeddium', 'rubidium', 'rhenium', 'super_resolution', 'shine', 'reeses']):
        return True, "Client rendering / shaders / graphics engine", "Graphics / Shaders"
        
    if fn_lower.startswith('immediatelyfast'):
        return True, "Client immediate-mode rendering optimization", "Client Performance"
        
    if fn_lower.startswith('badoptimizations'):
        return True, "Client-side entity/HUD optimization", "Client Performance"
        
    if fn_lower.startswith('dynamic-fps'):
        return True, "Client background FPS throttler", "Client Performance"
        
    if 'culling' in fn_lower or mid in ('moreculling', 'entityculling'):
        return True, "Client culling rendering optimization", "Client Performance"
        
    if 'smoothchunk' in fn_lower:
        return True, "Client chunk fade-in animation", "Client Visuals"
        
    if 'cirrus' in fn_lower or 'cloudlayers' in fn_lower:
        return True, "Client cloud and sky rendering", "Client Visuals"
        
    if 'simplefog' in fn_lower:
        return True, "Client fog customization", "Client Visuals"
        
    if 'denseflower' in fn_lower:
        return True, "Client flower rendering optimization/density", "Client Visuals"
        
    # Visuals / Models / Textures / Animations
    if any(k in fn_lower for k in ['entity_texture_features', 'entity_model_features', 'emf_compat', 'visuality', 'notenoughanimations', 'punchy', 'cinematic_respawn', 'skinlayers', 'waveycapes', 'eatinganimation', 'chatheads']):
        return True, "Client-side visual effects, entity models, textures, or animations", "Client Visuals"
        
    if fn_lower.startswith('particular') or fn_lower.startswith('particle_core') or fn_lower.startswith('explosiveenhancement'):
        return True, "Client particle effects and rendering", "Client Visuals"
        
    if 'perception' in fn_lower and mid == 'perception':
        return True, "Client visual post-processing effects", "Client Visuals"
        
    if 'lambdynamiclights' in fn_lower:
        return True, "Client dynamic lighting", "Client Visuals"
        
    # Camera / Third person / Input
    if any(k in fn_lower for k in ['betterthirdperson', 'smooththirdperson', 'cameraoverhaul', 'freecam', 'aero_cam_sync']):
        return True, "Client camera controls and third-person view", "Client Camera / Input"
        
    if any(k in fn_lower for k in ['mousetweaks', 'minecraft-cursor', 'nowheel', 'ixeris']):
        return True, "Client input, cursor, or inventory mouse dragging", "Client Camera / Input"
        
    # Audio
    if fn_lower.startswith('sounds-') or 'presencefootsteps' in fn_lower or 'soundphysics' in fn_lower or 'auditory' in fn_lower or 'dynamicmusic' in fn_lower:
        return True, "Client sound effects and acoustic reverb", "Client Audio"
        
    if fn_lower.startswith('towntalk'):
        return True, "Client voice pack audio files for MineColonies citizens (52MB)", "Client Audio"
        
    # HUD / Tooltips / Client GUI
    if fn_lower.startswith('controlling'):
        return True, "Client keybinding menu search bar", "Client GUI / HUD"
        
    if fn_lower.startswith('immersiveui'):
        return True, "Client HUD overhaul", "Client GUI / HUD"
        
    if fn_lower.startswith('overflowingbars') or fn_lower.startswith('healthbars') or fn_lower.startswith('locatorbar'):
        return True, "Client HUD bar and health indicator display", "Client GUI / HUD"
        
    if fn_lower.startswith('toastcontrol'):
        return True, "Client toast notification blocker", "Client GUI / HUD"
        
    if 'tooltipoverhaul' in fn_lower or 'miningspeedtooltips' in fn_lower or 'clean_tooltips' in fn_lower or 'simplytooltips' in fn_lower or 'enchdesc' in fn_lower:
        return True, "Client-side tooltip formatting and enhancements", "Client GUI / HUD"
        
    if fn_lower.startswith('not enough recipe book'):
        return True, "Client recipe book modifications", "Client GUI / HUD"
        
    if fn_lower.startswith('smoothswapping'):
        return True, "Client item swap visual animation", "Client GUI / HUD"
        
    # JEI purely client addons (no server networking)
    if fn_lower.startswith('justenoughbeacons'):
        return True, "JEI client addon showing beacon payment recipes", "Client JEI Addon"
        
    if fn_lower.startswith('justenoughprofessions'):
        return True, "JEI client addon showing villager workstations", "Client JEI Addon"
        
    if fn_lower.startswith('jeed'):
        return True, "JEI client addon showing status effect descriptions", "Client JEI Addon"
        
    if fn_lower.startswith('collapsible_groups'):
        return True, "JEI client recipe grouping", "Client JEI Addon"
        
    # Launcher / Social / Crash helper
    if fn_lower.startswith('essential'):
        return True, "Client social network, cosmetics, and peer-to-peer hosting (incompatible/unneeded on server)", "Client Social / Utility"
        
    if fn_lower.startswith('crashassistant'):
        return True, "Client crash GUI helper", "Client Social / Utility"
        
    if fn_lower.startswith('cosycritters'):
        return True, "Client-side critter visuals", "Client Visuals"

    return False, "Server or Common mod", "Server / Common"

results = []
for fn, m in sorted(mods_info.items()):
    is_ex, reason, cat = evaluate_mod(fn, m)
    results.append({
        'filename': fn,
        'mod_id': m.get('mod_id'),
        'name': m.get('display_name'),
        'excluded': is_ex,
        'reason': reason,
        'category': cat,
        'is_disabled': m.get('is_disabled', False),
        'is_backup': m.get('is_backup', False),
        'has_data': m.get('has_data', False)
    })

excluded = [x for x in results if x['excluded']]
included = [x for x in results if not x['excluded']]

print(f"Total mods audited: {len(results)}")
print(f"Excluded from server pack: {len(excluded)}")
print(f"Included on server: {len(included)}")

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\classification_results.json', 'w', encoding='utf-8') as out:
    json.dump({'excluded': excluded, 'included': included}, out, indent=2)

print("Classification results saved.")
