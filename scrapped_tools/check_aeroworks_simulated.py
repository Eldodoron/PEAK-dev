import urllib.request
import json
import zipfile
import io
import re

resp = urllib.request.urlopen("https://api.modrinth.com/v2/project/create-aeroworks/version")
vers = json.loads(resp.read().decode("utf-8"))
for v in vers:
    if "neoforge" in v["loaders"] and "1.21.1" in v["game_versions"]:
        vnum = v["version_number"]
        url = v["files"][0]["url"]
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as jar_resp:
            jar_bytes = jar_resp.read()
        zf = zipfile.ZipFile(io.BytesIO(jar_bytes))
        try:
            toml_text = zf.read("META-INF/neoforge.mods.toml").decode("utf-8")
            m = re.search(r'modId\s*=\s*"simulated"[\s\S]*?versionRange\s*=\s*"([^"]+)"', toml_text)
            print(f"{vnum}: simulated range = {m.group(1) if m else 'None'}")
        except Exception as e:
            print(f"{vnum}: {e}")
