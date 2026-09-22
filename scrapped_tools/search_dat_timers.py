import os
import gzip

world_dir = r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\saves\New World (4)'
for root, dirs, files in os.walk(world_dir):
    for f in files:
        if f.endswith('.dat'):
            p = os.path.join(root, f)
            try:
                with open(p, 'rb') as fp:
                    content = fp.read()
                if content[:2] == b'\x1f\x8b':
                    content = gzip.decompress(content)
                if b'Function' in content or b'Callback' in content or b'schedule' in content or b'function' in content:
                    print(f"Match in {os.path.relpath(p, world_dir)}")
                    # search for function names
                    import re
                    matches = re.findall(b'[a-z0-9_.-]+:[a-z0-9_./-]+', content)
                    for m in set(matches):
                        if b'func' in m or b'tick' in m or b'timer' in m:
                            print("   ", m.decode('latin-1'))
            except Exception as e:
                pass
