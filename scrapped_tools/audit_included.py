import json
import os

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\classification_results.json', 'r', encoding='utf-8') as f:
    res = json.load(f)

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\precise_mod_info.json', 'r', encoding='utf-8') as f:
    info = json.load(f)

included = res['included']
print(f"Auditing {len(included)} included mods for any overlooked client-side mods...")

suspicious_terms = [
    'render', 'hud', 'gui', 'screen', 'client', 'visual', 'sound', 'audio',
    'anim', 'camera', 'fov', 'tooltip', 'particle', 'texture', 'model', 'cull',
    'optimi', 'fps', 'key', 'chat', 'toast', 'cursor', 'menu'
]

flagged = []
for m in included:
    fn = m['filename']
    det = info.get(fn, {})
    mid = (det.get('mod_id') or '').lower()
    name = (det.get('display_name') or '').lower()
    desc = (det.get('description') or '').lower()
    
    matches = []
    for term in suspicious_terms:
        if term in fn.lower():
            matches.append(f"fn:{term}")
        if term in mid:
            matches.append(f"id:{term}")
        if term in name:
            matches.append(f"name:{term}")
        if term in desc:
            matches.append(f"desc:{term}")
            
    if matches:
        flagged.append({
            'filename': fn,
            'mod_id': mid,
            'name': det.get('display_name'),
            'matches': list(set(matches)),
            'data': det.get('has_data'),
            'data_dirs': det.get('data_dirs', []),
            'client_mixins': det.get('client_mixins_count', 0),
            'server_mixins': det.get('server_mixins_count', 0),
            'common_mixins': det.get('common_mixins_count', 0),
            'desc': desc[:100]
        })

print(f"Flagged {len(flagged)} potentially suspicious included mods:")
for f in sorted(flagged, key=lambda x: x['filename'].lower()):
    print(f"[{f['filename']}] ({f['mod_id']}) data={f['data']} ({f['data_dirs']}) c_mix={f['client_mixins']} comm_mix={f['common_mixins']}")
    print(f"   Matches: {', '.join(f['matches'])}")
    print(f"   Desc: {f['desc']}")
