import os
import sys
import re
import subprocess
import json

sys.stdout.reconfigure(encoding='utf-8')

def audit_ftbquests_all():
    ftb_dir = r'minecraft/config/ftbquests'
    print(f"=== Auditing ALL files in {ftb_dir} ===")
    buzzwords = ['surgical', 'cornerstone', 'unleash', 'meticulous', 'mastery', 'delv', 'embark']
    
    amp_violations = []
    buzz_violations = []
    snbt_files = []

    for root, _, files in os.walk(ftb_dir):
        for f in files:
            if f.endswith('.snbt'):
                p = os.path.join(root, f)
                snbt_files.append(p)
                with open(p, 'r', encoding='utf-8', errors='replace') as fp:
                    for idx, line in enumerate(fp, 1):
                        if '& ' in line:
                            amp_violations.append((p, idx, line.strip()))
                        clean = re.sub(r'&[0-9a-fk-orA-FK-OR#]', '', line)
                        for b in buzzwords:
                            if re.search(r'\b' + b + r'\w*', clean, re.I):
                                buzz_violations.append((p, idx, b, line.strip()))

    print(f"Total .snbt files inspected: {len(snbt_files)}")
    print(f"Total literal '& ' across all .snbt files: {len(amp_violations)}")
    print(f"Total core buzzword hits across all .snbt files: {len(buzz_violations)}")

def audit_block_models():
    print("\n=== Auditing Block Models (M1) ===")
    assets_dir = r'minecraft/kubejs/assets'
    blockbench_hits = []
    zanderest_hits = []
    invalid_json = []

    for root, _, files in os.walk(assets_dir):
        for f in files:
            if f.endswith('.json'):
                p = os.path.join(root, f)
                try:
                    with open(p, 'r', encoding='utf-8') as fp:
                        content = fp.read()
                        data = json.loads(content)
                        if 'Made with Blockbench' in content:
                            blockbench_hits.append(p)
                        if 'zanderest' in content:
                            zanderest_hits.append(p)
                except Exception as e:
                    invalid_json.append((p, str(e)))

    print(f"Blockbench occurrences in {assets_dir}: {len(blockbench_hits)}")
    print(f"Zanderest credits preserved: {len(zanderest_hits)}")
    print(f"Invalid JSON files: {len(invalid_json)}")

def audit_integrity_checks():
    print("\n=== Integrity & Adversarial Checks ===")
    # 1. Check for any dummy implementations, TODO, FIXME, mock, stub
    kubejs_dir = r'minecraft/kubejs'
    stubs = []
    for root, _, files in os.walk(kubejs_dir):
        for f in files:
            if f.endswith('.js'):
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8', errors='replace') as fp:
                    for idx, line in enumerate(fp, 1):
                        if re.search(r'\b(TODO|FIXME|XXX|HACK|DUMMY|STUB|PLACEHOLDER)\b', line):
                            stubs.append((p, idx, line.strip()))
    print(f"KubeJS developer stubs/FIXMEs count: {len(stubs)}")
    for s in stubs:
        print(f"   {s[0]}:{s[1]} -> {s[2]}")

if __name__ == '__main__':
    audit_ftbquests_all()
    audit_block_models()
    audit_integrity_checks()
