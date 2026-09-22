import urllib.request
import json

HEADERS = {'User-Agent': 'PEAK/1.0'}

def get_url(slug, ver):
    url = f"https://api.modrinth.com/v2/project/{slug}/version"
    req = urllib.request.Request(url, headers=HEADERS)
    versions = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    for v in versions:
        if v['version_number'] == ver:
            for f in v['files']:
                if f['filename'].endswith('.jar') and 'sources' not in f['filename']:
                    print(f"{slug} {ver}: {f['filename']} -> {f['url']}")

get_url("create-enchantment-industry", "2.5.0-preview-alpha1")
get_url("create-integrated-farming", "1.4.1c")
get_url("create-integrated-farming", "1.2.6")
