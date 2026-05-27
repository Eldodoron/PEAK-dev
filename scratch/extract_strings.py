import re
with open(r"c:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\scratch\dev\shadowsoffire\apotheosis\commands\WorldTierCommand.class", "rb") as f:
    data = f.read()

strings = re.findall(b"[a-zA-Z0-9_:/]{3,}", data)
decoded = sorted(list(set([s.decode('utf-8') for s in strings])))
print("\n".join(decoded))
