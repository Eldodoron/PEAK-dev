import os
import json

brain_dir = r"C:\Users\chris\.gemini\antigravity\brain"

for root, dirs, files in os.walk(brain_dir):
    if "transcript.jsonl" in files:
        tpath = os.path.join(root, "transcript.jsonl")
        try:
            with open(tpath, "r", encoding="utf-8") as f:
                for line in f:
                    if "sophisticated" in line.lower() or "3.26" in line:
                        try:
                            d = json.loads(line)
                            c = d.get("content", "")
                            if any(k in c.lower() for k in ["3.26", "downgrade", "upgrade", "crash", "compat", "soph"]):
                                print(f"Found in {root}:")
                                for sub in c.splitlines():
                                    if any(k in sub.lower() for k in ["3.26", "soph", "backpack", "compat"]):
                                        print("  ", sub[:140])
                        except Exception:
                            pass
        except Exception:
            pass
