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
K_OUT = "#0D0814"  # Outermost border
K_SHD = "#181120"  # Shadow border
K_DRK = "#22192B"  # Dark Netherite facet
K_MID = "#33263E"  # Netherite facet mid
K_LGT = "#4B3B59"  # Netherite facet light
K_HLT = "#6A557D"  # Netherite specular edge

# Soul Fire Cyan Glass
S_WHT = "#FFFFFF"  # Pure specular glint
S_HLT = "#E0FAFF"  # Glint cyan
S_LGT = "#72EAFF"  # Bright soul fire
S_MID = "#20BAE6"  # Rich soul cyan
S_DRK = "#10729C"  # Deep soul cyan
S_VOD = "#093F5E"  # Abyssal soul blue

# Wither Rose Petals (Obsidian Charcoal & Ashen Rose)
R_WHT = "#BFA6BA"  # Rose specular
R_HLT = "#8C6E85"  # Rose ash highlight
R_LGT = "#5C4656"  # Petal mid
R_MID = "#3E2D3A"  # Dark petal
R_DRK = "#261A24"  # Deep petal shadow
R_BLK = "#140B13"  # Inky black

# Wither Thorns & Stem
T_LGT = "#3F4522"  # Withered green leaf/stem
T_DRK = "#20260F"  # Deep shadow stem

# ==============================================================================
# OPTION 1: The Preserved Rose Crystal (Faceted Soul Glass with Whole Rose)
# An elongated, multi-faceted soul crystal holding a complete, distinct Wither Rose:
# layered dark blossom, thorny stem, and withered leaves encased inside glowing glass.
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
    [".",   ".",   ".",   K_OUT, S_DRK, S_DRK, S_DRK, S_DRK, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, S_DRK, S_VOD, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 2: Netherite Inlay Jewel (Dark Obsidian Gem with Glowing Soul Rose Inlay)
# The jewel itself is chiseled Netherite / Obsidian, with a glowing Soul Fire
# Wither Rose inlaid into the polished dark facet.
# ==============================================================================
grid_opt2 = [
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, K_HLT, K_LGT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, K_HLT, K_LGT, K_MID, K_DRK, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, K_HLT, K_LGT, S_DRK, S_MID, K_MID, K_DRK, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_HLT, K_LGT, S_MID, S_LGT, S_MID, S_DRK, K_DRK, K_SHD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_LGT, S_MID, S_LGT, S_WHT, S_LGT, S_MID, S_DRK, K_SHD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_LGT, S_DRK, S_MID, S_LGT, S_MID, S_DRK, S_DRK, K_SHD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_MID, K_DRK, S_DRK, S_MID, S_DRK, S_DRK, K_SHD, K_OUT, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_MID, K_DRK, K_DRK, S_MID, S_DRK, K_SHD, K_SHD, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_MID, K_DRK, S_DRK, S_MID, K_DRK, S_DRK, K_SHD, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, K_DRK, K_SHD, K_MID, S_MID, S_DRK, K_SHD, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, K_DRK, K_SHD, S_DRK, K_SHD, K_SHD, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, K_SHD, K_SHD, K_SHD, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, K_SHD, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 3: Wither Rose Geode (Crystallized Obsidian Rose with Soul Gem Core)
# The flower itself is sculpted of dark obsidian crystal petals, opening up to
# reveal a sparkling cyan soul fire crystal nestled in the center.
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
# OPTION 4: Necrotic Diamond Soul Gem (Backlit Rose in Rhombus Cut)
# Symmetrical, crisp diamond-cut jewel of deep soul cyan, featuring a dark
# Wither Rose silhouette perfectly centered and backlit by a white soul spark.
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

save_sprite(grid_opt1, "wither_opt1_preserved_crystal")
save_sprite(grid_opt2, "wither_opt2_netherite_inlay")
save_sprite(grid_opt3, "wither_opt3_rose_geode")
save_sprite(grid_opt4, "wither_opt4_necrotic_diamond")
