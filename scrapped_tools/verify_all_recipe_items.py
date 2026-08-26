import re

with open(r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\ct_dumps\item.txt", "r", encoding="utf-8") as f:
    items = set(re.findall(r"<item:([^>]+)>", f.read()))

with open(r"C:\Users\wamb9\MINECRAFT\Prism\Instances\PEAK dev\minecraft\ct_dumps\tag.txt", "r", encoding="utf-8") as f:
    tags = set(re.findall(r"<tag:[^:]+:([^>]+)>", f.read()))

check_items = [
    'irons_spellbooks:common_ink', 'irons_spellbooks:uncommon_ink', 'irons_spellbooks:rare_ink', 'irons_spellbooks:epic_ink', 'irons_spellbooks:legendary_ink',
    'ars_nouveau:novice_spell_book', 'ars_nouveau:apprentice_spell_book', 'ars_nouveau:archmage_spell_book',
    'minecraft:writable_book', 'refurbished_furniture:dark_oak_desk', 'refurbished_furniture:spruce_desk',
    'minecraft:polished_deepslate', 'minecraft:polished_deepslate_slab',
    'ars_nouveau:arcane_core', 'minecraft:crying_obsidian',
    'irons_spellbooks:arcane_essence', 'irons_spellbooks:cinder_essence',
    'ars_nouveau:abjuration_essence', 'ars_nouveau:air_essence', 'ars_nouveau:conjuration_essence',
    'ars_nouveau:earth_essence', 'ars_nouveau:fire_essence', 'ars_nouveau:manipulation_essence',
    'ars_nouveau:water_essence', 'gatesofavarice:arcane_essence', 'gatesofavarice:dark_essence',
    'gatesofavarice:mystic_essence', 'minecraft:cauldron', 'minecraft:stick'
]

check_tags = [
    'curios:spellbook'
]

print("=== ITEM CHECK ===")
for it in check_items:
    if it not in items:
        print(f"MISSING ITEM: {it}")
    else:
        print(f"OK: {it}")

print("=== TAG CHECK ===")
for tg in check_tags:
    if tg not in tags:
        print(f"MISSING TAG: {tg}")
    else:
        print(f"OK: {tg}")
