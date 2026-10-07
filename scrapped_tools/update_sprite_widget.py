import os
import base64
import json

BORDER_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568\scaling_borders"
SPRITE_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568\sprite_preview"
HTML_OUT = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568\reward_sprites_visualizer.html"

def load_b64(path):
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# Collect images
images = {}
for fname in os.listdir(BORDER_DIR):
    if fname.endswith("_256.png"):
        images[fname.replace("_256.png", "")] = load_b64(os.path.join(BORDER_DIR, fname))

for fname in os.listdir(SPRITE_DIR):
    if fname.endswith("_256.png"):
        images[fname.replace("_256.png", "")] = load_b64(os.path.join(SPRITE_DIR, fname))

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PEAK - Scaling Borders & Contrast Redesign</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    .pixelated {{
      image-rendering: pixelated;
      image-rendering: crisp-edges;
    }}
    .glow-mythic {{ box-shadow: 0 0 25px rgba(255, 120, 0, 0.45); }}
    .glow-epic {{ box-shadow: 0 0 25px rgba(224, 64, 251, 0.5); }}
    .glow-rare {{ box-shadow: 0 0 20px rgba(33, 150, 243, 0.4); }}
    .glow-uncommon {{ box-shadow: 0 0 20px rgba(76, 175, 80, 0.4); }}
    .glow-common {{ box-shadow: 0 0 15px rgba(158, 158, 158, 0.25); }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-6 font-sans">
  <div class="max-w-6xl mx-auto space-y-8">
    
    <!-- Header -->
    <header class="border-b border-slate-800 pb-6 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
      <div>
        <div class="flex items-center gap-2 mb-1">
          <span class="px-2 py-0.5 rounded text-xs font-bold bg-purple-500/20 text-purple-400 border border-purple-500/30">V2 Iteration</span>
          <span class="px-2 py-0.5 rounded text-xs font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30">Progressive Border Geometry</span>
          <span class="px-2 py-0.5 rounded text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">High-Contrast Epic Purple</span>
        </div>
        <h1 class="text-3xl font-black tracking-tight text-white">Scaling Border Progression & Contrast Fix</h1>
        <p class="text-sm text-slate-400 mt-1">Borders now physically evolve in shape and ornament density as rarity increases, with bright silver/magenta highlights separating Epic from the wood body.</p>
      </div>
    </header>

    <!-- SECTION 1: THE 5 SCALING BORDER TIERS -->
    <section class="bg-slate-900/60 border border-slate-800 rounded-2xl p-6 backdrop-blur">
      <div class="mb-5">
        <h2 class="text-xl font-bold text-white flex items-center gap-2">
          <span>🛡️</span> Progressive Border Evolution (Common $\\rightarrow$ Mythic)
        </h2>
        <p class="text-xs text-slate-400 mt-1">Notice how the metal coverage, corner spikes, and ornate trim grow with each tier:</p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
        
        <!-- Common -->
        <div class="bg-slate-900 border border-slate-800 p-4 rounded-xl flex flex-col items-center text-center glow-common hover:border-slate-600 transition">
          <div class="w-32 h-32 bg-slate-950 border border-slate-800 rounded-xl flex items-center justify-center p-2 mb-3">
            <img src="{images['coffer_common']}" alt="Common Tier" class="w-28 h-28 pixelated drop-shadow-md">
          </div>
          <span class="text-xs font-extrabold uppercase tracking-wider text-slate-400">Tier 1: Common</span>
          <h3 class="text-sm font-bold text-white mt-0.5">Rustic Tin L-Brackets</h3>
          <p class="text-[11px] text-slate-400 mt-1 leading-tight">Minimal flat corners, single rivets, clean raw wood exposure. Humble starter feel.</p>
        </div>

        <!-- Uncommon -->
        <div class="bg-slate-900 border border-emerald-900/40 p-4 rounded-xl flex flex-col items-center text-center glow-uncommon hover:border-emerald-600 transition">
          <div class="w-32 h-32 bg-slate-950 border border-emerald-950 rounded-xl flex items-center justify-center p-2 mb-3">
            <img src="{images['coffer_uncommon']}" alt="Uncommon Tier" class="w-28 h-28 pixelated drop-shadow-md">
          </div>
          <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-400">Tier 2: Uncommon</span>
          <h3 class="text-sm font-bold text-white mt-0.5">Bronze Corner Plates</h3>
          <p class="text-[11px] text-slate-400 mt-1 leading-tight">Solid 5×5 reinforced plates, double rivets, emerald gem studs on latch.</p>
        </div>

        <!-- Rare -->
        <div class="bg-slate-900 border border-blue-900/40 p-4 rounded-xl flex flex-col items-center text-center glow-rare hover:border-blue-600 transition">
          <div class="w-32 h-32 bg-slate-950 border border-blue-950 rounded-xl flex items-center justify-center p-2 mb-3">
            <img src="{images['coffer_rare']}" alt="Rare Tier" class="w-28 h-28 pixelated drop-shadow-md">
          </div>
          <span class="text-xs font-extrabold uppercase tracking-wider text-blue-400">Tier 3: Rare</span>
          <h3 class="text-sm font-bold text-white mt-0.5">Chamfered Cobalt Armor</h3>
          <p class="text-[11px] text-slate-400 mt-1 leading-tight">7×7 beveled armor plates with diagonal cut-outs, vertical side bands, and sapphire latch.</p>
        </div>

        <!-- Epic -->
        <div class="bg-slate-900 border border-purple-500/50 p-4 rounded-xl flex flex-col items-center text-center glow-epic hover:border-purple-400 transition ring-1 ring-purple-500/20">
          <div class="w-32 h-32 bg-slate-950 border border-purple-900/60 rounded-xl flex items-center justify-center p-2 mb-3">
            <img src="{images['coffer_epic']}" alt="Epic Tier" class="w-28 h-28 pixelated drop-shadow-lg">
          </div>
          <span class="text-xs font-extrabold uppercase tracking-wider text-purple-300">Tier 4: Epic</span>
          <h3 class="text-sm font-bold text-white mt-0.5">Winged Gothic Filigree</h3>
          <p class="text-[11px] text-purple-200/80 mt-1 leading-tight">High-contrast silver filigree bevels, neon magenta-violet arches, top crown crest, raised gems.</p>
        </div>

        <!-- Mythic -->
        <div class="bg-slate-900 border border-amber-500/50 p-4 rounded-xl flex flex-col items-center text-center glow-mythic hover:border-amber-400 transition ring-1 ring-amber-500/20">
          <div class="w-32 h-32 bg-slate-950 border border-amber-950 rounded-xl flex items-center justify-center p-2 mb-3">
            <img src="{images['coffer_mythic']}" alt="Mythic Tier" class="w-28 h-28 pixelated drop-shadow-lg">
          </div>
          <span class="text-xs font-extrabold uppercase tracking-wider text-amber-400">Tier 5: Mythic</span>
          <h3 class="text-sm font-bold text-white mt-0.5">Gilded Dragon Sarcophagus</h3>
          <p class="text-[11px] text-slate-400 mt-1 leading-tight">External corner spikes, royal 3-point crown with diamond gems, flame borders, floating embers.</p>
        </div>

      </div>
    </section>

    <!-- SECTION 2: EPIC CONTRAST FOCUS -->
    <section class="bg-slate-900/60 border border-purple-500/30 rounded-2xl p-6 backdrop-blur">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
        <div class="md:col-span-8 space-y-3">
          <div class="inline-flex items-center gap-2 px-2.5 py-1 rounded-full text-xs font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">
            <span>✨</span> Contrast & Readability Fix
          </div>
          <h2 class="text-2xl font-bold text-white">How the Epic Purple Contrast was Solved</h2>
          <p class="text-xs text-slate-300 leading-relaxed">
            In the initial sample, murky eggplant purple (`#38006B`) blended directly into the warm oak wood. In this redesign:
          </p>
          <ul class="text-xs text-slate-300 space-y-1.5 list-disc list-inside">
            <li><strong>Specular Silver Outlines (`#FFF5FF`):</strong> Razor-sharp silver bevel lines form the outermost boundary of the corner wings, creating an immediate luminance barrier against the wood.</li>
            <li><strong>Neon Magenta-Violet Core (`#E150FF`):</strong> Bright, luminous violet fills the filigree arches, delivering high saturation that pops instantly on dark backgrounds.</li>
            <li><strong>Cooler Ironwood Undertone:</strong> The chest wood is shaded with deeper charcoal/chestnut undertones so purple hues bounce vibrantly rather than getting swallowed.</li>
          </ul>
        </div>
        <div class="md:col-span-4 flex flex-col items-center justify-center p-4 bg-slate-950 border border-purple-500/40 rounded-xl glow-epic">
          <img src="{images['coffer_epic']}" alt="Epic Closeup" class="w-36 h-36 pixelated drop-shadow-2xl">
          <span class="text-xs font-mono text-purple-300 mt-2 font-semibold">Tier 4: Epic Coffer</span>
        </div>
      </div>
    </section>

    <!-- SECTION 3: EMBLEM REDESIGN DISCUSSION -->
    <section class="bg-slate-900/60 border border-slate-800 rounded-2xl p-6 backdrop-blur space-y-4">
      <div>
        <h2 class="text-xl font-bold text-white flex items-center gap-2">
          <span>🎨</span> Next Step: Redesigning the Emblems (Category Sigils)
        </h2>
        <p class="text-xs text-slate-400 mt-1">
          You mentioned you did not like the sample emblems (the 10×10 skull, crossed swords, apple, and compass). In this new base coffer, the central socket has been expanded to a spacious <strong>16×16 pixel canvas</strong> with deep recessed framing.
        </p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
        
        <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-2">
          <div class="text-2xl">💀</div>
          <h3 class="text-sm font-bold text-white">Boss Slaying</h3>
          <p class="text-[11px] text-slate-400 leading-tight">Instead of a tiny white skull: What about a 3D-shaded horned nether demon skull with glowing red eyes, an ancient dragon skull with horns, or an abyssal sea beast maw?</p>
        </div>

        <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-2">
          <div class="text-2xl">⚔️</div>
          <h3 class="text-sm font-bold text-white">Simply Swords</h3>
          <p class="text-[11px] text-slate-400 leading-tight">Instead of thin crossed lines: What about a glowing runic greatsword blade thrust into a heavy iron anvil, or a battleaxe and broadsword with gold hilt details?</p>
        </div>

        <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-2">
          <div class="text-2xl">🍖</div>
          <h3 class="text-sm font-bold text-white">Culinary</h3>
          <p class="text-[11px] text-slate-400 leading-tight">Instead of a tiny red apple with a fork: What about a steaming golden feast platter (roast turkey / ham), a chef's cleaver, or a bubbling iron stew pot?</p>
        </div>

        <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-2">
          <div class="text-2xl">🧭</div>
          <h3 class="text-sm font-bold text-white">Pioneer</h3>
          <p class="text-[11px] text-slate-400 leading-tight">Instead of a simple star: What about an authentic brass nautical compass with a red/blue directional needle, or an adventurer's backpack / map scroll?</p>
        </div>

      </div>
    </section>

  </div>
</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Updated visualizer generated at: {HTML_OUT}")
