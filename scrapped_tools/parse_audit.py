import json
import os
import re

json_path = r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\scrapped_tools\ironwood_precision_audit.json"
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Deduplicate and extract clean recipe info
recipes = {}

for entry in data:
    context = entry['context']
    file_rel = os.path.relpath(entry['file'], r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev")
    line = entry['line']
    
    # Try to extract the recipe output
    # Patterns like: event.shaped('output', ...), event.shapeless('output', ...), event.recipes.create...('output', ...)
    output_match = re.search(r"event\.(?:shaped|shapeless|recipes\.[a-z.]+)\(\s*['\"]([^'\"]+)['\"]", context)
    if not output_match:
        output_match = re.search(r"['\"]output['\"]\s*:\s*['\"]([^'\"]+)['\"]", context)
    if not output_match:
        output_match = re.search(r"event\.remove\(\s*\{\s*output\s*:\s*['\"]([^'\"]+)['\"]", context)
    
    output = output_match.group(1) if output_match else "Unknown / Contextual"
    
    # Find comments explaining the recipe
    comment_lines = [l.strip() for l in context.split('\n') if l.strip().startswith('//') or l.strip().startswith('#')]
    comment_summary = " ".join([c.lstrip('/# ') for c in comment_lines[-5:]]) if comment_lines else "No comment"
    
    key = f"{file_rel}:{line}:{output}"
    recipes[key] = {
        'file': file_rel,
        'line': line,
        'output': output,
        'type': entry['type'],
        'matched_line': entry['matched_line'],
        'context': context,
        'comment': comment_summary
    }

print(f"Total unique recipe occurrences: {len(recipes)}")

# Group by file and type
grouped = {}
for k, v in recipes.items():
    f = v['file']
    if f not in grouped:
        grouped[f] = []
    grouped[f].append(v)

for f, items in grouped.items():
    print(f"\n==========================================")
    print(f"FILE: {f}")
    print(f"==========================================")
    for it in items:
        print(f"  Line {it['line']} | Output: {it['output']} | Type: {it['type']}")
        print(f"    Line content: {it['matched_line']}")
