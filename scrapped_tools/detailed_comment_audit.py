import os
import sys
import re
import json

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r"C:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev"
KUBEJS_DIR = os.path.join(BASE_DIR, "minecraft", "kubejs")

# Targeted regex for conversational editorializing, AI inner monologue, first person dev commentary
CONV_PATTERNS = [
    # First-person dev
    (re.compile(r"\b(we|we're|we've|we'll|our|ours)\b", re.I), "FIRST_PERSON_PLURAL"),
    (re.compile(r"\bI\b\s+(am|was|have|had|will|would|can|could|should|think|thought|noticed|found|added|removed|fixed|created|checked|want|wanted|suggest|recommend|need|tried)", re.I), "FIRST_PERSON_SINGULAR"),
    # Conversational phrases & design editorializing
    (re.compile(r"\b(basically|actually|honestly|frankly|obviously|naturally)\b", re.I), "CONVERSATIONAL_MODIFIER"),
    (re.compile(r"\b(feel earned|worth crafting|insane price|cheap shortcut)\b", re.I), "EDITORIAL_OPINION"),
    (re.compile(r"\b(you can't skip|you need to|you must explore|you need)\b", re.I), "SECOND_PERSON_DIRECTIVE"),
    (re.compile(r"\b(hard to automate|died with them for a reason|they shamble|ensure we don't)\b", re.I), "INNER_RATIONALE"),
    (re.compile(r"\b(wait\s*[,.]|note to self|just in case|leave item in grid!)\b", re.I), "DEV_SELF_TALK")
]

results = {}

for root, dirs, files in os.walk(KUBEJS_DIR):
    for f in sorted(files):
        if f.endswith('.js'):
            p = os.path.join(root, f)
            rel = os.path.relpath(p, BASE_DIR).replace('\\', '/')
            with open(p, 'r', encoding='utf-8', errors='replace') as fp:
                for idx, line in enumerate(fp, 1):
                    s = line.strip()
                    comment = ""
                    if '//' in s:
                        comment = s[s.index('//'):].strip()
                    elif s.startswith('*') or s.startswith('/*'):
                        comment = s
                    
                    if comment:
                        matched_tags = []
                        for pat, tag in CONV_PATTERNS:
                            m = pat.findall(comment)
                            if m:
                                matched_tags.append(tag)
                        
                        if matched_tags:
                            results.setdefault(rel, []).append({
                                "line": idx,
                                "tags": list(set(matched_tags)),
                                "comment": comment
                            })

print(f"Total files with conversational / inner monologue comments: {len(results)}")
total_comments = sum(len(v) for v in results.values())
print(f"Total conversational comment lines: {total_comments}\n")

for f, items in sorted(results.items()):
    print(f"File: {f} ({len(items)} hits)")
    for it in items:
        print(f"  L{it['line']} [{', '.join(it['tags'])}]: {it['comment']}")
