import urllib.request
import json
import zipfile
import io

HEADERS = {'User-Agent': 'PEAK/1.0'}
url = "https://api.modrinth.com/v2/project/create-enchantment-industry/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D"
req = urllib.request.Request(url, headers=HEADERS)
versions = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

for v in versions:
    if v['version_number'] in ['2.5.0', '2.5.1', '2.5.1b']:
        for f in v['files']:
            if f['filename'].endswith('.jar') and 'sources' not in f['filename']:
                data = urllib.request.urlopen(urllib.request.Request(f['url'], headers=HEADERS)).read()
                zf = zipfile.ZipFile(io.BytesIO(data))
                if 'META-INF/neoforge.mods.toml' in zf.namelist():
                    lines = zf.read('META-INF/neoforge.mods.toml').decode('utf-8').splitlines()
                    print(f"=== CEI {v['version_number']} ===")
                    for i, l in enumerate(lines):
                        if any(k in l for k in ['modId="sable"', 'modId="apotheosis"', 'modId="apothic_enchanting"']):
                            print("\n".join(lines[i:i+4]))
                            print("---")
                    break
