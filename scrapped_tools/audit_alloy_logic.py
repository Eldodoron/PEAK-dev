import json, re

print("Auditing 67_allthemodium_expansion.js logic...")

with open('minecraft/kubejs/server_scripts/67_allthemodium_expansion.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Check removals
assert "event.remove({ type: 'minecraft:smelting', input: '#c:dusts/allthemodium_alloys' });" in text
assert "event.remove({ type: 'minecraft:blasting', input: '#c:dusts/allthemodium_alloys' });" in text
print("PASS: Furnace & blast furnace removals verified.")

# 2. Check base crushing
for metal in ['allthemodium', 'vibranium', 'unobtainium']:
    assert f"event.recipes.create.crushing('allthemodium:{metal}_dust', 'allthemodium:{metal}_ingot')" in text
print("PASS: Base ingot-to-dust crushing verified.")

# 3. Check 2x dust mixing
for alloy in ['unobtainium_allthemodium', 'unobtainium_vibranium', 'vibranium_allthemodium']:
    assert f"'2x allthemodium:{alloy}_alloy_dust'" in text
print("PASS: 2x Alloy dust mixing recipes verified.")

# 4. Check Advanced Create Machines for ingots
assert "create_new_age:energising" in text
assert "tfmg:vat_machine_recipe" in text
assert "dndesires:hydraulic_compacting" in text
assert "tfmg:graphite_electrode" in text
print("PASS: Advanced Create Addon machines (New Age Energiser, TFMG Electric Arc Furnace, DnDesires Hydraulic Press) verified.")

print("ALL LOGIC CHECKS PASSED PERFECTLY!")
