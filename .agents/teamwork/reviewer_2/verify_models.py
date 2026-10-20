import json
import os
import sys
import subprocess

TARGET_FILES = [
    "minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_bottom.json",
    "minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_top_no_seeds.json",
    "minecraft/kubejs/assets/adorablehamsterpets/models/block/sunflower_block_top_with_seeds.json",
    "minecraft/kubejs/assets/minecraft/models/block/flowerbed_1.json",
    "minecraft/kubejs/assets/minecraft/models/block/flowerbed_2.json",
    "minecraft/kubejs/assets/minecraft/models/block/flowerbed_3.json",
    "minecraft/kubejs/assets/minecraft/models/block/flowerbed_4.json",
    "minecraft/kubejs/assets/minecraft/models/block/sunflower_bottom.json",
    "minecraft/kubejs/assets/minecraft/models/block/sunflower_top.json",
]

base_dir = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev"
os.chdir(base_dir)

print("=== 1. VERIFY 9 TARGET MODEL FILES ===")
errors = 0
for rel_path in TARGET_FILES:
    full_path = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(full_path):
        print(f"ERROR: Target file does not exist: {rel_path}")
        errors += 1
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Adversarial check: Check for any occurrence of Blockbench
    if "blockbench" in content.lower():
        print(f"ERROR: 'Blockbench' still found in raw content: {rel_path}")
        errors += 1
    
    # Strict JSON parse check
    try:
        data = json.loads(content)
        print(f"PASS [JSON valid]: {rel_path}")
    except Exception as e:
        print(f"ERROR: Failed JSON parsing: {rel_path} - {e}")
        errors += 1
        continue

    # Credit key check
    if "credit" in data:
        print(f"ERROR: 'credit' property still present in JSON: {rel_path} (value={data['credit']})")
        errors += 1
    else:
        print(f"PASS [No credit]: {rel_path}")

    # Geometry integrity check
    if "elements" not in data:
        print(f"WARNING: 'elements' missing in: {rel_path}")
    else:
        print(f"PASS [Elements intact, count={len(data['elements'])}]: {rel_path}")

print(f"\nTarget 9 files errors: {errors}")

print("\n=== 2. SCAN ALL JSON FILES IN KUBEJS/ASSETS FOR BLOCKBENCH ===")
blockbench_matches = []
all_json_count = 0
json_parse_errors = 0

assets_dir = os.path.join(base_dir, "minecraft", "kubejs", "assets")
for root, dirs, files in os.walk(assets_dir):
    for file in files:
        if file.endswith(".json"):
            all_json_count += 1
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8") as f:
                c = f.read()
            if "blockbench" in c.lower():
                blockbench_matches.append(os.path.relpath(fpath, base_dir))
            try:
                json.loads(c)
            except Exception as e:
                print(f"JSON Parse Error in {os.path.relpath(fpath, base_dir)}: {e}")
                json_parse_errors += 1

print(f"Total JSON files scanned in kubejs/assets: {all_json_count}")
print(f"Total JSON parse errors: {json_parse_errors}")
print(f"Total Blockbench matches in kubejs/assets: {len(blockbench_matches)}")
if blockbench_matches:
    for m in blockbench_matches:
        print(f"  Match: {m}")

print("\n=== 3. VERIFY PRESERVED CREDITS ===")
zanderest_count = 0
cubicleaves_dir = os.path.join(assets_dir, "cubicleaves", "models", "block")
if os.path.exists(cubicleaves_dir):
    for f in os.listdir(cubicleaves_dir):
        if f.endswith(".json"):
            fpath = os.path.join(cubicleaves_dir, f)
            with open(fpath, "r", encoding="utf-8") as fp:
                data = json.load(fp)
                if data.get("credit") == "zanderest":
                    zanderest_count += 1
                else:
                    print(f"Unexpected credit in {f}: {data.get('credit')}")
print(f"Cubicleaves 'zanderest' credit count: {zanderest_count} (expected: 25)")

green_screen_path = os.path.join(assets_dir, "kubejs", "models", "block", "green_screen.json")
green_screen_credit = None
if os.path.exists(green_screen_path):
    with open(green_screen_path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
        green_screen_credit = data.get("credit")
print(f"green_screen.json credit: '{green_screen_credit}' (expected: 'PEAK')")

print("\n=== 4. SCOPE CONFINEMENT VERIFICATION ===")
# Check ct_dumps
ct_dumps_dir = os.path.join(base_dir, "minecraft", "ct_dumps")
# Run git status on ct_dumps
res_ct = subprocess.run(["git", "status", "--porcelain", "minecraft/ct_dumps/"], capture_output=True, text=True)
print(f"Git status minecraft/ct_dumps/ output: '{res_ct.stdout.strip()}' (expected: empty)")

# Check PEAK DEV MULTIMEDIA
multimedia_dir = r"c:\Users\chris\Desktop\PEAK DEV MULTIMEDIA"
print(f"Checking multimedia directory: {multimedia_dir}")
if os.path.exists(multimedia_dir):
    # Check if there's a git repo or check last modified times
    print(f"Multimedia directory exists.")
    # Walk directory to see any modified files in last 2 hours
    import time
    now = time.time()
    recent_files = []
    for root, dirs, files in os.walk(multimedia_dir):
        for f in files:
            fp = os.path.join(root, f)
            try:
                mtime = os.path.getmtime(fp)
                if now - mtime < 7200: # 2 hours
                    recent_files.append((fp, now - mtime))
            except Exception:
                pass
    print(f"Files modified in multimedia dir in last 2 hours: {len(recent_files)}")
    if recent_files:
        for rf, age in recent_files:
            print(f"  {rf} (modified {age:.1f}s ago)")
else:
    print("Multimedia directory does not exist or not accessible.")

# Check git diff --stat for kubejs/assets
res_diff = subprocess.run(["git", "diff", "--stat", "minecraft/kubejs/assets/"], capture_output=True, text=True)
print("\nGit diff --stat for minecraft/kubejs/assets/:")
print(res_diff.stdout.strip())
