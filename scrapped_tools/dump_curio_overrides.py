import zipfile, json

with zipfile.ZipFile('minecraft/mods/apothic_compats-0.2.4.2.jar') as z:
    for n in z.namelist():
        if n.startswith('data/apothic_compats/rarity_override/apothic_compats/') and n.endswith('.json'):
            cat = n.split('/')[-1]
            data = json.loads(z.read(n).decode('utf-8'))
            print(f"=== {cat} ===")
            print(json.dumps(data, indent=2)[:350])
