import json

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\deep_scan.json', 'r', encoding='utf-8') as f:
    all_mods = json.load(f)

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\candidates.json', 'r', encoding='utf-8') as f:
    candidates = json.load(f)

candidate_files = set(x['filename'] for x in candidates)
remaining = [v for k, v in all_mods.items() if k not in candidate_files]

print(f"Remaining non-candidate mods: {len(remaining)}")

# Print filenames of remaining
with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\remaining_mods.txt', 'w', encoding='utf-8') as out:
    for m in sorted(remaining, key=lambda x: x['filename'].lower()):
        out.write(f"{m['filename']} | id: {m.get('mod_id')} | name: {m.get('display_name')}\n")

print("Wrote remaining_mods.txt")
