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

# Pure White Starlight Heart
W = "#FFFFFF"

# Outlines: Cosmic Void Obsidian & Nebula Indigo
V_O = "#140A26"  # Main void outline
V_T = "#1A1A46"  # Upper navy void outline
V_S = "#28103E"  # Cosmic shadow outline
V_D = "#0C0418"  # Absolute void black

# ==============================================================================
# The 8 Cosmic Colors of Infinity Catalyst (Pastel Inner -> Saturated Outer -> Deep Shadow)
# ==============================================================================
# 1. North: Hot Pink / Magenta
P_1 = "#FFD1EC"  # Pastel root
P_2 = "#FF5CB4"  # Vibrant neon
P_3 = "#D61A7C"  # Deep magenta

# 2. North-East: Astral Violet
V_1 = "#ECC8FF"  # Pastel root
V_2 = "#B64DFF"  # Vivid violet
V_3 = "#7A18E0"  # Royal nebula

# 3. East: Cobalt / Starlight Blue
B_1 = "#CBE0FF"  # Pastel root
B_2 = "#4D8AFF"  # Electric cobalt
B_3 = "#1E4EDE"  # Deep astral blue

# 4. South-East: Electric Cyan / Turquoise
C_1 = "#BAF9F4"  # Pastel root
C_2 = "#32E0D4"  # Vivid starlight cyan
C_3 = "#12968E"  # Deep teal

# 5. South: Auroral Emerald / Lime
L_1 = "#DCFFB8"  # Pastel root
L_2 = "#7CF536"  # Electric lime
L_3 = "#3FA812"  # Deep emerald

# 6. South-West: Solar Gold / Topaz
G_1 = "#FFF0AA"  # Pastel root
G_2 = "#FFC826"  # Brilliant gold
G_3 = "#DB8608"  # Deep amber

# 7. West: Fiery Orange / Solar Flare
O_1 = "#FFE0C4"  # Pastel root
O_2 = "#FF7D24"  # Fiery orange
O_3 = "#C94508"  # Burning ember

# 8. North-West: Radiant Coral / Crimson
R_1 = "#FFCCD4"  # Pastel root
R_2 = "#FF4F6E"  # Vivid coral
R_3 = "#C71836"  # Deep crimson

# ==============================================================================
# OPTION 1: Whimscape Chromatic Nether Star
# Faithful Whimscape pinwheel geometry with all 8 Infinity Catalyst rainbow rays
# converging into a concentrated 4x4 white starlight diamond.
# ==============================================================================
grid_opt1 = [
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   V_T,   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   W,     V_T,   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   P_2,   V_2,   V_T,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   V_T,   V_T,   V_T,   P_1,   V_2,   V_3,   V_S,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   R_2,   R_1,   P_1,   P_1,   V_1,   V_2,   V_S,   B_2,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   V_T,   R_2,   R_1,   W,     W,     V_1,   B_1,   B_2,   V_O,   ".",   ".",   "."],
    [".",   ".",   V_T,   O_2,   O_1,   R_2,   W,     W,     W,     W,     B_1,   B_2,   V_S,   V_O,   V_O,   V_O],
    [".",   V_T,   W,     O_1,   O_2,   W,     W,     W,     W,     W,     W,     C_1,   C_2,   C_3,   C_2,   V_O],
    [V_O,   O_2,   O_3,   O_3,   G_1,   W,     W,     W,     W,     W,     W,     C_2,   C_3,   C_3,   V_O,   "."],
    [V_O,   V_O,   V_O,   V_O,   G_2,   G_1,   W,     W,     W,     W,     C_2,   C_3,   L_3,   V_O,   ".",   "."],
    [".",   ".",   ".",   V_O,   G_2,   G_3,   G_2,   G_1,   L_1,   L_2,   L_2,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_O,   G_3,   V_O,   G_3,   G_3,   L_1,   L_2,   L_3,   L_3,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_O,   V_O,   V_O,   G_3,   L_1,   L_2,   V_O,   V_O,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_O,   L_2,   L_3,   V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   L_3,   V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   V_O,   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 2: Cosmic Avaritia Drift (Diagonal Gradient Shading on Whimscape Star)
# Amber/Gold/Lime top-left, pure white starlight heart, Neon Magenta & Royal Violet bottom-right
# High-contrast crystalline shading matching Whimscape facets.
# ==============================================================================
grid_opt2 = [
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   V_T,   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   W,     V_T,   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   G_1,   G_2,   V_T,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   V_T,   V_T,   V_T,   G_1,   G_2,   O_2,   V_S,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   L_1,   G_1,   G_1,   W,     G_2,   O_2,   V_S,   C_1,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   V_T,   L_2,   G_1,   W,     W,     C_1,   C_2,   B_2,   V_O,   ".",   ".",   "."],
    [".",   ".",   V_T,   L_2,   L_1,   G_2,   W,     W,     W,     W,     C_2,   B_1,   V_S,   V_O,   V_O,   V_O],
    [".",   V_T,   W,     L_1,   G_2,   W,     W,     W,     W,     W,     W,     C_2,   B_2,   B_3,   C_2,   V_O],
    [V_O,   G_2,   O_2,   O_3,   W,     W,     W,     W,     W,     W,     V_1,   V_2,   V_3,   V_3,   V_O,   "."],
    [V_O,   V_O,   V_O,   V_O,   G_3,   P_1,   W,     W,     W,     W,     V_2,   V_3,   V_3,   V_O,   ".",   "."],
    [".",   ".",   ".",   V_O,   P_1,   P_2,   P_3,   P_1,   V_1,   V_2,   V_3,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_O,   P_2,   V_O,   P_3,   P_3,   V_2,   V_2,   V_3,   V_3,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_O,   V_O,   V_O,   P_3,   V_1,   V_2,   V_O,   V_O,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_O,   V_2,   V_3,   V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   V_3,   V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   V_O,   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 3: Classic Vanilla Cosmic Star
# Minecraft Vanilla 13x13 Nether Star silhouette, with 8-color Infinity Catalyst
# spectrum and sharp starlight core.
# ==============================================================================
grid_opt3 = [
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   P_2,   V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_O,   P_1,   W,     V_1,   V_O,   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_O,   R_2,   W,     V_2,   V_O,   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   V_O,   V_O,   R_1,   W,     W,     W,     B_1,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_O,   O_2,   O_1,   W,     W,     W,     W,     B_1,   B_2,   B_3,   V_O,   ".",   "."],
    [".",   ".",   V_O,   O_3,   O_2,   W,     W,     W,     W,     W,     W,     C_2,   C_3,   V_O,   ".",   "."],
    [".",   ".",   ".",   V_O,   G_2,   G_1,   W,     W,     W,     W,     C_1,   C_2,   C_3,   V_O,   ".",   "."],
    [".",   ".",   ".",   ".",   V_O,   V_O,   G_2,   W,     W,     W,     C_2,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_O,   G_3,   W,     L_2,   V_O,   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_O,   L_1,   L_2,   L_3,   V_O,   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   L_3,   V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 4: Stellar Prismatic Cross (Radial 4-Point Prism Star)
# Highly distinct: Cardinal 4 rays carry the cosmic elements:
# North: Solar Gold, East: Electric Cyan, South: Royal Violet, West: Neon Magenta
# Diagonal corners sparkle with white-hot stars.
# ==============================================================================
grid_opt4 = [
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   V_T,   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   W,     V_T,   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_T,   G_1,   G_2,   V_T,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   V_T,   V_T,   V_T,   G_1,   G_2,   G_3,   V_S,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   W,     P_1,   G_1,   W,     G_2,   C_1,   W,     C_2,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_T,   V_T,   P_2,   P_1,   W,     W,     C_1,   C_2,   C_2,   V_O,   ".",   ".",   "."],
    [".",   ".",   V_T,   P_3,   P_2,   P_2,   W,     W,     W,     W,     C_2,   C_2,   V_S,   V_O,   V_O,   V_O],
    [".",   V_T,   W,     P_2,   P_1,   W,     W,     W,     W,     W,     W,     C_1,   C_2,   C_3,   W,     V_O],
    [V_O,   P_3,   P_3,   P_3,   P_2,   W,     W,     W,     W,     W,     W,     C_2,   C_3,   C_3,   V_O,   "."],
    [V_O,   V_O,   V_O,   V_O,   P_3,   V_1,   W,     W,     W,     W,     C_3,   C_3,   C_3,   V_O,   ".",   "."],
    [".",   ".",   ".",   V_O,   V_2,   V_2,   V_1,   V_1,   V_1,   V_2,   V_3,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_O,   V_3,   V_O,   V_3,   V_2,   V_2,   V_2,   V_3,   V_3,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   V_O,   V_O,   V_O,   V_3,   V_2,   V_3,   V_O,   V_O,   V_O,   V_O,   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   V_O,   V_3,   W,     V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   V_3,   V_O,   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   V_O,   V_O,   ".",   ".",   ".",   ".",   ".",   "."]
]

save_sprite(grid_opt1, "opt1_chromatic_pinwheel_v3")
save_sprite(grid_opt2, "opt2_cosmic_nebula_drift_v3")
save_sprite(grid_opt3, "opt3_classic_vanilla_infinity_v3")
save_sprite(grid_opt4, "opt4_stellar_prismatic_cross_v3")
