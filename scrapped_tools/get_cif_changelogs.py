import urllib.request
import json

HEADERS = {'User-Agent': 'PEAK/1.0'}
url = "https://api.modrinth.com/v2/project/create-integrated-farming/version"
req = urllib.request.Request(url, headers=HEADERS)
data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

for v in data:
    if v['version_number'] in ['1.4.2', '1.4.1c', '1.4.1b', '1.4.1', '1.4.0']:
        print(f"=== Version {v['version_number']} ({v['name']}) ===")
        print(v.get('changelog', ''))
        print()
