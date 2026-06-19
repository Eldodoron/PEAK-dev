import os
import re

directory = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\config\morerelics\relics"

for filename in os.listdir(directory):
    if filename.endswith(".yaml"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        def revert_weight(match):
            original_weight = int(match.group(1))
            new_weight = original_weight * 3
            return f"weight: {new_weight}"
        
        new_content = re.sub(r'weight:\s*(\d+)', revert_weight, content)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Reverted {filename}")
        else:
            print(f"No changes in {filename}")

print("Done reverting weights.")
