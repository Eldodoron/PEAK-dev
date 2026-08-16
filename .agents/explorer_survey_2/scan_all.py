import os

kubejs_dir = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs"

for root, dirs, files in sorted(os.walk(kubejs_dir)):
    for f in sorted(files):
        if f.endswith('.js'):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, kubejs_dir)
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as file_obj:
                lines = file_obj.readlines()
            
            # Print file header if it has interesting comments
            interesting_lines = []
            for idx, line in enumerate(lines):
                s = line.strip()
                if s.startswith('//') or s.startswith('/*') or '/*' in s:
                    interesting_lines.append((idx + 1, s))
            
            # Let's inspect
            # We can write all interesting comments to a report
