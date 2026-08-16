import os

kubejs_dir = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs"
out_file = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\.agents\explorer_survey_2\all_headers.txt"

with open(out_file, 'w', encoding='utf-8') as out:
    for root, dirs, files in sorted(os.walk(kubejs_dir)):
        for f in sorted(files):
            if f.endswith('.js'):
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, kubejs_dir)
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as file_obj:
                    lines = file_obj.readlines()
                
                header = "".join(lines[:10]).strip()
                out.write(f"=== {rel_path} ===\n")
                out.write(header + "\n")
                out.write("-" * 40 + "\n\n")

print(f"Wrote all headers to {out_file}")
