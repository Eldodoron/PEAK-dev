import urllib.request
import json

HEADERS = {'User-Agent': 'Mozilla/5.0'}
CF_API_KEY = "$2a$10$bL4bIL5pUWqfcO7KQtnMReakwtfHbNKh6v1uTpKlzhwoueEJQnPnm"

def check_fwa():
    url = "https://api.curseforge.com/v1/mods/search?gameId=432&searchFilter=Fancy+World+Animations"
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for m in data.get('data', []):
                print(f"CF: {m['name']} (ID: {m['id']})")
                furl = f"https://api.curseforge.com/v1/mods/{m['id']}/files?gameVersion=1.21.1&modLoaderType=6"
                freq = urllib.request.Request(furl, headers={**HEADERS, 'x-api-key': CF_API_KEY})
                with urllib.request.urlopen(freq) as fresp:
                    fdata = json.loads(fresp.read().decode('utf-8'))
                    for f in fdata.get('data', [])[:3]:
                        print(f"  File: {f['displayName']} -> {f.get('fileName')}")
    except Exception as e:
        print(f"CF error: {e}")

check_fwa()
