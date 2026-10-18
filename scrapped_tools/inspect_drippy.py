import zipfile
import re

with zipfile.ZipFile("minecraft/mods/drippyloadingscreen_neoforge_3.1.5_MC_1.21.1.jar") as z:
    for name in sorted(z.namelist()):
        if name.endswith(".class") and not "$" in name:
            print(name)
