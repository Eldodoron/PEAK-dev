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

# Core White & Halos
W_CORE = "#FFFFFF"  # Blinding white
W_HALO = "#FFF6FD"  # Warm starlight
W_ICE  = "#F0FDFF"  # Cool starlight
W_LIL  = "#F7EEFF"  # Soft astral starlight

# Dark Void / Cosmic Indigo Outline
V_OUT  = "#150A26"  # Deep space void
V_TOP  = "#1B1842"  # Void azure outline (top)
V_MID  = "#26103E"  # Cosmic shadow
V_DRK  = "#0E051C"  # Obsidian black

# ==============================================================================
# Palette 1: 8-Ray Infinity Catalyst Colors
# ==============================================================================
# 1. North: Hot Pink / Radiant Magenta
PNK_L = "#FFA3D8"
PNK_M = "#FF3D9E"
PNK_D = "#C71872"

# 2. North-East: Astral Violet
VIO_L = "#DA8CFF"
VIO_M = "#A836FF"
VIO_D = "#7212DC"

# 3. East: Cobalt / Starlight Blue
BLU_L = "#99BCFF"
BLU_M = "#487DFF"
BLU_D = "#1C47D6"

# 4. South-East: Electric Cyan / Teal
CYN_L = "#94F7F2"
CYN_M = "#30D4CE"
CYN_D = "#128C88"

# 5. South: Auroral Emerald / Lime
LME_L = "#B8FF6E"
LME_M = "#76E832"
LME_D = "#3EA818"

# 6. South-West: Solar Gold / Amber
GLD_L = "#FFE875"
GLD_M = "#FFBA24"
GLD_D = "#D9800D"

# 7. West: Fiery Orange / Solar Flare
ORG_L = "#FFA866"
ORG_M = "#FF6E1C"
ORG_D = "#C43E08"

# 8. North-West: Radiant Coral / Crimson Spark
CRL_L = "#FFA1AA"
CRL_M = "#FF425E"
CRL_D = "#C21532"

# ==============================================================================
# OPTION 1: Chromatic Pinwheel Nether Star
# Exact 8-ray Infinity Catalyst mapping onto Whimscape's Nether Star facets
# ==============================================================================
grid_opt1 = [
    [".",     ".",     ".",     ".",     ".",     ".",     V_TOP,   V_TOP,   ".",     ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_TOP,   W_CORE,  V_TOP,   ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_TOP,   PNK_L,   VIO_L,   V_TOP,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     V_TOP,   V_TOP,   V_TOP,   V_TOP,   PNK_M,   VIO_M,   VIO_D,   V_MID,   V_OUT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_TOP,   CRL_L,   CRL_M,   W_HALO,  W_HALO,  VIO_L,   VIO_M,   V_MID,   BLU_L,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_TOP,   V_TOP,   CRL_M,   CRL_L,   W_CORE,  W_CORE,  BLU_L,   BLU_L,   BLU_M,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     V_TOP,   ORG_L,   ORG_L,   CRL_M,   W_HALO,  W_CORE,  W_CORE,  W_HALO,  BLU_M,   W_ICE,   V_MID,   V_OUT,   V_OUT,   V_OUT],
    [".",     V_TOP,   W_CORE,  W_CORE,  ORG_L,   W_HALO,  W_CORE,  W_CORE,  W_CORE,  W_CORE,  W_HALO,  CYN_L,   CYN_M,   CYN_D,   CYN_L,   V_OUT],
    [V_OUT,   ORG_M,   ORG_D,   ORG_D,   W_HALO,  W_HALO,  W_CORE,  W_CORE,  W_CORE,  W_CORE,  W_HALO,  CYN_M,   CYN_M,   CYN_D,   V_OUT,   "."],
    [V_OUT,   V_OUT,   V_OUT,   V_OUT,   W_HALO,  GLD_L,   W_HALO,  W_CORE,  W_CORE,  W_HALO,  CYN_D,   CYN_D,   LME_D,   V_OUT,   ".",     "."],
    [".",     ".",     ".",     V_OUT,   GLD_L,   GLD_M,   GLD_D,   W_HALO,  W_HALO,  LME_L,   LME_M,   V_OUT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_OUT,   GLD_M,   V_OUT,   GLD_D,   GLD_D,   LME_L,   LME_M,   LME_D,   LME_D,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_OUT,   V_OUT,   V_OUT,   GLD_D,   LME_L,   LME_M,   V_OUT,   V_OUT,   V_OUT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   LME_M,   LME_D,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   LME_D,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."]
]

# ==============================================================================
# OPTION 2: Cosmic Nebula Drift (Dynamic Diagonal Flow on Whimscape Star)
# Amber/Gold/Lime at top-left -> Blinding White Core -> Magenta/Violet/Cyan at bottom-right
# Shaded with subtle crystalline facets like Whimscape
# ==============================================================================
grid_opt2 = [
    [".",     ".",     ".",     ".",     ".",     ".",     V_TOP,   V_TOP,   ".",     ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_TOP,   W_CORE,  V_TOP,   ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_TOP,   GLD_L,   GLD_M,   V_TOP,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     V_TOP,   V_TOP,   V_TOP,   V_TOP,   GLD_L,   GLD_M,   ORG_M,   V_MID,   V_OUT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_TOP,   LME_L,   GLD_L,   W_HALO,  W_HALO,  GLD_M,   ORG_M,   V_MID,   CYN_L,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_TOP,   V_TOP,   LME_M,   GLD_L,   W_CORE,  W_CORE,  CYN_L,   CYN_L,   CYN_M,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     V_TOP,   LME_L,   GLD_L,   GLD_M,   W_HALO,  W_CORE,  W_CORE,  W_HALO,  CYN_M,   W_ICE,   V_MID,   V_OUT,   V_OUT,   V_OUT],
    [".",     V_TOP,   W_CORE,  W_CORE,  GLD_L,   W_HALO,  W_CORE,  W_CORE,  W_CORE,  W_CORE,  W_HALO,  CYN_M,   BLU_M,   BLU_D,   CYN_L,   V_OUT],
    [V_OUT,   GLD_M,   ORG_M,   ORG_D,   W_HALO,  W_HALO,  W_CORE,  W_CORE,  W_CORE,  W_CORE,  W_HALO,  VIO_M,   VIO_D,   VIO_D,   V_OUT,   "."],
    [V_OUT,   V_OUT,   V_OUT,   V_OUT,   W_HALO,  PNK_L,   W_HALO,  W_CORE,  W_CORE,  W_HALO,  PNK_D,   VIO_D,   VIO_D,   V_OUT,   ".",     "."],
    [".",     ".",     ".",     V_OUT,   PNK_L,   PNK_M,   PNK_D,   W_HALO,  W_HALO,  VIO_L,   VIO_M,   V_OUT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_OUT,   PNK_M,   V_OUT,   PNK_D,   PNK_D,   VIO_M,   VIO_M,   VIO_D,   VIO_D,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_OUT,   V_OUT,   V_OUT,   PNK_D,   VIO_L,   VIO_M,   V_OUT,   V_OUT,   V_OUT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   VIO_M,   VIO_D,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   VIO_D,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."]
]

# ==============================================================================
# OPTION 3: Classic Vanilla Cosmic Star
# Minecraft 13x13 Vanilla Nether Star silhouette with full 8-color Infinity Rainbow
# ==============================================================================
grid_opt3 = [
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   PNK_L,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   PNK_L,   W_CORE,  VIO_L,   V_OUT,   ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   CRL_M,   W_CORE,  VIO_M,   V_OUT,   ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     V_OUT,   V_OUT,   ORG_L,   W_HALO,  W_CORE,  W_HALO,  BLU_L,   V_OUT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_OUT,   ORG_L,   ORG_M,   W_HALO,  W_CORE,  W_CORE,  W_CORE,  W_HALO,  BLU_M,   BLU_D,   V_OUT,   ".",     "."],
    [".",     ".",     V_OUT,   ORG_M,   W_CORE,  W_CORE,  W_CORE,  W_CORE,  W_CORE,  W_CORE,  W_CORE,  W_CORE,  CYN_M,   CYN_D,   V_OUT,   "."],
    [".",     ".",     ".",     V_OUT,   GLD_L,   GLD_M,   W_HALO,  W_CORE,  W_CORE,  W_CORE,  W_HALO,  CYN_M,   CYN_D,   V_OUT,   ".",     "."],
    [".",     ".",     ".",     ".",     V_OUT,   V_OUT,   GLD_M,   W_HALO,  W_CORE,  W_HALO,  CYN_L,   V_OUT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   GLD_D,   W_CORE,  LME_M,   V_OUT,   ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   LME_L,   LME_M,   LME_D,   V_OUT,   ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   LME_M,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     "."]
]

# ==============================================================================
# OPTION 4: Gilded Infinity Relic Star
# Whimscape Nether Star chassis in Solar Gold, holding the 8-ray Infinity Core
# ==============================================================================
GLD_H = "#FFF8B8"  # Highlight gold
GLD_1 = "#FFD84A"  # Primary bright gold
GLD_2 = "#E0981B"  # Warm amber gold
GLD_3 = "#8C5209"  # Shadow gold
GLD_O = "#2E1803"  # Deep gold-bronze outline

grid_opt4 = [
    [".",     ".",     ".",     ".",     ".",     ".",     GLD_O,   GLD_O,   ".",     ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     GLD_O,   GLD_H,   GLD_O,   ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     GLD_O,   GLD_1,   GLD_2,   GLD_O,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     GLD_O,   GLD_O,   GLD_O,   GLD_O,   GLD_1,   GLD_2,   GLD_3,   GLD_O,   GLD_O,   GLD_O,   ".",     ".",     "."],
    [".",     ".",     ".",     GLD_O,   GLD_H,   GLD_1,   W_HALO,  W_HALO,  VIO_L,   GLD_2,   GLD_O,   GLD_1,   GLD_O,   ".",     ".",     "."],
    [".",     ".",     ".",     GLD_O,   GLD_O,   GLD_1,   PNK_L,   W_CORE,  W_CORE,  CYN_L,   GLD_1,   GLD_2,   GLD_O,   ".",     ".",     "."],
    [".",     ".",     GLD_O,   GLD_H,   GLD_1,   ORG_L,   W_HALO,  W_CORE,  W_CORE,  W_HALO,  CYN_M,   GLD_1,   GLD_O,   GLD_O,   GLD_O,   GLD_O],
    [".",     GLD_O,   GLD_H,   GLD_1,   ORG_M,   W_HALO,  W_CORE,  W_CORE,  W_CORE,  W_CORE,  W_HALO,  GLD_1,   GLD_2,   GLD_3,   GLD_1,   GLD_O],
    [GLD_O,   GLD_H,   GLD_1,   ORG_D,   W_HALO,  W_HALO,  W_CORE,  W_CORE,  W_CORE,  W_CORE,  W_HALO,  GLD_2,   GLD_3,   GLD_O,   GLD_O,   "."],
    [GLD_O,   GLD_O,   GLD_O,   GLD_O,   W_HALO,  GLD_L,   W_HALO,  W_CORE,  W_CORE,  W_HALO,  VIO_D,   GLD_3,   GLD_O,   GLD_O,   ".",     "."],
    [".",     ".",     ".",     GLD_O,   GLD_L,   GLD_M,   GLD_D,   W_HALO,  W_HALO,  LME_L,   GLD_2,   GLD_O,   GLD_O,   ".",     ".",     "."],
    [".",     ".",     ".",     GLD_O,   GLD_M,   GLD_O,   GLD_D,   GLD_D,   LME_M,   LME_D,   GLD_2,   GLD_3,   GLD_O,   ".",     ".",     "."],
    [".",     ".",     ".",     GLD_O,   GLD_O,   GLD_O,   GLD_D,   LME_M,   LME_D,   GLD_O,   GLD_O,   GLD_O,   GLD_O,   ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     GLD_O,   GLD_2,   GLD_3,   GLD_O,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     GLD_O,   GLD_3,   GLD_O,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     GLD_O,   GLD_O,   ".",     ".",     ".",     ".",     ".",     "."]
]

save_sprite(grid_opt1, "opt1_chromatic_pinwheel")
save_sprite(grid_opt2, "opt2_cosmic_nebula_drift")
save_sprite(grid_opt3, "opt3_classic_vanilla_infinity")
save_sprite(grid_opt4, "opt4_gilded_infinity_relic")
