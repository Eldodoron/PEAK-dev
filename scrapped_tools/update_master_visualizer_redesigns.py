import os
import base64
import json

BRAIN_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568"
PREMIUM_DIR = os.path.join(BRAIN_DIR, "premium_emblems")
BORDER_DIR = os.path.join(BRAIN_DIR, "scaling_borders")
REDESIGN_DIR = os.path.join(BRAIN_DIR, "emblem_redesigns")
HTML_OUT = os.path.join(BRAIN_DIR, "reward_sprites_visualizer.html")

def load_b64(path):
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# Collect images
images = {}
for folder in [PREMIUM_DIR, BORDER_DIR, REDESIGN_DIR]:
    if os.path.exists(folder):
        for fname in os.listdir(folder):
            if fname.endswith("_256.png"):
                images[fname.replace("_256.png", "")] = load_b64(os.path.join(folder, fname))

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PEAK - Master Supply Cache Sprites & Redesigns</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    .pixelated {{
      image-rendering: pixelated;
      image-rendering: crisp-edges;
    }}
    .glow-mythic {{ box-shadow: 0 0 30px rgba(255, 120, 0, 0.55); }}
    .glow-epic {{ box-shadow: 0 0 30px rgba(224, 64, 251, 0.55); }}
    .glow-rare {{ box-shadow: 0 0 25px rgba(33, 150, 243, 0.45); }}
    .glow-uncommon {{ box-shadow: 0 0 20px rgba(76, 175, 80, 0.45); }}
    .glow-common {{ box-shadow: 0 0 15px rgba(158, 158, 158, 0.3); }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-6 font-sans">
  <div class="max-w-6xl mx-auto space-y-10">
    
    <!-- Header -->
    <header class="border-b border-slate-800 pb-6 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
      <div>
        <div class="flex items-center gap-2 mb-1.5">
          <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30">V3 Iteration</span>
          <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">Culinary Approved</span>
          <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-cyan-500/20 text-cyan-400 border border-cyan-500/30">Boss & Pioneer Candidates</span>
        </div>
        <h1 class="text-3xl font-black tracking-tight text-white">PEAK Supply Cache Sprites & Emblem Redesigns</h1>
        <p class="text-sm text-slate-400 mt-1">Comparing new artistic emblem options for Boss Slaying and Pioneer, touched-up Broadswords, and the approved Culinary feast.</p>
      </div>
    </header>

    <!-- SECTION 1: CANDIDATE COMPARISON -->
    <section class="bg-slate-900/70 border border-slate-800 rounded-2xl p-6 backdrop-blur space-y-6">
      <div>
        <h2 class="text-2xl font-bold text-white flex items-center gap-2">
          <span>🎯</span> Emblem Redesign Showdown (Pick Your Favorites)
        </h2>
        <p class="text-xs text-slate-400 mt-1">Inspecting the new concepts rendered directly inside their respective coffers:</p>
      </div>

      <!-- Boss Slaying Comparison -->
      <div class="space-y-3">
        <h3 class="text-sm font-extrabold uppercase tracking-wider text-red-400 flex items-center gap-2">
          <span>💀</span> Boss Slaying Candidates (Replacing old skull)
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          
          <div class="p-4 bg-slate-900 border border-red-500/40 rounded-xl flex items-center gap-4 hover:border-red-400 transition">
            <img src="{images['comp_boss_v1_dragon_skull']}" class="w-24 h-24 pixelated drop-shadow-lg">
            <div>
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-red-500/20 text-red-300 border border-red-500/30">Option A</span>
              <h4 class="text-base font-bold text-white mt-1">Ancient Dragon Skull</h4>
              <p class="text-xs text-slate-400 mt-1">Elongated beast skull with sweeping obsidian horns, fanged maw, and glowing red eye slits. Much more menacing and badass.</p>
            </div>
          </div>

          <div class="p-4 bg-slate-900 border border-purple-500/40 rounded-xl flex items-center gap-4 hover:border-purple-400 transition">
            <img src="{images['comp_boss_v2_void_eye']}" class="w-24 h-24 pixelated drop-shadow-lg">
            <div>
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Option B</span>
              <h4 class="text-base font-bold text-white mt-1">The Apex Void Eye</h4>
              <p class="text-xs text-slate-400 mt-1">Mesmerizing Cataclysm/Ender Eye with a vertical slit pupil, electric cyan inner ring, and obsidian talons. Directly matches the 12 Eyes progression!</p>
            </div>
          </div>

        </div>
      </div>

      <!-- Pioneer Candidates -->
      <div class="space-y-3 pt-2">
        <h3 class="text-sm font-extrabold uppercase tracking-wider text-yellow-400 flex items-center gap-2">
          <span>🧭</span> Pioneer / Starter Candidates (Replacing old clock compass)
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          
          <div class="p-4 bg-slate-900 border border-amber-500/40 rounded-xl flex flex-col items-center text-center hover:border-amber-400 transition">
            <img src="{images['comp_pioneer_v1_pick_torch']}" class="w-24 h-24 pixelated drop-shadow-lg mb-2">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Option A</span>
            <h4 class="text-sm font-bold text-white mt-1">Pickaxe & Blazing Torch</h4>
            <p class="text-[11px] text-slate-400 mt-1">Crossed steel mining pick and flaming survival torch. Iconic Minecraft survival feel!</p>
          </div>

          <div class="p-4 bg-slate-900 border border-lime-500/40 rounded-xl flex flex-col items-center text-center hover:border-lime-400 transition">
            <img src="{images['comp_pioneer_v2_backpack']}" class="w-24 h-24 pixelated drop-shadow-lg mb-2">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-lime-500/20 text-lime-300 border border-lime-500/30">Option B</span>
            <h4 class="text-sm font-bold text-white mt-1">Explorer's Field Pack</h4>
            <p class="text-[11px] text-slate-400 mt-1">Leather adventurer's backpack with brass buckles and a rolled green sleeping bag on top.</p>
          </div>

          <div class="p-4 bg-slate-900 border border-cyan-500/40 rounded-xl flex flex-col items-center text-center hover:border-cyan-400 transition">
            <img src="{images['comp_pioneer_v3_nautical_star']}" class="w-24 h-24 pixelated drop-shadow-lg mb-2">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Option C</span>
            <h4 class="text-sm font-bold text-white mt-1">Faceted Nautical Star</h4>
            <p class="text-[11px] text-slate-400 mt-1">Bold 3D gold compass star with a diamond core. Crisp, clean emblem without cluttered dials.</p>
          </div>

        </div>
      </div>

      <!-- Simply Swords Touch-ups -->
      <div class="space-y-3 pt-2">
        <h3 class="text-sm font-extrabold uppercase tracking-wider text-cyan-400 flex items-center gap-2">
          <span>⚔️</span> Simply Swords Touch-ups
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          
          <div class="p-4 bg-slate-900 border border-cyan-500/40 rounded-xl flex items-center gap-4 hover:border-cyan-400 transition">
            <img src="{images['comp_weapons_v1_heavy_claymores']}" class="w-24 h-24 pixelated drop-shadow-lg">
            <div>
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Touch-up A</span>
              <h4 class="text-base font-bold text-white mt-1">Broad Runic Claymores</h4>
              <p class="text-xs text-slate-400 mt-1">Double-thickness broad steel blades with glowing cyan fuller runes, flared quillons, and ruby pommels.</p>
            </div>
          </div>

          <div class="p-4 bg-slate-900 border border-slate-700 rounded-xl flex items-center gap-4 hover:border-slate-500 transition">
            <img src="{images['comp_weapons_v2_anvil_blade']}" class="w-24 h-24 pixelated drop-shadow-lg">
            <div>
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-500/20 text-slate-300 border border-slate-500/30">Touch-up B</span>
              <h4 class="text-base font-bold text-white mt-1">Blade on Black Iron Anvil</h4>
              <p class="text-xs text-slate-400 mt-1">Heavy forge anvil with a massive runic two-handed greatsword thrust vertically down into it.</p>
            </div>
          </div>

        </div>
      </div>

    </section>

  </div>
</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Master visualizer updated with redesigns: {HTML_OUT}")
