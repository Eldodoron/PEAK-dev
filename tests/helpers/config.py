"""
Central configuration for E2E Test Suite.
Defines paths, banned AI patterns, expected files, and test settings.
"""
from pathlib import Path
import re

# Base Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
MINECRAFT_DIR = PROJECT_ROOT / "minecraft"
SCRAPPED_TOOLS_DIR = PROJECT_ROOT / "scrapped_tools"
KUBEJS_DIR = MINECRAFT_DIR / "kubejs"
SERVER_SCRIPTS_DIR = KUBEJS_DIR / "server_scripts"
CLIENT_SCRIPTS_DIR = KUBEJS_DIR / "client_scripts"
STARTUP_SCRIPTS_DIR = KUBEJS_DIR / "startup_scripts"
ASSETS_MODELS_DIR = KUBEJS_DIR / "assets" / "minecraft" / "models" / "block"
CONFIG_DIR = MINECRAFT_DIR / "config"
FTBQUESTS_LANG_FILE = CONFIG_DIR / "ftbquests" / "quests" / "lang" / "en_us.snbt"

# The 24 Standalone Python Scripts to be Archived in scrapped_tools/
EXPECTED_PY_FILES = [
    "check_client_toml.py",
    "check_mods.py",
    "check_shine.py",
    "check_specific.py",
    "deep_check.py",
    "find_recipes.py",
    "fix_fluids.py",
    "fix_json.py",
    "fix_suppressor.py",
    "fix_syntax.py",
    "fix_syntax_errors.py",
    "generate_dummy_recipes.py",
    "generate_high_priority_data.py",
    "generate_physical_datapack.py",
    "get_missing_items.py",
    "replace_missing_items.py",
    "rewrite_20_fixed_datapacks.py",
    "clean_suppressor.py",
    "convert_chance.py",
    "convert_to_js.py",
    "fix_datapacks.py",
    "fix_fluid.py",
    "fix_transitional.py",
    "convert_recipes.py",
]

# Relative paths in original minecraft/ tree for all 24 scripts
ORIGINAL_PY_REL_PATHS = [
    "check_client_toml.py",
    "check_mods.py",
    "check_shine.py",
    "check_specific.py",
    "deep_check.py",
    "find_recipes.py",
    "fix_fluids.py",
    "fix_json.py",
    "fix_suppressor.py",
    "fix_syntax.py",
    "fix_syntax_errors.py",
    "generate_dummy_recipes.py",
    "generate_high_priority_data.py",
    "generate_physical_datapack.py",
    "get_missing_items.py",
    "kubejs/server_scripts/clean_suppressor.py",
    "kubejs/server_scripts/convert_chance.py",
    "kubejs/server_scripts/convert_to_js.py",
    "kubejs/server_scripts/fix_datapacks.py",
    "kubejs/server_scripts/fix_fluid.py",
    "kubejs/server_scripts/fix_transitional.py",
    "replace_missing_items.py",
    "rewrite_20_fixed_datapacks.py",
    "scratch/mod_extraction/convert_recipes.py",
]

# Flowerbed 3D Block Models
FLOWERBED_MODEL_FILES = [
    "flowerbed_1.json",
    "flowerbed_2.json",
    "flowerbed_3.json",
    "flowerbed_4.json",
]

# Banned AI / LLM / Agent Signature Regex Patterns
BANNED_REGEX_RULES = [
    {
        "id": "AI_AGENT_ANTIGRAVITY",
        "name": "Antigravity Agent Attribution",
        "pattern": re.compile(r"(?i)\bantigravity\b"),
        "description": "Mentions of Antigravity AI coding assistant or agent attribution.",
    },
    {
        "id": "AI_MODELS_CHATGPT_CLAUDE",
        "name": "Commercial AI Model Names",
        "pattern": re.compile(r"(?i)\b(chatgpt|openai|claude|anthropic|copilot|gemini)\b"),
        "description": "Mentions of LLM models or AI providers.",
    },
    {
        "id": "AI_PROMPT_ITERATION",
        "name": "Prompt Iteration Remnants",
        "pattern": re.compile(r"(?i)\bprompt\s*[0-9]+"),
        "description": "References to multi-turn prompts (e.g., 'Prompt 2', 'Prompt 4').",
    },
    {
        "id": "AI_AUTOGEN_HEADER",
        "name": "Auto-Generated Header",
        "pattern": re.compile(r"(?i)\bauto-generated\s+by\b"),
        "description": "Header indicating automated code generation by AI.",
    },
    {
        "id": "AI_FIXED_BY",
        "name": "Fixed by AI Agent",
        "pattern": re.compile(r"(?i)\bfixed\s+by\s+antigravity\b"),
        "description": "Credit or header indicating repair by AI agent.",
    },
    {
        "id": "AI_USER_REQUEST_CONVERSATION",
        "name": "User-AI Conversational Remnants",
        "pattern": re.compile(r"(?i)\b(per\s+user\s+request|the\s+user\s+wants|the\s+user\s+used|from\s+user\s+prompt|so\s+the\s+user\s+knows)\b"),
        "description": "Dialogue traces between user and AI in code comments.",
    },
    {
        "id": "AI_LLM_MONOLOGUE",
        "name": "Internal LLM Monologue",
        "pattern": re.compile(r"(?i)\bwait,\s*kubejs\b"),
        "description": "Internal reasoning monologue from LLM generation.",
    },
    {
        "id": "AI_SPANISH_AUTOGEN",
        "name": "Spanish Auto-Generated Header",
        "pattern": re.compile(r"(?i)archivo\s+generado\s+autom[aá]ticamente"),
        "description": "Spanish automated generation comment header.",
    },
    {
        "id": "DEV_ABSOLUTE_PATH_LEAKAGE",
        "name": "Developer Environment Absolute Path Leakage",
        "pattern": re.compile(r"(?i)[a-z]:\\users\\[a-z0-9_.-]+\\(appdata|desktop|prism)"),
        "description": "Hardcoded local developer paths from debugging sessions.",
    },
]

# Legitimate In-Game / Mod Whitelist Exceptions
WHITELIST_PATTERNS = [
    re.compile(r"effect\.irons_spellbooks\.antigravity"),  # In-game potion / status effect
    re.compile(r"irons_spellbooks:antigravity"),           # Registry identifier for in-game spell/effect
]
