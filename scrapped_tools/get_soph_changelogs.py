import urllib.request
import json

HEADERS = {'User-Agent': 'Mozilla/5.0'}
CF_API_KEY = "$2a$10$bL4bIL5pUWqfcO7KQtnMReakwtfHbNKh6v1uTpKlzhwoueEJQnPnm"

def get_changelog(mod_id, file_id):
    url = f"https://api.curseforge.com/v1/mods/{mod_id}/files/{file_id}/changelog"
    req = urllib.request.Request(url, headers={**HEADERS, 'x-api-key': CF_API_KEY})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('data', '')
    except Exception as e:
        return str(e)

# SB 3.26.0 (8817433) and 3.26.3 (8845926)
print("=== SB 3.26.0 Changelog ===")
print(get_changelog(422301, 8817433))
print("=== SB 3.26.3 Changelog ===")
print(get_changelog(422301, 8845926))

# SC 1.5.0 (8815718) and 1.5.1 (8838842)
print("=== SC 1.5.0 Changelog ===")
print(get_changelog(618298, 8815718))
print("=== SC 1.5.1 Changelog ===")
print(get_changelog(618298, 8838842))
