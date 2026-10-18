import zipfile, json

with zipfile.ZipFile('minecraft/mods/nadir-1.0.0.jar') as z:
    for r in ['worthless', 'cataclysmic', 'divine', 'esoteric', 'stellar']:
        path = f'data/nadir/rarities/{r}.json'
        data = json.loads(z.read(path).decode('utf-8'))
        rules = data.get('rules', [])
        print(f"\n=== {r}.json rules ({len(rules)}) ===")
        for rule in rules:
            print(" ", rule)
