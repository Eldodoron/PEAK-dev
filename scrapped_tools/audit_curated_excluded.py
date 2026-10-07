import os
import json

with open(r'c:\Users\chris\AppData\Roaming\PrismLauncher\instances\PEAK-dev\scrapped_tools\exact_toml_data.json', 'r', encoding='utf-8') as f:
    toml_data = json.load(f)

# The definitive list of excluded mods (client-only mods + dev/backup files)
EXCLUDED_FILENAMES = {
    # 1. Performance / Rendering (Client-Only)
    'BadOptimizations-2.4.1-1.21.1.jar': ('BadOptimizations', 'Client Performance', 'Optimizes client-side entity rendering, HUD, and particle tick rates. Fully client-side only.'),
    'ImmediatelyFast-NeoForge-1.6.11+1.21.1.jar': ('ImmediatelyFast', 'Client Performance', 'Optimizes immediate mode buffer rendering on the client GPU. Purely client rendering.'),
    'dynamic-fps-3.7.7+minecraft-1.21.0-neoforge.jar': ('Dynamic FPS', 'Client Performance', 'Throttles Minecraft rendering framerate when window is blurred or backgrounded. Client-side only.'),
    'entityculling-neoforge-1.10.5-mc1.21.1.jar': ('EntityCulling', 'Client Performance', 'Skips rendering entities and tile entities hidden behind solid blocks via raytracing. Client-side rendering optimization.'),
    'moreculling-neoforge-1.21.1-1.0.7.jar': ('More Culling', 'Client Performance', 'Changes block and leaf culling algorithms to boost client FPS. Client-side rendering only.'),
    'rhenium-1.0.0+neo.jar': ('Rhenium', 'Client Performance', 'Fork/implementation of client rendering pipeline for Sodium ecosystem. Client-side only.'),
    'sodium-neoforge-0.6.13+mc1.21.1.jar': ('Sodium', 'Client Performance / Graphics', 'Modern rendering engine for Minecraft replacement of vanilla chunk rendering. Client-side only.'),
    'denseflower-1.0.0.jar': ('Dense Flowers', 'Client Performance / Rendering', 'Optimizes and alters flower chunk meshing for Sodium. Client-side meshing only.'),

    # 2. Shaders & Graphics Engines
    'iris-neoforge-1.8.12+mc1.21.1.jar.disabled': ('Iris', 'Graphics / Shaders', 'Modern shaderpack loader for Sodium. Client-side only (disabled in dev instance).'),
    'reeses-sodium-options-neoforge-2.2.3+mc1.21.1.jar.disabled': ("Reese's Sodium Options", 'Client GUI / Settings', 'Replaces the video settings GUI with scrolling tabs. Client GUI only.'),
    'sodiumoptionsapi-neoforge-1.0.10-1.21.1.jar.disabled': ('Sodium Options API', 'Client GUI / API', 'API for modded video settings tabs inside Sodium menu. Client-side only.'),
    'sodiumoptionsmodcompat-neoforge-1.0.0-1.21.1.jar.disabled': ('Sodium Options Mod Compat', 'Client GUI / Compat', 'Compatibility options inside Sodium video settings. Client-side only.'),
    'super_resolution-neoforge-1.21..1.21.1-0.8.3-alpha.4+opengl.jar.disabled': ('Super Resolution', 'Graphics / Upscaling', 'DLSS / FSR / Intel XeSS post-processing upscaler for client rendering.'),
    'shine-2.0.1+1.21.1-neoforge.jar': ('Shine', 'Graphics / Shaders', 'Screen-space bloom and glow shader post-processing. Purely client rendering.'),

    # 3. Client Visuals, Textures, Models & Animations
    'entity_texture_features_1.21-neoforge-7.1.jar': ('Entity Texture Features (ETF)', 'Client Visuals', 'Supports OptiFine/Custom Entity textures, blinking, and emissive skins on client.'),
    'entity_model_features-3.2.4-1.21-neoforge.jar': ('Entity Model Features (EMF)', 'Client Visuals', 'Supports OptiFine custom entity models (.jem) and animations client-side.'),
    'emf_compat_better_combat_1.21.1_1.1.0.jar': ('EMF Compat Better Combat', 'Client Visuals', 'Synchronizes EMF custom models with Better Combat animations client-side.'),
    'emf_compat_core-1.1.2.jar': ('EMF Compat Core', 'Client Visuals', 'Core compatibility bridge for EMF custom entity models.'),
    'notenoughanimations-neoforge-1.12.3-mc1.21.1.jar': ('Not Enough Animations', 'Client Visuals / Animations', 'Adds third-person player animations for eating, drinking, rowing, holding maps, etc. Client-side only.'),
    'visuality-forge-3.0.0.jar': ('Visuality: Reforged', 'Client Visuals / Particles', 'Spawns extra visual particles (slime droplets, splash particles, sparklers) client-side.'),
    'particle_core-0.3.3+1.21+neoforge.jar': ('Particle Core', 'Client Visuals / Particles', 'Library for rendering custom client particle effects.'),
    'particular-1.21.1-NeoForge-1.5.5.jar': ('Particular', 'Client Visuals / Particles', 'Ambient biome particles and weather particle enhancements on the client.'),
    'explosiveenhancement-neoforge-1.21.1-1.1.2.jar': ('Explosive Enhancement', 'Client Visuals / Particles', 'Replaces standard explosion particles with high-definition animated explosion sprites.'),
    'Perception-NEOFORGE-0.2.1+1.21.1.jar': ('Perception', 'Client Visuals / Shaders', 'Adds visual immersion shaders, depth of field, speed lines, and vignette client-side.'),
    'lambdynamiclights-4.8.8+1.21.1.jar': ('LambDynamicLights', 'Client Visuals / Lighting', 'Dynamic lighting for held torches and glowing items in real-time. Client-side rendering only.'),
    'cirrus-neoforge-1.21.1-1.2.1.jar.disabled': ('Cirrus', 'Client Visuals / Sky', 'Custom volumetric cloud rendering engine. Client-side only.'),
    'cloudlayers-1.21.1-1.1.jar': ('Cloud Layers', 'Client Visuals / Sky', 'Renders multiple altitude cloud layers in the skybox. Client-side only.'),
    'simplefog-neoforge-1.21.1-2.0.5.jar.disabled': ('Simple Fog Control', 'Client Visuals / Fog', 'In-game GUI to adjust fog distance, color, and density. Client-side only.'),
    'atmospherics-2.6.5-mc-1.21.1.jar': ('Atmospherics (Beash)', 'Client Visuals / Sky & Fog', 'Interactive in-game editor for custom sky, fog, air haze, and clouds. Pure client rendering.'),
    'bigwater-1.2.0-neoforge+mc1.21.1.jar.disabled': ('Big Water', 'Client Visuals / Textures', 'Modifies water texture UV scale and fluid meshing in Sodium. Pure client rendering.'),
    'cinematic_respawn-1.21.1-neoforge-1.2.0.jar': ('Cinematic Respawn', 'Client Visuals / Camera', 'Animates camera pan and fade when dying and respawning. Client-side only.'),
    'punchy-2.6.2-neoforge-1.21.1.jar': ('Punchy', 'Client Visuals / Animations', 'Adds dynamic weapon recoil and screen punch impact animations client-side.'),
    'fwa+1.21.1-neoforge-1.2.31.jar': ('Fancy World Animations (FWA)', 'Client Visuals / Animations', 'Adds smooth opening and ringing animations to chests, shulker boxes, and bells.'),
    'smoothchunk-1.21-4.1.jar.disabled': ('Smooth Chunk', 'Client Visuals / Rendering', 'Fades in newly loaded chunks smoothly on the client display.'),
    'cosycritters-0.3.2+1.21.1-neoforge.jar': ('Cosy Critters', 'Client Visuals / Particles', 'Spawns client-only particle bugs, moths, and birds in ambient biomes.'),

    # 4. Client Camera & Input Controls
    'BetterThirdPerson-neoforge-1.9.0.jar': ('Better Third Person', 'Client Camera / Input', 'Independent 360-degree camera rotation around the player in third person. Client-side only.'),
    'smooththirdpersoncamera-26.05.28-mc1.21.1.jar.disabled': ('Smooth Third Person Camera', 'Client Camera / Input', 'Smooth camera movement and interpolation when moving the mouse in third person.'),
    'CameraOverhaul-v2.1.1-neoforge+mc[1.21-1.21.1].jar.disabled': ('Camera Overhaul', 'Client Camera / Input', 'Adds first-person camera roll and momentum tilting when turning and strafing.'),
    'freecam-neoforge-1.3.0+mc1.21.jar': ('Freecam', 'Client Camera / Input', 'Allows detaching the camera into free flying spectator mode on the client.'),
    'aero_cam_sync-1.3.1.jar': ('Aero Cam Sync', 'Client Camera / Input', 'Synchronizes client camera yaw with moving Create Aeronautics vehicles.'),
    'MouseTweaks-neoforge-mc1.21-2.26.1.jar': ('Mouse Tweaks', 'Client Input / Controls', 'Replaces drag mechanics in inventory GUIs with quick mouse gestures. Client-side only.'),
    'minecraft-cursor-neoforge-3.11.3+1.21.1.jar': ('Minecraft Cursor', 'Client Input / Controls', 'Replaces standard operating system mouse pointer with styled game cursor.'),
    'nowheel-1.0.6+1.21.1neoforge.jar': ('Nowheel', 'Client Input / Controls', 'Disables hotbar slot switching via the mouse scroll wheel. Client input only.'),
    'Ixeris-4.4.1+1.21.1-neoforge.jar': ('Ixeris', 'Client Input / Latency', 'Threaded raw mouse input polling and GLFW event queue bypass. Pure client input engine.'),
    'smooth_steps-neoforge-1.1.0.jar': ('Smooth Steps', 'Client Camera / Visuals', 'Exponentially interpolates the camera height when walking up stairs and slabs.'),

    # 5. Client HUD, Tooltips & GUI Overhauls
    'catalogue-neoforge-1.21.1-1.11.2.jar': ('Catalogue', 'Client GUI / Menus', 'Replaces the in-game Mod List screen with a modernized search and filter UI.'),
    'Controlling-neoforge-1.21.1-19.0.5.jar': ('Controlling', 'Client GUI / Controls', 'Adds a search bar to filter keybindings in the Controls / Key Binds menu. Pure client GUI.'),
    'Searchables-neoforge-1.21.1-1.0.2.jar': ('Searchables', 'Client GUI / Library', 'Helper search bar widget library used exclusively by Controlling and client menus.'),
    'ImmersiveUI-NEOFORGE-0.3.3+1.21.1.jar': ('Immersive UI', 'Client GUI / HUD', 'Overhauls health, hunger, air, and mount HUD displays with modernized widgets.'),
    'HealthBars-v21.1.0-1.21.1-NeoForge.jar': ('Health Bars', 'Client GUI / HUD', 'Renders health indicators above entity heads and on screen HUD. Pure client rendering.'),
    'healthbars-dd-compat-0.3.0+1.21.1.jar': ('Health Bars - Deeper and Darker Compat', 'Client GUI / HUD', 'Compatibility bridge for Health Bars indicators on Deeper and Darker entities.'),
    'OverflowingBars-v21.1.1-1.21.1-NeoForge.jar': ('Overflowing Bars', 'Client GUI / HUD', 'Wraps armor and health bars into layered colored tiers when exceeding 20 points.'),
    'LocatorBar-neoforge-1.2.2+1.21.1.jar': ('Locator Bar', 'Client GUI / HUD', 'Skyrim-style horizontal compass bar rendered at the top of the HUD for waypoints.'),
    'ToastControl-1.21.1-9.0.1.jar': ('Toast Control', 'Client GUI / Toasts', 'Blocks, silences, or customizes tutorial, advancement, and recipe pop-up toasts.'),
    'Not Enough Recipe Book-NEOFORGE-0.4.3+1.21.jar': ('Not Enough Recipe Book (NERB)', 'Client GUI / Recipes', 'Removes restrictions from the vanilla crafting recipe book UI. Client-side only.'),
    'smoothswapping-0.9.3.2-1.21.1-neoforge.jar': ('Smooth Swapping', 'Client GUI / Animations', 'Adds smooth sliding item transition animations when swapping hotbar slots.'),
    'tooltipoverhaul-neoforge-1.21.1-1.5.1.jar': ('Tooltip Overhaul', 'Client GUI / Tooltips', 'Customizable stylized frame and font rendering for item tooltips.'),
    'miningspeedtooltips-neoforge-1.0.0-1.21.1.jar': ('Mining Speed Tooltips', 'Client GUI / Tooltips', 'Calculates and displays harvest speed and attack delay tooltips on equipment.'),
    'SimplyTooltips-neoforge-0.1.5.jar': ('Simply Tooltips', 'Client GUI / Tooltips', 'Clean and compact tooltip layout formatting for item hover boxes.'),
    'clean_tooltips-1.1-neoforge-1.21.1.jar.disabled': ('Clean Tooltips', 'Client GUI / Tooltips', 'Strips redundant mod tags and formats item hover tooltips cleanly.'),
    'enchdesc-neoforge-1.21.1-21.1.10.jar': ('Enchantment Descriptions', 'Client GUI / Tooltips', 'Appends brief descriptions explaining what each enchantment does on enchanted books.'),
    'NBTac-NEOFORGE-1.21.1-1.3.10.jar': ('NBT Autocomplete', 'Client GUI / Chat', 'Provides auto-completion dropdowns for NBT data tags when typing commands in client chat.'),

    # 6. JEI Purely Client-Side Addons (No Server Network Sync)
    'JustEnoughBeacons-NeoForge-1.21-1.3.0.jar': ('Just Enough Beacons', 'Client JEI Addon', 'Adds a JEI tab displaying beacon base block patterns and payments. Client GUI only.'),
    'JustEnoughProfessions-neoforge-1.21.1-4.0.5.jar': ('Just Enough Professions (JEP)', 'Client JEI Addon', 'Adds a JEI tab displaying villager profession uniforms and workstations. Client GUI only.'),
    'jeed-1.21-2.3.3.jar': ('Just Enough Effect Descriptions (JEED)', 'Client JEI Addon', 'Adds a JEI recipe tab explaining status effect potion icons and mechanics.'),
    'collapsible_groups-neoforge-1.21.1-1.4.2.jar': ('Collapsible Recipe Groups', 'Client JEI Addon', 'Folds redundant recipe variants (e.g., all wood dyes) into collapsible groups in JEI.'),

    # 7. Client Audio & Sound Enhancements
    'sounds-2.4.22+lts+1.21.1-neoforge.jar': ('Sounds', 'Client Audio', 'Dynamic sound effects, footstep acoustics, dynamic reverb, and sound muffling through walls.'),
    'towntalk-1.2.0.jar': ('TownTalk', 'Client Audio / Resource Pack', '52.3 MB client sound pack adding spoken voice lines for MineColonies citizens. Purely audio assets.'),

    # 8. Client Utility, Social & Crash Assistants
    'Essential_1-5-0-1_neoforge_1-21-1.jar': ('Essential', 'Client Social / Utility', 'Client social platform, cosmetics wardrobe, and P2P world sharing. Causes crashes/overhead on dedicated server.'),
    'CrashAssistant-neoforge-1.20.6-1.21.4-1.11.9.jar': ('Crash Assistant', 'Client Social / Utility', 'Pop-up crash diagnostic screen allowing one-click log uploading and viewing upon crash.'),

    # 9. Development & Backup Artifacts (Must Never Be in Any Pack)
    'txnilib-neoforge-1.0.24-1.21.1.jar.backup': ('TxniLib (Backup Copy)', 'Backup / Redundant', 'Leftover backup file of TxniLib jar; causes duplicate mod loading conflicts if retained.'),
    'txnilib-neoforge-1.0.24-1.21.1.jar.modified': ('TxniLib (Modified Copy)', 'Backup / Redundant', 'Leftover modified binary of TxniLib; causes duplicate classloader collisions.')
}

print(f"Total curated excluded mods: {len(EXCLUDED_FILENAMES)}")
for fn, (name, cat, desc) in sorted(EXCLUDED_FILENAMES.items(), key=lambda x: (x[1][1], x[0])):
    print(f"[{cat}] {fn} -> {name}: {desc}")
