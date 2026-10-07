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
# Palette Definitions
# ==============================================================================
# Deep Void / Netherite Black
K_OUT = "#0E0914"  # Darkest border
K_SHD = "#191222"  # Shadow border
K_DRK = "#241A2E"  # Dark Netherite facet
K_MID = "#362842"  # Netherite facet mid
K_LGT = "#4F3C5E"  # Netherite facet light
K_HLT = "#705882"  # Netherite specular edge

# Soul Fire Cyan Spectrum
S_WHT = "#FFFFFF"  # Pure specular glint
S_HLT = "#E2FAFF"  # Glint cyan
S_LGT = "#76EBFF"  # Bright soul fire
S_MID = "#22BAE6"  # Rich soul cyan
S_DRK = "#12729C"  # Deep soul cyan
S_VOD = "#093F5E"  # Abyssal soul blue

# Wither Rose Petals (Whimscape Charcoal & Rose Ash)
R_WHT = "#BFA6BA"  # Rose specular
R_HLT = "#8C6E85"  # Rose ash highlight
R_LGT = "#5C4656"  # Petal mid
R_MID = "#3E2D3A"  # Dark petal
R_DRK = "#271A24"  # Deep petal shadow
R_BLK = "#140B13"  # Inky black

# Wither Thorns & Stem
T_LGT = "#3F4522"  # Withered green leaf/stem
T_DRK = "#20260F"  # Deep shadow stem

# ==============================================================================
# OPTION 1: The Preserved Rose Crystal (Faceted Cyan Soul Glass)
# Elongated hexagonal soul crystal, holding a dark fossilized Wither Rose inside.
# Balanced, clean symmetry, crisp crystal facets.
# ==============================================================================
grid_opt1 = [
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, S_WHT, S_HLT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, S_WHT, S_LGT, S_MID, S_DRK, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, S_WHT, S_LGT, R_MID, R_HLT, R_LGT, S_DRK, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_HLT, S_LGT, R_HLT, R_LGT, R_MID, R_HLT, R_LGT, S_DRK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_WHT, R_MID, R_LGT, R_MID, R_LGT, R_MID, R_DRK, S_DRK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_LGT, R_DRK, R_MID, R_DRK, R_DRK, R_MID, R_BLK, S_MID, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_LGT, S_MID, R_BLK, T_DRK, T_DRK, R_BLK, S_MID, S_DRK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_LGT, S_MID, T_LGT, T_DRK, T_DRK, S_MID, S_MID, S_DRK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_MID, S_MID, S_LGT, T_DRK, T_LGT, S_DRK, S_DRK, S_VOD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_MID, S_DRK, S_MID, T_DRK, S_MID, S_DRK, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_DRK, S_DRK, S_DRK, S_DRK, S_DRK, S_VOD, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, S_DRK, S_DRK, S_VOD, S_VOD, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, S_VOD, S_VOD, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 2: Netherite Soul Inlay (Dark Nether Crystal with Glowing Rose Inlay)
# Polished obsidian/netherite crystal with an intricate glowing cyan soul-fire
# Wither Rose engraved into the dark crystalline facet.
# ==============================================================================
grid_opt2 = [
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, K_HLT, K_LGT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, K_HLT, K_LGT, K_MID, K_DRK, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, K_HLT, K_LGT, S_DRK, S_MID, K_MID, K_DRK, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_HLT, K_LGT, S_MID, S_LGT, S_MID, S_DRK, K_DRK, K_SHD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_LGT, S_MID, S_LGT, S_WHT, S_LGT, S_MID, S_DRK, K_SHD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_LGT, S_DRK, S_MID, S_LGT, S_MID, S_DRK, S_DRK, K_SHD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_MID, K_DRK, S_DRK, S_MID, S_DRK, S_DRK, K_SHD, K_SHD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_MID, K_DRK, K_DRK, S_MID, S_DRK, K_SHD, K_SHD, K_SHD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_MID, K_DRK, S_DRK, S_MID, K_DRK, S_DRK, K_SHD, K_SHD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_DRK, K_SHD, K_MID, S_MID, S_DRK, K_SHD, K_SHD, K_SHD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_DRK, K_SHD, K_SHD, S_DRK, K_SHD, K_SHD, K_SHD, K_SHD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, K_SHD, K_SHD, K_SHD, K_SHD, K_SHD, K_SHD, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, K_SHD, K_SHD, K_SHD, K_SHD, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, K_SHD, K_SHD, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 3: Crystallized Wither Rose (Sculpted Obsidian Blossom with Soul Core)
# A blooming Wither Rose sculpted out of black obsidian petals with crisp ash
# facets, cradling a glowing cyan soul core at its heart.
# ==============================================================================
grid_opt3 = [
    [".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, R_HLT, R_LGT, K_OUT, K_OUT, R_HLT, R_LGT, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, R_WHT, R_HLT, R_LGT, R_MID, R_MID, R_HLT, R_LGT, R_MID, K_OUT, ".",   ".",   ".",   "."],
    [".",   K_OUT, R_HLT, R_LGT, R_MID, S_MID, S_LGT, S_HLT, S_MID, R_LGT, R_MID, R_DRK, K_OUT, ".",   ".",   "."],
    [".",   K_OUT, R_LGT, R_MID, S_LGT, S_WHT, S_WHT, S_WHT, S_LGT, S_MID, R_MID, R_DRK, K_OUT, ".",   ".",   "."],
    [".",   K_OUT, R_MID, R_DRK, S_HLT, S_WHT, S_WHT, S_WHT, S_MID, S_DRK, R_DRK, R_BLK, K_OUT, ".",   ".",   "."],
    [".",   K_OUT, R_MID, R_DRK, S_LGT, S_WHT, S_MID, S_DRK, S_DRK, R_DRK, R_BLK, R_BLK, K_OUT, ".",   ".",   "."],
    [".",   ".",   K_OUT, R_DRK, R_MID, S_MID, S_DRK, S_VOD, R_MID, R_DRK, R_BLK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, R_DRK, R_BLK, R_DRK, R_DRK, R_BLK, R_BLK, R_DRK, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, R_BLK, R_DRK, R_DRK, R_BLK, R_BLK, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, T_LGT, T_DRK, T_DRK, T_LGT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, T_LGT, T_DRK, S_LGT, S_MID, T_DRK, T_LGT, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, T_DRK, S_LGT, S_WHT, S_LGT, S_MID, T_DRK, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, T_DRK, S_MID, S_DRK, T_DRK, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, T_DRK, T_DRK, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 4: Necrotic Soul Rhombus (Diamond-Cut Gem with Backlit Rose)
# Crisp 45° diamond-cut soul crystal with deep abyssal cyan facets,
# enclosing a dark Wither Rose backlit by an ethereal soul fire heart.
# ==============================================================================
grid_opt4 = [
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, S_WHT, S_HLT, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, S_WHT, S_LGT, S_MID, S_DRK, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, S_HLT, S_LGT, R_DRK, R_MID, S_MID, S_DRK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, S_WHT, S_LGT, R_MID, R_HLT, R_LGT, R_MID, S_DRK, S_VOD, K_OUT, ".",   ".",   "."],
    [".",   ".",   K_OUT, S_HLT, S_LGT, R_MID, R_LGT, S_HLT, S_LGT, R_MID, R_DRK, S_DRK, S_VOD, K_OUT, ".",   "."],
    [".",   K_OUT, S_WHT, S_LGT, R_LGT, R_HLT, S_LGT, S_WHT, S_WHT, S_LGT, R_MID, R_DRK, S_DRK, S_VOD, K_OUT, "."],
    [K_OUT, S_HLT, S_LGT, S_MID, R_MID, R_LGT, S_WHT, S_WHT, S_WHT, S_MID, R_MID, R_BLK, S_VOD, S_VOD, K_OUT, "."],
    [K_OUT, S_LGT, S_MID, S_MID, R_DRK, R_MID, S_LGT, S_MID, S_DRK, R_MID, R_DRK, R_BLK, S_VOD, S_VOD, K_OUT, "."],
    [".",   K_OUT, S_MID, S_DRK, S_MID, R_DRK, R_DRK, T_LGT, T_DRK, R_DRK, R_BLK, S_VOD, S_VOD, K_OUT, ".",   "."],
    [".",   ".",   K_OUT, S_DRK, S_DRK, S_MID, T_DRK, T_DRK, T_DRK, S_DRK, S_VOD, S_VOD, K_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, S_DRK, S_DRK, S_DRK, T_DRK, S_DRK, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, S_DRK, S_VOD, S_VOD, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, S_VOD, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, S_VOD, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

save_sprite(grid_opt1, "wither_soul_opt1_preserved_crystal")
save_sprite(grid_opt2, "wither_soul_opt2_netherite_inlay")
save_sprite(grid_opt3, "wither_soul_opt3_crystallized_rose")
save_sprite(grid_opt4, "wither_soul_opt4_necrotic_rhombus")
