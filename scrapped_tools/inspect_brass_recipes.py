import json

with open(r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\scrapped_tools\brass_melting_recipes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    mod = item['mod']
    fname = item['file']
    c = item['content']
    rtype = c.get('type', 'unknown')
    results = c.get('results', c.get('result', 'unknown'))
    ingredients = c.get('ingredients', 'unknown')
    heat = c.get('heatRequirement', 'none')
    print(f"MOD: {mod} | FILE: {fname}")
    print(f"  Type: {rtype} | Heat: {heat}")
    print(f"  Ingredients: {ingredients}")
    print(f"  Result: {results}\n")
