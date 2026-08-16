import os

ROOT_DIR = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft"

with open(r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\.agents\explorer_3\py_scripts_summary.txt", 'w', encoding='utf-8') as out:
    for root, dirs, files in os.walk(ROOT_DIR):
        if 'scratch' in root or '.git' in root:
            continue
        for f in sorted(files):
            if f.endswith('.py'):
                fpath = os.path.join(root, f)
                rel_path = os.path.relpath(fpath, ROOT_DIR)
                with open(fpath, 'r', encoding='utf-8', errors='replace') as pyf:
                    content = pyf.read()
                lines = content.splitlines()
                out.write(f"=== {rel_path} ({len(lines)} lines) ===\n")
                out.write("\n".join(lines[:15]))
                out.write("\n\n")

print("Wrote py_scripts_summary.txt")
