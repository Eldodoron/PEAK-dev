import os
import json
import re

DATA_DIR = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs\data"

json_matches = []

for root, dirs, files in os.walk(DATA_DIR):
    for f in files:
        if f.endswith('.json'):
            path = os.path.join(root, f)
            rel = os.path.relpath(path, DATA_DIR)
            with open(path, 'r', encoding='utf-8', errors='replace') as fp:
                text = fp.read()
            
            # Check for keywords
            for kw in ['antigravity', 'chatgpt', 'openai', 'claude', 'prompt', 'credit', 'author', 'description', 'fixed', 'generated']:
                if re.search(rf"\b{kw}\b", text, re.IGNORECASE):
                    json_matches.append((rel, kw, path))

print(f"Found {len(json_matches)} matches in data/ jsons:")
for rel, kw, path in json_matches:
    print(f"  {rel} -> matched '{kw}'")
