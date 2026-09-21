import re

file_path = r"c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\minecraft\config\apotheosis\enchantments.cfg"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Match blocks like "tombstone:..." { ... }
pattern = r'("tombstone:[^"]+"\s*\{[^}]*\})'

matches = re.findall(pattern, content)
print(f"Found {len(matches)} tombstone enchantment blocks.")

cleaned = re.sub(r'\n*"tombstone:[^"]+"\s*\{[^}]*\}\n*', '\n\n', content)

# Clean up any excessive blank lines (more than 2 consecutive newlines)
cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(cleaned)

print("Updated enchantments.cfg successfully.")
