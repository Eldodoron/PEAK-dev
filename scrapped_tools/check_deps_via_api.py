import urllib.request
import json

HEADERS = {'User-Agent': 'PEAK/1.0'}

def check_project(slug):
    url = f"https://api.modrinth.com/v2/project/{slug}/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D"
    req = urllib.request.Request(url, headers=HEADERS)
    data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    print(f"=== {slug} versions ===")
    for v in data[:6]:
        print(f"Version: {v['version_number']} ({v['name']})")
        for d in v.get('dependencies', []):
            print(f"   dep: {d}")

check_project("create-enchantment-industry")
print()
check_project("create-integrated-farming")
