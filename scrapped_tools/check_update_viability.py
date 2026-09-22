import urllib.request
import json

HEADERS = {'User-Agent': 'PEAK/1.0'}

def get_mr(slug):
    url = f"https://api.modrinth.com/v2/project/{slug}/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
        print(f"=== {slug} on Modrinth ===")
        for v in data[:5]:
            print(f"  {v['version_number']} ({v['name']})")
    except Exception as e:
        print(f"Error {slug}: {e}")

get_mr("supplementaries")
get_mr("apotheosis")
get_mr("apothic-enchanting")
