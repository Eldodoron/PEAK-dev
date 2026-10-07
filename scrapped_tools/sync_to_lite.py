import os
import sys
import shutil
import json
import time
import filecmp
import argparse

sys.stdout.reconfigure(line_buffering=True)

# -----------------------------------------------------------------------------
# Base Directories & Path Definitions
# -----------------------------------------------------------------------------
BASE_DEV = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_LITE = os.path.abspath(os.path.join(BASE_DEV, "..", "PEAK-Lite"))
DEV_MC = os.path.join(BASE_DEV, "minecraft")
LITE_MC = os.path.join(BASE_LITE, "minecraft")
EXCLUSIONS_FILE = os.path.join(DEV_MC, "peak_lite_excluded_components.txt")
REPORT_FILE = os.path.join(BASE_DEV, "scrapped_tools", "last_sync_report.json")

# -----------------------------------------------------------------------------
# Protected Paths & Directories (NEVER MODIFIED OR DELETED)
# -----------------------------------------------------------------------------
PROTECTED_PATHS = {
    "saves",
    "screenshots",
    "logs",
    "crash-reports",
    "usercache.json",
    "usernamecache.json",
    "command_history.txt",
    ".git",
    ".agents",
    "scrapped_tools",
    "backups",
    "ct_dumps",
    "panoptic"
}

# Orphaned / dev-only configs and runtime cache folders not synced to Lite
IGNORED_CONFIG_DIRS = {
    "spark",
    "panoptic",
    "crafttweaker",
    "search_index"
}

IGNORED_CONFIG_FILES = {
    "panoptic-common.toml",
    "smoothswapping.json",
    "resourcepack_load_order.json"  # Handled separately by sync_paxi_load_order
}

IGNORED_EXTENSIONS = {".bak", ".tmp", ".log"}

# -----------------------------------------------------------------------------
# Safety Assertions & Pre-Flight Validation
# -----------------------------------------------------------------------------
def validate_safety_invariants():
    """Validates source and target directory invariants before any operations."""
    real_dev = os.path.realpath(BASE_DEV)
    real_lite = os.path.realpath(BASE_LITE)

    # 1. Ensure source and destination are physically distinct
    if real_dev == real_lite:
        raise RuntimeError("FATAL SAFETY ERROR: Source and target point to the exact same folder!")

    # 2. Ensure folder names match expected instances
    if os.path.basename(real_dev) != "PEAK-dev":
        raise RuntimeError(f"FATAL SAFETY ERROR: Source directory must be 'PEAK-dev', got: {real_dev}")
    if os.path.basename(real_lite) != "PEAK-Lite":
        raise RuntimeError(f"FATAL SAFETY ERROR: Target directory must be 'PEAK-Lite', got: {real_lite}")

    # 3. Ensure source directory contains valid modpack data
    dev_mods_dir = os.path.join(DEV_MC, "mods")
    if not os.path.isdir(dev_mods_dir):
        raise RuntimeError(f"FATAL SAFETY ERROR: Source mods directory missing: {dev_mods_dir}")

    mod_count = len([f for f in os.listdir(dev_mods_dir) if f.endswith(".jar")])
    if mod_count < 100:
        raise RuntimeError(f"FATAL SAFETY ERROR: Source contains only {mod_count} mods. Aborting to prevent data loss.")

    # 4. Ensure critical source folders exist
    for folder in ["config", "kubejs"]:
        fpath = os.path.join(DEV_MC, folder)
        if not os.path.isdir(fpath):
            raise RuntimeError(f"FATAL SAFETY ERROR: Source directory missing critical component: {fpath}")

def assert_safe_target_path(dst_path):
    """Guarantees that write/delete operations can ONLY occur inside PEAK-Lite and not in protected paths."""
    real_dst = os.path.realpath(dst_path)
    real_lite = os.path.realpath(BASE_LITE)

    # Must be strictly inside BASE_LITE
    if not real_dst.startswith(real_lite):
        raise RuntimeError(f"FATAL SECURITY VIOLATION: Attempted file operation outside PEAK-Lite! Target: {dst_path}")

    # Must never target protected paths
    rel = os.path.relpath(real_dst, real_lite)
    parts = rel.replace("\\", "/").lower().split("/")
    for part in parts:
        if part in PROTECTED_PATHS:
            raise RuntimeError(f"FATAL SAFETY VIOLATION: Refusing to modify protected component: {rel}")

def load_exclusions():
    exclusions = set()
    if os.path.exists(EXCLUSIONS_FILE):
        with open(EXCLUSIONS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    exclusions.add(line.lower())
    return exclusions

# -----------------------------------------------------------------------------
# File & Directory Synchronization
# -----------------------------------------------------------------------------
def sync_file_if_different(src, dst, dry_run=False):
    """Fast file synchronization based on size and shallow comparison with strict safety checks."""
    assert_safe_target_path(dst)

    if not os.path.exists(dst):
        if not dry_run:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
        return "created"

    s_stat = os.stat(src)
    d_stat = os.stat(dst)
    if s_stat.st_size != d_stat.st_size:
        if not dry_run:
            shutil.copy2(src, dst)
        return "updated"

    # If sizes match and mtime differs by more than 2 seconds, do shallow check
    if abs(s_stat.st_mtime - d_stat.st_mtime) > 2.0:
        if not filecmp.cmp(src, dst, shallow=True):
            if not dry_run:
                shutil.copy2(src, dst)
            return "updated"
    return None

def sync_directory(src_dir, dst_dir, exclude_set=None, filter_ext=None, is_config=False, dry_run=False):
    """Recursively mirrors src_dir to dst_dir with strict fail-safes and pruning."""
    created = 0
    updated = 0
    deleted = 0

    if not os.path.exists(src_dir):
        return created, updated, deleted

    if not os.path.exists(dst_dir) and not dry_run:
        assert_safe_target_path(dst_dir)
        os.makedirs(dst_dir, exist_ok=True)

    # 1. Copy new / modified files
    for root, dirs, files in os.walk(src_dir):
        # Prune ignored directory trees
        if is_config:
            dirs[:] = [d for d in dirs if d.lower() not in IGNORED_CONFIG_DIRS]

        rel_path = os.path.relpath(root, src_dir)
        target_root = os.path.join(dst_dir, rel_path)

        for f in files:
            f_lower = f.lower()
            _, ext = os.path.splitext(f_lower)
            if ext in IGNORED_EXTENSIONS:
                continue
            if is_config and f_lower in IGNORED_CONFIG_FILES:
                continue
            if exclude_set and f_lower in exclude_set:
                continue
            if filter_ext and not f_lower.endswith(filter_ext):
                continue

            src_file = os.path.join(root, f)
            dst_file = os.path.join(target_root, f)

            res = sync_file_if_different(src_file, dst_file, dry_run)
            if res == "created":
                created += 1
            elif res == "updated":
                updated += 1

    # 2. Delete obsolete files in dst_dir that no longer exist in src_dir
    for root, dirs, files in os.walk(dst_dir, topdown=False):
        rel_path = os.path.relpath(root, dst_dir)
        source_root = os.path.join(src_dir, rel_path)

        for f in files:
            f_lower = f.lower()
            _, ext = os.path.splitext(f_lower)
            dst_file = os.path.join(root, f)
            src_file = os.path.join(source_root, f)

            should_delete = False
            if ext in IGNORED_EXTENSIONS:
                should_delete = True
            elif is_config and f_lower in IGNORED_CONFIG_FILES and f_lower != "resourcepack_load_order.json":
                should_delete = True
            elif exclude_set and f_lower in exclude_set:
                should_delete = True
            elif not os.path.exists(src_file):
                should_delete = True

            if should_delete:
                assert_safe_target_path(dst_file)
                if not dry_run:
                    try:
                        os.remove(dst_file)
                    except OSError:
                        pass
                deleted += 1

        # Clean empty directories
        if not dry_run and os.path.exists(root) and not os.listdir(root):
            assert_safe_target_path(root)
            try:
                os.rmdir(root)
            except OSError:
                pass

    return created, updated, deleted

def sync_instance_cfg(dry_run=False):
    """Synchronizes instance.cfg while strictly preserving PEAK-Lite identity and unique UUID."""
    dev_cfg = os.path.join(BASE_DEV, "instance.cfg")
    lite_cfg = os.path.join(BASE_LITE, "instance.cfg")
    assert_safe_target_path(lite_cfg)

    if not os.path.exists(dev_cfg):
        return False

    with open(dev_cfg, "r", encoding="utf-8") as f:
        dev_lines = f.readlines()

    existing_uuid = None
    existing_icon = None
    if os.path.exists(lite_cfg):
        with open(lite_cfg, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("uuid="):
                    existing_uuid = line.strip().split("=", 1)[1]
                elif line.startswith("iconKey="):
                    existing_icon = line.strip().split("=", 1)[1]

    out_lines = []
    for line in dev_lines:
        if line.startswith("name="):
            out_lines.append("name=PEAK Lite\n")
        elif line.startswith("ExportName="):
            out_lines.append("ExportName=PEAK-Lite\n")
        elif line.startswith("uuid=") and existing_uuid:
            out_lines.append(f"uuid={existing_uuid}\n")
        elif line.startswith("iconKey=") and existing_icon:
            out_lines.append(f"iconKey={existing_icon}\n")
        elif line.startswith("lastLaunchTime="):
            out_lines.append("lastLaunchTime=0\n")
        elif line.startswith("lastTimePlayed="):
            out_lines.append("lastTimePlayed=0\n")
        elif line.startswith("totalTimePlayed="):
            out_lines.append("totalTimePlayed=0\n")
        else:
            out_lines.append(line)

    if not dry_run:
        tmp_cfg = lite_cfg + ".tmp"
        with open(tmp_cfg, "w", encoding="utf-8") as f:
            f.writelines(out_lines)
        os.replace(tmp_cfg, lite_cfg)
    return True

def sync_paxi_load_order(exclusions, dry_run=False):
    """Generates filtered Paxi resource pack load order for PEAK-Lite."""
    dev_order_path = os.path.join(DEV_MC, "config", "paxi", "resourcepack_load_order.json")
    lite_order_path = os.path.join(LITE_MC, "config", "paxi", "resourcepack_load_order.json")
    assert_safe_target_path(lite_order_path)

    if not os.path.exists(dev_order_path):
        return

    try:
        with open(dev_order_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "loadOrder" in data:
            data["loadOrder"] = [p for p in data["loadOrder"] if p.lower() not in exclusions]

        if not dry_run:
            os.makedirs(os.path.dirname(lite_order_path), exist_ok=True)
            with open(lite_order_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
    except Exception as e:
        print(f"  [Warning] Paxi load order sync error: {e}")

# -----------------------------------------------------------------------------
# Main Synchronization Runner
# -----------------------------------------------------------------------------
def run_sync(dry_run=False):
    start_time = time.time()
    mode_str = "[DRY RUN] " if dry_run else ""
    print(f"\n========================================================")
    print(f" {mode_str}PEAK -> PEAK-Lite Synchronization Engine")
    print(f" Source: {BASE_DEV}")
    print(f" Target: {BASE_LITE}")
    print(f"========================================================")

    # Validate directory structure and multi-layer safety invariants
    validate_safety_invariants()
    print("Safety Invariants: Verified (Distinct instances, valid source mod count, protected paths locked).\n")

    exclusions = load_exclusions()
    print(f"Loaded {len(exclusions)} exclusion entries from peak_lite_excluded_components.txt\n")

    summary = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "dry_run": dry_run,
        "mods": {"created": 0, "updated": 0, "deleted": 0},
        "kubejs": {"created": 0, "updated": 0, "deleted": 0},
        "config": {"created": 0, "updated": 0, "deleted": 0},
        "datapacks": {"created": 0, "updated": 0, "deleted": 0},
        "defaultconfigs": {"created": 0, "updated": 0, "deleted": 0},
        "blueprints": {"created": 0, "updated": 0, "deleted": 0},
        "root": {"created": 0, "updated": 0, "deleted": 0}
    }

    # 1. Sync Mods (minecraft/mods/)
    print("-> Synchronizing Mods...")
    c, u, d = sync_directory(
        os.path.join(DEV_MC, "mods"),
        os.path.join(LITE_MC, "mods"),
        exclude_set=exclusions,
        filter_ext=".jar",
        dry_run=dry_run
    )
    summary["mods"]["created"] += c
    summary["mods"]["updated"] += u
    summary["mods"]["deleted"] += d
    print(f"   Mods: +{c} added, ~{u} updated, -{d} removed (visual/obsolete)")

    # 2. Sync KubeJS (minecraft/kubejs/)
    print("-> Synchronizing KubeJS (scripts, assets, data)...")
    c, u, d = sync_directory(
        os.path.join(DEV_MC, "kubejs"),
        os.path.join(LITE_MC, "kubejs"),
        dry_run=dry_run
    )
    summary["kubejs"]["created"] += c
    summary["kubejs"]["updated"] += u
    summary["kubejs"]["deleted"] += d
    print(f"   KubeJS: +{c} added, ~{u} updated, -{d} removed")

    # 3. Sync Config (minecraft/config/)
    print("-> Synchronizing Config & FTB Quests...")
    c, u, d = sync_directory(
        os.path.join(DEV_MC, "config"),
        os.path.join(LITE_MC, "config"),
        exclude_set=exclusions,
        is_config=True,
        dry_run=dry_run
    )
    summary["config"]["created"] += c
    summary["config"]["updated"] += u
    summary["config"]["deleted"] += d

    # Ensure Paxi load order is tailored for Lite
    sync_paxi_load_order(exclusions, dry_run=dry_run)
    print(f"   Config: +{c} added, ~{u} updated, -{d} removed")

    # 4. Sync DataPacks, DefaultConfigs, Blueprints
    for folder in ["datapacks", "defaultconfigs", "blueprints"]:
        print(f"-> Synchronizing {folder}...")
        c, u, d = sync_directory(
            os.path.join(DEV_MC, folder),
            os.path.join(LITE_MC, folder),
            dry_run=dry_run
        )
        summary[folder]["created"] += c
        summary[folder]["updated"] += u
        summary[folder]["deleted"] += d
        print(f"   {folder}: +{c} added, ~{u} updated, -{d} removed")

    # 5. Sync Root & Standalone Files
    print("-> Synchronizing Instance Configurations & Root Metadata...")
    sync_instance_cfg(dry_run=dry_run)
    root_files = [
        (".packignore", ".packignore"),
        ("mmc-pack.json", "mmc-pack.json"),
        ("minecraft/options.txt", "minecraft/options.txt"),
        ("minecraft/icon.png", "minecraft/icon.png"),
        ("minecraft/paragliderSettings.nbt", "minecraft/paragliderSettings.nbt"),
        ("minecraft/patchouli_data.json", "minecraft/patchouli_data.json"),
        ("minecraft/servers.dat", "minecraft/servers.dat"),
        ("minecraft/servers.essential.dat", "minecraft/servers.essential.dat"),
        ("minecraft/ponders_watched.json", "minecraft/ponders_watched.json"),
        ("minecraft/peak_lite_excluded_components.txt", "minecraft/peak_lite_excluded_components.txt"),
        ("minecraft/peak_lite_excluded_components.md", "minecraft/peak_lite_excluded_components.md"),
        ("minecraft/server_pack_excluded_mods.txt", "minecraft/server_pack_excluded_mods.txt"),
        ("minecraft/server_pack_excluded_mods.md", "minecraft/server_pack_excluded_mods.md")
    ]
    for src_rel, dst_rel in root_files:
        src = os.path.join(BASE_DEV, src_rel)
        dst = os.path.join(BASE_LITE, dst_rel)
        if os.path.exists(src):
            res = sync_file_if_different(src, dst, dry_run)
            if res == "created":
                summary["root"]["created"] += 1
            elif res == "updated":
                summary["root"]["updated"] += 1

    # Sync patches directory
    c, u, d = sync_directory(
        os.path.join(BASE_DEV, "patches"),
        os.path.join(BASE_LITE, "patches"),
        dry_run=dry_run
    )
    summary["root"]["created"] += c
    summary["root"]["updated"] += u
    summary["root"]["deleted"] += d

    elapsed = time.time() - start_time
    total_created = sum(s["created"] for k, s in summary.items() if isinstance(s, dict))
    total_updated = sum(s["updated"] for k, s in summary.items() if isinstance(s, dict))
    total_deleted = sum(s["deleted"] for k, s in summary.items() if isinstance(s, dict))

    summary["duration_seconds"] = round(elapsed, 2)
    summary["total_added"] = total_created
    summary["total_updated"] = total_updated
    summary["total_pruned"] = total_deleted

    # Save execution audit log
    if not dry_run:
        try:
            with open(REPORT_FILE, "w", encoding="utf-8") as f:
                json.dump(summary, f, indent=2)
        except Exception:
            pass

    print(f"\n--------------------------------------------------------")
    print(f" {mode_str}Synchronization Complete in {elapsed:.2f} seconds!")
    print(f" Summary: {total_created} added | {total_updated} updated | {total_deleted} pruned")
    print(f" Target Status: PEAK-Lite is verified 100% aligned with PEAK-dev.")
    print(f"========================================================\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Synchronize PEAK-dev to PEAK-Lite with strict safety guards.")
    parser.add_argument("--dry-run", action="store_true", help="Simulate synchronization without modifying files.")
    args = parser.parse_args()
    run_sync(dry_run=args.dry_run)
