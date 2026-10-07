import os
from PIL import Image

OUT_DIR = "C:/Users/chris/.gemini/antigravity/brain/6d94d33a-8771-44bb-b233-6e02f1167405"
os.makedirs(OUT_DIR, exist_ok=True)

def hex_to_rgba(h):
    if h == "." or h is None or h == ".......":
        return (0, 0, 0, 0)
    h = h.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255)

def save_sprite(grid, name):
    im = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            im.putpixel((x, y), hex_to_rgba(c))
    
    path_16 = os.path.join(OUT_DIR, f"{name}_16.png")
    path_256 = os.path.join(OUT_DIR, f"{name}_256.png")
    im.save(path_16)
    
    im256 = im.resize((256, 256), Image.NEAREST)
    im256.save(path_256)
    print(f"Saved {name}: {path_256}")
    return path_256

# Pure White Starlight Core
W = "#FFFFFF"

# Outlines: Deep Void Obsidian / Cosmic Indigo
V_O = "#140A26"  # Main void outline
V_T = "#181842"  # Top navy void
V_S = "#28103E"  # Shadow violet
V_D = "#0C0418"  # Absolute void

# ==============================================================================
# Palette: Avaritia Infinity Catalyst Colors
# ==============================================================================
# North: Hot Pink / Magenta
P1 = "#FFD6EE"  # Lightest
P2 = "#FF54B0"  # Vibrant
P3 = "#D61578"  # Deep

# North-East: Astral Violet
V1 = "#ECC8FF"
V2 = "#B242FF"
V3 = "#7614D9"

# East: Cobalt / Starlight Blue
B1 = "#CCE2FF"
B2 = "#4A84FF"
B3 = "#1A46D6"

# South-East: Electric Cyan / Turquoise
C1 = "#BCFBF6"
C2 = "#34E2D6"
C3 = "#129890"

# South: Auroral Emerald / Lime
L1 = "#E0FFBC"
L2 = "#7CF534"
L3 = "#3DA810"

# South-West: Solar Gold / Amber
G1 = "#FFF2AA"
G2 = "#FFC822"
G3 = "#DA8406"

# West: Fiery Orange / Solar Flare
O1 = "#FFE2C6"
O2 = "#FF7C20"
O3 = "#C94206"

# North-West: Radiant Coral / Crimson
R1 = "#FFCFD8"
R2 = "#FF4D6E"
R3 = "#C71636"

# ==============================================================================
# OPTION 1: Whimscape Infinity Nova (8-Ray Prismatic Pinwheel)
# Exact Whimscape facet structure, with 8 rainbow rays converging into a tight
# 4x4 brilliant white starlight diamond.
# ==============================================================================
grid_opt1 = [
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   V_T,   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   W,     V_T,   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   P2,    V2,    V_T,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   V_T,   V_T,   V_T,   P1,    V2,    V3,    V_S,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   R2,    R1,    P1,    W,     V1,    V2,    V_S,   B2,    V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   V_T,   R2,    R1,    W,     W,     V1,    B1,    B2,    V_O,   ".",   ".",   "."],
    [".",   ".",   V_T,   O2,    O1,    R2,    W,     W,     W,     W,     B1,    B2,    V_S,   V_O,   V_O,   V_O],
    [".",   V_T,   W,     O1,    O2,    W,     W,     W,     W,     W,     W,     C1,    C2,    C3,    C2,    V_O],
    [V_O,   O2,    O3,    O3,    G1,    W,     W,     W,     W,     W,     W,     C2,    C3,    C3,    V_O,   "."],
    [V_O,   V_O,   V_O,   V_O,   G2,    G1,    W,     W,     W,     W,     C2,    C3,    L3,    V_O,   ".",   "."],
    [".",   ".",   ".",   V_O,   G2,    G3,    G2,    G1,    L1,    L2,    L2,    V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_O,   G3,    V_O,   G3,    G3,    L1,    L2,    L3,    L3,    V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_O,   V_O,   V_O,   G3,    L1,    L2,    V_O,   V_O,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_O,   L2,    L3,    V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   L3,    V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   V_O,   ".",   ".",   ".",   ".",   ".",   "."]
]

# Let's refine grid_opt1 center so the core feels faceted like Whimscape:
# Whimscape has:
# Row 6: x=6: P1, x=7,8: W, x=9: V1, x=10: B1, x=11: B2
# Row 7: x=5: O1, x=6..9: W, x=10: C1, x=11: C2
# Row 8: x=4: G1, x=5: G1, x=6..9: W, x=10: C2
# Row 9: x=5: G1, x=6: G1, x=7,8: W, x=9: C1
grid_opt1[6][6] = P1
grid_opt1[6][7] = W
grid_opt1[6][8] = W
grid_opt1[6][9] = V1

grid_opt1[7][5] = O1
grid_opt1[7][6] = W
grid_opt1[7][7] = W
grid_opt1[7][8] = W
grid_opt1[7][9] = W
grid_opt1[7][10] = C1

grid_opt1[8][4] = G1
grid_opt1[8][5] = G1
grid_opt1[8][6] = W
grid_opt1[8][7] = W
grid_opt1[8][8] = W
grid_opt1[8][9] = W
grid_opt1[8][10] = C2

grid_opt1[9][5] = G1
grid_opt1[9][6] = G1
grid_opt1[9][7] = W
grid_opt1[9][8] = W
grid_opt1[9][9] = L1

# ==============================================================================
# OPTION 2: Avaritia Cosmic Swirl (Diagonal Galaxy Nebula)
# Top-Left solar gold & lime, White core, Bottom-Right magenta & royal purple
# ==============================================================================
grid_opt2 = [
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   V_T,   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   W,     V_T,   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   G1,    G2,    V_T,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   V_T,   V_T,   V_T,   G1,    G2,    O2,    V_S,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   L1,    G1,    G1,    W,     G2,    O2,    V_S,   C1,    V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   V_T,   L2,    G1,    W,     W,     C1,    C2,    B2,    V_O,   ".",   ".",   "."],
    [".",   ".",   V_T,   L2,    L1,    G2,    G1,    W,     W,     C1,    C2,    B1,    V_S,   V_O,   V_O,   V_O],
    [".",   V_T,   W,     L1,    G2,    G1,    W,     W,     W,     W,     C1,    C2,    B2,    B3,    C2,    V_O],
    [V_O,   G2,    O2,    O3,    G1,    G1,    W,     W,     W,     W,     V1,    V2,    V3,    V3,    V_O,   "."],
    [V_O,   V_O,   V_O,   V_O,   G3,    P1,    P1,    W,     W,     V1,    V2,    V3,    V3,    V_O,   ".",   "."],
    [".",   ".",   ".",   V_O,   P1,    P2,    P3,    P1,    V1,    V2,    V3,    V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_O,   P2,    V_O,   P3,    P3,    V2,    V2,    V3,    V3,    V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_O,   V_O,   V_O,   P3,    V1,    V2,    V_O,   V_O,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_O,   V2,    V3,    V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   V3,    V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   V_O,   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 3: Classic Vanilla Infinity Star (Vanilla 13x13 × 8-Color Spectrum)
# Minecraft's iconic vanilla Nether Star shape with crisp rainbow rays
# ==============================================================================
grid_opt3 = [
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   P2,    V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_O,   P1,    W,     V1,    V_O,   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_O,   R2,    W,     V2,    V_O,   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   V_O,   V_O,   R1,    R1,    W,     V1,    B1,    V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_O,   O2,    O1,    O1,    W,     W,     W,     B1,    B2,    B3,    V_O,   ".",   "."],
    [".",   ".",   V_O,   O3,    O2,    O1,    W,     W,     W,     W,     C1,    C2,    C3,    V_O,   ".",   "."],
    [".",   ".",   ".",   V_O,   G2,    G1,    G1,    W,     W,     W,     C1,    C2,    C3,    V_O,   ".",   "."],
    [".",   ".",   ".",   ".",   V_O,   V_O,   G2,    G1,    W,     L1,    C2,    V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_O,   G3,    W,     L2,    V_O,   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_O,   L1,    L2,    L3,    V_O,   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   L3,    V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 4: Gilded Infinity Relic Star (Solar Gold Armor × 8-Color Starlight Core)
# ==============================================================================
GLD_H = "#FFF8B8"  # Highlight gold
GLD_1 = "#FFD84A"  # Primary bright gold
GLD_2 = "#E0981B"  # Warm amber gold
GLD_3 = "#8C5209"  # Shadow gold
GLD_O = "#2E1803"  # Deep gold-bronze outline

grid_opt4 = [
    [".",   ".",   ".",   ".",   ".",   ".",   GLD_O, GLD_O, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   GLD_O, GLD_H, GLD_O, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   GLD_O, GLD_1, GLD_2, GLD_O, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   GLD_O, GLD_O, GLD_O, GLD_O, GLD_1, GLD_2, GLD_3, GLD_O, GLD_O, GLD_O, ".",   ".",   "."],
    [".",   ".",   ".",   GLD_O, GLD_H, GLD_1, P1,    W,     V1,    GLD_2, GLD_O, GLD_1, GLD_O, ".",   ".",   "."],
    [".",   ".",   ".",   GLD_O, GLD_O, GLD_1, R1,    W,     W,     B1,    GLD_1, GLD_2, GLD_O, ".",   ".",   "."],
    [".",   ".",   GLD_O, GLD_H, GLD_1, O1,    O1,    W,     W,     C1,    C1,    GLD_1, GLD_O, GLD_O, GLD_O, GLD_O],
    [".",   GLD_O, GLD_H, GLD_1, O2,    O1,    W,     W,     W,     W,     C1,    GLD_1, GLD_2, GLD_3, GLD_1, GLD_O],
    [GLD_O, GLD_H, GLD_1, O3,    G1,    W,     W,     W,     W,     W,     C2,    GLD_2, GLD_3, GLD_O, GLD_O, "."],
    [GLD_O, GLD_O, GLD_O, GLD_O, G2,    G1,    W,     W,     W,     L1,    C2,    GLD_3, GLD_O, GLD_O, ".",   "."],
    [".",   ".",   ".",   GLD_O, G2,    G1,    L1,    W,     L1,    L2,    GLD_2, GLD_O, GLD_O, ".",   ".",   "."],
    [".",   ".",   ".",   GLD_O, G3,    GLD_O, L1,    L2,    L2,    L3,    GLD_2, GLD_3, GLD_O, ".",   ".",   "."],
    [".",   ".",   ".",   GLD_O, GLD_O, GLD_O, L2,    L2,    L3,    GLD_O, GLD_O, GLD_O, GLD_O, ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   GLD_O, GLD_2, GLD_3, GLD_O, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   GLD_O, GLD_3, GLD_O, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   GLD_O, GLD_O, ".",   ".",   ".",   ".",   ".",   "."]
]

save_sprite(grid_opt1, "opt1_infinity_nova")
save_sprite(grid_opt2, "opt2_cosmic_swirl")
save_sprite(grid_opt3, "opt3_classic_infinity_star")
save_sprite(grid_opt4, "opt4_gilded_infinity_relic")
