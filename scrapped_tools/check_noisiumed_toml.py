import zipfile
import io
import urllib.request

HEADERS = {'User-Agent': 'Mozilla/5.0'}
url = "https://edge.forgecdn.net/files/8475/257/noisiumed-3.0.6-neoforge-1.21.1.jar"
req = urllib.request.Request(url, headers=HEADERS)
with urllib.request.urlopen(req) as resp:
    zf = zipfile.ZipFile(io.BytesIO(resp.read()))
    for name in zf.namelist():
        if "neoforge.mods.toml" in name:
            print(zf.read(name).decode('utf-8'))
