import zipfile, io, glob
from PIL import Image

jars = glob.glob("minecraft/mods/*Cataclysm*3.27*.jar")
if jars:
    with zipfile.ZipFile(jars[0], "r") as z:
        for item in ["assets/cataclysm/textures/item/ancient_metal_ingot.png", "assets/cataclysm/textures/block/ancient_metal_block.png"]:
            im = Image.open(io.BytesIO(z.read(item)))
            print(item, im.size)
            colors = sorted(list(set(im.getdata())), key=lambda c: (c[3], c[0]+c[1]+c[2]))
            print("Colors:")
            for c in colors:
                if c[3] > 0:
                    print(f"  #{c[0]:02X}{c[1]:02X}{c[2]:02X} {c}")
