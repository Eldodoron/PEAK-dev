import urllib.request
import json

HEADERS = {'User-Agent': 'PEAK-Modpack/1.0'}

def get_mr_version_deps(slug):
    url = f"https://api.modrinth.com/v2/project/{slug}/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for v in data[:3]:
            print(f"=== {slug} {v['version_number']} ===")
            print("Dependencies:", v.get('dependencies', []))
            print("Files:", [f['filename'] for f in v['files']])

print("Checking aeroworks:")
get_mr_version_deps("create-aeroworks")

print("\nChecking create-enchantment-industry:")
get_mr_version_deps("create-enchantment-industry")

print("\nChecking create-central-kitchen:")
get_mr_version_deps("create-central-kitchen")
