import os

script_dir = os.path.dirname(__file__)
saves_dir = os.path.abspath(os.path.join(script_dir, "..", "minecraft", "saves"))

matches = []
for root, dirs, files in os.walk(saves_dir):
    if "serverconfig" in root:
        for f in files:
            matches.append(os.path.join(root, f))

print("Found server configs:")
for m in matches:
    print(m)
