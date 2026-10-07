# Let's write an exact symmetric template builder for Ignis Emblem:

def make_symmetric_row(left_chars):
    # left_chars is 8 characters (x=0..7)
    # right_chars is left_chars reversed or adjusted for light
    pass

# Row templates:
# Type A (Top/Bottom rim, 8 width):
# "    KKKKKKKK    " (x=4..11)

# Type B (12 width with flame spurs):
# "  KKYYYYYYYYKK  " (x=2..13)

# Type C (14 width with full wings):
# " KXXXXXXXXXXXXK " (x=1..14)

# Let's test a complete 16x16 grid:
GRID_FAITHFUL_IGNIS = [
    "                ", # 0
    "    KKKKKKKK    ", # 1: Top outline
    "  KKYYYYYYYYKK  ", # 2: Top gold frame (x=2..13)
    " KGYAYYYYYYAOGK ", # 3: Wings (x=1..3, 12..14) + frame top
    " KGYABBBBBBBAOGK", # 4: Wings + black window top (wait: len 16)
    " KGYABYGGAYBAOGK", # 5: Ignis brow bar (YGGA)
    " KGYABBBGABBAOGK", # 6: Ignis nose bridge (GA)
    " KGYABYBBBBGAOGK", # 7: Ignis twin tusks (Y left, G right)
    " KGYABGBBBBAAOGK", # 8: Lower tusks (G left, A right)
    " KGYABBBBBBBAOGK", # 9: Black window bottom
    " KGYAOOOOOOAOOGK", # 10: Frame bottom
    "  KKOOOOOOOOKK  ", # 11: Lower frame bevel
    "    KKKKKKKK    ", # 12: Bottom outline
    "                ", # 13
    "                ", # 14
    "                "  # 15
]

# Let's check each line length:
for y, r in enumerate(GRID_FAITHFUL_IGNIS):
    if len(r) != 16:
        print(f"Row {y} len={len(r)}: '{r}'")
