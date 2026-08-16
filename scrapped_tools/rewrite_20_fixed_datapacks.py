import re
import json

file_path = 'c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/kubejs/server_scripts/20_fixed_datapacks.js'
out_path = 'c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/minecraft/kubejs/server_scripts/20_fixed_datapacks.js'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []

def format_ingredient(ing):
    if "item" in ing:
        return f"'{ing['item']}'"
    elif "tag" in ing:
        return f"'#{ing['tag']}'"
    elif "fluid" in ing:
        fluid = ing["fluid"]
        amount = ing.get("amount", 1000)
        return f"Fluid.of('{fluid}', {amount})"
    return f"'{json.dumps(ing)}'"

def format_result(res):
    if "item" in res:
        if isinstance(res["item"], dict) and "id" in res["item"]:
            item = res["item"]["id"]
            count = res.get("count", res["item"].get("count", 1))
            return f"'{count}x {item}'"
        else:
            item = res["item"]
            count = res.get("count", 1)
            return f"'{count}x {item}'"
    elif "id" in res:
        item = res["id"]
        count = res.get("count", 1)
        return f"'{count}x {item}'"
    elif "fluid" in res:
        fluid = res["fluid"]
        amount = res.get("amount", 1000)
        return f"Fluid.of('{fluid}', {amount})"
    return f"'{json.dumps(res)}'"

for line in lines:
    if not line.strip().startswith("event.custom({"):
        new_lines.append(line)
        continue
    
    # Extract the JSON inside event.custom(...)
    match = re.search(r"event\.custom\((.*?)\)\.id\('(.*?)'\);", line)
    if not match:
        new_lines.append(line)
        continue
        
    json_str = match.group(1)
    recipe_id = match.group(2)
    
    try:
        obj = json.loads(json_str)
        rtype = obj.get("type", "")
        
        if rtype.startswith("create:"):
            # It's a create recipe, try to use KubeJS native builder
            method = rtype.replace("create:", "")
            if method in ["mixing", "compacting", "crushing", "cutting", "pressing", "filling", "emptying", "deploying"]:
                ingredients = obj.get("ingredients", [])
                results = obj.get("results", [])
                
                # Format ingredients array
                ing_str = "[" + ", ".join([format_ingredient(i) for i in ingredients]) + "]"
                if len(ingredients) == 1:
                    ing_str = format_ingredient(ingredients[0])
                    
                # Format results array
                res_str = "[" + ", ".join([format_result(r) for r in results]) + "]"
                if len(results) == 1:
                    res_str = format_result(results[0])
                
                builder = f"event.recipes.create.{method}({res_str}, {ing_str})"
                
                # add heat
                heat = obj.get("heat_requirement", obj.get("heatRequirement"))
                if heat == "heated":
                    builder += ".heated()"
                elif heat == "superheated":
                    builder += ".superheated()"
                    
                # add processing time
                ptime = obj.get("processingTime", obj.get("processing_time"))
                if ptime:
                    builder += f".processingTime({ptime})"
                
                builder += f".id('{recipe_id}')"
                new_lines.append(f"    {builder}\n")
                continue
            
            # Sequenced Assembly uses custom builder, harder to parse natively.
            # We will just fix the fluid tags inside event.custom
            # Fallthrough to event.custom fixes
        
        # Avaritia fix
        if rtype == "avaritia:extreme_smithing":
            if "addition" in obj and isinstance(obj["addition"], list):
                if len(obj["addition"]) > 0:
                    obj["addition"] = obj["addition"][0]
                else:
                    obj["addition"] = {"item": "minecraft:air"}
            
        # Fix all fluid tags and ids generically in the object
        def fix_fluids(d):
            if isinstance(d, dict):
                if "fluid" in d:
                    fval = d["fluid"]
                    if fval.startswith("#"):
                        # Convert to tag
                        d["tag"] = fval[1:]
                        del d["fluid"]
                if "results" in obj or rtype.startswith("create:"):
                    # Create results sometimes use fluid, but KubeJS 1.21 might want id for outputs
                    if "fluid" in d and "amount" in d and "id" not in d:
                        # Only fix results, this is tricky. Just let Fluid.of handle it if possible.
                        pass
                        
                for k, v in d.items():
                    fix_fluids(v)
            elif isinstance(d, list):
                for item in d:
                    fix_fluids(item)
                    
        fix_fluids(obj)
        
        # Write back fixed event.custom
        new_lines.append(f"    event.custom({json.dumps(obj)}).id('{recipe_id}');\n")

    except Exception as e:
        # If parsing fails, just keep the line
        print(f"Error parsing line: {e}")
        new_lines.append(line)

with open(out_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Finished rewriting 20_fixed_datapacks.js")
