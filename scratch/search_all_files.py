import os

script_dir = os.path.dirname(__file__)
config_dir = os.path.abspath(os.path.join(script_dir, "..", "minecraft", "config"))

matches = []
for root, dirs, files in os.walk(config_dir):
    for f in files:
        if f.endswith((".toml", ".json", ".json5", ".cfg", ".yml", ".yaml")):
            path = os.path.join(root, f)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as file:
                    content = file.read()
                    if "mimic" in content.lower() or "artifacts" in content.lower():
                        matches.append(path)
            except Exception:
                pass

print("Matching config files:")
for m in matches:
    print(m)
