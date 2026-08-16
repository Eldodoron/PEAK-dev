import os
import json
import re

ASSETS_DIR = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs\assets"

asset_matches = []

for root, dirs, files in os.walk(ASSETS_DIR):
    for f in files:
        path = os.path.join(root, f)
        rel = os.path.relpath(path, ASSETS_DIR)
        ext = os.path.splitext(f)[1].lower()
        if ext in ['.json', '.mcmeta', '.txt', '.lang']:
            with open(path, 'r', encoding='utf-8', errors='replace') as fp:
                text = fp.read()
            
            for kw in ['antigravity', 'chatgpt', 'openai', 'claude', 'prompt', 'credit', 'author', 'description', 'fixed', 'generated', 'blockbench']:
                if re.search(rf"\b{kw}\b", text, re.IGNORECASE):
                    asset_matches.append((rel, kw, path))

print(f"Found {len(asset_matches)} matches in assets/ text files:")
for rel, kw, path in asset_matches:
    print(f"  {rel} -> matched '{kw}'")
