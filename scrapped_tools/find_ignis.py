import zipfile, glob, os

jars = glob.glob("minecraft/mods/*Cataclysm*3.27*.jar")
if jars:
    with zipfile.ZipFile(jars[0], "r") as z:
        for name in z.namelist():
            if "ignis" in name.lower() and name.endswith(".png"):
                print(name)
