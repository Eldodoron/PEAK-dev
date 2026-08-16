import os
import json

KUBEJS_DIR = r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\kubejs"

# Let's inspect each category of findings:
# 1. Definite (Explicit AI tool names, explicit prompt sequence references)
# 2. High (Conversational dialogue remnants like "user request", "so the user knows", "the user wants")
# 3. Probable (Standardized "PEAK EXPERT MODE" generation pipeline: Script XX headers, console logs, mojibake em-dashes/arrows, AI helper scripts)
# 4. Low (Short utility scripts following the same ecosystem / conventions)

findings = []

# List of all files in kubejs
all_kubejs_files = []
for root, dirs, files in os.walk(KUBEJS_DIR):
    for f in files:
        all_kubejs_files.append(os.path.join(root, f))

print(f"Total files under minecraft/kubejs/: {len(all_kubejs_files)}")

# Let's write the detailed verification script
verification_results = []
for f in all_kubejs_files:
    verification_results.append({
        "path": f,
        "exists": os.path.exists(f),
        "size": os.path.getsize(f)
    })

with open(r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\.agents\explorer_1\verification_check.json", "w", encoding="utf-8") as f:
    json.dump(verification_results, f, indent=2)

print("Verification check completed for all files.")
