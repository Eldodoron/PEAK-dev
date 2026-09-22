import urllib.request
import json

HEADERS = {'User-Agent': 'PEAK/1.0'}
CF_API_KEY = "$2a$10$bL4bIL5pUWqfcO7KQtnMReakwtfHbNKh6v1uTpKlzhwoueEJQnPnm"

def check_sable_mr():
    url = "https://api.modrinth.com/v2/project/sable/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
        print("=== Sable on Modrinth ===")
        for v in data[:6]:
            print(f"  {v['version_number']} ({v['name']}) -> files: {[f['filename'] for f in v['files']]}")
    except Exception as e:
        print(f"MR error: {e}")

def check_sable_cf():
    url = "https://api.curseforge.com/v1/mods/search?gameId=432&searchFilter=Sable"
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        data = json.loads(urllib.request.urlopen(req).read().decode('utf-8')).get('data', [])
        for m in data:
            if m['slug'] == 'sable':
                print(f"=== Sable on CF (ID: {m['id']}) ===")
                furl = f"https://api.curseforge.com/v1/mods/{m['id']}/files?gameVersion=1.21.1&modLoaderType=6"
                freq = urllib.request.Request(furl, headers={**HEADERS, 'x-api-key': CF_API_KEY})
                fdata = json.loads(urllib.request.urlopen(freq).read().decode('utf-8')).get('data', [])
                for f in fdata[:6]:
                    print(f"  {f['displayName']} -> {f['fileName']}")
    except Exception as e:
        print(f"CF error: {e}")

check_sable_mr()
check_sable_cf()
