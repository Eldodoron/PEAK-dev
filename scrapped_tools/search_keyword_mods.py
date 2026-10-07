import os
import zipfile
import tomllib
import json
import sys
sys.path.append('.')
from scrapped_tools.audit_curated_excluded import EXCLUDED_FILENAMES

mods_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\mods"
all_files = sorted([f for f in os.listdir(mods_dir) if f.endswith('.jar') or '.jar.' in f])

keywords = [
    'ui', 'hud', 'gui', 'screen', 'menu', 'font', 'text', 'tooltip', 'bar', 'overlay',
    'chat', 'sound', 'audio', 'voice', 'music', 'camera', 'zoom', 'view', 'perspective',
    'anim', 'motion', 'particle', 'beam', 'light', 'glow', 'cull', 'opti', 'fps', 'shader',
    'texture', 'jem', 'cursor', 'key', 'bind', 'input', 'mouse', 'scroll', 'toast', 'notify',
    'border', 'rarity', 'info', 'desc'
]

matches = []
for fn in all_files:
    if fn in EXCLUDED_FILENAMES:
        continue
    fn_lower = fn.lower()
    matched_kws = [kw for kw in keywords if kw in fn_lower]
    if matched_kws:
        matches.append((fn, matched_kws))

print(f"Total keyword matches not currently excluded: {len(matches)}")
for fn, kws in matches:
    print(f"  {fn} -> {kws}")
