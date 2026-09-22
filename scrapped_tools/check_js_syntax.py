import os
import subprocess

kubejs_dir = 'minecraft/kubejs'
syntax_errors = []

for root, dirs, files in os.walk(kubejs_dir):
    for f in files:
        if f.endswith('.js'):
            fp = os.path.join(root, f)
            res = subprocess.run(['node', '--check', fp], capture_output=True, text=True)
            if res.returncode != 0:
                syntax_errors.append((f, res.stderr.strip()))

if syntax_errors:
    print(f'Found {len(syntax_errors)} SYNTAX ERRORS:')
    for f, err in syntax_errors:
        print(f'=== {f} ===')
        print(err)
else:
    print('ALL KubeJS scripts passed syntax validation with ZERO syntax errors!')
