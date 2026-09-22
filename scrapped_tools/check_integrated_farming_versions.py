import urllib.request
import json
import zipfile
import io

HEADERS = {'User-Agent': 'PEAK/1.0'}
url = "https://api.modrinth.com/v2/project/create-integrated-farming/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D"
req = urllib.request.Request(url, headers=HEADERS)
versions = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

for v in versions[:10]:
    vnum = v['version_number']
    for f in v['files']:
        if f['filename'].endswith('.jar') and 'sources' not in f['filename']:
            data = urllib.request.urlopen(urllib.request.Request(f['url'], headers=HEADERS)).read()
            zf = zipfile.ZipFile(io.BytesIO(data))
            if 'META-INF/neoforge.mods.toml' in zf.namelist():
                lines = zf.read('META-INF/neoforge.mods.toml').decode('utf-8').splitlines()
                supp_range = None
                in_supp = False
                for line in lines:
                    if 'modId="supplementaries"' in line:
                        in_supp = True
                    elif in_supp and 'versionRange' in line:
                        supp_range = line.split("=")[-1].strip().strip('"')
                        in_supp = False
                print(f"Integrated Farming {vnum:12} -> Supplementaries: {supp_range}")
            break
