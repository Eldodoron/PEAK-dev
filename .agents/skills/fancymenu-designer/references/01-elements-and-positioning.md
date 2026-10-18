# FancyMenu Reference 01: Elements, Screens, Positioning & Widgets

## 1. Screen Architecture & Targeting

### Screen Identifiers
- Every screen in Minecraft (Vanilla, modded, or Custom GUI) is targeted by a **case-sensitive** FancyMenu **Screen Identifier** (NOT a Minecraft resource location).
  - Built-in Vanilla screens use short universal identifiers (e.g., `title_screen`, `pause_screen`, `select_world_screen`, `join_multiplayer_screen`, `options_screen`, `level_loading_screen`, `generic_dirt_message_screen`, `receiving_level_screen`).
  - Modded screens typically use their full Java class name (e.g., `net.neoforged.neoforge.client.gui.ModListScreen`).
  - Custom GUIs use the custom identifier assigned in the Custom GUI manager.
- **How to Find a Screen Identifier**:
  1. Press **`CTRL + ALT + D`** outside the layout editor to toggle the **Debug Overlay**.
  2. Left-click the screen identifier on the first line of the overlay to copy it to the clipboard, or use **Menu Bar -> Customization -> Copy Identifier of Current Screen**.

### Enabling Screen Customization
- By default, screen customization is **disabled** for all screens (`<game-directory>/config/fancymenu/customizablemenus.txt`).
- Enable it per-screen via **Menu Bar -> Customization -> Current Screen Customization: Enabled**.
- **Rule**: Never put Universal Layout identifiers (`%fancymenu:universal_layout%`) into `customizablemenus.txt`; FancyMenu ignores them there.

### Screen-Specific Layouts vs. Universal Layouts
- **Screen-Specific Layout (`Layouts -> New -> For Current Screen`)**:
  - Applies to a single screen identifier.
  - **Required** if you want to see, move, resize, re-texture, or delete **Vanilla/mod widgets** (buttons, sliders, title logo, splash text).
- **Universal Layout (`Layouts -> New -> For All Screens [Universal]`)**:
  - Uses identifier `%fancymenu:universal_layout%`.
  - Applies across all supported screens that have **Current Screen Customization: Enabled** (except blocked/incompatible screens).
  - Ideal for shared elements: persistent background music (`Audio` element), global overlays, branding logos, or navigation headers.
  - Can be filtered via **Whitelist** (only listed screen identifiers) or **Blacklist** (all eligible screens except listed identifiers), plus **Layout-Wide Loading Requirements**.
- **Layout Stacking Order (`layout_index`)**:
  - Eligible Universal Layouts and Screen-Specific Layouts are combined and stacked by **Layout Index** (lower index applied first; later stackable settings override earlier ones).
  - At the same `layout_index`, Universal Layouts are applied **before** screen-specific layouts.

### Custom GUIs & Screen Overrides
- Stored in `<game-directory>/config/fancymenu/custom_gui_screens.txt`.
- Created via **Customization -> Custom GUIs -> Manage Custom GUIs -> New GUI**.
- **Identifier rules**: Lowercase letters, digits, `.`, `_`, `-` only; no spaces; must be unique.
- **Screen Settings**:
  | Setting | Behavior |
  | :--- | :--- |
  | `Allow ESC` | Escape closes the Custom GUI and returns to its parent screen. |
  | `Pause Game/World` | Pauses singleplayer while the Custom GUI is open. |
  | `Render World Background` | Renders the loaded world behind the GUI when opened in-game. |
  | `World Background Overlay` | Renders standard blur/dark tint over the world background. |
  | `Popup Mode` | Renders the parent screen behind the Custom GUI without merging widgets. |
  | `Popup Background Overlay` | Adds blur/tint over the parent screen while in Popup Mode. |
- **Opening Custom GUIs**:
  - Via Action: `opengui` with the Custom GUI identifier.
  - Via Command: `/openguiscreen <screen_identifier> [<target_players>]` (targeting players requires OP level 2 + FancyMenu on both server and client). Close via `/closeguiscreen [<target_players>]`.
- **Overriding Existing Screens**:
  - Enable **Customization -> Settings -> Advanced Customization Mode**, open target screen, and choose **Customization -> Custom GUIs -> Override Current with Custom GUI**.

### Dummy Screen Instances & Fast-Vanishing Screens
- Screens that close automatically during world/server join (`level_loading_screen`, `generic_dirt_message_screen`, etc.) can be opened safely for editing via **Menu Bar -> Tools -> Dummy Screen Instances**.
- **Important Distinction**:
  - **World Loading Screen** (`level_loading_screen`): Shown when entering a world/server — customizable directly in FancyMenu via Dummy Screen Instances.
  - **Game Loading / Splash Screen**: Shown on Minecraft launch / resource reload (`F3+T`) — requires the **Drippy Loading Screen** addon.
- **World Creation Screen Caveat**:
  - Customizing widgets on the modern tabbed **Create New World** screen is **not recommended** due to stacked tabbed widgets; limit customizations there to simple backgrounds if needed.

### Scrollable Screens
- By default, FancyMenu cannot see widgets inside scroll areas (e.g. Options sub-screens).
- Experimental workaround: **Menu Bar -> Customization -> Expose Scroll Area Content Of Current Screen** (not available on Singleplayer/Multiplayer world/server lists).
- **Warning**: Exposing scroll area content removes the original scroll container and stacks all discovered buttons/sliders in the top-left corner; non-widget content inside the scroll container is lost while enabled.

---

## 2. Positioning, Anchoring & Sizing

### Anchor Points (9 Screen Anchors + Element Anchors)
Every element calculates its position `(x, y)` as an offset from its connected **Anchor Point**:
1. **9 Screen Anchor Points**:
   - `top-left`, `top-centered`, `top-right`
   - `mid-left`, `mid-centered` (**Center of Screen** — default for new custom elements), `mid-right`
   - `bottom-left`, `bottom-centered`, `bottom-right`
2. **Element-to-Element Anchor (`element`)**:
   - Dragging an element onto another element sets the hovered element as its **parent anchor**.
   - The child element moves dynamically whenever the parent element moves or animates.
   - Special case: **Progress Bar** has **Use Progress for Element Anchor**, which moves the anchor point dynamically along the leading edge of the filled bar!
   - Special case: **Dragger** acts as an invisible user-movable anchor outside the editor.
3. **Vanilla Widget Default Anchor (`vanilla`)**:
   - Vanilla and mod widgets default to the **Original (`vanilla`)** anchor, which locks them to Minecraft's hardcoded coordinates.
   - **Rule**: To move or resize a Vanilla/mod widget, you **MUST** first change its Anchor Point from `Original` (`vanilla`) to any screen or element anchor!

### Positioning Safeguards & Modifiers
- **Stay On Screen (`stay_on_screen`)**:
  - Enabled by default; prevents elements from going off-screen when the window shrinks.
  - **Crucial for Slide-In Animations**: Disable **Stay On Screen** if an element needs to start or animate outside the screen bounds! (If disabling it causes an element whose real offset was off-screen to vanish, press `Ctrl+Z`, move it near the center, then disable `Stay On Screen`).
- **Sticky Anchors (`sticky_anchor`)**:
  - Essential for elements whose width/height changes dynamically (e.g., Text or Button elements with dynamic placeholders).
  - Keeps the distance from the anchor to the element's **center** (for center anchors), **left edge** (for left anchors), or **right edge** (for right anchors) constant regardless of size changes.
- **Forced GUI Scale & Auto-Scaling**:
  - Right-click editor background -> **Force GUI Scale** locks a menu to a specific GUI scale regardless of user settings.
  - Right-click editor background -> **Auto-Scaling** scales the menu proportionally to window dimensions. (Note: fractional scaling can make bitmap Minecraft fonts look uneven; bake button text into textures if using heavy auto-scaling).
- **FancyMenu's Own UI Scale**:
  - Configured separately at **Customization -> Settings -> FancyMenu's UI** (`Auto` minimum is `1.25`; can be manually set to `1`).

### Advanced Positioning & Sizing (Calculator-Driven Coordinates)
- Right-click an element -> **Advanced Positioning** or **Advanced Sizing** to use expressions/placeholders for X, Y, Width, or Height.
- **Important**: **Advanced Positioning** ignores the element's anchor point and always uses the **top-left screen corner (`X=0, Y=0`)** as its origin (`Stay On Screen` still applies unless disabled).
- Combine with the `calc` placeholder (`"decimal":"false"` for whole pixels):
  ```json
  {"placeholder":"calc","values":{"expression":"{"placeholder":"guiwidth"} / 2 - {"placeholder":"elementwidth","values":{"id":"my_element_id"}} / 2","decimal":"false"}}
  ```
- Clear all advanced position/size fields to return the element to normal anchor-based positioning/sizing.

### Layers & Groups
- Manage render order via **Window -> Editor Widgets -> Layers** or right-click element -> **Move One Layer Up / Down**.
- **Groups**: Group related layers to move, collapse, or hide/show them together in the editor. Saved inside the layout file.
- **Note**: `Player Entity` and `Item` elements use 3D entity/item rendering passes that can have depth-sorting limits relative to flat 2D layers.

---

## 3. Complete Catalog of Built-in Elements (`elements.md`)

Every element receives a unique **Element Identifier** on creation (copy via right-click -> **Copy Element Identifier**).

| Element Type | Purpose & Key Capabilities |
| :--- | :--- |
| **Button** (`button`) | Interactive clickable button. Runs **Action Scripts** on click. Supports normal/hover/inactive textures, nine-slicing, transparent background, custom label + hover label, label scale/shadow/colors, button icon texture, click/hover/unhover sounds, and **Template Mode**. |
| **Vanilla/Mod Widget** (`vanilla_button`) | Wraps existing screen buttons/sliders. Customize label, textures, anchor, size, visibility (**Delete** hides it; restore via **Element -> Deleted Vanilla Elements**), and **Automated Clicks** (integer `>0` triggers real widget clicks on screen load). Cannot edit its action script directly (hide it and use a custom Button with `mimicbutton` if you need custom logic + original action). **Note**: The Title Screen Copyright widget cannot be deleted. |
| **Slider** (`slider`) | Interactive draggable slider. Modes: `Value List` (e.g. Easy/Normal/Hard), `Integer Range` (e.g. `1` to `100`), or `Decimal Range` (e.g. `0.0` to `1.0`). Runs Action Scripts on value change (supplies `$$value`). Supports **Template Mode**, custom handle/background textures, and dynamic label. |
| **Checkbox** (`checkbox`) | Toggleable boolean box. Runs Action Scripts on toggle. **Variable Mode**: binds directly to a FancyMenu variable. When Variable Mode is off, persists state automatically in `<game-directory>/checkbox_states.json` by element ID. Custom background & checkmark textures. |
| **Text Input Field** (`text_input_field`) | User text box bound to a FancyMenu variable. Supports input validation modes (numbers, URLs, plain text, etc.), max character length, custom background/border colors, rounded borders, hint text/color, and hover/unhover/click sounds. |
| **Tooltip** (`tooltip`) | Fixed or **mouse-following** tooltip box, typically gated by `is_hovered` Loading Requirements. Full Markdown support + solid color or nine-sliced texture background. |
| **Item** (`item`) | Renders a 2D GUI Minecraft item (vanilla or modded). Supports custom display name, lore, stack count, enchantment glint, hover tooltip display, and full NBT/component JSON (`nbt-data-placeholder`). |
| **Block/Item JSON Model** (`block_item_model`) | Renders a 3D Block/Item JSON model from resources or local assets. Supports texture overrides, 3-axis rotation, scale, offset, translucent rendering, GUI transform, and **two independent configurable lights** (hue + rotation). |
| **Image** (`image`) | Static or animated (`.fma` / `.apng` / `.gif`) image from Local (`config/fancymenu/assets/`), Web URL, or Resource Location. Supports **Nine-Slicing**, **Texture Repeating (Tiling)**, HEX color tinting, **Rounded Corners** (when not nine-sliced/tiled), and mouse **Parallax Effect**. Can display 2D/3D player heads via Minotar (`https://minotar.net/avatar/{"placeholder":"playername"}.png` or `/cube/.../200.png`). |
| **Text** (`text`) | Single-line or multi-page scrollable Markdown text block. Sources: Direct Input, Local `.txt`/`.md` file, Web URL (cached per session; clear with `Reload FancyMenu`), or Resource Pack. Supports full **FancyMenu Markdown**, custom scroll grabber textures, line wrapping toggle, shadow, line spacing, and alignment. |
| **Splash Text** (`splash_text`) | Custom bouncing title splash (delete Vanilla splash first!). Sources: `Vanilla`, `Direct Input` (single line with placeholders), or `Text File` (UTF-8 without BOM, picks random non-empty line; `Refresh On Screen Load` rerolls). Supports scale, rotation angle, HEX color, shadow toggle, bounce toggle, `&` codes, and raw JSON text components. |
| **Video** (`video`) | Plays MP4 videos (Local or URL). **Requires Watermedia V3 + Watermedia Binaries V3 and OpenGL renderer (does not work on Vulkan or inside Loading Screens)**. Supports loop, volume, sound channel, aspect ratio lock, and playback actions/placeholders. |
| **GLSL Shader** (`glsl_shader`) | Renders single-pass or multipass GLSL fragment shaders (including Shadertoy `mainImage` shaders) clipped to the element's bounds. |
| **Slideshow** (`slideshow`) | Renders an image slideshow configured in `<game-directory>/config/fancymenu/slideshows/<name>/properties.txt`. |
| **Rectangle Shape** (`shape:rectangle`) | Procedural rectangle supporting HEX RGBA color, rounded corners, and background **blur**. Great for glassmorphism panels and dividers. |
| **Circle Shape** (`shape:circle`) | Procedural circle/ellipse supporting HEX RGBA color, background **blur**, and configurable roundness/exponent. |
| **Player Entity** (`player_entity`) | 3D player model (**requires Fancy Entity Renderer (FER) mod on MC 1.20.1+**). Modes: **Copy Client Player**, specific **Player Name**, or custom skin/cape/name. Full **Player Pose** limb X/Y/Z rotation (slider mode or placeholder-driven text mode for procedural animation!), baby/crouching/slim toggles, and head/body mouse-following. |
| **Browser** (`browser`) | Live embedded Chromium web view (**requires Rinku mod**). Supports local HTML (`file:///config/fancymenu/assets/page.html`) and exposes the `window.fancymenu` / `window.FancyMenu` JavaScript bridge (`fancymenu.actions.execute(...)` & `fancymenu.placeholders.get(...)`). |
| **Element Animator** (`element_animator`) | Keyframe timeline controller that animates position, size, and anchor points of one or more target elements with easing curves, loops, and start offsets. |
| **Ticker** (`ticker`) | Invisible screen-bound loop that runs an Action Script every `N` milliseconds (`Continuous`, `Once Per Session`, or `Once Per Screen Load`; optional `Async` mode). |
| **Audio** (`audio`) | Invisible multi-track playlist player (`.ogg`, `.wav`, `.mp3`). Supports sequential or weighted shuffle playback, looping, sound channel selection, and playback control actions. |
| **Music Controller** (`music_controller`) | Invisible element that suppresses Vanilla **Menu Music** and/or **World Music** while the layout is active. |
| **Progress Bar** (`progress_bar`) | Dynamic progress bar driven by a placeholder/number (`0-100` or `0.0-1.0`, e.g., `{"placeholder":"world_load_progress"}`). Supports Up/Down/Left/Right fill direction, smooth fill animation, nine-sliced bar/background textures, and **Use Progress for Element Anchor**. |
| **Dragger** (`dragger`) | Invisible user-draggable handle outside the editor. Elements anchored to it move when dragged by the player. Optional **Save User Drag Offset** persists in `<game-directory>/fancymenu_data/dragger_metas.json`. |
| **Cursor** (`cursor`) | Invisible element that replaces the OS mouse cursor with a custom texture and configurable click hotspot pixel while the layout is active. |

---

## 4. Text Formatting Rules (Markdown vs. `&` Codes vs. JSON Components)

1. **Text Elements (`text`) & Tooltips (`tooltip`) -> Use FancyMenu Markdown**:
   - **Bold**: `**text**` | **Italic**: `*text*` or `_text_` | **Strikethrough**: `~text~`
   - **Headlines** (underlined): `# Very Big`, `## Big`, `### Small`
   - **Custom Resource Pack Font**: `%!!<font_name>%text%!!%` (e.g., `%!!uniform%text%!!%`)
   - **HEX / Named Color**: `%#77fc03%green text%#%` or `%#aqua%aqua text%#%` (`black`, `silver`, `gray`, `grey`, `white`, `maroon`, `red`, `purple`, `fuchsia`, `magenta`, `green`, `lime`, `olive`, `yellow`, `navy`, `blue`, `teal`, `aqua`, `cyan`, `transparent`).
   - **Block Alignment**: Wrap lines between `^^^` (centered) or `|||` (right-aligned) on their own lines.
   - **Quotes / Lists / Rule**: `> quote`, `- bullet`, `---` horizontal rule.
   - **Inline / Multi-line Plain Text Escape**: `;;unformatted;;` or `;;;` block.
   - **Hyperlinks & Images**: `[label](https://...)`, `![](path_or_url)`, `[![](img)](https://...)`.
   - **Interactive Markdown Events**:
     - `[Click Me](click:my_click_id)` -> triggers **On Markdown Text Clicked** (`text_clicked`) listener with `$$text_event_id`.
     - `[Hover Me](hover:my_hover_id)` -> triggers **On Markdown Text Hovered** (`text_hovered`) listener with `$$text_event_id`.
   - *Do NOT use `&` formatting codes or raw JSON components inside `Text` elements.*

2. **Button / Slider Labels & Splash Text -> Use `&` Codes or Raw JSON Text Components**:
   - **Minecraft Formatting Codes**: Use `&` instead of `§` (e.g., `&6&lPLAY GAME`).
   - **Raw JSON Text Component**: Set the entire label to a valid JSON object (e.g., `{"text":"Play Now","color":"#00FFAA","bold":true,"font":"uniform"}`). Supports FancyMenu placeholders inside `"text"`.

---

## 5. Editor & Global Keyboard Shortcuts

| Context | Shortcut | Action |
| :--- | :--- | :--- |
| **Global (Outside Editor)** | `Ctrl + Alt + C` | Toggle FancyMenu Menu Bar |
| **Global (Outside Editor)** | `Ctrl + Alt + D` | Toggle Debug Overlay (copy Screen ID / Widget Locator) |
| **Global (Outside Editor)** | `Ctrl + Alt + L` | Open Layout Editor with last edited layout |
| **Global (Outside Editor)** | `Ctrl + Alt + R` | Reload FancyMenu & clear resource caches |
| **Layout Editor** | `Ctrl + Left-Click` | Multi-select / drag multiple elements |
| **Layout Editor** | `Shift + Resize` | Preserve element aspect ratio while resizing |
| **Layout Editor** | `Arrow Keys` | Nudge selected elements by 1 pixel |
| **Layout Editor** | `Ctrl + C` / `Ctrl + V` | Copy / Paste elements (works across different layouts!) |
| **Layout Editor** | `Ctrl + Z` / `Ctrl + Y` | Undo / Redo |
| **Layout Editor** | `Ctrl + G` | Toggle alignment grid |
| **Layout Editor** | `O` (Hold) | Show anchor points when visibility is set to Show On Key Press |
| **Layout Editor** | `Ctrl + S` | Save layout |
| **Layout Editor** | `Delete` | Delete/hide selected elements |
