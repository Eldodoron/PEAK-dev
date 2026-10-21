import re

items = set()
with open("minecraft/ct_dumps/item.txt", encoding="utf-8") as fh:
    for line in fh:
        m = re.match(r"<item:([^>]+)>", line.strip())
        if m:
            items.add(m.group(1))

tomes = {f"kubejs:{n}" for n in ("stonebook", "melonbook", "beebook", "hellbook", "seabook", "deepbook", "sculkbook", "endbook")}
text = open("minecraft/kubejs/server_scripts/66_bookshelf_overhaul.js", encoding="utf-8").read()

# Only ids used in item positions: item: '...', shaped keys/results, apparatus args, event.remove output
ids = set(re.findall(r"item: '([^']+)'", text))
ids |= set(re.findall(r"(?:^|\s)[A-Z]: '([^']+)'", text, re.M))
ids |= set(re.findall(r"id: '([^']+)', count", text))
ids |= set(re.findall(r"results: \[\{ id: '([^']+)'", text))
ids |= set(re.findall(r"event\.shaped\((?:Item\.of\()?'([^']+)'", text))
ids |= set(re.findall(r"^\s+'((?:apothic_enchanting|minecraft|create|irons_spellbooks|avaritia)[^']*)',?$", text, re.M))
ids |= set(re.findall(r"repeat\('([^']+)'", text))

checked = 0
bad = []
for ident in sorted(ids):
    if ident in tomes:
        continue
    checked += 1
    if ident not in items:
        bad.append(ident)
print("checked", checked, "item ids")
print("missing:", bad if bad else "none")
