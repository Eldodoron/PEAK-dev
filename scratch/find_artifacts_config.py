import os

instance_path = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft"

matches = []
for root, dirs, files in os.walk(instance_path):
    # Skip huge folders to avoid slow runs
    if ".mixin.out" in root or "mods" in root or "logs" in root or "kubejs" in root:
        continue
    for f in files:
        if "artifacts" in f.lower() or "mimic" in f.lower():
            matches.append(os.path.join(root, f))

print("Matching files:")
for m in matches:
    print(m)
