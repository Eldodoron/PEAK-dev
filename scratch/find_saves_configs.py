import os

saves_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\saves"

matches = []
for root, dirs, files in os.walk(saves_dir):
    if "serverconfig" in root:
        for f in files:
            matches.append(os.path.join(root, f))

print("Found server configs:")
for m in matches:
    print(m)
