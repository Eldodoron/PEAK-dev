import os
import json

base_dir = "c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/scratch/mod_extraction/data"
output_script = []

def parse_ingredient(ing):
    if isinstance(ing, list):
        return str(ing)
        
    if "item" in ing:
        return f"'{ing['item']}'"
    elif "tag" in ing:
        return f"'#{ing['tag']}'"
    elif "fluid" in ing or "fluid_tag" in ing or ing.get("type") in ["fluid_stack", "fluid_tag", "neoforge:fluid", "neoforge:fluid_tag"]:
        fluid = ing.get("fluid") or ing.get("fluid_tag") or ""
        amt = ing.get("amount", 250)
        if ing.get("type") == "fluid_tag" or "fluid_tag" in ing:
            return f"Fluid.of('#{fluid.replace('c:', 'c:')}', {amt})" 
        else:
            return f"Fluid.of('{fluid}', {amt})"
    
    if isinstance(ing, list):
        # KubeJS allows array of ingredients as alternatives, but in Create mixing it's usually just multiple ingredients.
        # If it's a list, it usually means standard alternatives (like NeoForge ingredient array).
        return str(ing)
        
    return str(ing)

def parse_result(res):
    if "id" in res:
        amt = res.get("amount", res.get("count", 1))
        if amt > 1:
            return f"'{amt}x {res['id']}'"
        return f"'{res['id']}'"
    elif "item" in res:
        amt = res.get("count", 1)
        if amt > 1:
            return f"'{amt}x {res['item']}'"
        return f"'{res['item']}'"
    elif "fluid" in res:
        amt = res.get("amount", 250)
        return f"Fluid.of('{res['fluid']}', {amt})"
    return str(res)

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".json"):
            path = os.path.join(root, file)
            path_str = path.replace('\\', '/')
            if "/data/" not in path_str:
                continue
            
            mod_id = path_str.split("/data/")[-1].split("/")[0]
            
            try:
                rel_path = path_str.split(f"/data/{mod_id}/recipe/")[-1]
            except Exception:
                continue
                
            recipe_id = f"{mod_id}:{rel_path.replace('.json', '')}"
            
            with open(path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except:
                    continue
                
                recipe_type = data.get("type", "")
                if recipe_type.startswith("create:"):
                    method = recipe_type.replace("create:", "")
                    
                    ingredients = []
                    if "ingredients" in data:
                        for ing in data["ingredients"]:
                            ingredients.append(parse_ingredient(ing))
                    
                    results = []
                    if "results" in data:
                        for res in data["results"]:
                            results.append(parse_result(res))
                    
                    heat = ""
                    if "heat_requirement" in data:
                        if data["heat_requirement"] == "heated":
                            heat = ".heated()"
                        elif data["heat_requirement"] == "superheated":
                            heat = ".superheated()"
                    
                    results_str = f"[{', '.join(results)}]" if len(results) > 1 else (results[0] if len(results) == 1 else "[]")
                    ingredients_str = f"[{', '.join(ingredients)}]"
                    
                    kubejs_line = f"    event.recipes.create.{method}({results_str}, {ingredients_str}){heat}.id('{recipe_id}')"
                    output_script.append(kubejs_line)

with open("c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/kubejs/server_scripts/00_recipe_error_suppressor.js", 'w', encoding='utf-8') as out:
    out.write("// Archivo generado automáticamente para corregir las recetas rotas de Create en 1.21.1\n")
    out.write("ServerEvents.recipes(event => {\n")
    out.write("\n".join(output_script))
    out.write("\n})\n")

print(f"Generated {len(output_script)} recipes.")
