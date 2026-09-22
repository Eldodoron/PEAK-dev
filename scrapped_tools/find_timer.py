import gzip

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\saves\New World (4)\level.dat', 'rb') as f:
    data = gzip.decompress(f.read())

# Search for "CustomEvents" or "ScheduledEvents" or "Timer"
import re
idx = 0
while True:
    pos = data.find(b'Timer', idx)
    if pos == -1:
        break
    print(f"Found 'Timer' at {pos}:")
    snippet = data[max(0, pos-50):min(len(data), pos+300)]
    print(repr(snippet))
    idx = pos + 1
