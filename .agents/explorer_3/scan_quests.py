import os
import re

QUESTS_DIR = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\config\ftbquests"

if os.path.exists(QUESTS_DIR):
    for root, dirs, files in os.walk(QUESTS_DIR):
        for f in files:
            if f.endswith('.snbt'):
                fpath = os.path.join(root, f)
                with open(fpath, 'r', encoding='utf-8', errors='replace') as qf:
                    text = qf.read()
                
                # Check for AI indicators or comments
                for pat in [r'(?i)chatgpt', r'(?i)openai', r'(?i)claude', r'(?i)antigravity', r'(?i)prompt', r'(?i)generated', r'(Ã¢â‚¬â€|Ã¢â€ â€™|â€”|â†’)']:
                    matches = list(re.finditer(pat, text))
                    if matches:
                        print(f"Match in {f} for {pat}: {len(matches)} occurrences")
                        for m in matches[:3]:
                            start = max(0, m.start() - 30)
                            end = min(len(text), m.end() + 30)
                            snippet = text[start:end].replace('\n', ' ')
                            print(f"   Snippet: ...{snippet}...")
else:
    print("Quests dir not found")
