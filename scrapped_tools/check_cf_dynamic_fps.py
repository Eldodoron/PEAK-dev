import urllib.request
import json

HEADERS = {'User-Agent': 'Mozilla/5.0'}
CF_API_KEY = "$2a$10$bL4bIL5pUWqfcO7KQtnMReakwtfHbNKh6v1uTpKlzhwoueEJQnPnm"

def search_cf_exact(slug):
    url = f"https://api.curseforge.com/v1/mods/search?gameId=432&slug={slug}"
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('data', [])
    except Exception as e:
        print(e)
        return []

def get_cf_files(mod_id):
    url = f"https://api.curseforge.com/v1/mods/{mod_id}/files?gameVersion=1.21.1&modLoaderType=6"
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('data', [])
    except Exception as e:
        print(e)
        return []

res = search_cf_exact("dynamic-fps")
for m in res:
    print(f"Mod: {m['name']} ID: {m['id']}")
    files = get_cf_files(m['id'])
    for f in files:
        print(f"  File: {f['displayName']} -> {f.get('downloadUrl')}")
