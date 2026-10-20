# Let's check DefaultMinPowerFunction:
# If level > def.maxLevel():
# diff = minCost(maxLevel) - minCost(maxLevel - 1)
# if diff == 0: diff = 15
# cost = minCost(maxLevel) + diff * int(pow(level - maxLevel, 1.6))
# Else:
# cost = minCost(level)

# For Sharpness: vanilla maxLevel = 5.
# minCost(1) = 1
# minCost(2) = 1 + 11 = 12
# minCost(3) = 1 + 22 = 23
# minCost(4) = 1 + 33 = 34
# minCost(5) = 1 + 44 = 45.
# diff = 45 - 34 = 11.
# Level 6: 45 + 11 * int(pow(1, 1.6)) = 45 + 11 * 1 = 56.
# Level 7: 45 + 11 * int(pow(2, 1.6)) = 45 + 11 * 3 = 78.
# Level 8: 45 + 11 * int(pow(3, 1.6)) = 45 + 11 * 5 = 100.
# Level 9: 45 + 11 * int(pow(4, 1.6)) = 45 + 11 * 9 = 144.
# Level 10: 45 + 11 * int(pow(5, 1.6)) = 45 + 11 * 13 = 188.

print("Sharpness min powers:")
for lvl in range(1, 11):
    if lvl <= 5:
        cost = 1 + (lvl - 1) * 11
    else:
        diff = 11
        cost = 45 + diff * int((lvl - 5) ** 1.6)
    print(f"Lvl {lvl}: minPower = {cost}")
