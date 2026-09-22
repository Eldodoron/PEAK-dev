import zipfile

with zipfile.ZipFile("minecraft/mods/sophisticatedbackpacks-1.21.1-3.26.3.2158.jar") as zf:
    print("Recipe serializers in SB 3.26:")
    for n in zf.namelist():
        if "recipe" in n.lower():
            print(" ", n)

with zipfile.ZipFile("minecraft/mods/sophisticatedcore-1.21.1-1.5.1.2341.jar") as zf:
    print("\nRecipe classes in SC 1.5:")
    for n in zf.namelist():
        if "recipe" in n.lower() or "condition" in n.lower():
            print(" ", n)
