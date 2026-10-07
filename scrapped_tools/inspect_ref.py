import zipfile
import glob
import os
from PIL import Image

def find_matching_textures():
    jars = glob.glob("minecraft/mods/*.jar")
    # Let's search for textures with red/orange plus/cross in gray border
    # Or specifically inspect Ancient Remnant, Cataclysm, etc.
    for j in jars:
        bname = os.path.basename(j).lower()
        if "cataclysm" in bname:
            with zipfile.ZipFile(j, "r") as z:
                for name in z.namelist():
                    if ("ancient" in name or "remnant" in name or "core" in name or "monstrous" in name) and name.endswith(".png"):
                        print(f"Cataclysm: {name}")

if __name__ == '__main__':
    find_matching_textures()
