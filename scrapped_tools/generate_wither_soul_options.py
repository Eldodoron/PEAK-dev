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
# Outlines: Deep Obsidian Nether Black
K_OUT = "#0E0914"  # Darkest border
K_SHD = "#191222"  # Shadow border
K_MID = "#281E33"  # Deep nether stone

# Soul Fire Cyan / Soul Glass Spectrum
S_WHT = "#FFFFFF"  # Pure specular glint
S_HLT = "#E0FAFF"  # Soft starlight cyan
S_LGT = "#7CE8FF"  # Bright soul fire cyan
S_MID = "#24BCE6"  # Rich soul cyan
S_DRK = "#12749E"  # Deep soul cyan
S_VOD = "#093D5C"  # Darkest soul abyss

# Wither Rose Petals (Dark Ash & Dried Blood Charcoal from Whimscape)
R_WHT = "#B89EB3"  # Petal edge specular
R_HLT = "#8C6E85"  # Rose ash highlight
R_LGT = "#5C4456"  # Rose petal mid
R_MID = "#3E2C3C"  # Dark petal
R_DRK = "#271A26"  # Deep shadow petal
R_BLK = "#140C15"  # Inky rose black

# Obsidian Gemstone Body (for Option 2 & 4)
O_HLT = "#5A4C63"  # Polished obsidian highlight
O_LGT = "#40344A"  # Obsidian facet mid
O_MID = "#2B2234"  # Deep obsidian
O_DRK = "#1A1322"  # Dark obsidian shadow

# ==============================================================================
# OPTION 1: Crystalline Soul Shard (Cyan Soul Crystal with Encased Wither Rose)
# Elongated hexagonal cut soul crystal, with layered dark Wither Rose blossom
# suspended inside. Symmetrical, balanced, crisp facets.
# ==============================================================================
grid_opt1 = [
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, S_WHT, S_HLT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, S_WHT, S_LGT, S_MID, S_DRK, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, S_WHT, S_LGT, R_DRK, R_MID, S_MID, S_DRK, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_HLT, S_LGT, R_MID, R_HLT, R_LGT, R_MID, S_MID, S_DRK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_WHT, R_MID, R_LGT, R_HLT, R_HLT, R_LGT, R_MID, S_DRK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_LGT, R_DRK, R_MID, R_LGT, R_LGT, R_MID, R_DRK, S_MID, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_LGT, R_BLK, R_DRK, R_MID, R_MID, R_DRK, R_BLK, S_MID, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_LGT, S_MID, R_BLK, R_DRK, R_DRK, R_BLK, S_MID, S_DRK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_MID, S_MID, S_LGT, R_BLK, R_BLK, S_MID, S_DRK, S_VOD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_MID, S_DRK, S_MID, S_MID, S_MID, S_DRK, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, S_DRK, S_DRK, S_DRK, S_DRK, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, S_DRK, S_VOD, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 2: Dark Netherite Gem (Obsidian Jewel with Glowing Cyan Rose Core)
# A faceted dark Netherite crystal where the Wither Rose is carved into the face
# and blazes with intense soul fire cyan from its heart.
# ==============================================================================
grid_opt2 = [
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, O_HLT, O_LGT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, O_HLT, O_LGT, O_MID, O_DRK, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, O_HLT, R_DRK, R_MID, R_HLT, R_MID, O_DRK, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, O_HLT, R_MID, R_LGT, S_LGT, S_HLT, R_LGT, R_MID, O_DRK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, O_LGT, R_LGT, S_LGT, S_WHT, S_WHT, S_LGT, R_MID, O_DRK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, O_LGT, R_MID, S_LGT, S_WHT, S_MID, S_MID, R_DRK, O_DRK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, O_MID, R_DRK, R_MID, S_MID, S_DRK, R_MID, R_DRK, O_DRK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, O_MID, O_MID, R_DRK, R_DRK, R_DRK, R_DRK, O_DRK, K_SHD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, O_MID, O_DRK, O_MID, S_MID, S_DRK, O_DRK, K_SHD, K_OUT, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, O_DRK, O_DRK, O_MID, S_DRK, O_DRK, K_SHD, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, O_DRK, K_SHD, K_SHD, K_SHD, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, K_SHD, K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 3: Occult Soul Rhombus (Geometric Diamond Cut with Rose Emblem)
# Balanced diamond/rhombus cut jewel with deep cyan facets, backlit by a white-hot
# soul core outlining the Wither Rose blossom.
# ==============================================================================
grid_opt3 = [
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, S_WHT, S_HLT, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, S_WHT, S_LGT, S_MID, S_DRK, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, S_WHT, S_LGT, R_DRK, R_MID, S_MID, S_DRK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, S_HLT, S_LGT, R_MID, R_HLT, R_LGT, R_MID, S_MID, S_DRK, K_OUT, ".",   ".",   "."],
    [".",   ".",   K_OUT, S_WHT, S_LGT, R_MID, R_LGT, S_HLT, S_LGT, R_MID, R_DRK, S_DRK, S_VOD, K_OUT, ".",   "."],
    [".",   K_OUT, S_WHT, S_LGT, R_LGT, R_HLT, S_LGT, S_WHT, S_WHT, S_LGT, R_MID, R_DRK, S_DRK, S_VOD, K_OUT, "."],
    [K_OUT, S_HLT, S_LGT, S_MID, R_MID, R_LGT, S_WHT, S_WHT, S_WHT, S_MID, R_MID, R_BLK, S_VOD, S_VOD, K_OUT, "."],
    [K_OUT, S_LGT, S_MID, S_MID, R_DRK, R_MID, S_LGT, S_MID, S_DRK, R_MID, R_DRK, R_BLK, S_VOD, S_VOD, K_OUT, "."],
    [".",   K_OUT, S_MID, S_DRK, S_MID, R_DRK, R_DRK, R_MID, R_DRK, R_DRK, R_BLK, S_VOD, S_VOD, K_OUT, ".",   "."],
    [".",   ".",   K_OUT, S_DRK, S_DRK, S_MID, R_BLK, R_DRK, R_BLK, S_DRK, S_VOD, S_VOD, K_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, S_DRK, S_DRK, S_DRK, R_BLK, S_DRK, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, S_DRK, S_VOD, S_VOD, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   K_OUT, S_VOD, S_VOD, S_VOD, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   K_OUT, S_VOD, K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   K_OUT, ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 4: Sculpted Obsidian Wither Rose (Blooming Jewel Flower)
# A stylized, blooming Wither Rose sculpted entirely out of dark obsidian crystal,
# featuring a bright cyan soul core burning at the heart of the flower.
# ==============================================================================
grid_opt4 = [
    [".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, R_HLT, R_LGT, K_OUT, K_OUT, R_HLT, R_LGT, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, R_WHT, R_HLT, R_LGT, R_MID, R_MID, R_HLT, R_LGT, R_MID, K_OUT, ".",   ".",   ".",   "."],
    [".",   K_OUT, R_HLT, R_LGT, R_MID, R_HLT, S_HLT, S_LGT, R_HLT, R_LGT, R_MID, R_DRK, K_OUT, ".",   ".",   "."],
    [".",   K_OUT, R_LGT, R_MID, S_HLT, S_LGT, S_WHT, S_WHT, S_LGT, S_MID, R_MID, R_DRK, K_OUT, ".",   ".",   "."],
    [".",   K_OUT, R_MID, R_DRK, S_LGT, S_WHT, S_WHT, S_WHT, S_MID, S_DRK, R_DRK, R_BLK, K_OUT, ".",   ".",   "."],
    [".",   ".",   K_OUT, R_MID, S_LGT, S_WHT, S_MID, S_DRK, S_DRK, R_DRK, R_BLK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, R_DRK, R_MID, S_MID, S_DRK, S_VOD, R_MID, R_DRK, R_BLK, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, R_DRK, R_BLK, R_DRK, R_DRK, R_BLK, R_BLK, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, R_BLK, R_DRK, R_DRK, R_BLK, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, K_OUT, R_BLK, R_BLK, R_BLK, R_BLK, K_OUT, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_LGT, S_MID, K_OUT, R_BLK, R_BLK, K_OUT, S_DRK, S_VOD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   K_OUT, S_WHT, S_LGT, S_MID, K_OUT, K_OUT, S_MID, S_DRK, S_VOD, K_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   ".",   K_OUT, S_MID, S_DRK, K_OUT, K_OUT, S_DRK, S_VOD, K_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   K_OUT, K_OUT, ".",   ".",   K_OUT, K_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

save_sprite(grid_opt1, "wither_opt1_encased_crystal")
save_sprite(grid_opt2, "wither_opt2_netherite_gem")
save_sprite(grid_opt3, "wither_opt3_soul_rhombus")
save_sprite(grid_opt4, "wither_opt4_sculpted_rose")
