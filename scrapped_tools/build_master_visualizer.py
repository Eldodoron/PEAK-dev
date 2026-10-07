import os
import base64
import json

PREMIUM_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568\premium_emblems"
BORDER_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568\scaling_borders"
HTML_OUT = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568\reward_sprites_visualizer.html"

def load_b64(path):
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# Collect images
images = {}
for fname in os.listdir(PREMIUM_DIR):
    if fname.endswith("_256.png"):
        images[fname.replace("_256.png", "")] = load_b64(os.path.join(PREMIUM_DIR, fname))

for fname in os.listdir(BORDER_DIR):
    if fname.endswith("_256.png"):
        images[fname.replace("_256.png", "")] = load_b64(os.path.join(BORDER_DIR, fname))

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PEAK - Master Supply Cache Sprites (V3 Artisan Polish)</title>
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
          <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">Artisan Edition</span>
          <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30">Scaling Tier Geometry</span>
          <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-purple-500/20 text-purple-400 border border-purple-500/30">High-Contrast Luminous Epic</span>
        </div>
        <h1 class="text-3xl font-black tracking-tight text-white">PEAK Supply Cache Sprites (32×32 Web Preview)</h1>
        <p class="text-sm text-slate-400 mt-1">Full artisan polish with multi-step lighting ramps, specular reflections, scaling border armor, and high-contrast palettes.</p>
      </div>
      <div class="bg-slate-900 border border-slate-800 rounded-xl px-4 py-3 text-xs text-slate-400 flex items-center gap-3">
        <div class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></div>
        <span><strong>20 Custom Caches</strong> (4 Categories $\\times$ 5 Tiers)</span>
      </div>
    </header>

    <!-- SECTION 1: THE NEW ARTISAN EMBLEMS -->
    <section class="bg-slate-900/70 border border-slate-800 rounded-2xl p-6 backdrop-blur">
      <div class="mb-5">
        <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30 mb-2">
          <span>✨</span> Detailed Pixel Art
        </div>
        <h2 class="text-2xl font-bold text-white">The 4 Redesigned Category Emblems</h2>
        <p class="text-xs text-slate-400 mt-1">Drawn with full specular highlights, 3D cylindrical lighting, shadow outlines, and vibrant color gradients.</p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        
        <!-- Boss Emblem -->
        <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl flex flex-col items-center text-center hover:border-red-500/50 transition">
          <div class="w-36 h-36 bg-slate-950 border border-slate-800 rounded-xl flex items-center justify-center p-3 mb-3 shadow-inner">
            <img src="{images['emblem_boss']}" alt="Boss Emblem" class="w-28 h-28 pixelated drop-shadow-lg">
          </div>
          <span class="text-xs font-extrabold uppercase tracking-wider text-red-400">Boss Slaying</span>
          <h3 class="text-sm font-bold text-white mt-1">The Crowned Demon Skull</h3>
          <p class="text-[11px] text-slate-400 mt-1 leading-tight">
            Curved ivory demon horns, rounded 3D cranium with specular shine, glowing crimson eye sockets with white pupils, fanged teeth, and a golden ruby crown.
          </p>
        </div>

        <!-- Weapons Emblem -->
        <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl flex flex-col items-center text-center hover:border-blue-500/50 transition">
          <div class="w-36 h-36 bg-slate-950 border border-slate-800 rounded-xl flex items-center justify-center p-3 mb-3 shadow-inner">
            <img src="{images['emblem_weapons']}" alt="Weapons Emblem" class="w-28 h-28 pixelated drop-shadow-lg">
          </div>
          <span class="text-xs font-extrabold uppercase tracking-wider text-cyan-400">Simply Swords</span>
          <h3 class="text-sm font-bold text-white mt-1">Crossed Runic Broadswords</h3>
          <p class="text-[11px] text-slate-400 mt-1 leading-tight">
            Twin heavy steel claymores with glowing electric-cyan runic fuller channels, golden quillon crossguards, ruby-set pommels, and a central white clash burst.
          </p>
        </div>

        <!-- Culinary Emblem -->
        <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl flex flex-col items-center text-center hover:border-amber-500/50 transition">
          <div class="w-36 h-36 bg-slate-950 border border-slate-800 rounded-xl flex items-center justify-center p-3 mb-3 shadow-inner">
            <img src="{images['emblem_culinary']}" alt="Culinary Emblem" class="w-28 h-28 pixelated drop-shadow-lg">
          </div>
          <span class="text-xs font-extrabold uppercase tracking-wider text-amber-400">Culinary</span>
          <h3 class="text-sm font-bold text-white mt-1">Steaming Glazed Feast</h3>
          <p class="text-[11px] text-slate-400 mt-1 leading-tight">
            Glistening golden-brown roast with honey specular glaze, caramelized crosshatch score lines, clean white knuckle bone, fresh parsley garnish, and dual rising steam curls.
          </p>
        </div>

        <!-- Pioneer Emblem -->
        <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl flex flex-col items-center text-center hover:border-yellow-500/50 transition">
          <div class="w-36 h-36 bg-slate-950 border border-slate-800 rounded-xl flex items-center justify-center p-3 mb-3 shadow-inner">
            <img src="{images['emblem_pioneer']}" alt="Pioneer Emblem" class="w-28 h-28 pixelated drop-shadow-lg">
          </div>
          <span class="text-xs font-extrabold uppercase tracking-wider text-yellow-400">Pioneer</span>
          <h3 class="text-sm font-bold text-white mt-1">Ornate Brass Compass</h3>
          <p class="text-[11px] text-slate-400 mt-1 leading-tight">
            Heavy polished brass bezel with top pocket-watch loop, aged parchment dial, cardinal ticks, sharp magnetized red/blue spearhead needle, and a central gold pivot.
          </p>
        </div>

      </div>
    </section>

    <!-- SECTION 2: INTERACTIVE LIVE COMPOSER -->
    <section class="bg-slate-900/70 border border-slate-800 rounded-2xl p-6 backdrop-blur">
      <div class="mb-6">
        <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 mb-2">
          <span>🎛️</span> Real-Time Inspection
        </div>
        <h2 class="text-2xl font-bold text-white">Interactive Cache Composer</h2>
        <p class="text-xs text-slate-400 mt-1">Click any category and rarity to preview the finalized composite sprite:</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        <!-- Controls -->
        <div class="lg:col-span-7 space-y-6">
          <!-- Category Selector -->
          <div>
            <label class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">1. Category Emblem (Theme)</label>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
              <button onclick="setCategory('boss')" id="btn-cat-boss" class="cat-btn flex items-center gap-2 p-3 rounded-lg border text-left transition border-slate-500 bg-slate-800 text-white shadow">
                <span class="text-xl">💀</span>
                <div>
                  <div class="text-xs font-bold">Boss Slaying</div>
                  <div class="text-[10px] text-red-400 font-semibold">Crowned Skull</div>
                </div>
              </button>
              <button onclick="setCategory('weapons')" id="btn-cat-weapons" class="cat-btn flex items-center gap-2 p-3 rounded-lg border text-left transition border-slate-800 bg-slate-900/70 text-slate-300 hover:border-slate-700">
                <span class="text-xl">⚔️</span>
                <div>
                  <div class="text-xs font-bold">Simply Swords</div>
                  <div class="text-[10px] text-cyan-400 font-semibold">Runic Blades</div>
                </div>
              </button>
              <button onclick="setCategory('culinary')" id="btn-cat-culinary" class="cat-btn flex items-center gap-2 p-3 rounded-lg border text-left transition border-slate-800 bg-slate-900/70 text-slate-300 hover:border-slate-700">
                <span class="text-xl">🍖</span>
                <div>
                  <div class="text-xs font-bold">Culinary</div>
                  <div class="text-[10px] text-amber-400 font-semibold">Glazed Roast</div>
                </div>
              </button>
              <button onclick="setCategory('pioneer')" id="btn-cat-pioneer" class="cat-btn flex items-center gap-2 p-3 rounded-lg border text-left transition border-slate-800 bg-slate-900/70 text-slate-300 hover:border-slate-700">
                <span class="text-xl">🧭</span>
                <div>
                  <div class="text-xs font-bold">Pioneer</div>
                  <div class="text-[10px] text-yellow-400 font-semibold">Brass Compass</div>
                </div>
              </button>
            </div>
          </div>

          <!-- Rarity Tier Selector -->
          <div>
            <label class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">2. Rarity Tier (Border Armor & Palette)</label>
            <div class="grid grid-cols-2 sm:grid-cols-5 gap-2">
              <button onclick="setRarity('common')" id="btn-rar-common" class="rar-btn p-3 rounded-lg border text-center transition border-slate-700 bg-slate-800/80 text-slate-300 hover:border-slate-500">
                <div class="text-xs font-bold">Common</div>
                <div class="text-[10px] text-slate-400">Tin L-Brackets</div>
              </button>
              <button onclick="setRarity('uncommon')" id="btn-rar-uncommon" class="rar-btn p-3 rounded-lg border text-center transition border-emerald-900/40 bg-emerald-950/20 text-emerald-400 hover:border-emerald-600">
                <div class="text-xs font-bold">Uncommon</div>
                <div class="text-[10px] text-emerald-500">Bronze Plates</div>
              </button>
              <button onclick="setRarity('rare')" id="btn-rar-rare" class="rar-btn p-3 rounded-lg border text-center transition border-blue-900/40 bg-blue-950/20 text-blue-400 hover:border-blue-600">
                <div class="text-xs font-bold">Rare</div>
                <div class="text-[10px] text-blue-500">Cobalt Armor</div>
              </button>
              <button onclick="setRarity('epic')" id="btn-rar-epic" class="rar-btn p-3 rounded-lg border text-center transition border-purple-500 bg-purple-900/30 text-purple-300 ring-2 ring-purple-500/30">
                <div class="text-xs font-bold">Epic</div>
                <div class="text-[10px] text-purple-400">Gothic Filigree</div>
              </button>
              <button onclick="setRarity('mythic')" id="btn-rar-mythic" class="rar-btn p-3 rounded-lg border text-center transition border-amber-900/40 bg-amber-950/20 text-amber-400 hover:border-amber-600">
                <div class="text-xs font-bold">Mythic</div>
                <div class="text-[10px] text-amber-500">Gilded Spikes</div>
              </button>
            </div>
          </div>

          <!-- Description Box -->
          <div class="p-4 bg-slate-950/80 border border-slate-800 rounded-xl text-xs space-y-1.5 shadow-inner">
            <div class="flex items-center justify-between">
              <span class="text-slate-400">FTB Quests Reward Table:</span>
              <span id="tier-badge" class="px-2 py-0.5 rounded text-[10px] font-extrabold uppercase bg-purple-500/20 text-purple-300 border border-purple-500/30">Tier 4</span>
            </div>
            <div id="reward-table-binding" class="font-mono text-amber-400 font-bold text-sm">peak_supplies_boss_epic.snbt</div>
            <div id="reward-desc" class="text-slate-400 text-xs">Rewards apex boss conquest spoils, mythic armor materials, and rare combat trophies.</div>
          </div>
        </div>

        <!-- Big Live Preview Display -->
        <div class="lg:col-span-5 flex flex-col items-center justify-center p-6 bg-slate-950 border border-slate-800 rounded-2xl relative overflow-hidden shadow-2xl">
          <div class="text-xs font-mono uppercase text-slate-500 mb-3 flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emerald-400"></span> Live 8× Crisp Nearest-Neighbor Render
          </div>
          <div id="preview-glow" class="w-52 h-52 rounded-2xl flex items-center justify-center p-4 bg-slate-900/60 border transition-all duration-300 glow-epic border-purple-500/50">
            <img id="live-sprite" src="{images['final_cache_boss_epic']}" alt="Live Preview" class="w-44 h-44 pixelated drop-shadow-2xl transition-all">
          </div>
          <div class="mt-4 text-center">
            <div id="preview-title" class="text-base font-black text-white">Epic Boss Slaying Cache</div>
            <div id="preview-sub" class="text-xs text-purple-400 font-mono mt-0.5">kubejs:cache_boss_epic</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: THE COMPLETE 4x5 MATRIX -->
    <section class="bg-slate-900/70 border border-slate-800 rounded-2xl p-6 backdrop-blur">
      <div class="mb-6 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
        <div>
          <h2 class="text-2xl font-bold text-white flex items-center gap-2">
            <span>📋</span> Complete 4×5 Normalized Matrix (All 20 Final Caches)
          </h2>
          <p class="text-xs text-slate-400 mt-1">Every sprite is ready to be copied into <code>kubejs/assets/kubejs/textures/item/</code> and assigned to FTB Quests.</p>
        </div>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse text-xs">
          <thead>
            <tr class="border-b border-slate-800 text-slate-400 bg-slate-950/40">
              <th class="p-3.5 font-bold uppercase">Theme \\ Rarity</th>
              <th class="p-3.5 font-bold text-slate-300">Common (Slate)</th>
              <th class="p-3.5 font-bold text-emerald-400">Uncommon (Verdant)</th>
              <th class="p-3.5 font-bold text-blue-400">Rare (Cobalt)</th>
              <th class="p-3.5 font-bold text-purple-400">Epic (Amethyst)</th>
              <th class="p-3.5 font-bold text-amber-400">Mythic (Flame)</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/60">
            <!-- Boss -->
            <tr class="hover:bg-slate-900/40 transition">
              <td class="p-3.5 font-semibold text-white flex items-center gap-2">
                <span class="text-lg">💀</span> Boss Slaying
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_boss_common']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Trophy Spoils</div>
                    <div class="text-[10px] text-slate-500 font-mono">boss_trophy.snbt</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_boss_uncommon']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Slayer Cache</div>
                    <div class="text-[10px] text-slate-500 font-mono">boss_uncommon</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_boss_rare']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Relic Urn</div>
                    <div class="text-[10px] text-slate-500 font-mono">boss_relic.snbt</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_boss_epic']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Conqueror Coffer</div>
                    <div class="text-[10px] text-slate-500 font-mono">boss_epic</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_boss_mythic']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-amber-300">Apex Reliquary</div>
                    <div class="text-[10px] text-amber-500/80 font-mono">boss_mythic.snbt</div>
                  </div>
                </div>
              </td>
            </tr>

            <!-- Weapons -->
            <tr class="hover:bg-slate-900/40 transition">
              <td class="p-3.5 font-semibold text-white flex items-center gap-2">
                <span class="text-lg">⚔️</span> Simply Swords
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_weapons_common']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Smithing Crate</div>
                    <div class="text-[10px] text-slate-500 font-mono">simply_common</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_weapons_uncommon']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Forge Kit</div>
                    <div class="text-[10px] text-slate-500 font-mono">simply_uncommon</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_weapons_rare']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Runic Arsenal</div>
                    <div class="text-[10px] text-slate-500 font-mono">simply_rare.snbt</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_weapons_epic']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Relic Arms</div>
                    <div class="text-[10px] text-slate-500 font-mono">simply_epic</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_weapons_mythic']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-amber-300">Mythic Armory</div>
                    <div class="text-[10px] text-amber-500/80 font-mono">simply_mythic.snbt</div>
                  </div>
                </div>
              </td>
            </tr>

            <!-- Culinary -->
            <tr class="hover:bg-slate-900/40 transition">
              <td class="p-3.5 font-semibold text-white flex items-center gap-2">
                <span class="text-lg">🍖</span> Culinary
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_culinary_common']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Homestead Crate</div>
                    <div class="text-[10px] text-slate-500 font-mono">culinary_common</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_culinary_uncommon']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Ration Satchel</div>
                    <div class="text-[10px] text-slate-500 font-mono">adventurer_ration</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_culinary_rare']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Gourmet Box</div>
                    <div class="text-[10px] text-slate-500 font-mono">culinary_rare.snbt</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_culinary_epic']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Master Banquet</div>
                    <div class="text-[10px] text-slate-500 font-mono">culinary_master</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_culinary_mythic']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-amber-300">Ambrosia Feast</div>
                    <div class="text-[10px] text-amber-500/80 font-mono">culinary_mythic</div>
                  </div>
                </div>
              </td>
            </tr>

            <!-- Pioneer -->
            <tr class="hover:bg-slate-900/40 transition">
              <td class="p-3.5 font-semibold text-white flex items-center gap-2">
                <span class="text-lg">🧭</span> Pioneer
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_pioneer_common']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Starter Pack</div>
                    <div class="text-[10px] text-slate-500 font-mono">starter_common</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_pioneer_uncommon']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Pioneer Kit</div>
                    <div class="text-[10px] text-slate-500 font-mono">starter_uncommon</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_pioneer_rare']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Expedition Cache</div>
                    <div class="text-[10px] text-slate-500 font-mono">starter_rare.snbt</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_pioneer_epic']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-slate-200">Vanguard Trove</div>
                    <div class="text-[10px] text-slate-500 font-mono">starter_epic.snbt</div>
                  </div>
                </div>
              </td>
              <td class="p-3.5">
                <div class="flex items-center gap-2.5">
                  <img src="{images['final_cache_pioneer_mythic']}" class="w-10 h-10 pixelated drop-shadow">
                  <div>
                    <div class="font-bold text-amber-300">Pinnacle Vault</div>
                    <div class="text-[10px] text-amber-500/80 font-mono">starter_mythic</div>
                  </div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

  </div>

  <script>
    const images = {json.dumps(images)};
    let curCat = 'boss';
    let curRar = 'epic';

    const metadata = {{
      boss: {{
        name: "Boss Slaying",
        desc: "Rewards apex boss conquest spoils, mythic armor materials, and rare combat trophies."
      }},
      weapons: {{
        name: "Simply Swords & Forging",
        desc: "Smithing supplies, runic tablets, weapon archetypes, and gem dust."
      }},
      culinary: {{
        name: "Culinary & Gastronome",
        desc: "Gourmet dishes, hearty adventure rations, and rich homestead crops."
      }},
      pioneer: {{
        name: "Pioneer & Exploration",
        desc: "Essential starter kits, building materials, tools, and utility gadgets."
      }}
    }};

    const glowClasses = {{
      common: 'glow-common border-slate-600',
      uncommon: 'glow-uncommon border-emerald-500/50',
      rare: 'glow-rare border-blue-500/50',
      epic: 'glow-epic border-purple-500/50',
      mythic: 'glow-mythic border-amber-500/50'
    }};

    const rarColors = {{
      common: 'text-slate-400',
      uncommon: 'text-emerald-400',
      rare: 'text-blue-400',
      epic: 'text-purple-400',
      mythic: 'text-amber-400'
    }};

    const tierBadges = {{
      common: 'Tier 1 • Common',
      uncommon: 'Tier 2 • Uncommon',
      rare: 'Tier 3 • Rare',
      epic: 'Tier 4 • Epic',
      mythic: 'Tier 5 • Mythic'
    }};

    function updateView() {{
      const key = `final_cache_${{curCat}}_${{curRar}}`;
      const imgUrl = images[key];
      if (imgUrl) {{
        document.getElementById('live-sprite').src = imgUrl;
      }}

      // Glow & border
      const glowEl = document.getElementById('preview-glow');
      glowEl.className = `w-52 h-52 rounded-2xl flex items-center justify-center p-4 bg-slate-900/60 border transition-all duration-300 ${{glowClasses[curRar]}}`;

      // Text
      const capRar = curRar.charAt(0).toUpperCase() + curRar.slice(1);
      document.getElementById('preview-title').textContent = `${{capRar}} ${{metadata[curCat].name}} Cache`;
      document.getElementById('preview-sub').textContent = `kubejs:cache_${{curCat}}_${{curRar}}`;
      document.getElementById('preview-sub').className = `text-xs font-mono mt-0.5 ${{rarColors[curRar]}} font-bold`;

      document.getElementById('tier-badge').textContent = tierBadges[curRar];
      document.getElementById('reward-table-binding').textContent = `peak_supplies_${{curCat}}_${{curRar}}.snbt`;
      document.getElementById('reward-desc').textContent = metadata[curCat].desc;
    }}

    function setCategory(cat) {{
      curCat = cat;
      document.querySelectorAll('.cat-btn').forEach(b => {{
        b.className = 'cat-btn flex items-center gap-2 p-3 rounded-lg border text-left transition border-slate-800 bg-slate-900/70 text-slate-300 hover:border-slate-700';
      }});
      const active = document.getElementById(`btn-cat-${{cat}}`);
      if (active) {{
        active.className = 'cat-btn flex items-center gap-2 p-3 rounded-lg border text-left transition border-slate-500 bg-slate-800 text-white shadow';
      }}
      updateView();
    }}

    function setRarity(rar) {{
      curRar = rar;
      document.querySelectorAll('.rar-btn').forEach(b => {{
        b.classList.remove('ring-2', 'ring-purple-500/30', 'ring-emerald-500/30', 'ring-blue-500/30', 'ring-amber-500/30', 'border-purple-500', 'border-emerald-500', 'border-blue-500', 'border-amber-500');
      }});
      const active = document.getElementById(`btn-rar-${{rar}}`);
      if (active) {{
        active.classList.add('ring-2');
        if (rar === 'epic') active.classList.add('border-purple-500', 'ring-purple-500/30');
        else if (rar === 'rare') active.classList.add('border-blue-500', 'ring-blue-500/30');
        else if (rar === 'uncommon') active.classList.add('border-emerald-500', 'ring-emerald-500/30');
        else if (rar === 'mythic') active.classList.add('border-amber-500', 'ring-amber-500/30');
        else active.classList.add('border-slate-500');
      }}
      updateView();
    }}

    // Init
    updateView();
  </script>
</body>
</html>
"""

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Master visualizer updated at: {HTML_OUT}")
