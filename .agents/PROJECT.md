# Project: AI Sanitization & Script Archiving

## Architecture
- Target Scope: `minecraft/`
- Scrap archive destination: `c:/Users/wamb9/MINECRAFT/Prism/Instances/PEAK dev/scrapped_tools/`
- Test Harness: `tests/`
- Verification standard: AST parsing, JSON load validation, recursive zero-match regex sweeps, and Blockbench credit integrity checks.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Python Utilities Archiving | Relocate 24 `.py` maintenance scripts from `minecraft/` into `scrapped_tools/`, preserving relative paths | M1 | Explorer 1 |
| 2 | Scrap & Temp Cleanup | Move `ai_audit_report.md`, `ore_report.md`, `suspect_mods.txt`, `errors*.txt` to `scrapped_tools/` and remove temporary `tmp_*` / `temp_*` extraction scrap | M1 | Explorer 3 |
| 3 | KubeJS Script AI Sanitization | Eradicate 11 AI/prompt/user-dialogue comments across 8 server scripts in `minecraft/kubejs/server_scripts/` with neutral comments / clean removals | M2 | Explorer 2 |
| 4 | Blockbench Models AI Sanitization | Revert `"credit"` in 4 custom block models (`flowerbed_1.json`..`flowerbed_4.json`) to standard `"Made with Blockbench"` | M3 | Explorer 3 |
| 5 | Quests, Configs & Non-JS Preservation | Retain 100% of 3,310 FTB quest lines, 130+ mod configs, 59 `kubejs/data/` JSONs, and verify zero unintended modifications | M3 | Explorer 3 |
| 6 | 4-Tier E2E Test Suite Pass | Automated test suite verifying zero AI mentions, zero `.py` in `minecraft/`, all `.js` parse cleanly, all `.json` parse cleanly, 100% functional AST/token match | M4 | Test Writer |
| 7 | Adversarial Coverage Hardening | White-box stress testing, corner cases, case-insensitive regex checks, and forensic integrity audit | M4 | Challenger / Auditor |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Archive Python Utilities & Scrap | Relocate 24 `.py` files and temporary scrap/reports from `minecraft/` to `scrapped_tools/` | none | DONE |
| 2 | Sanitize KubeJS Server Scripts | Clean 11 AI/prompt lines across 8 server scripts in `minecraft/kubejs/server_scripts/` | none | DONE |
| 3 | Sanitize Blockbench Models & Assets | Sanitize `flowerbed_1..4.json` credits in `kubejs/assets/` and verify quests/configs | none | DONE |
| 4 | Final E2E Test Verification & Hardening | Pass 100% of E2E test suite (Tiers 1-4) and complete Adversarial Hardening (Tier 5) + Forensic Audit | M1, M2, M3 | DONE |

## Interface Contracts
### Archival Contract
- All `.py` files in `minecraft/` moved to `scrapped_tools/`. Exactly 0 `.py` files remain in `minecraft/` and 24 `.py` files reside in `scrapped_tools/`.
- All `scrapped_tools/` relative paths match original locations minus `minecraft/` prefix.

### KubeJS Script Contract
- Zero syntax errors under Node/Rhino JS parser (`node -c`). 64/64 files compile cleanly.
- Zero changes to recipe IDs, outputs, inputs, event handlers, or functional code. AST token equivalence verified across 46,221 tokens.

### Block Model Contract
- Valid JSON format.
- `"credit"` property equals `"Made with Blockbench"` exactly without `"Fixed by Antigravity"`.
- Geometry, textures, elements, and ambientocclusion remain 100% identical.

## Code Layout
- `minecraft/kubejs/server_scripts/*.js`: Target server scripts (8 sanitized, 0 logic breaks)
- `minecraft/kubejs/assets/minecraft/models/block/flowerbed_*.json`: Block models (4 sanitized, geometries 100% intact)
- `scrapped_tools/`: Archived scripts and tools (24 .py files + 5 scrap reports)
- `tests/`: Automated E2E verification test suite (23/23 tests passing)
