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

# ==============================================================================
# Palette definitions based on Re-Avaritia Infinity Catalyst & Ingot
# ==============================================================================
# Void Outlines
V_BLK = "#0C0517"  # Deepest void
V_OUT = "#160A29"  # Void outline primary
V_MID = "#261242"  # Cosmic shadow
V_BLU = "#121A45"  # Upper void blue outline

# Pure Starlight Core
W_HOT = "#FFFFFF"  # Pure blinding white
W_HAL = "#F6F0FF"  # White starlight halo
W_GLW = "#E8DCFF"  # Soft starlight tint

# Solar Flare / Gold / Amber (Avaritia Top/Left)
G_LGT = "#FFF080"  # Starlight pale gold
G_MID = "#FFD034"  # Radiant gold
G_AMB = "#FFA51C"  # Fiery amber
G_ORG = "#EE6818"  # Cosmic ember orange
G_LIM = "#A8F544"  # Auroral lime spark

# Cosmic Neon Magenta / Rose (Avaritia Diagonal Heart)
M_LGT = "#FFA8DC"  # Soft cosmic pink
M_MID = "#FF52B5"  # Radiant neon magenta
M_DRK = "#D61F85"  # Deep cosmic magenta
M_VIO = "#99106E"  # Shadow magenta

# Astral Violet / Deep Nebula Purple (Avaritia Bottom/Right)
P_LGT = "#D98AFF"  # Astral lilac
P_MID = "#B044FF"  # Vivid astral violet
P_DRK = "#7818DE"  # Deep nebula purple
P_VOD = "#460A96"  # Void violet shadow

# Starlight Cyan / Auroral Azure (Avaritia High-energy Spark)
C_WHT = "#DCFFFF"  # Glint cyan
C_LGT = "#7DF4FF"  # Electric cyan
C_MID = "#26C8F0"  # Starlight azure
C_DRK = "#127CB8"  # Deep astral blue

# ==============================================================================
# OPTION 1: Whimscape Prismatic Star (Avaritia Re-color of Whimscape Nether Star)
# ==============================================================================
# Takes the exact faceted Whimscape Nether Star layout, but upgrades every facet
# to the authentic glowing Avaritia cosmic spectrum:
# White core, golden top solar flare, electric cyan right ray, magenta/violet bottom.
grid_opt1 = [
    [".",     ".",     ".",     ".",     ".",     ".",     V_BLU,   V_BLU,   ".",     ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_BLU,   W_HOT,   V_BLU,   ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_BLU,   G_LGT,   G_AMB,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     V_BLU,   V_BLU,   V_BLU,   V_BLU,   G_LGT,   G_AMB,   G_ORG,   V_MID,   V_OUT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_BLU,   G_LGT,   G_MID,   W_HOT,   W_HOT,   G_AMB,   G_ORG,   V_MID,   C_LGT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_BLU,   V_BLU,   G_MID,   G_LGT,   W_HOT,   W_HOT,   M_LGT,   C_LGT,   C_MID,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     V_BLU,   G_LIM,   G_LGT,   M_LGT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   C_LGT,   W_HOT,   V_MID,   V_OUT,   V_OUT,   V_OUT],
    [".",     V_BLU,   W_HOT,   W_HOT,   G_LGT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   C_LGT,   C_MID,   C_DRK,   C_LGT,   V_OUT],
    [V_OUT,   M_LGT,   M_MID,   M_MID,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   P_DRK,   P_DRK,   P_DRK,   V_OUT,   "."],
    [V_OUT,   V_OUT,   V_OUT,   V_OUT,   W_HOT,   M_MID,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   P_MID,   P_DRK,   P_DRK,   V_OUT,   ".",     "."],
    [".",     ".",     ".",     V_OUT,   M_MID,   M_DRK,   M_DRK,   W_HOT,   W_HOT,   P_LGT,   P_MID,   V_OUT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_OUT,   M_DRK,   V_OUT,   P_LGT,   P_MID,   P_MID,   P_DRK,   P_DRK,   P_DRK,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_OUT,   V_OUT,   V_OUT,   P_LGT,   P_MID,   P_DRK,   V_OUT,   V_OUT,   V_OUT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   P_MID,   P_DRK,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   P_DRK,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."]
]

# ==============================================================================
# OPTION 2: Cosmic Catalyst Nether Star (Vanilla Shape with Diagonal Catalyst Aura)
# ==============================================================================
# Uses Minecraft's classic 13x13 Nether Star silhouette, shaded with the exact
# diagonal celestial gradient of the Avaritia Infinity Catalyst:
# Amber/Gold/Lime at top-left, Blinding White Nova Core, Magenta/Violet/Cyan at bottom-right.
grid_opt2 = [
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   G_LGT,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   G_LGT,   W_HOT,   G_AMB,   V_OUT,   ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   G_MID,   W_HOT,   G_AMB,   V_OUT,   ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     V_OUT,   V_OUT,   G_LIM,   G_LGT,   W_HOT,   W_HOT,   G_AMB,   V_OUT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     V_OUT,   G_LIM,   G_LGT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   M_LGT,   M_MID,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     V_OUT,   G_LGT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   M_MID,   M_DRK,   P_DRK,   V_OUT,   ".",     "."],
    [".",     ".",     ".",     V_OUT,   G_AMB,   G_AMB,   W_HOT,   W_HOT,   M_MID,   M_MID,   P_MID,   P_DRK,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     ".",     V_OUT,   V_OUT,   M_MID,   M_MID,   P_LGT,   P_MID,   P_DRK,   V_OUT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   M_DRK,   P_MID,   P_DRK,   V_OUT,   ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   P_MID,   P_DRK,   P_VOD,   V_OUT,   ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   P_DRK,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     "."]
]

# ==============================================================================
# OPTION 3: Symmetrical Prismatic Nova Star (4-Way Balanced Chromatic Rays)
# ==============================================================================
# Perfectly centered 16x16 cross star with 4 cardinal rays channeling the cosmic
# spectrum outward from a pure white diamond core:
# North: Solar Gold, East: Starlight Cyan, South: Astral Violet, West: Cosmic Magenta.
grid_opt3 = [
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   V_OUT,   ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     W_HOT,   G_LGT,   ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   G_LGT,   G_MID,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     V_OUT,   G_LGT,   G_MID,   G_AMB,   G_LGT,   V_OUT,   ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     V_OUT,   M_LGT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   C_LGT,   V_OUT,   ".",     ".",     ".",     "."],
    [".",     ".",     ".",     V_OUT,   M_LGT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   C_LGT,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     V_OUT,   M_LGT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   C_LGT,   V_OUT,   ".",     "."],
    [V_OUT,   W_HOT,   M_LGT,   M_MID,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   C_MID,   C_LGT,   W_HOT,   V_OUT],
    [V_OUT,   W_HOT,   M_MID,   M_DRK,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   C_MID,   C_DRK,   W_HOT,   V_OUT],
    [".",     ".",     V_OUT,   M_DRK,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   C_DRK,   V_OUT,   ".",     "."],
    [".",     ".",     ".",     V_OUT,   M_DRK,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   C_DRK,   V_OUT,   ".",     ".",     "."],
    [".",     ".",     ".",     ".",     V_OUT,   P_LGT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   P_LGT,   V_OUT,   ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     V_OUT,   P_LGT,   P_MID,   P_DRK,   P_LGT,   V_OUT,   ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   P_MID,   P_DRK,   V_OUT,   ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     P_MID,   P_DRK,   ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     V_OUT,   V_OUT,   ".",     ".",     ".",     ".",     ".",     ".",     "."]
]

# ==============================================================================
# OPTION 4: Gilded Infinity Relic Star (Solar Gold Armor × Pulsing Cosmic Nebula)
# ==============================================================================
# Outer star facets framed in celestial gold (matching §6 Gold in item title),
# with the inner starlight core pulsating with Avaritia cosmic rainbow energy.
GLD_H = "#FFF5A6"
GLD_1 = "#FFD642"
GLD_2 = "#E69C17"
GLD_3 = "#8A5408"
GLD_OUT = "#2B1602"

grid_opt4 = [
    [".",     ".",     ".",     ".",     ".",     ".",     GLD_OUT, GLD_OUT, ".",     ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     GLD_OUT, GLD_H,   GLD_OUT, ".",     ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     GLD_OUT, GLD_1,   GLD_2,   GLD_OUT, ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     GLD_OUT, GLD_OUT, GLD_OUT, GLD_OUT, GLD_1,   GLD_2,   GLD_3,   GLD_OUT, GLD_OUT, GLD_OUT, ".",     ".",     "."],
    [".",     ".",     ".",     GLD_OUT, GLD_H,   GLD_1,   W_HOT,   W_HOT,   C_LGT,   GLD_2,   GLD_OUT, GLD_1,   GLD_OUT, ".",     ".",     "."],
    [".",     ".",     ".",     GLD_OUT, GLD_OUT, GLD_1,   W_HOT,   W_HOT,   W_HOT,   C_MID,   GLD_1,   GLD_2,   GLD_OUT, ".",     ".",     "."],
    [".",     ".",     GLD_OUT, GLD_H,   GLD_1,   M_LGT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   C_LGT,   GLD_1,   GLD_OUT, GLD_OUT, GLD_OUT, GLD_OUT],
    [".",     GLD_OUT, GLD_H,   GLD_1,   M_MID,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   GLD_1,   GLD_2,   GLD_3,   GLD_1,   GLD_OUT],
    [GLD_OUT, GLD_H,   GLD_1,   M_MID,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   W_HOT,   GLD_2,   GLD_3,   GLD_OUT, GLD_OUT, "."],
    [GLD_OUT, GLD_OUT, GLD_OUT, GLD_OUT, W_HOT,   M_MID,   W_HOT,   W_HOT,   W_HOT,   P_MID,   GLD_2,   GLD_3,   GLD_OUT, GLD_OUT, ".",     "."],
    [".",     ".",     ".",     GLD_OUT, M_MID,   M_DRK,   P_LGT,   W_HOT,   W_HOT,   P_MID,   GLD_2,   GLD_OUT, GLD_OUT, ".",     ".",     "."],
    [".",     ".",     ".",     GLD_OUT, M_DRK,   GLD_OUT, P_MID,   P_MID,   P_DRK,   GLD_2,   GLD_3,   GLD_OUT, ".",     ".",     ".",     "."],
    [".",     ".",     ".",     GLD_OUT, GLD_OUT, GLD_OUT, P_MID,   P_DRK,   GLD_3,   GLD_OUT, GLD_OUT, GLD_OUT, GLD_OUT, ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     GLD_OUT, GLD_2,   GLD_3,   GLD_OUT, ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     GLD_OUT, GLD_3,   GLD_OUT, ".",     ".",     ".",     ".",     ".",     "."],
    [".",     ".",     ".",     ".",     ".",     ".",     ".",     ".",     GLD_OUT, GLD_OUT, ".",     ".",     ".",     ".",     ".",     "."]
]

save_sprite(grid_opt1, "opt1_whimscape_prismatic")
save_sprite(grid_opt2, "opt2_catalyst_nether_star")
save_sprite(grid_opt3, "opt3_symmetrical_nova")
save_sprite(grid_opt4, "opt4_gilded_infinity_relic")
