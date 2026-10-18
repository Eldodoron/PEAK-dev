# 06 — Modpack Packaging, Special Screens, Compatibility & Troubleshooting

This reference covers **modpack production readiness**, **special screen nuances**, **rendering & interaction gotchas**, **mod compatibility workarounds**, and **troubleshooting** in FancyMenu v3.

---

## 1. Modpack Packaging & Production Checklist

When shipping a FancyMenu v3 setup inside a modpack:

1. **Copy `/config/fancymenu/`**:
   - Ensure all custom assets reside inside `/config/fancymenu/assets/` (never outside the instance folder).
   - Include `/config/fancymenu/customization/`, `/config/fancymenu/panoramas/`, `/config/fancymenu/slideshows/`, `/config/fancymenu/custom_gui_screens.txt`, `/config/fancymenu/element_animations/`, `/config/fancymenu/schedulers/`, `/config/fancymenu/event_listeners/`, and `/config/fancymenu/options.txt`.
2. **Enable Modpack Lock Mode (`modpack_mode`)**:
   - In `/config/fancymenu/options.txt`, set:
     ```ini
     modpack_mode = true
     show_welcome_screen = false
     ```
   - `modpack_mode = true` completely disables the top customization menu bar, debug overlays, and editor hotkeys so end-users cannot accidentally open the editor or break the UI.
3. **Clean Runtime Databases**:
   - Delete `/config/fancymenu/fm_data.db` and `/fancymenu_data/seamless_world_loading/` before exporting the modpack so developer test screenshots and world data aren't shipped.
   - Review `/config/fancymenu/user_variables.db` — either delete it (for a fresh state) or keep only intentional default variables.

---

## 2. Special Screens & Built-in Protections

### 2.1 Title Screen Copyright Notice (`copyright_button`)
- **Cannot Be Hidden or Moved Off-Screen**: By design, the `Copyright Mojang AB` widget (`title_screen_copyright_button`) **cannot** be hidden (`is_hidden = true` is ignored), cannot be moved outside the screen bounds, cannot be resized smaller than `60x6` px, and cannot have its opacity reduced to `0.0`.
- **Best Practice**: Anchor it cleanly to `bottom-right` or `bottom-left` with subtle opacity (e.g., `0.5`–`0.7`) so it blends harmoniously into your layout.

### 2.2 Loading Screen vs. Drippy Loading Screen
- **World Loading Screen (`level_loading_screen`)**: Customizable directly in FancyMenu (supports custom backgrounds, text, percentage, and chunk loading progress chunk map).
- **Game Startup / Resource Reload Screen (Mojang Studios Splash)**: Requires **Drippy Loading Screen** (an official addon for FancyMenu) to customize using the exact same FancyMenu Layout Editor and the `{"placeholder":"drippy_gl_percent"}` placeholder.
- **Seamless World Loading**: Available in **Customization → Global Customizations → Seamless World Loading**. Periodically captures a screenshot of the current world/server (saved in `<game-directory>/fancymenu_data/seamless_world_loading/`) and uses the latest screenshot as the background the next time the player loads into that world/server.

### 2.3 World Creation Screen (`create_world_screen`)
- Uses a tabbed navigation bar (`Game`, `World`, `More`) where vanilla widgets are dynamically added/removed when switching tabs.
- When customizing vanilla widgets on `create_world_screen`, test all three tabs to verify your anchors and visibility conditions don't collide across tabs.

### 2.4 Scrollable Screens & Dirt Header/Footer Bars
- Scroll list containers (e.g. Controls, Resource Packs, World Selection list items) cannot have their internal scrolling entries individually dragged in the editor.
- **Removing Dirt Header/Footer Bars**: In the Layout Editor, right-click the background → **Layout Properties → Header/Footer Customizations** (serialized as `scroll_list_customization`), and replace the header/footer textures with a 1×1 transparent PNG or disable header/footer shadows (`render_scroll_list_header_shadow = false`, `render_scroll_list_footer_shadow = false`).
- **Removing 1.21+ Menu Blur**: Set `apply_vanilla_background_blur = false` in `scroll_list_customization`.

### 2.5 Inventory & Container Screens
- FancyMenu allows adding custom elements (texts, images, buttons, tickers, shaders) to inventory screens (`inventory_screen`, `container_screen`, etc.), but **cannot move or resize individual item slots or the container grid itself**.

---

## 3. Rendering & Interaction Gotchas

| Issue / Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| **Buttons behind/in front of a Text element cannot be clicked** | `text_v2` elements are `interactable = true` by default (for scrolling and clicking Markdown links), consuming mouse events inside their bounding box. | Right-click the Text element → set **Interactable** to **Disabled** (`interactable = false`). |
| **Weird translucent grey boxes on Text elements** | Those are the vertical/horizontal scroll grabbers of `text_v2`. | Right-click the Text element → set **Scrolling** to **Disabled** (`enable_scrolling = false`) OR assign a transparent texture to the scroll grabbers. |
| **Arrow keys in Chat screen select custom buttons instead of chat history** | Buttons and sliders are keyboard-navigable (`navigatable = true`) by default. | Right-click the Button/Slider → set **Navigable** to **Disabled** (`navigatable = false`). |
| **Player Entity or Item element renders on top of everything regardless of Layer order** | Minecraft's 3D entity/item projection uses depth buffer state that bypasses 2D GUI layer ordering on older/current versions. | Position 2D overlapping elements around the 3D element, or use pre-rendered sprites if strict 2D occlusion is required. |
| **Custom elements cover vanilla buttons (or vice versa)** | Layout-wide foreground/background render order. | Right-click the editor background → toggle **Render Custom Elements Behind Vanilla** (`render_custom_elements_behind_vanilla = true/false`). |
| **Cannot exclude one button from a Button Template** | Template textures apply globally to all buttons/sliders on the screen. | Disable the template and apply custom textures per-button, or use custom buttons instead. |

---

## 4. Mod Compatibility & Required Config Tweaks

### 4.1 Mods Requiring a Quick Config Change to Work with FancyMenu

| Mod | Symptom | Fix |
| :--- | :--- | :--- |
| **Ice and Fire** | Overrides Title Screen with dragon main menu, ignoring FancyMenu layout. | In `<game-dir>/config/iceandfire-client.toml`, set `B:"Custom main menu"=false`. |
| **Mod Menu (Fabric)** | Duplicated or uncustomizable "Mods" button on Title Screen. | In **Main Menu → Mods → Mod Menu Settings**, set **Mods Button Style** to **Adjacent**. |
| **Replay Mod** | Replay button on Title Screen behaves erratically. | In `<game-dir>/config/replaymod.json`, set `"mainMenuButton": "BIG"`. |
| **Bedrockify** | Title screen / pause screen conflict. | Disable Bedrockify's menu modifications in its config for the screens you customize with FancyMenu. |
| **RandomPatches** | Main menu layout fails to apply. | Set `patchMinecraftClass = false` in RandomPatches config. |
| **Fossils and Archeology / Dalek Mod** | Custom main menu overrides `title_screen`. | Disable the mod's custom main menu in its client config. |

### 4.2 Intentionally Blocked Screen Packages
To prevent hard crashes, FancyMenu intentionally disables customization on screens belonging to these mods' internal packages:
- **Create**, **Cobblemon** (specific internal screens), **Applied Energistics 2 (AE2)**, **Tinkers' Construct / SlimeKnights**, **Immersive Engineering**, **Twilight Forest**, **Supplementaries**, **Alex's Mobs**, **Xaero's Minimap / World Map**, **MidnightDust** config screens, **Screenshot Viewer**, **Panoramica**, **SkinSwapper**, **Dungeonz**, **RPG-Hud**.

### 4.3 Known Incompatible Mods & Clients
- **OptiFine**: **Strictly incompatible** (breaks GUI rendering, shaders, and fonts). Use **Sodium + Iris** (Fabric/NeoForge) or **Embeddium + Oculus** (Forge).
- **Essential Mod**: Breaks FancyMenu layout editor visibility and resets customized Essential buttons when leaving the editor.
- **Sinytra Connector**: Cross-loader translation layer causes severe mixin/GUI instability; not supported.
- **Wakes**: Causes `IncompatibleClassChangeError` on `AbstractSliderButton.getSprite()`.
- **Remove Reloading Screen (RRLS)** / **Animated Mojang Logo** / **Seamless Loading Screen**: Break FancyMenu and Drippy Loading Screen lifecycle hooks.
- **Custom Clients (Lunar Client, Feather, Badlion, etc.)**: Heavily rewrite Minecraft's GUI pipeline and trigger `"Modified FancyMenu JAR Found"` or break layouts completely. Use **Modrinth App** or **CurseForge App** instead.
