# Project: PEAK Modpack Codebase Sanitization

## Architecture
- **KubeJS Script Infrastructure**: `minecraft/kubejs/` (client_scripts, server_scripts, startup_scripts) providing modpack progression, recipe fixes, custom mob mechanics, and cross-mod integrations.
- **Custom Block Models**: `minecraft/kubejs/assets/` containing custom JSON models (`adorablehamsterpets`, `minecraft`, `cubicleaves`, `kubejs`).
- **FTB Quests Localization Engine**: `minecraft/config/ftbquests/quests/lang/en_us.snbt` centralizing all quest titles, subtitles, and descriptions.

## Code Layout & Write Boundaries
- **Milestone 1 (Block Models)**: Exclusive write access to `minecraft/kubejs/assets/*/models/block/*.json` (the 9 target files).
- **Milestone 2 (FTB Quests Localization)**: Exclusive write access to `minecraft/config/ftbquests/quests/lang/en_us.snbt`.
- **Milestone 3 (KubeJS Scripts)**: Exclusive write access to the 26 target `.js` files in `minecraft/kubejs/`.
- Concurrent workers strictly respected these file boundaries.

## Feature Inventory
| # | Feature | Description | Milestone | Source | Status |
|---|---------|-------------|-----------|--------|--------|
| 1 | Blockbench Metadata Removal | Remove `"credit": "Made with Blockbench"` from 9 custom block models | M1 | Survey E2 | DONE |
| 2 | Open-Source Credit Protection | Verify preservation of 25 `"credit": "zanderest"` and 1 `"credit": "PEAK"` credits | M1 | Survey E2 | DONE |
| 3 | Quest Surgical Marker Removal | Replace 1 occurrence of "surgical" in quest line 1810 | M2 | Survey E3 | DONE |
| 4 | Quest Core Buzzword Sanitization | Replace 21 occurrences of *delves*, *cornerstone*, *unleashed*, *meticulously*, *mastery*, *embark* | M2 | Survey E3 | DONE |
| 5 | Quest Secondary Buzzword Polish | Replace 10 occurrences of *vital*, *harness*, *robust*, *masterpiece*, *masterfully*, etc. | M2 | Survey E3 | DONE |
| 6 | Quest Formatting & SNBT Integrity | Ensure 0 literal `& `, valid quotes, and clean SNBT syntax in `en_us.snbt` | M2 | Survey E3 | DONE |
| 7 | Script "Surgical" Phrasing Removal | Replace all 6 occurrences of "surgical"/"surgically" across 3 KubeJS scripts | M3 | Survey E1 | DONE |
| 8 | Script First-Person Plural Sanitization | Replace all 24 first-person plural comments ("we", "our") across 18 scripts | M3 | Survey E1 | DONE |
| 9 | Script Inner Deliberation & Editorializing | Convert conversational self-talk, "just in case", and opinion comments to professional technical docs | M3 | Survey E1 | DONE |
| 10 | Game Mechanics Protection | Preserve authentic game mechanics (`custom_items.js` Stage 5 dragons) | M3 | Survey E1 | DONE |
| 11 | JavaScript Syntax Compilation | Ensure all 26 modified `.js` files pass syntax compilation with zero errors | M3 | Survey E1 | DONE |
| 12 | Final Forensic Integrity Audit | Comprehensive audit across all files: zero surgical, zero Blockbench, clean formatting, no dummy logic | M4 | Project Acceptance | DONE |

## Milestones
| # | Name | Scope | Dependencies | Status | Key Outputs |
|---|------|-------|-------------|--------|-------------|
| M1 | Block Model Metadata Cleanup | 9 block model JSONs in `minecraft/kubejs/assets/` | none | DONE | 9 files cleaned, 0 Blockbench tags, 25 zanderest community credits intact, valid JSON |
| M2 | FTB Quests Localization Tone Polish | `minecraft/config/ftbquests/quests/lang/en_us.snbt` | none | DONE | 32 lines replaced, 0 surgical, 0 buzzwords, 0 literal `& `, balanced SNBT |
| M3 | KubeJS Script Comment & Log Sanitization | 27 JavaScript files in `minecraft/kubejs/` | none | DONE | 27 files sanitized, 0 surgical, 0 first-person, 89/89 `.js` pass `node -c` |
| M4 | Final Forensic Audit & Verification | Full modpack codebase verification | M1, M2, M3 | DONE | Reviewer 1: APPROVE, Reviewer 2: APPROVE, Challenger 1: APPROVE, Challenger 2: APPROVE, Auditor 1: CLEAN |

## Interface Contracts
- **M1 ↔ Minecraft Client**: Block model JSONs parse cleanly with `ConvertFrom-Json` / Python / Node.js Jackson parser, retaining geometry, textures, and ambient occlusion flags.
- **M2 ↔ FTB Quests Engine**: `en_us.snbt` remains a valid SNBT root compound `{ ... }`. String values preserve Minecraft color escapes (`&6`, `&a`, etc.) with zero literal `& ` codes and correctly escaped quotation marks.
- **M3 ↔ KubeJS Rhino Engine**: All 89 `.js` files compile cleanly with `node -c` with zero syntax or runtime definition errors.
