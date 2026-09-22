import urllib.request
import zipfile
import io
import json

HEADERS = {'User-Agent': 'PEAK/1.0'}

# Check Sable 2.0.5 toml
url = "https://cdn.modrinth.com/data/T9PomCSv/versions/k9eBqC2d/sable-neoforge-1.21.1-2.0.5.jar"
# Let's get exact URL from modrinth API
req = urllib.request.Request("https://api.modrinth.com/v2/project/sable/version?game_versions=%5B%221.21.1%22%5D&loaders=%5B%22neoforge%22%5D", headers=HEADERS)
data = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
file_url = data[0]['files'][0]['url']
print("Downloading Sable 2.0.5 from", file_url)
req_file = urllib.request.Request(file_url, headers=HEADERS)
with urllib.request.urlopen(req_file) as resp:
    zf = zipfile.ZipFile(io.BytesIO(resp.read()))
    for n in zf.namelist():
        if "mods.toml" in n:
            print("=== Sable 2.0.5 toml ===")
            print(zf.read(n).decode('utf-8', errors='ignore'))
