import zipfile
import json
import os

jar_path = r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\mods\createmetalwork-2.0.0.jar"

with zipfile.ZipFile(jar_path, 'r') as z:
    for name in z.namelist():
        if 'recipe/' in name and name.endswith('.json'):
            data = json.loads(z.read(name).decode('utf-8'))
            if data.get('type') == 'create:mixing':
                ings = data.get('ingredients', [])
                results = data.get('results', [])
                print(f"RECIPE: {name}")
                print(f"  Inputs: {ings}")
                print(f"  Outputs: {results}")
                print(f"  Heat: {data.get('heat_requirement')}\n")
