import os
import base64
import json

IMG_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568\sprite_preview"
HTML_OUT = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568\reward_sprites_visualizer.html"

def load_b64(filename):
    path = os.path.join(IMG_DIR, filename)
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# Collect all base64 images
images = {}
for fname in os.listdir(IMG_DIR):
    if fname.endswith("_256.png"):
        key = fname.replace("_256.png", "")
        images[key] = load_b64(fname)

print(f"Loaded {len(images)} base64 sprites.")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PEAK - Normalized Reward Sprites Visualizer</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    .pixelated {{
      image-rendering: pixelated;
      image-rendering: crisp-edges;
    }}
    .glow-mythic {{
      box-shadow: 0 0 20px rgba(255, 100, 0, 0.4);
    }}
    .glow-epic {{
      box-shadow: 0 0 20px rgba(171, 71, 188, 0.4);
    }}
    .glow-rare {{
      box-shadow: 0 0 20px rgba(33, 150, 243, 0.4);
    }}
    .glow-uncommon {{
      box-shadow: 0 0 20px rgba(76, 175, 80, 0.4);
    }}
    .glow-common {{
      box-shadow: 0 0 15px rgba(158, 158, 158, 0.3);
    }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-6 font-sans">
  <div class="max-w-6xl mx-auto space-y-8">
    
    <!-- Header -->
    <header class="border-b border-slate-800 pb-6 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
      <div>
        <div class="flex items-center gap-2 mb-1">
          <span class="px-2 py-0.5 rounded text-xs font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30">32×32 Native Pixel Art</span>
          <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-500/20 text-blue-400 border border-blue-500/30">Modular Normalized Layers</span>
        </div>
        <h1 class="text-3xl font-black tracking-tight text-white">PEAK Supply Cache Normalization System</h1>
        <p class="text-sm text-slate-400 mt-1">Modular architecture ensuring scalable, instant asset creation for all current and future FTB Quest reward tables.</p>
      </div>
      <div class="bg-slate-900 border border-slate-800 rounded-lg p-3 text-xs text-slate-400 flex items-center gap-3">
        <div class="w-3 h-3 rounded-full bg-emerald-500 animate-pulse"></div>
        <span>1 Base Frame + 5 Rarity Trims + 4 Emblems = <strong>20 Caches</strong></span>
      </div>
    </header>

    <!-- SECTION 1: How the 3 Layers Combine -->
    <section class="bg-slate-900/60 border border-slate-800 rounded-2xl p-6 backdrop-blur">
      <div class="mb-5">
        <h2 class="text-xl font-bold text-white flex items-center gap-2">
          <span>🛠️</span> Layer Deconstruction: The 3 Composable Layers
        </h2>
        <p class="text-xs text-slate-400 mt-1">See how the 3 distinct elements stack together to produce the final sprite without redrawing from scratch.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 items-center">
        <!-- Layer 1 -->
        <div class="bg-slate-900 border border-slate-800 p-4 rounded-xl flex flex-col items-center text-center">
          <div class="w-24 h-24 bg-slate-950/80 border border-slate-800 rounded-lg flex items-center justify-center p-2 mb-3">
            <img src="{images['layer1_base_coffer']}" alt="Layer 1 Base" class="w-20 h-20 pixelated drop-shadow">
          </div>
          <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Layer 1: Base Frame</span>
          <h3 class="text-sm font-semibold text-white mt-1">Reinforced Coffer</h3>
          <p class="text-[11px] text-slate-400 mt-1">Universal silhouette, wood panels, light shading, and center medallion recess.</p>
        </div>

        <div class="hidden md:flex justify-center text-2xl font-black text-slate-600">+</div>

        <!-- Layer 2 -->
        <div class="bg-slate-900 border border-slate-800 p-4 rounded-xl flex flex-col items-center text-center">
          <div class="w-24 h-24 bg-slate-950/80 border border-slate-800 rounded-lg flex items-center justify-center p-2 mb-3">
            <img src="{images['layer2_trim_epic']}" alt="Layer 2 Trim" class="w-20 h-20 pixelated drop-shadow">
          </div>
          <span class="text-xs font-bold uppercase tracking-wider text-purple-400">Layer 2: Rarity Trim</span>
          <h3 class="text-sm font-semibold text-white mt-1">Epic (Amethyst)</h3>
          <p class="text-[11px] text-slate-400 mt-1">Corner brackets, reinforced bands, rivets, and gemstone studs color-coded by tier.</p>
        </div>

        <div class="hidden md:flex justify-center text-2xl font-black text-slate-600">+</div>

        <!-- Layer 3 -->
        <div class="bg-slate-900 border border-slate-800 p-4 rounded-xl flex flex-col items-center text-center">
          <div class="w-24 h-24 bg-slate-950/80 border border-slate-800 rounded-lg flex items-center justify-center p-2 mb-3">
            <img src="{images['layer3_emblem_boss']}" alt="Layer 3 Emblem" class="w-20 h-20 pixelated drop-shadow">
          </div>
          <span class="text-xs font-bold uppercase tracking-wider text-red-400">Layer 3: Emblem</span>
          <h3 class="text-sm font-semibold text-white mt-1">Horned Skull</h3>
          <p class="text-[11px] text-slate-400 mt-1">Crisp 10×10 icon stamped into the center medallion defining the reward theme.</p>
        </div>

        <div class="hidden md:flex justify-center text-2xl font-black text-slate-600">=</div>

        <!-- Composite Result -->
        <div class="bg-slate-800/80 border border-purple-500/40 p-4 rounded-xl flex flex-col items-center text-center glow-epic">
          <div class="w-24 h-24 bg-slate-950/90 border border-purple-500/30 rounded-lg flex items-center justify-center p-2 mb-3">
            <img src="{images['cache_boss_epic']}" alt="Boss Epic Composite" class="w-20 h-20 pixelated drop-shadow-lg">
          </div>
          <span class="text-xs font-bold uppercase tracking-wider text-purple-300">Composite Result</span>
          <h3 class="text-sm font-bold text-white mt-1">Mythic Boss Spoils</h3>
          <p class="text-[11px] text-slate-300 mt-1">Complete, ready-to-render 32×32 in-game item texture.</p>
        </div>
      </div>
    </section>

    <!-- SECTION 2: Interactive Mix-and-Match Composer -->
    <section class="bg-slate-900/60 border border-slate-800 rounded-2xl p-6 backdrop-blur">
      <div class="mb-5">
        <h2 class="text-xl font-bold text-white flex items-center gap-2">
          <span>🎛️</span> Interactive Modular Composer
        </h2>
        <p class="text-xs text-slate-400 mt-1">Select any Category Emblem and Rarity Tier below to instantly inspect the composite cache sprite in real time.</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        <!-- Controls -->
        <div class="lg:col-span-7 space-y-6">
          <!-- Category Selector -->
          <div>
            <label class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">1. Select Category Emblem (Theme)</label>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
              <button onclick="setCategory('boss')" id="btn-cat-boss" class="cat-btn flex items-center gap-2 p-3 rounded-lg border text-left transition border-slate-700 bg-slate-800 text-white hover:border-slate-500">
                <span class="text-lg">💀</span>
                <div>
                  <div class="text-xs font-bold">Boss Slaying</div>
                  <div class="text-[10px] text-slate-400">Skull Sigil</div>
                </div>
              </button>
              <button onclick="setCategory('weapons')" id="btn-cat-weapons" class="cat-btn flex items-center gap-2 p-3 rounded-lg border text-left transition border-slate-800 bg-slate-900/70 text-slate-300 hover:border-slate-700">
                <span class="text-lg">⚔️</span>
                <div>
                  <div class="text-xs font-bold">Simply Swords</div>
                  <div class="text-[10px] text-slate-400">Crossed Blades</div>
                </div>
              </button>
              <button onclick="setCategory('food')" id="btn-cat-food" class="cat-btn flex items-center gap-2 p-3 rounded-lg border text-left transition border-slate-800 bg-slate-900/70 text-slate-300 hover:border-slate-700">
                <span class="text-lg">🍎</span>
                <div>
                  <div class="text-xs font-bold">Culinary</div>
                  <div class="text-[10px] text-slate-400">Apple & Fork</div>
                </div>
              </button>
              <button onclick="setCategory('pioneer')" id="btn-cat-pioneer" class="cat-btn flex items-center gap-2 p-3 rounded-lg border text-left transition border-slate-800 bg-slate-900/70 text-slate-300 hover:border-slate-700">
                <span class="text-lg">🧭</span>
                <div>
                  <div class="text-xs font-bold">Pioneer</div>
                  <div class="text-[10px] text-slate-400">Compass Rose</div>
                </div>
              </button>
            </div>
          </div>

          <!-- Rarity Tier Selector -->
          <div>
            <label class="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">2. Select Rarity Tier (Border & Trim)</label>
            <div class="grid grid-cols-2 sm:grid-cols-5 gap-2">
              <button onclick="setRarity('common')" id="btn-rar-common" class="rar-btn p-2.5 rounded-lg border text-center transition border-slate-700 bg-slate-800 text-slate-300 hover:border-slate-500">
                <div class="text-xs font-bold">Common</div>
                <div class="text-[10px] text-slate-400">Slate Grey</div>
              </button>
              <button onclick="setRarity('uncommon')" id="btn-rar-uncommon" class="rar-btn p-2.5 rounded-lg border text-center transition border-emerald-900/40 bg-emerald-950/20 text-emerald-400 hover:border-emerald-600">
                <div class="text-xs font-bold">Uncommon</div>
                <div class="text-[10px] text-emerald-500">Verdant Green</div>
              </button>
              <button onclick="setRarity('rare')" id="btn-rar-rare" class="rar-btn p-2.5 rounded-lg border text-center transition border-blue-900/40 bg-blue-950/20 text-blue-400 hover:border-blue-600">
                <div class="text-xs font-bold">Rare</div>
                <div class="text-[10px] text-blue-500">Cobalt Blue</div>
              </button>
              <button onclick="setRarity('epic')" id="btn-rar-epic" class="rar-btn p-2.5 rounded-lg border text-center transition border-purple-500 bg-purple-900/30 text-purple-300 ring-2 ring-purple-500/30">
                <div class="text-xs font-bold">Epic</div>
                <div class="text-[10px] text-purple-400">Royal Amethyst</div>
              </button>
              <button onclick="setRarity('mythic')" id="btn-rar-mythic" class="rar-btn p-2.5 rounded-lg border text-center transition border-amber-900/40 bg-amber-950/20 text-amber-400 hover:border-amber-600">
                <div class="text-xs font-bold">Mythic</div>
                <div class="text-[10px] text-amber-500">Flame & Gold</div>
              </button>
            </div>
          </div>

          <!-- Description Callout -->
          <div class="p-3 bg-slate-950/60 border border-slate-800 rounded-lg text-xs space-y-1">
            <div class="text-slate-400">Associated FTB Quests Reward Table:</div>
            <div id="reward-table-binding" class="font-mono text-amber-400 font-semibold">peak_supplies_boss_epic.snbt</div>
            <div id="reward-desc" class="text-slate-400 text-[11px]">Rewards high-tier boss conquest spoils, mythic armor materials, and rare combat trophies.</div>
          </div>
        </div>

        <!-- Big Live Preview Display -->
        <div class="lg:col-span-5 flex flex-col items-center justify-center p-6 bg-slate-950 border border-slate-800 rounded-xl relative overflow-hidden">
          <div class="text-xs font-mono uppercase text-slate-500 mb-2">Live Scaled Preview (8× Zoom)</div>
          <div id="preview-glow" class="w-48 h-48 rounded-2xl flex items-center justify-center p-4 bg-slate-900/60 border transition-all duration-300 glow-epic border-purple-500/40">
            <img id="live-sprite" src="{images['cache_boss_epic']}" alt="Live Preview" class="w-40 h-40 pixelated drop-shadow-2xl transition-all">
          </div>
          <div class="mt-4 text-center">
            <div id="preview-title" class="text-base font-bold text-white">Epic Boss Slaying Cache</div>
            <div id="preview-sub" class="text-xs text-purple-400 font-mono mt-0.5">kubejs:cache_boss_epic</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: The Complete 4x5 Matrix -->
    <section class="bg-slate-900/60 border border-slate-800 rounded-2xl p-6 backdrop-blur">
      <div class="mb-5">
        <h2 class="text-xl font-bold text-white flex items-center gap-2">
          <span>📋</span> Complete 4×5 Normalized Matrix (All 20 Combinations)
        </h2>
        <p class="text-xs text-slate-400 mt-1">Every cell is a ready 32×32 texture automatically mapped to an FTB Quests reward table.</p>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse text-xs">
          <thead>
            <tr class="border-b border-slate-800 text-slate-400">
              <th class="p-3 font-bold uppercase">Theme \ Rarity</th>
              <th class="p-3 font-bold text-slate-300">Common (Slate)</th>
              <th class="p-3 font-bold text-emerald-400">Uncommon (Verdant)</th>
              <th class="p-3 font-bold text-blue-400">Rare (Cobalt)</th>
              <th class="p-3 font-bold text-purple-400">Epic (Amethyst)</th>
              <th class="p-3 font-bold text-amber-400">Mythic (Flame)</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/60">
            <!-- Boss -->
            <tr>
              <td class="p-3 font-semibold text-white flex items-center gap-2">
                <span class="text-base">💀</span> Boss Slaying
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_boss_common']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Trophy Spoils</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_boss_uncommon']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Slayer Cache</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_boss_rare']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Relic Urn</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_boss_epic']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Conqueror Coffer</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_boss_mythic']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-amber-300 font-semibold">Apex Reliquary</span>
                </div>
              </td>
            </tr>

            <!-- Weapons -->
            <tr>
              <td class="p-3 font-semibold text-white flex items-center gap-2">
                <span class="text-base">⚔️</span> Simply Swords
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_weapons_common']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Smithing Crate</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_weapons_uncommon']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Forge Kit</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_weapons_rare']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Runic Arsenal</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_weapons_epic']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Relic Arms</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_weapons_mythic']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-amber-300 font-semibold">Mythic Armory</span>
                </div>
              </td>
            </tr>

            <!-- Culinary -->
            <tr>
              <td class="p-3 font-semibold text-white flex items-center gap-2">
                <span class="text-base">🍎</span> Culinary
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_food_common']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Homestead Crate</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_food_uncommon']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Pantry Hamper</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_food_rare']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Gourmet Box</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_food_epic']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Master Banquet</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_food_mythic']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-amber-300 font-semibold">Ambrosia Feast</span>
                </div>
              </td>
            </tr>

            <!-- Pioneer -->
            <tr>
              <td class="p-3 font-semibold text-white flex items-center gap-2">
                <span class="text-base">🧭</span> Pioneer
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_pioneer_common']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Starter Pack</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_pioneer_uncommon']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Pioneer Kit</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_pioneer_rare']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Expedition Cache</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_pioneer_epic']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-slate-400">Vanguard Trove</span>
                </div>
              </td>
              <td class="p-3">
                <div class="flex items-center gap-2">
                  <img src="{images['cache_pioneer_mythic']}" class="w-8 h-8 pixelated">
                  <span class="text-[11px] text-amber-300 font-semibold">Pinnacle Vault</span>
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
        desc: "Spoils from apex conquests, boss mob drops, relics, and trophies."
      }},
      weapons: {{
        name: "Simply Swords & Forging",
        desc: "Smithing supplies, runic tablets, weapon archetypes, and gem dust."
      }},
      food: {{
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

    function updateView() {{
      const key = `cache_${{curCat}}_${{curRar}}`;
      const imgUrl = images[key];
      if (imgUrl) {{
        document.getElementById('live-sprite').src = imgUrl;
      }}

      // Glow & border
      const glowEl = document.getElementById('preview-glow');
      glowEl.className = `w-48 h-48 rounded-2xl flex items-center justify-center p-4 bg-slate-900/60 border transition-all duration-300 ${{glowClasses[curRar]}}`;

      // Text
      const capRar = curRar.charAt(0).toUpperCase() + curRar.slice(1);
      document.getElementById('preview-title').textContent = `${{capRar}} ${{metadata[curCat].name}} Cache`;
      document.getElementById('preview-sub').textContent = `kubejs:cache_${{curCat}}_${{curRar}}`;
      document.getElementById('preview-sub').className = `text-xs font-mono mt-0.5 ${{rarColors[curRar]}}`;

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
        active.className = 'cat-btn flex items-center gap-2 p-3 rounded-lg border text-left transition border-slate-500 bg-slate-800 text-white';
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

print(f"Interactive visualizer generated at: {HTML_OUT}")
