import os
import re

kubejs_dir = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs"

js_files = []
for root, dirs, files in os.walk(kubejs_dir):
    for f in files:
        if f.endswith('.js'):
            js_files.append(os.path.join(root, f))

print(f"Total JS files: {len(js_files)}")

all_comments = []

for filepath in sorted(js_files):
    rel_path = os.path.relpath(filepath, kubejs_dir)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    in_block_comment = False
    block_start_line = 0
    block_lines = []

    for idx, line in enumerate(lines):
        line_num = idx + 1
        stripped = line.strip()
        
        # Check single line comments
        if '//' in line:
            # simple check
            comment_part = line[line.index('//'):].strip()
            all_comments.append({
                'file': rel_path,
                'line': line_num,
                'type': 'single',
                'text': comment_part,
                'full_line': stripped
            })
        
        # Check block comments /* */
        if '/*' in line:
            in_block_comment = True
            block_start_line = line_num
            block_lines = [line]
            if '*/' in line:
                in_block_comment = False
                all_comments.append({
                    'file': rel_path,
                    'line': block_start_line,
                    'type': 'block',
                    'text': "".join(block_lines).strip(),
                    'full_line': stripped
                })
        elif in_block_comment:
            block_lines.append(line)
            if '*/' in line:
                in_block_comment = False
                all_comments.append({
                    'file': rel_path,
                    'line': block_start_line,
                    'type': 'block',
                    'text': "".join(block_lines).strip(),
                    'full_line': stripped
                })

print(f"Total comments found: {len(all_comments)}")

# Write all comments to an analysis file for review
out_path = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\.agents\explorer_survey_2\all_comments_dump.txt"
with open(out_path, 'w', encoding='utf-8') as out:
    for c in all_comments:
        out.write(f"[{c['file']}:{c['line']}] {c['text']}\n")

print(f"Wrote all comments to {out_path}")
