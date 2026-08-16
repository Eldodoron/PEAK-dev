import os

minecraft_dir = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft"

print("Top level entries in minecraft/:")
for entry in os.listdir(minecraft_dir):
    full_p = os.path.join(minecraft_dir, entry)
    is_dir = os.path.isdir(full_p)
    print(f"  {'[DIR]' if is_dir else '[FILE]'} {entry}")

# Let's inspect scratch/
scratch_dir = os.path.join(minecraft_dir, "scratch")
if os.path.exists(scratch_dir):
    print("\nEntries in scratch/:")
    for root, dirs, files in os.walk(scratch_dir):
        for f in files:
            print(" ", os.path.relpath(os.path.join(root, f), minecraft_dir))

# Let's check global_packs/
gp_dir = os.path.join(minecraft_dir, "global_packs")
if os.path.exists(gp_dir):
    print("\nEntries in global_packs/:")
    for root, dirs, files in os.walk(gp_dir):
        for f in files:
            print(" ", os.path.relpath(os.path.join(root, f), minecraft_dir))
