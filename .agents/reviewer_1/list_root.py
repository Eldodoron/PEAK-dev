import os

minecraft_dir = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft"
entries = os.listdir(minecraft_dir)
files = [e for e in entries if os.path.isfile(os.path.join(minecraft_dir, e))]
dirs = [e for e in entries if os.path.isdir(os.path.join(minecraft_dir, e))]

print("Files in minecraft/ root:")
for f in sorted(files):
    sz = os.path.getsize(os.path.join(minecraft_dir, f))
    print(f"  {f} ({sz} bytes)")

print("\nDirectories in minecraft/ root:")
for d in sorted(dirs):
    print(f"  {d}/")
