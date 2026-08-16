import os
import glob

for filepath in glob.glob('*.js'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '"transitionalItem":' in content:
        new_content = content.replace('"transitionalItem":', '"transitional_item":')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed transitionalItem in {filepath}")
