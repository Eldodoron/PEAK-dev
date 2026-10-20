import math, random

# Let's inspect what ApothEnchantmentHelper does:
# power = 30 (from 15 bookshelves)
# Arcana = 0%
# Quanta = 0%

# In selectEnchantment:
# 1) var13 loop (Arcana threshold loop):
# var13 starts at 0, steps by 33 while var13 < 100:
# var13 = 0: stats.arcana() >= 0 -> TRUE! Picks 1st enchantment.
# var13 = 33: stats.arcana() >= 33 -> False.
# var13 = 66: stats.arcana() >= 66 -> False.
# var13 = 99: stats.arcana() >= 99 -> False.

# 2) Vanilla-like loop:
# int bound = Math.max(50, (int)(power * 1.15f));
# while (random.nextInt(bound) <= power && !list.isEmpty()) {
#     pickEnchantment(...)
#     power /= 2;
# }

def simulate_count(power=30, arcana=0):
    # Arcana loop
    count = 0
    var13 = 0
    while var13 < 100:
        if arcana >= var13:
            count += 1
        var13 += 33
    
    # Vanilla extra loop
    bound = max(50, int(power * 1.15))
    p = power
    while random.randint(0, bound - 1) <= p:
        count += 1
        p //= 2
    return count

sims = [simulate_count(30, 0) for _ in range(10000)]
from collections import Counter
c = Counter(sims)
print("Simulation with Power=30, Arcana=0:")
for k in sorted(c.keys()):
    print(f"{k} enchantments: {c[k]/100:.1f}%")

print("\nWhat if power is 45, 60, 100?")
for p in [45, 60, 100]:
    sims_p = [simulate_count(p, 0) for _ in range(10000)]
    cp = Counter(sims_p)
    print(f"Power={p}, Arcana=0: {dict(sorted(cp.items()))}")
