import os
import re
import json

base_dir = r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft"
kubejs_dir = os.path.join(base_dir, "kubejs", "server_scripts")
datapacks_dir = os.path.join(base_dir, "datapacks")
paxi_dir = os.path.join(base_dir, "config", "paxi", "datapacks")

def scan_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    lines = content.split('\n')
    results = []
    
    # We want to find recipes mentioning ironwood or precision_mechanism
    patterns = [
        ('ironwood', r'twilightforest:ironwood[a-zA-Z0-9_]*'),
        ('precision_mechanism', r'create:precision_mechanism')
    ]
    
    for i, line in enumerate(lines):
        for tag, pat in patterns:
            if re.search(pat, line, re.IGNORECASE):
                # find surrounding context (recipe block)
                start = max(0, i - 10)
                end = min(len(lines), i + 15)
                block = "\n".join(lines[start:end])
                results.append({
                    'file': filepath,
                    'line': i + 1,
                    'type': tag,
                    'matched_line': line.strip(),
                    'context': block
                })
    return results

all_results = []
for root, dirs, files in os.walk(kubejs_dir):
    for f in files:
        if f.endswith('.js') or f.endswith('.json'):
            all_results.extend(scan_file(os.path.join(root, f)))

if os.path.exists(datapacks_dir):
    for root, dirs, files in os.walk(datapacks_dir):
        for f in files:
            if f.endswith('.json'):
                all_results.extend(scan_file(os.path.join(root, f)))

if os.path.exists(paxi_dir):
    for root, dirs, files in os.walk(paxi_dir):
        for f in files:
            if f.endswith('.json'):
                all_results.extend(scan_file(os.path.join(root, f)))

out_path = r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\scrapped_tools\ironwood_precision_audit.json"
with open(out_path, 'w', encoding='utf-8') as out:
    json.dump(all_results, out, indent=2)

print(f"Audit finished. Found {len(all_results)} occurrences.")
