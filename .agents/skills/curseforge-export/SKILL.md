---
name: curseforge-export
description: Procedures and verification scripts for packaging, sanitizing manifest.json (BOM stripping, loose jar migration, dead ID purging), and uploading CurseForge modpacks.
---

# CurseForge Modpack Export & Validation Guide

This skill provides the required procedures, verification scripts, and automated upload patterns for publishing modpack ZIP exports to CurseForge without ingestion rejections.

---

## 0. Prerequisite: Strict Explicit User Directive & Version Confirmation Required

Building, rebuilding, or packaging modpack export archives (`scrapped_tools/build_export_alpha2.py`, `Peak-*.zip`) creates production release files and stages them for upload.

* **NEVER** run export packaging scripts autonomously as a "routine check", cleanup step, or general post-fix validation.
* Packaging scripts must **ONLY** be invoked when the user explicitly states that an export or build of the packages is being performed.
* **Mandatory Target Release Version Confirmation:** ALWAYS ask and confirm the exact target release version string (e.g., `alpha3`, `alpha2c`, `beta1`) with the user prior to building. NEVER assume or reuse previous version strings from prior export scripts or manifests to avoid overwriting existing release files or generating incorrect `manifest.json` version metadata.
* Pass the confirmed version string to the export tooling (e.g., `--version alpha3`) so output archives (`Peak-<version>.zip`) and `manifest.json` strictly match the intended milestone.

---

## 1. Automated Manifest Sanitization (BOM Stripping)

CurseForge's backend uses a C#/.NET JSON parser (Newtonsoft.Json) that crashes if `manifest.json` starts with an invisible UTF-8 Byte Order Mark (`\xEF\xBB\xBF`):
> `Invalid JSON - Unexpected character encountered while parsing value: . Path '', line 0, position 0.`

### Invariant
The very first byte of `manifest.json` inside the exported ZIP **MUST** be `{` (`0x7B`).

### Python Sanitization Snippet
```python
import zipfile, json, shutil

def sanitize_manifest(zip_path, author_name="eldodoron"):
    temp_zip = zip_path + ".tmp"
    with zipfile.ZipFile(zip_path, 'r') as zin, zipfile.ZipFile(temp_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        # Read and strip BOM
        raw = zin.read('manifest.json')
        manifest_text = raw.decode('utf-8-sig') # strips BOM automatically
        data = json.loads(manifest_text)
        
        # Ensure author is explicitly set
        if not data.get('author'):
            data['author'] = author_name
            
        # Re-encode pure UTF-8 without BOM
        clean_bytes = json.dumps(data, indent=2).encode('utf-8')
        assert clean_bytes[0] == ord('{'), "Manifest must start with '{'"
        
        # Write clean manifest
        zout.writestr('manifest.json', clean_bytes)
        
        # Copy remaining files, stripping BOM from other text files
        for item in zin.infolist():
            if item.filename == 'manifest.json':
                continue
            content = zin.read(item.filename)
            if content.startswith(b'\xef\xbb\xbf'):
                content = content[3:]
            zout.writestr(item, content)
            
    shutil.move(temp_zip, zip_path)
```

---

## 2. Moderation Compliance: Zero Loose JARs in Overrides

CurseForge moderation policy strictly forbids loose `.jar` files in `overrides/mods/`. All mods must be mapped into `manifest.json`.

### Verification Procedure
1. Check the ZIP for any `.jar` entries:
```python
with zipfile.ZipFile(zip_path, 'r') as z:
    jars = [n for n in z.namelist() if n.endswith('.jar')]
    if jars:
        print("Violation: Loose JARs found in export:", jars)
```
2. For any loose JAR found, resolve its CurseForge `projectID` and `fileID` via the CurseForge API:
   - Endpoint: `GET https://api.curseforge.com/v1/mods/search?gameId=432&slug=<mod-slug>`
   - Endpoint: `GET https://api.curseforge.com/v1/mods/<id>/files`
3. Add the resolved `{ "projectID": <int>, "fileID": <int>, "required": true }` to `manifest.json['files']`.
4. Delete the loose `.jar` from the ZIP's `overrides/mods/` folder.

---

## 3. Dead Dependency Purging

CurseForge's validator checks all `projectID` references. If a referenced project is deleted or rejected, the upload will fail with:
> `References invalid fileIDs: fileID: <id>, projectID: <id>`

### Invariant
Always filter out dead projects (such as `1277910`):
```python
data['files'] = [f for f in data['files'] if f['projectID'] != 1277910]
```

---

## 4. Browser Agent File Upload Staging

When uploading files via the `browser` subagent (`chrome_devtools` MCP server):
* The MCP server validates upload file paths against its configured workspace roots in `McpContext.js`.
* `McpContext.js` always permits the operating system temp directory (`os.tmpdir()` / `%TEMP%`).
* Attempting to upload directly from `C:\Users\<user>\Desktop\...` will result in:
  > `Error: Access denied: path ... is not within any of the configured workspace roots.`

### Staging Procedure Before Invoking Browser Subagent
Always stage the export file into `%TEMP%` before invoking the browser agent:
```powershell
Copy-Item -Path $exportZip -Destination (Join-Path $env:TEMP "Peak-alpha1.zip") -Force
```
Then pass `C:\Users\<user>\AppData\Local\Temp\Peak-alpha1.zip` to the browser agent's `upload_file` command.

---

## 5. File Changelogs Allowed; Project Descriptions Strictly Untouchable

When publishing files via CurseForge automation:
* **Allowed Scope (File Uploads)**:
  - Populate the file changelog / description field in the file creation form (`/#/projects/<id>/files/create`) using Markdown formatting.
  - Verify submitted files on the files list (`/#/projects/<id>/files`).
* **Strictly Forbidden Scope (Project Descriptions)**:
  - **NEVER** navigate to or edit the project description tab (`/#/projects/<id>/description`).
  - **NEVER** switch the main project description editor format to Markdown.
  - The project's main description is handcrafted in rich WYSIWYG HTML with custom styling and palette colors (`#2dc26b`, `#f1c40f`) and must remain completely untouched.

---

## 6. Personal Keybind Sanitization (`overrides/options.txt`)

When exporting modpack ZIP files for CurseForge, **NEVER** export common vanilla player keybinds (e.g. movement, sprint, crouch/sneak, jump, inventory, perspective toggle, attack, use, swap offhand, hotbar slots) configured in the local development environment.

### Invariant & Rationale
- If developer-specific or non-standard keybindings (such as sneak on `X` or sprint on `Shift`) are included in `overrides/options.txt`, CurseForge will extract them into the user's Minecraft directory, overwriting their personal control scheme whenever they install or update the modpack.
- Modded keybinds (such as FTB Quests, Create, Jade, Wands, Spatial GUI) **should** be preserved in `overrides/options.txt` so intentional modpack key conflict resolutions remain functional.
- Common vanilla player keybinds must be stripped from `overrides/options.txt` during export. When omitted, Minecraft automatically falls back to standard vanilla defaults on new installations and leaves existing player controls untouched across updates.

### List of Stripped Vanilla Key Identifiers
```python
VANILLA_KEYBINDS = {
    "key_key.attack",
    "key_key.use",
    "key_key.forward",
    "key_key.left",
    "key_key.back",
    "key_key.right",
    "key_key.jump",
    "key_key.sneak",
    "key_key.sprint",
    "key_key.drop",
    "key_key.inventory",
    "key_key.chat",
    "key_key.playerlist",
    "key_key.pickItem",
    "key_key.command",
    "key_key.socialInteractions",
    "key_key.screenshot",
    "key_key.togglePerspective",
    "key_key.smoothCamera",
    "key_key.fullscreen",
    "key_key.spectatorOutlines",
    "key_key.swapOffhand",
    "key_key.saveToolbarActivator",
    "key_key.loadToolbarActivator",
    "key_key.advancements",
    "key_key.hotbar.1",
    "key_key.hotbar.2",
    "key_key.hotbar.3",
    "key_key.hotbar.4",
    "key_key.hotbar.5",
    "key_key.hotbar.6",
    "key_key.hotbar.7",
    "key_key.hotbar.8",
    "key_key.hotbar.9"
}
```

### Python Sanitization Snippet
```python
def sanitize_options_txt(opt_content):
    if opt_content.startswith(b"\xef\xbb\xbf"):
        opt_content = opt_content[3:]
    opt_text = opt_content.decode("utf-8", errors="replace")
    
    clean_lines = []
    for line in opt_text.splitlines():
        line_clean = line.strip()
        key_name = line_clean.split(":", 1)[0].strip() if ":" in line_clean else ""
        if key_name in VANILLA_KEYBINDS:
            continue
        clean_lines.append(line)
        
    return ("\n".join(clean_lines) + "\n").encode("utf-8")
```

---

## 7. PEAK-Lite Better Combat First-Person Swing Animations

### Invariant & Context
- **PEAK-dev** includes the `Punchy!` mod (`punchy-neoforge-1.21.1-*.jar`) for first-person weapon attack animations. As a result, Better Combat's built-in first-person animations setting (`firstPersonAnimations` in `config/bettercombat/client.json5`) is set to `"NO"` in PEAK-dev to prevent visual jitter and animation double-rendering.
- **PEAK-Lite** excludes `Punchy!` (as part of lightweight client optimization). Without Punchy, PEAK-Lite players would have completely static weapon models during Better Combat attacks if `firstPersonAnimations` remained `"NO"`.
- Therefore, PEAK-Lite must always have Better Combat's first-person animations active (`"firstPersonAnimations": "YES"`).

### Automated Enforcement
- **`scrapped_tools/sync_to_lite.py`**:
  Contains `configure_lite_better_combat()` which automatically enforces `"firstPersonAnimations": "YES"` inside `PEAK-Lite/minecraft/config/bettercombat/client.json5` whenever synchronizing from dev.
- **`scrapped_tools/build_export_alpha2.py`**:
  Verifies that `overrides/config/bettercombat/client.json5` has `"firstPersonAnimations": "YES"` when packaging `Peak-Lite-*.zip`.

---

## 8. Mandatory Pre-Export Synchronization for Derived Editions (PEAK-Lite)

When exporting derived modpack editions (such as **PEAK-Lite**), the export builder (`build_export_alpha2.py`) collects override files directly from the derived instance directory (`PEAK-Lite/minecraft`).

### Invariant & Procedural Requirement
- **NEVER** package a derived edition without first running the synchronization engine (`python scrapped_tools/sync_to_lite.py`).
- If synchronization is skipped, the derived instance will retain stale KubeJS scripts, outdated dimension gating, and obsolete mod configs from earlier sessions. Bundling stale overrides causes fatal worldgen crashes and illegal state exceptions when clients launch into a world.
- Always execute `python scrapped_tools/sync_to_lite.py` immediately before building derived release packages to guarantee 0 diffs across KubeJS and config trees.

---

## 9. Non-CurseForge / Modrinth JAR Mapping in `manifest.json`

Mods originally added via Modrinth (`.pw.toml` / packwiz) or manual JAR drops (such as `FancyMenu`, `Drippy Loading Screen`, `Drippy Early Loading Module`, `Konkrete`, and `Melody`) are absent from legacy CurseForge base manifests.

### Invariant & Ingestion Requirement
- Every active mod required by the modpack must be mapped to valid CurseForge `projectID` and `fileID` entries in the export script's `INJECTED_CF_MODS` registry.
- If a mod is omitted from `manifest.json`, CurseForge will not install the JAR file on client instances, causing missing UI features (e.g. blank white early window screen instead of custom tunnel background art).
- Verify that both Dev and Lite manifests contain all injected Project IDs (`367706`, `511770`, `1390924`, `410295`, `938643`).

---

## 10. Sanitized UI & Companion Data Bundling (`fancymenu_data`)

In addition to `config/fancymenu/`, FancyMenu stores companion progression and browser player settings in `fancymenu_data/`.

### Overrides Collection Invariant
- **Included:** `fancymenu_data/buddy/` (companion save/leveling JSONs), `browser_audio_settings.json`, and `browser_video_settings.json`.
- **Excluded:** Temporary developer session artifacts must never be bundled into release archives:
  - `fancymenu_temp/` (decoded image cache)
  - `seamless_world_loading/` (developer world save screenshots)
  - `video_thumbnails/`
  - `last_world.fmdata`
- **Config Invariant:** Never exclude user-requested utility configs (such as `smoothswapping.json`).

---

## 11. Strict Memory Allocation Invariants
- **PEAK-dev:** Recommended RAM in `manifest.json` must be set to `7520` MB (~7.3 GB).
- **PEAK-Lite:** Recommended RAM in `manifest.json` must be set to `6348` MB (6.2 GB).

---

## 12. Cross-Play Network Parity & Diagnostic Mod Lifecycle

### NeoForge Network Handshake Invariant
- NeoForge strictly validates custom packet payloads and network channels between server and client during the configuration phase. If a server mod registers network channels without `.optional()`, any connecting client lacking the mod will be disconnected with `ModMismatchDisconnectedScreen: Channel of mod "<modid>" failed to connect`.
- `CraftTweaker` registers three mandatory channels (`crafttweaker:copy`, `crafttweaker:data`, `crafttweaker:open_file`) without setting them optional.

### Edition Alignment Strategy
- **Alpha3 Invariant:** Because standard PEAK alpha3 was already published carrying CraftTweaker, `Peak-Lite-alpha3` retains CraftTweaker (PID `239197`) in its manifest so PEAK Lite players can connect to standard PEAK alpha3 Essential / dedicated servers.
- **Alpha4+ Invariant (Both Packs Purged):** Starting with alpha4, CraftTweaker (PID `239197`) must be added to `REMOVED_PIDS_DEV` in `scrapped_tools/build_export_alpha2.py` and excluded from both standard PEAK and PEAK Lite production manifests. Since PEAK uses KubeJS exclusively for all scripting with zero CraftTweaker scripts (`minecraft/scripts/` is empty), purging CraftTweaker from production saves ~40 MB RAM, improves boot times, and preserves 100% multiplayer network parity across all editions.




