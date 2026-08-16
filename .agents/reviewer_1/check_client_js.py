import os

minecraft_dir = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft"
for root, dirs, files in os.walk(os.path.join(minecraft_dir, "kubejs", "client_scripts")):
    for file in files:
        if file.endswith(".js"):
            full_p = os.path.join(root, file)
            rel_p = os.path.relpath(full_p, minecraft_dir).replace("\\", "/")
            with open(full_p, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
            print(f"{rel_p}: {len(lines)} lines | Header: {[l.strip() for l in lines[:2] if l.strip()]}")
