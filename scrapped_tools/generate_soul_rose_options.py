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
# Wither Stem & Leaves Palette (Obsidian / Wither Bone / Deep Nether Charcoal)
W_OUT = "#0F0B14"  # Darkest outline
W_SHD = "#1B1522"  # Shadow leaf/stem
W_DRK = "#292033"  # Dark stem
W_MID = "#3E324C"  # Mid stem
W_LGT = "#59496B"  # Highlight stem
W_HLT = "#78658F"  # Brightest edge highlight

# Soul Blue / Celeste Palette (Option 1: Faithful Grade)
S1_WHT = "#FFFFFF"  # Specular edge
S1_HLT = "#E0FAFF"  # Pale celeste highlight
S1_LGT = "#82EFFF"  # Bright celeste
S1_MID = "#34C6EB"  # Rich soul blue
S1_DRK = "#1680A6"  # Deep soul cyan
S1_VOD = "#0E4866"  # Shadow cyan
S1_OUT = "#0A2436"  # Darkest soul border

# ==============================================================================
# OPTION 1: Faithful Soul Rose (Direct Color Grade of Whimscape Rose)
# Direct 1:1 color grade mapping Whimscape's wither rose petal ramp to soul blue/celeste,
# and green stem ramp to Wither charcoal/obsidian.
# ==============================================================================
# Whimscape original mapping:
# Petals:
# #9E7E73 -> S1_HLT (highlight)
# #72625E -> S1_LGT (light petal)
# #674649 -> S1_MID (mid petal)
# #493A3B -> S1_DRK (shadow petal)
# #332B34 -> S1_VOD (deep shadow petal)
# #1D1720 -> S1_OUT / W_OUT (outline / crease)
# Stem & Leaves:
# #ABA130 -> W_HLT
# #7F8024 -> W_LGT
# #404D18 -> W_MID
# #273D18 -> W_DRK
# #193012 -> W_SHD
# #032620 -> W_OUT

grid_opt1 = [
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   S1_VOD,S1_VOD,S1_VOD,S1_VOD,".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   S1_VOD,S1_MID,S1_VOD,S1_LGT,S1_LGT,S1_VOD,".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   S1_VOD,S1_LGT,S1_OUT,S1_OUT,S1_VOD,S1_VOD,S1_MID,S1_OUT,".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   S1_VOD,S1_LGT,S1_LGT,S1_HLT,S1_HLT,S1_MID,S1_MID,S1_OUT,".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   S1_OUT,S1_DRK,S1_DRK,S1_VOD,S1_OUT,S1_OUT,".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   S1_OUT,S1_DRK,S1_DRK,S1_VOD,S1_VOD,S1_OUT,".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   S1_OUT,S1_OUT,S1_OUT,S1_OUT,".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   W_SHD, W_DRK, W_OUT, W_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   W_SHD, W_SHD, W_MID, W_LGT, W_LGT, W_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   W_SHD, W_LGT, W_LGT, W_MID, W_DRK, W_MID, W_MID, W_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   W_SHD, W_LGT, W_LGT, W_MID, W_OUT, W_MID, W_MID, W_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   ".",   W_SHD, W_HLT, W_LGT, W_OUT, W_MID, W_OUT, W_OUT, W_OUT, W_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   ".",   W_OUT, W_OUT, W_OUT, W_OUT, W_DRK, W_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   W_OUT, W_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 2: Luminous Soul Flame Rose (Glowing Celeste Bloom with White Core)
# High-energy bioluminescent petals with a brilliant starlight white heart,
# glowing electric cyan outer petals, and a dark obsidian/wither stem.
# ==============================================================================
S2_WHT = "#FFFFFF"
S2_HLT = "#E6FBFF"
S2_CYN = "#7DF0FF"
S2_MID = "#20C2EB"
S2_DRK = "#107AA6"
S2_VOD = "#0A466B"
S2_OUT = "#062238"

grid_opt2 = [
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   S2_VOD,S2_VOD,S2_VOD,S2_VOD,".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   S2_VOD,S2_MID,S2_VOD,S2_CYN,S2_CYN,S2_VOD,".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   S2_VOD,S2_CYN,S2_OUT,S2_OUT,S2_VOD,S2_VOD,S2_MID,S2_OUT,".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   S2_VOD,S2_CYN,S2_HLT,S2_WHT,S2_WHT,S2_CYN,S2_MID,S2_OUT,".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   S2_OUT,S2_MID,S2_CYN,S2_MID,S2_DRK,S2_OUT,".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   S2_OUT,S2_DRK,S2_MID,S2_DRK,S2_VOD,S2_OUT,".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   S2_OUT,S2_OUT,S2_OUT,S2_OUT,".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   W_SHD, W_DRK, W_OUT, W_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   W_SHD, W_SHD, W_MID, W_LGT, W_LGT, W_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   W_SHD, W_LGT, W_LGT, W_MID, W_DRK, W_MID, W_MID, W_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   W_SHD, W_LGT, W_LGT, W_MID, W_OUT, W_MID, W_MID, W_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   ".",   W_SHD, W_HLT, W_LGT, W_OUT, W_MID, W_OUT, W_OUT, W_OUT, W_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   ".",   W_OUT, W_OUT, W_OUT, W_OUT, W_DRK, W_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   W_OUT, W_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 3: Crystalline Celeste Rose (Sharp Crystal Facets & Thorn Accents)
# Sharp gem-like facets on the petals with white-cyan specular edges,
# and deep obsidian thorny stem with sharp dark silhouettes.
# ==============================================================================
S3_WHT = "#FFFFFF"
S3_HLT = "#D6F7FF"
S3_CYN = "#62E2F8"
S3_MID = "#1CB4DC"
S3_DRK = "#0E6E96"
S3_VOD = "#083B56"
S3_OUT = "#051A29"

grid_opt3 = [
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   S3_OUT,S3_OUT,S3_OUT,S3_OUT,".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   S3_OUT,S3_WHT,S3_HLT,S3_CYN,S3_CYN,S3_OUT,".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   S3_OUT,S3_WHT,S3_CYN,S3_VOD,S3_DRK,S3_MID,S3_CYN,S3_OUT,".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   S3_OUT,S3_HLT,S3_CYN,S3_WHT,S3_HLT,S3_CYN,S3_MID,S3_OUT,".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   S3_OUT,S3_MID,S3_CYN,S3_MID,S3_DRK,S3_OUT,".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   S3_OUT,S3_DRK,S3_DRK,S3_VOD,S3_VOD,S3_OUT,".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   S3_OUT,S3_OUT,S3_OUT,S3_OUT,".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   W_SHD, W_DRK, W_OUT, W_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   W_SHD, W_SHD, W_MID, W_LGT, W_LGT, W_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   W_SHD, W_LGT, W_LGT, W_MID, W_DRK, W_MID, W_MID, W_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   W_SHD, W_LGT, W_LGT, W_MID, W_OUT, W_MID, W_MID, W_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   ".",   W_SHD, W_HLT, W_LGT, W_OUT, W_MID, W_OUT, W_OUT, W_OUT, W_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   ".",   W_OUT, W_OUT, W_OUT, W_OUT, W_DRK, W_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   W_OUT, W_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

# ==============================================================================
# OPTION 4: Wither Rose of the Abyss (Deep Soul Celeste with Calyx Glow)
# Rich two-tone contrast: Petal tips in radiant celeste aqua fading to deep
# abyssal indigo-cyan, with a subtle soul glow at the base of the petals.
# ==============================================================================
S4_WHT = "#FFFFFF"
S4_CEL = "#9AF2FF"
S4_LGT = "#45D4F5"
S4_MID = "#1299C9"
S4_DRK = "#0A658A"
S4_IND = "#083C59"
S4_OUT = "#061F33"

grid_opt4 = [
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   S4_OUT,S4_OUT,S4_OUT,S4_OUT,".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   S4_OUT,S4_CEL,S4_LGT,S4_CEL,S4_WHT,S4_OUT,".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   S4_OUT,S4_WHT,S4_CEL,S4_IND,S4_DRK,S4_MID,S4_CEL,S4_OUT,".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   S4_OUT,S4_CEL,S4_CEL,S4_CEL,S4_LGT,S4_MID,S4_MID,S4_OUT,".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   S4_OUT,S4_MID,S4_LGT,S4_MID,S4_DRK,S4_OUT,".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   S4_OUT,S4_DRK,S4_MID,S4_DRK,S4_IND,S4_OUT,".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   S4_OUT,S4_CEL,S4_CEL,S4_OUT,".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   W_SHD, W_DRK, W_OUT, W_OUT, ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   W_SHD, W_SHD, W_MID, W_LGT, W_LGT, W_OUT, ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   W_SHD, W_LGT, W_LGT, W_MID, W_DRK, W_MID, W_MID, W_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   W_SHD, W_LGT, W_LGT, W_MID, W_OUT, W_MID, W_MID, W_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   ".",   W_SHD, W_HLT, W_LGT, W_OUT, W_MID, W_OUT, W_OUT, W_OUT, W_OUT, ".",   ".",   "."],
    [".",   ".",   ".",   ".",   W_OUT, W_OUT, W_OUT, W_OUT, W_DRK, W_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   W_OUT, W_OUT, ".",   ".",   ".",   ".",   ".",   "."],
    [".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   ".",   "."]
]

save_sprite(grid_opt1, "wither_rose_soul_opt1_faithful")
save_sprite(grid_opt2, "wither_rose_soul_opt2_luminous")
save_sprite(grid_opt3, "wither_rose_soul_opt3_crystalline")
save_sprite(grid_opt4, "wither_rose_soul_opt4_abyssal")
