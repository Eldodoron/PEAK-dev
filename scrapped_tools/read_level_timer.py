import gzip
import io

def parse_nbt(data):
    # simple reader to search for strings in nbt
    # or print any scheduled function names
    import re
    strings = re.findall(b'[a-z0-9_.-]+:[a-z0-9_./-]+', data)
    print("Found potential namespaced IDs in level.dat:")
    for s in set(strings):
        if b'function' in s or b'tick' in s or b'timer' in s or b'schedule' in s or b'compat' in s or b'boss' in s:
            print(" -", s.decode('latin-1'))

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\saves\New World (4)\level.dat', 'rb') as f:
    raw = gzip.decompress(f.read())
    parse_nbt(raw)
