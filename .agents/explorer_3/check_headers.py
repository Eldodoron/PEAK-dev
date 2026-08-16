import os

KUBEJS_DIR = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs"

with open(r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\.agents\explorer_3\headers_summary.txt", 'w', encoding='utf-8') as out:
    for subdir in ['server_scripts', 'startup_scripts', 'client_scripts']:
        full_sub = os.path.join(KUBEJS_DIR, subdir)
        if not os.path.exists(full_sub):
            continue
        for fname in sorted(os.listdir(full_sub)):
            fpath = os.path.join(full_sub, fname)
            if os.path.isfile(fpath) and fname.endswith('.js'):
                with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                    lines = [f.readline() for _ in range(8)]
                header = "".join(lines).strip().replace('\n', ' \\ ')
                out.write(f"{subdir}/{fname} : {header}\n\n")

print("Wrote headers_summary.txt")
