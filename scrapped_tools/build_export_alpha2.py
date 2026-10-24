import os
import sys
import json
import zipfile
import shutil
import re
import glob
import hashlib
import argparse
import urllib.request
import urllib.error

try:
    import tomllib
except ImportError:
    tomllib = None

sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

BASE_DEV = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BASE_LITE = os.path.abspath(os.path.join(BASE_DEV, "..", "PEAK-Lite"))
DEV_MC = os.path.join(BASE_DEV, "minecraft")
LITE_MC = os.path.join(BASE_LITE, "minecraft")

REGISTRY_FILE = os.path.join(BASE_DEV, "scrapped_tools", "curseforge_mod_registry.json")
CF_INST_FILE = r"C:\Users\chris\curseforge\minecraft\Instances\Peak (Dev)\minecraftinstance.json"
PACK_EXPORTS_DIR = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\PackExports"
ALPHA1_ZIP = os.path.join(PACK_EXPORTS_DIR, "Peak-alpha1.zip")
TEMP_DIR = os.environ.get("TEMP", r"C:\Users\chris\AppData\Local\Temp")

DEAD_PIDS = {1277910}

IGNORED_EXTENSIONS = {".bak", ".tmp", ".log"}
IGNORED_CONFIG_DIRS = {"panoptic", "crafttweaker", "search_index"}
IGNORED_CONFIG_FILES = {"panoptic-common.toml", "fm_data.db"}
IGNORED_FANCYMENU_DATA_DIRS = {"fancymenu_temp", "seamless_world_loading", "video_thumbnails"}
IGNORED_FANCYMENU_DATA_FILES = {"last_world.fmdata"}

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


def get_neoforge_version():
    """Reads the active NeoForge version dynamically from mmc-pack.json."""
    mmc_path = os.path.join(BASE_DEV, "mmc-pack.json")
    if os.path.exists(mmc_path):
        try:
            with open(mmc_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for comp in data.get("components", []):
                if comp.get("uid") == "net.neoforged":
                    return comp.get("version", "21.1.248")
        except Exception:
            pass
    return "21.1.248"


def get_minecraft_version():
    """Reads the active Minecraft version dynamically from mmc-pack.json."""
    mmc_path = os.path.join(BASE_DEV, "mmc-pack.json")
    if os.path.exists(mmc_path):
        try:
            with open(mmc_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for comp in data.get("components", []):
                if comp.get("uid") == "net.minecraft":
                    return comp.get("version", "1.21.1")
        except Exception:
            pass
    return "1.21.1"


def extract_declared_mods(toml_text):
    """Extracts only declared [[mods]] modId and version from neoforge.mods.toml."""
    mod_ids = []
    version = ""
    if tomllib is not None:
        try:
            data = tomllib.loads(toml_text)
            for m in data.get("mods", []):
                mid = m.get("modId")
                if mid and mid not in mod_ids:
                    mod_ids.append(mid)
                if not version and m.get("version"):
                    version = str(m.get("version"))
            if mod_ids:
                return mod_ids, version
        except Exception:
            pass

    current_section = ""
    for line in toml_text.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("["):
            current_section = s.lower()
            continue
        if current_section == "[[mods]]":
            m_id = re.match(r'^modId\s*=\s*["\']([^"\']+)["\']', s)
            if m_id and m_id.group(1) not in mod_ids:
                mod_ids.append(m_id.group(1))
            m_ver = re.match(r'^version\s*=\s*["\']([^"\']+)["\']', s)
            if m_ver and not version:
                version = m_ver.group(1)
    return mod_ids, version


def inspect_jar_file(jar_path):
    """Computes SHA-1, size, declared mod_ids, version, and network channel requirements for a JAR."""
    sha1 = hashlib.sha1()
    size = os.path.getsize(jar_path)
    with open(jar_path, "rb") as f:
        while chunk := f.read(65536):
            sha1.update(chunk)
    sha1_hex = sha1.hexdigest()

    mod_ids = []
    version = ""
    has_mandatory_channels = False
    is_client_only_toml = False

    try:
        with zipfile.ZipFile(jar_path, "r") as zf:
            names = zf.namelist()
            for candidate in ["META-INF/neoforge.mods.toml", "META-INF/mods.toml"]:
                if candidate in names:
                    toml_text = zf.read(candidate).decode("utf-8", errors="replace")
                    m_ids, ver = extract_declared_mods(toml_text)
                    for mid in m_ids:
                        if mid not in mod_ids:
                            mod_ids.append(mid)
                    if not version and ver:
                        version = ver
                    if re.search(r'clientSideOnly\s*=\s*true', toml_text, re.IGNORECASE):
                        is_client_only_toml = True

            if "META-INF/MANIFEST.MF" in names and (not version or "${" in version):
                mf = zf.read("META-INF/MANIFEST.MF").decode("utf-8", errors="replace")
                m_imp = re.search(r"Implementation-Version:\s*([^\r\n]+)", mf)
                if m_imp:
                    version = m_imp.group(1).strip()

            for n in names:
                if n.endswith(".class"):
                    raw = zf.read(n)
                    if b"net/neoforged/neoforge/network/registration/PayloadRegistrar" in raw:
                        if b"optional" not in raw:
                            has_mandatory_channels = True
    except Exception:
        pass

    return {
        "sha1": sha1_hex,
        "size": size,
        "mod_ids": mod_ids,
        "mod_version": version,
        "is_client_only_toml": is_client_only_toml,
        "has_mandatory_network_channels": has_mandatory_channels
    }


def resolve_via_cfwidget(filename, filesize, project_id=None, candidate_slugs=None):
    """
    Queries https://api.cfwidget.com to automatically resolve CurseForge (projectID, fileID)
    when a mod is updated or added via Modrinth or manual JAR drop without .pw.toml CF metadata.
    """
    urls_to_try = []
    if project_id:
        urls_to_try.append(f"https://api.cfwidget.com/{project_id}")
    if candidate_slugs:
        for slug in candidate_slugs:
            if slug:
                urls_to_try.append(f"https://api.cfwidget.com/minecraft/mc-mods/{slug}")

    fn_lower = filename.lower()
    for api_url in urls_to_try:
        try:
            req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8", errors="replace"))
            pid = data.get("id") or project_id
            if not pid:
                continue
            files = data.get("files") or []
            # 1. Exact filename match
            for f in files:
                if (f.get("name") or "").lower() == fn_lower or (f.get("display") or "").lower() == fn_lower:
                    return {
                        "projectID": int(pid),
                        "fileID": int(f["id"]),
                        "name": data.get("title") or filename,
                        "url": (data.get("urls") or {}).get("curseforge") or f"https://www.curseforge.com/minecraft/mc-mods/{pid}"
                    }
            # 2. Exact filesize match for 1.21.1
            size_matches = [
                f for f in files
                if f.get("filesize") == filesize and "1.21.1" in (f.get("versions") or [])
            ]
            if len(size_matches) == 1:
                return {
                    "projectID": int(pid),
                    "fileID": int(size_matches[0]["id"]),
                    "name": data.get("title") or filename,
                    "url": (data.get("urls") or {}).get("curseforge") or f"https://www.curseforge.com/minecraft/mc-mods/{pid}"
                }
        except Exception:
            continue
    return None


def verify_cf_file_ownership(project_id, file_id):
    """
    Verifies via CFWidget API that `file_id` genuinely belongs to `project_id` on CurseForge
    and that `project_id` is a valid mod project (not a modpack).
    Returns (is_valid: bool, reason: str).
    """
    try:
        req = urllib.request.Request(f"https://api.cfwidget.com/{project_id}", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="replace"))
        cf_url = (data.get("urls") or {}).get("curseforge") or ""
        if "/modpacks/" in cf_url:
            return False, f"Project {project_id} ('{data.get('title')}') is a Modpack, not a Mod!"
        files = data.get("files") or []
        if files:
            known_fids = {int(f["id"]) for f in files if "id" in f}
            if int(file_id) not in known_fids:
                return False, f"File ID {file_id} does NOT belong to Project ID {project_id} ('{data.get('title')}')!"
        return True, "OK"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False, f"Project ID {project_id} returned HTTP 404 on CurseForge/CFWidget!"
        return True, f"Skipped online check ({e})"
    except Exception as e:
        return True, f"Skipped online check ({e})"


def load_pw_toml_index(mods_dir):
    """Loads CurseForge metadata from mods/.index/*.pw.toml."""
    index_dir = os.path.join(mods_dir, ".index")
    pw_by_fn = {}
    if not os.path.isdir(index_dir):
        return pw_by_fn

    for toml_path in glob.glob(os.path.join(index_dir, "*.pw.toml")):
        try:
            with open(toml_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception:
            continue
        fn = None
        pid = None
        fid = None
        name = None
        side = None
        slug_stem = os.path.splitext(os.path.splitext(os.path.basename(toml_path))[0])[0]
        for line in lines:
            l = line.strip()
            if l.startswith("filename ="):
                fn = l.split("=", 1)[1].strip().strip('"').strip("'")
            elif l.startswith("name ="):
                name = l.split("=", 1)[1].strip().strip('"').strip("'")
            elif l.startswith("side ="):
                side = l.split("=", 1)[1].strip().strip('"').strip("'").lower()
            elif l.startswith("project-id ="):
                try:
                    pid = int(l.split("=", 1)[1].strip())
                except Exception:
                    pass
            elif l.startswith("file-id ="):
                try:
                    fid = int(l.split("=", 1)[1].strip())
                except Exception:
                    pass
        if fn:
            pw_by_fn[fn] = {"projectID": pid, "fileID": fid, "name": name, "side": side, "slug": slug_stem}
    return pw_by_fn


def load_cf_instance_metadata():
    """Loads CurseForge instance metadata from Peak (Dev)/minecraftinstance.json if present."""
    cf_by_fn = {}
    cf_by_pid = {}
    if not os.path.isfile(CF_INST_FILE):
        return cf_by_fn, cf_by_pid
    try:
        with open(CF_INST_FILE, "r", encoding="utf-8") as f:
            inst_data = json.load(f)
        for addon in inst_data.get("installedAddons", []):
            pid = addon.get("addonID")
            name = addon.get("name", "")
            url = addon.get("webSiteURL", "")
            authors = [a.get("name", "") for a in addon.get("authors", []) if a.get("name")]
            inst_file = addon.get("installedFile") or {}
            fid = inst_file.get("id")
            fn = inst_file.get("fileNameOnDisk") or inst_file.get("fileName")
            info = {
                "projectID": pid,
                "fileID": fid,
                "name": name,
                "url": url,
                "authors": authors,
                "filename": fn
            }
            if fn:
                cf_by_fn[fn] = info
            if pid:
                cf_by_pid[pid] = info
    except Exception:
        pass
    return cf_by_fn, cf_by_pid


def load_master_registry():
    if not os.path.isfile(REGISTRY_FILE):
        raise RuntimeError(f"Master CurseForge mod registry not found at: {REGISTRY_FILE}")
    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_master_registry(registry):
    sorted_reg = {k: registry[k] for k in sorted(registry.keys())}
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted_reg, f, indent=2)


def apply_cli_mappings(registry, map_args):
    """Applies manual --map <filename>=<projectID>:<fileID> overrides to the master registry."""
    if not map_args:
        return False
    mods_dir = os.path.join(DEV_MC, "mods")
    _, cf_by_pid = load_cf_instance_metadata()

    # Build lookup by mod_id / projectID from existing registry to inherit metadata
    reg_by_pid = {v["projectID"]: v for v in registry.values() if "projectID" in v}

    modified = False
    for item in map_args:
        if "=" not in item or ":" not in item:
            raise ValueError(f"Invalid --map format '{item}'. Expected: <filename.jar>=<projectID>:<fileID>")
        fn, ids = item.split("=", 1)
        pid_str, fid_str = ids.split(":", 1)
        pid, fid = int(pid_str.strip()), int(fid_str.strip())
        fn = fn.strip()

        jar_path = os.path.join(mods_dir, fn)
        if not os.path.isfile(jar_path):
            raise FileNotFoundError(f"Cannot map '{fn}': file not found in {mods_dir}")

        ok, reason = verify_cf_file_ownership(pid, fid)
        if not ok:
            raise RuntimeError(f"FATAL CURSEFORGE OWNERSHIP ERROR for '{fn}': {reason}")

        jmeta = inspect_jar_file(jar_path)
        prev = reg_by_pid.get(pid) or cf_by_pid.get(pid) or {}
        slug = re.sub(r"[^a-z0-9]+", "-", (prev.get("name") or fn).lower()).strip("-")

        registry[fn] = {
            "filename": fn,
            "projectID": pid,
            "fileID": fid,
            "name": prev.get("name") or fn,
            "authors": prev.get("authors") or ["Mod Author"],
            "url": prev.get("url") or f"https://www.curseforge.com/minecraft/mc-mods/{slug}",
            "mod_ids": jmeta["mod_ids"],
            "mod_version": jmeta["mod_version"],
            "sha1": jmeta["sha1"],
            "size": jmeta["size"],
            "client_side_only": prev.get("client_side_only", False),
            "lite_excluded": prev.get("lite_excluded", False),
            "has_mandatory_network_channels": jmeta["has_mandatory_network_channels"]
        }
        print(f"[MANUAL MAP APPLIED] {fn} -> projectID: {pid}, fileID: {fid}")
        modified = True

    if modified:
        save_master_registry(registry)
    return modified


def resolve_and_verify_mods(mods_dir, edition_label="PEAK (Dev)", update_registry=True):
    """
    100% Disk-Driven Mod Resolver & Validator.
    Scans every active .jar file in `mods_dir` and resolves its exact CurseForge (projectID, fileID).
    Halts with a loud, actionable error if any new or updated mod lacks a valid CurseForge mapping.
    """
    registry = load_master_registry()
    pw_by_fn = load_pw_toml_index(mods_dir)
    cf_by_fn, cf_by_pid = load_cf_instance_metadata()

    # Index existing registry by mod_id and projectID to identify updated versions of known mods
    reg_by_mod_id = {}
    reg_by_pid = {}
    for r_fn, r_meta in registry.items():
        reg_by_pid[r_meta["projectID"]] = r_meta
        for mid in r_meta.get("mod_ids", []):
            reg_by_mod_id[mid] = r_meta

    active_jars = sorted([
        f for f in os.listdir(mods_dir)
        if os.path.isfile(os.path.join(mods_dir, f)) and f.endswith(".jar")
    ])

    resolved_mods = []
    auto_registered_new = []
    auto_updated = []
    replaced_old_filenames = set()
    unmapped_errors = []
    registry_dirty = False

    for fn in active_jars:
        jar_path = os.path.join(mods_dir, fn)
        pw_info = pw_by_fn.get(fn)
        cf_info = cf_by_fn.get(fn)
        reg_info = registry.get(fn)

        # Case 1: Known filename in registry
        if reg_info is not None:
            # Verify file size / SHA1 hasn't silently changed in-place
            cur_size = os.path.getsize(jar_path)
            if cur_size != reg_info.get("size"):
                jmeta = inspect_jar_file(jar_path)
            else:
                jmeta = None

            if jmeta and jmeta["sha1"] != reg_info.get("sha1"):
                # JAR with same filename was modified in-place; check .pw.toml or CFWidget
                new_fid = None
                if pw_info and pw_info.get("projectID") and pw_info.get("fileID") and pw_info["fileID"] != reg_info["fileID"]:
                    new_fid = pw_info["fileID"]
                else:
                    cfw = resolve_via_cfwidget(fn, jmeta["size"], project_id=reg_info["projectID"])
                    if cfw and cfw["fileID"] != reg_info["fileID"]:
                        new_fid = cfw["fileID"]

                if new_fid:
                    old_fid = reg_info["fileID"]
                    reg_info["fileID"] = new_fid
                    reg_info["sha1"] = jmeta["sha1"]
                    reg_info["size"] = jmeta["size"]
                    reg_info["mod_version"] = jmeta["mod_version"]
                    reg_info["has_mandatory_network_channels"] = jmeta["has_mandatory_network_channels"]
                    auto_updated.append((fn, reg_info["name"], reg_info["projectID"], old_fid, reg_info["fileID"]))
                    registry_dirty = True
                else:
                    unmapped_errors.append(
                        f"  [!] IN-PLACE MODIFIED JAR: '{fn}' (SHA-1 changed on disk, but CurseForge fileID is unchanged: {reg_info['fileID']}).\n"
                        f"      -> Run with: --map \"{fn}={reg_info['projectID']}:<NEW_FILE_ID>\""
                    )
                    continue

            # Also check if .pw.toml has an updated CurseForge fileID
            if pw_info and pw_info.get("projectID") == reg_info["projectID"] and pw_info.get("fileID"):
                if pw_info["fileID"] != reg_info["fileID"]:
                    old_fid = reg_info["fileID"]
                    reg_info["fileID"] = pw_info["fileID"]
                    auto_updated.append((fn, reg_info["name"], reg_info["projectID"], old_fid, reg_info["fileID"]))
                    registry_dirty = True

            resolved_mods.append(reg_info)
            continue

        # Case 2: New filename on disk (either a newly added mod or an updated version of an existing mod)
        jmeta = inspect_jar_file(jar_path)
        pid = None
        fid = None
        name = ""
        authors = []
        url = ""

        if pw_info and pw_info.get("projectID") and pw_info.get("fileID"):
            pid = pw_info["projectID"]
            fid = pw_info["fileID"]
            name = pw_info.get("name") or fn
        elif cf_info and cf_info.get("projectID") and cf_info.get("fileID"):
            pid = cf_info["projectID"]
            fid = cf_info["fileID"]
            name = cf_info.get("name") or fn
            authors = cf_info.get("authors") or []
            url = cf_info.get("url") or ""

        # Inherit metadata from previous version in registry or CurseForge instance if available
        prev_entry = reg_by_pid.get(pid) if pid else None
        if not prev_entry:
            for mid in jmeta["mod_ids"]:
                if mid in reg_by_mod_id:
                    prev_entry = reg_by_mod_id[mid]
                    break

        # If updated or added via Modrinth / manual drop without CF fileID, auto-resolve via CFWidget API
        if not (pid and fid):
            candidate_pid = prev_entry["projectID"] if prev_entry else None
            candidate_slugs = []
            if prev_entry and prev_entry.get("url"):
                candidate_slugs.append(prev_entry["url"].rstrip("/").split("/")[-1])
            if pw_info and pw_info.get("slug"):
                candidate_slugs.append(pw_info["slug"])
            if pw_info and pw_info.get("name"):
                candidate_slugs.append(re.sub(r"[^a-z0-9]+", "-", pw_info["name"].lower()).strip("-"))
            for mid in jmeta["mod_ids"]:
                candidate_slugs.append(mid.replace("_", "-"))
                candidate_slugs.append(mid)

            cfw = resolve_via_cfwidget(fn, jmeta["size"], project_id=candidate_pid, candidate_slugs=candidate_slugs)
            if cfw:
                pid = cfw["projectID"]
                fid = cfw["fileID"]
                name = cfw.get("name") or name or fn
                url = cfw.get("url") or url

        if pid and fid:
            if pid in DEAD_PIDS:
                unmapped_errors.append(
                    f"  [!] DEAD CURSEFORGE PROJECT ID: '{fn}' maps to dead/deleted projectID {pid}."
                )
                continue

            ok, reason = verify_cf_file_ownership(pid, fid)
            if not ok:
                unmapped_errors.append(
                    f"  [!] INVALID CURSEFORGE FILE OWNERSHIP for '{fn}': {reason}"
                )
                continue

            if prev_entry:
                name = prev_entry.get("name") or name
                authors = prev_entry.get("authors") or authors
                url = prev_entry.get("url") or url
                client_only = prev_entry.get("client_side_only", False)
                lite_excl = prev_entry.get("lite_excluded", False)
                old_fid = prev_entry.get("fileID")
                old_fn = prev_entry.get("filename")
                if old_fn and old_fn != fn:
                    replaced_old_filenames.add(old_fn)
                auto_updated.append((fn, name, pid, f"{old_fn} ({old_fid})", fid))
            else:
                if pid in cf_by_pid:
                    c = cf_by_pid[pid]
                    name = c.get("name") or name
                    authors = c.get("authors") or authors
                    url = c.get("url") or url
                slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
                if not url:
                    url = f"https://www.curseforge.com/minecraft/mc-mods/{slug}"
                if not authors:
                    authors = ["Mod Author"]
                client_only = bool((pw_info and pw_info.get("side") == "client") or jmeta.get("is_client_only_toml"))
                lite_excl = False
                auto_registered_new.append((fn, name, pid, fid))
                if client_only and update_registry:
                    srv_excl_path = os.path.join(DEV_MC, "server_pack_excluded_mods.txt")
                    if os.path.isfile(srv_excl_path):
                        with open(srv_excl_path, "r", encoding="utf-8") as sf:
                            existing_srv = sf.read().lower()
                        if fn.lower() not in existing_srv:
                            with open(srv_excl_path, "a", encoding="utf-8") as sf:
                                sf.write(f"\n{fn}")
                            print(f"   [AUTO-EXCLUDED CLIENT MOD FROM SERVER PACK]: {fn}")

            new_entry = {
                "filename": fn,
                "projectID": pid,
                "fileID": fid,
                "name": name,
                "authors": authors,
                "url": url,
                "mod_ids": jmeta["mod_ids"],
                "mod_version": jmeta["mod_version"],
                "sha1": jmeta["sha1"],
                "size": jmeta["size"],
                "client_side_only": client_only,
                "lite_excluded": lite_excl,
                "has_mandatory_network_channels": jmeta["has_mandatory_network_channels"]
            }
            registry[fn] = new_entry
            resolved_mods.append(new_entry)
            registry_dirty = True
        else:
            # FAIL-FAST: Active JAR on disk has NO CurseForge (projectID, fileID)!
            if prev_entry:
                unmapped_errors.append(
                    f"  [!] UPDATED MOD MISSING CURSEFORGE FILE ID: '{fn}'\n"
                    f"      -> Identified as update of '{prev_entry['filename']}' ({prev_entry['name']}, modId: {jmeta['mod_ids']})\n"
                    f"      -> CurseForge projectID: {prev_entry['projectID']} | Previous fileID: {prev_entry['fileID']}\n"
                    f"      -> Fix: Re-run with --map \"{fn}={prev_entry['projectID']}:<NEW_CURSEFORGE_FILE_ID>\""
                )
            else:
                unmapped_errors.append(
                    f"  [!] NEW UNMAPPED MOD ON DISK: '{fn}' (modId: {jmeta['mod_ids']}, version: {jmeta['mod_version']})\n"
                    f"      -> Added via Modrinth or manual drop without CurseForge projectID/fileID metadata.\n"
                    f"      -> Fix: Re-run with --map \"{fn}=<CURSEFORGE_PROJECT_ID>:<CURSEFORGE_FILE_ID>\""
                )

    # Prune obsolete entries from master registry when running on DEV_MC
    removed_from_registry = []
    if os.path.realpath(mods_dir) == os.path.realpath(os.path.join(DEV_MC, "mods")):
        active_set = set(active_jars)
        for r_fn in list(registry.keys()):
            if r_fn not in active_set:
                removed_meta = registry.pop(r_fn)
                if r_fn not in replaced_old_filenames:
                    removed_from_registry.append((r_fn, removed_meta.get("name"), removed_meta.get("projectID")))
                registry_dirty = True

    print(f"\n========================================================")
    print(f" Disk-to-Manifest Audit: {edition_label}")
    print(f" Directory: {mods_dir}")
    print(f" Active JARs on Disk: {len(active_jars)}")
    print(f"========================================================")

    if auto_registered_new:
        print(f"[NEW MODS AUTO-REGISTERED] ({len(auto_registered_new)}):")
        for fn, name, pid, fid in auto_registered_new:
            print(f"   + {fn} [{name}] -> projectID: {pid}, fileID: {fid}")

    if auto_updated:
        print(f"[UPDATED MODS AUTO-SYNCED] ({len(auto_updated)}):")
        for fn, name, pid, old_desc, fid in auto_updated:
            print(f"   ~ {fn} [{name}] (PID {pid}): {old_desc} -> {fid}")

    if removed_from_registry:
        print(f"[REMOVED / DISABLED MODS PRUNED] ({len(removed_from_registry)}):")
        for fn, name, pid in removed_from_registry:
            print(f"   - {fn} [{name}] (PID {pid})")

    if not auto_registered_new and not auto_updated and not removed_from_registry and not unmapped_errors:
        print("[STATUS] All active JARs on disk match the verified CurseForge registry 1-to-1.")

    if unmapped_errors:
        print("\n========================================================")
        print(" FATAL EXPORT BLOCKED: UNMAPPED OR STALE MODS DETECTED!")
        print("========================================================")
        for err in unmapped_errors:
            print(err)
        print("========================================================\n")
        sys.exit(1)

    # Verify zero duplicate projectIDs among active mods
    seen_pids = {}
    for m in resolved_mods:
        pid = m["projectID"]
        if pid in seen_pids:
            raise RuntimeError(
                f"FATAL: Duplicate CurseForge projectID {pid} on disk: '{seen_pids[pid]}' and '{m['filename']}'! "
                f"Delete the older duplicate JAR from {mods_dir}."
            )
        seen_pids[pid] = m["filename"]

    assert len(resolved_mods) == len(active_jars), (
        f"FATAL 1-TO-1 INVARIANT VIOLATION: Resolved {len(resolved_mods)} mods != {len(active_jars)} active JARs!"
    )

    if registry_dirty and update_registry:
        save_master_registry(registry)
        print(f"[REGISTRY] Updated {REGISTRY_FILE} with live disk changes.")

    return resolved_mods


def print_release_diff(current_mods, current_version, is_lite=False):
    """Compares the current manifest against the previous export in PackExports/ and prints a diff table."""
    prefix = "Peak-Lite-" if is_lite else "Peak-"
    candidates = []
    if os.path.isdir(PACK_EXPORTS_DIR):
        for fn in os.listdir(PACK_EXPORTS_DIR):
            if not fn.endswith(".zip"):
                continue
            if is_lite and fn.startswith("Peak-Lite-") and fn != f"Peak-Lite-{current_version}.zip":
                candidates.append(os.path.join(PACK_EXPORTS_DIR, fn))
            elif not is_lite and fn.startswith("Peak-") and not fn.startswith("Peak-Lite-") and not fn.startswith("Peak-Server-") and fn != f"Peak-{current_version}.zip":
                candidates.append(os.path.join(PACK_EXPORTS_DIR, fn))

    if not candidates:
        return

    candidates.sort(key=lambda p: os.path.getmtime(p), reverse=True)
    prev_zip = candidates[0]
    try:
        with zipfile.ZipFile(prev_zip, "r") as zf:
            prev_man = json.loads(zf.read("manifest.json").decode("utf-8-sig"))
    except Exception:
        return

    prev_files = {f["projectID"]: f["fileID"] for f in prev_man.get("files", [])}
    curr_by_pid = {m["projectID"]: m for m in current_mods}

    added = [m for pid, m in curr_by_pid.items() if pid not in prev_files]
    removed = [pid for pid in prev_files if pid not in curr_by_pid]
    updated = [
        (m, prev_files[pid], m["fileID"])
        for pid, m in curr_by_pid.items()
        if pid in prev_files and prev_files[pid] != m["fileID"]
    ]

    print(f"--------------------------------------------------------")
    print(f" Release Diff vs. {os.path.basename(prev_zip)} ({len(prev_files)} -> {len(current_mods)} mods)")
    print(f"   + Added: {len(added)} | ~ Updated: {len(updated)} | - Removed: {len(removed)}")
    for m in added:
        print(f"     [+] {m['name']} ({m['filename']}) [PID {m['projectID']}, FID {m['fileID']}]")
    for m, old_fid, new_fid in updated:
        print(f"     [~] {m['name']} ({m['filename']}) [PID {m['projectID']}: {old_fid} -> {new_fid}]")
    for pid in removed:
        print(f"     [-] Removed PID {pid} (prev FID {prev_files[pid]})")
    print(f"--------------------------------------------------------")


def build_modlist_html(resolved_mods):
    """Generates clean, deterministic CurseForge modlist.html directly from the resolved mods."""
    sorted_mods = sorted(resolved_mods, key=lambda m: (m.get("name") or m["filename"]).lower())
    lines = ["<ul>"]
    for m in sorted_mods:
        url = m.get("url") or f"https://www.curseforge.com/minecraft/mc-mods/{m['projectID']}"
        name = m.get("name") or m["filename"]
        authors = ", ".join(m.get("authors") or ["Mod Author"])
        lines.append(f'<li><a href="{url}">{name} (by {authors})</a></li>')
    lines.append("</ul>")
    return ("\n".join(lines) + "\n").encode("utf-8")


def load_logo_bytes():
    """Loads the modpack profile image from minecraft/icon.png or Peak-alpha1.zip."""
    icon_path = os.path.join(DEV_MC, "icon.png")
    if os.path.isfile(ALPHA1_ZIP):
        try:
            with zipfile.ZipFile(ALPHA1_ZIP, "r") as zf:
                return zf.read("profileImage/logo_square_preview.png")
        except Exception:
            pass
    if os.path.isfile(icon_path):
        with open(icon_path, "rb") as f:
            return f.read()
    return b""


def collect_overrides(mc_dir, is_lite=False):
    """Walks override folders and collects file entries, stripping BOMs and preventing loose jars."""
    entries = {}
    override_folders = ["config", "defaultconfigs", "kubejs", "fancymenu_data"]
    for folder in override_folders:
        folder_path = os.path.join(mc_dir, folder)
        if not os.path.isdir(folder_path):
            continue

        for root, dirs, files in os.walk(folder_path):
            if folder == "config":
                dirs[:] = [d for d in dirs if d.lower() not in IGNORED_CONFIG_DIRS]
            elif folder == "fancymenu_data":
                dirs[:] = [d for d in dirs if d.lower() not in IGNORED_FANCYMENU_DATA_DIRS]

            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in IGNORED_EXTENSIONS:
                    continue
                if folder == "config" and file.lower() in IGNORED_CONFIG_FILES:
                    continue
                if folder == "fancymenu_data" and file.lower() in IGNORED_FANCYMENU_DATA_FILES:
                    continue
                if file.lower().endswith(".jar") or file.lower().endswith(".jar.disabled"):
                    raise RuntimeError(f"FATAL: Loose JAR found in overrides: {file} at {root}")

                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, mc_dir)
                entry_name = ("overrides/" + rel_path.replace("\\", "/")).strip()

                with open(abs_path, "rb") as f_in:
                    content = f_in.read()

                if content.startswith(b"\xef\xbb\xbf"):
                    content = content[3:]

                if is_lite and entry_name == "overrides/config/DistantHorizons.toml":
                    text = content.decode("utf-8", errors="replace")
                    text = re.sub(r"lodChunkRenderDistanceRadius\s*=\s*\d+", "lodChunkRenderDistanceRadius = 32", text)
                    content = text.encode("utf-8")

                if is_lite and entry_name == "overrides/config/bettercombat/client.json5":
                    text = content.decode("utf-8", errors="replace")
                    text = re.sub(r'"firstPersonAnimations"\s*:\s*"[^"]*"', '"firstPersonAnimations": "YES"', text)
                    content = text.encode("utf-8")

                if entry_name == "overrides/config/fancymenu/options.txt":
                    text = content.decode("utf-8", errors="replace")
                    text = re.sub(r"B:modpack_mode\s*=\s*'[a-zA-Z]+';", "B:modpack_mode = 'true';", text)
                    text = re.sub(r"B:show_welcome_screen\s*=\s*'[a-zA-Z]+';", "B:show_welcome_screen = 'false';", text)
                    content = text.encode("utf-8")

                entries[entry_name] = content

    options_path = os.path.join(mc_dir, "options.txt")
    if os.path.isfile(options_path):
        with open(options_path, "rb") as f_in:
            opt_content = f_in.read()
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
        entries["overrides/options.txt"] = ("\n".join(clean_lines) + "\n").encode("utf-8")

    return entries


def verify_cross_play_network_parity(dev_mods, lite_mods):
    """
    Ensures that no mod excluded from PEAK Lite registers mandatory non-optional network channels.
    Prevents ModMismatchDisconnectedScreen when PEAK Lite joins a PEAK Essential or Dedicated server.
    """
    lite_pids = {m["projectID"] for m in lite_mods}
    dev_pids = {m["projectID"] for m in dev_mods}

    extra_in_lite = [m for m in lite_mods if m["projectID"] not in dev_pids]
    if extra_in_lite:
        names = [f"{m['filename']} (PID {m['projectID']})" for m in extra_in_lite]
        raise RuntimeError(f"FATAL PARITY ERROR: PEAK Lite contains mods not present in PEAK Dev: {names}")

    excluded_from_lite = [m for m in dev_mods if m["projectID"] not in lite_pids]
    channel_violations = [m for m in excluded_from_lite if m.get("has_mandatory_network_channels")]

    if channel_violations:
        print("\n========================================================")
        print(" FATAL CROSS-PLAY NETWORK PARITY VIOLATION DETECTED!")
        print("========================================================")
        for m in channel_violations:
            print(f"  [!] Mod '{m['name']}' ({m['filename']}, PID {m['projectID']}) is excluded from PEAK Lite,")
            print(f"      but registers non-optional network channels! PEAK Lite clients will fail to connect to PEAK servers!")
        print("========================================================\n")
        sys.exit(1)

    print(f"[NETWORK PARITY] Verified {len(excluded_from_lite)} Lite-excluded visual/client mods: 0 mandatory network channel conflicts.")


def build_dev_pack(version="alpha3", audit_only=False):
    neoforge_ver = get_neoforge_version()
    mc_ver = get_minecraft_version()
    dev_mods_dir = os.path.join(DEV_MC, "mods")

    resolved_mods = resolve_and_verify_mods(dev_mods_dir, edition_label=f"PEAK ({version})", update_registry=True)
    print_release_diff(resolved_mods, version, is_lite=False)

    if audit_only:
        return resolved_mods

    dev_out_zip = os.path.join(PACK_EXPORTS_DIR, f"Peak-{version}.zip")
    dev_staged_zip = os.path.join(TEMP_DIR, f"Peak-{version}.zip")
    print(f"\nBuilding CurseForge Export: Peak-{version}.zip ({len(resolved_mods)} mods, NeoForge {neoforge_ver})...")

    manifest_data = {
        "minecraft": {
            "version": mc_ver,
            "modLoaders": [{"id": f"neoforge-{neoforge_ver}", "primary": True}],
            "recommendedRam": 7520
        },
        "manifestType": "minecraftModpack",
        "manifestVersion": 1,
        "name": "Peak",
        "version": version,
        "author": "eldodoron",
        "files": [
            {"projectID": m["projectID"], "fileID": m["fileID"], "required": True}
            for m in resolved_mods
        ],
        "overrides": "overrides"
    }

    manifest_bytes = json.dumps(manifest_data, indent=2).encode("utf-8")
    assert manifest_bytes[0] == ord("{"), "Manifest must start with '{' (no BOM)"

    modlist_bytes = build_modlist_html(resolved_mods)
    logo_bytes = load_logo_bytes()

    print("Collecting overrides from PEAK-dev...")
    overrides = collect_overrides(DEV_MC, is_lite=False)
    print(f"Collected {len(overrides)} override files.")

    os.makedirs(PACK_EXPORTS_DIR, exist_ok=True)
    temp_zip = dev_out_zip + ".tmp"
    with zipfile.ZipFile(temp_zip, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        zout.writestr("manifest.json", manifest_bytes)
        zout.writestr("modlist.html", modlist_bytes)
        if logo_bytes:
            zout.writestr("profileImage/logo_square_preview.png", logo_bytes)
        for name, content in overrides.items():
            zout.writestr(name, content)

    if os.path.exists(dev_out_zip):
        os.remove(dev_out_zip)
    shutil.move(temp_zip, dev_out_zip)
    print(f"Export ZIP written to: {dev_out_zip} ({os.path.getsize(dev_out_zip) / (1024*1024):.2f} MB)")

    shutil.copy2(dev_out_zip, dev_staged_zip)
    print(f"Staged ZIP for browser agent at: {dev_staged_zip}")

    with zipfile.ZipFile(dev_out_zip, "r") as zver:
        man_raw = zver.read("manifest.json")
        assert man_raw[0] == ord("{")
        man = json.loads(man_raw.decode("utf-8"))
        assert man["name"] == "Peak"
        assert man["version"] == version
        assert man["author"] == "eldodoron"
        assert man["minecraft"]["modLoaders"][0]["id"] == f"neoforge-{neoforge_ver}"
        assert len(man["files"]) == len(resolved_mods)
        jars = [n for n in zver.namelist() if n.endswith(".jar") or n.endswith(".jar.disabled")]
        assert len(jars) == 0, f"Found loose jars in overrides: {jars}"

    print(f"[VERIFIED] Peak-{version}.zip ({len(resolved_mods)} mods) passed all integrity checks!")
    return resolved_mods


def build_lite_pack(dev_mods, version="alpha3", audit_only=False):
    # Mandatory Pre-Export Synchronization from PEAK-dev -> PEAK-Lite
    import sync_to_lite
    sync_to_lite.run_sync(dry_run=audit_only)

    neoforge_ver = get_neoforge_version()
    mc_ver = get_minecraft_version()
    lite_mods_dir = os.path.join(LITE_MC, "mods")

    if audit_only:
        lite_exclusions = sync_to_lite.load_exclusions(dry_run=True)
        lite_mods = [m for m in dev_mods if not sync_to_lite.is_excluded(m["filename"], lite_exclusions)]
        print(f"\n========================================================")
        print(f" Disk-to-Manifest Audit: PEAK Lite ({version}) [Projected from Dev - Exclusions]")
        print(f" Projected Active JARs: {len(lite_mods)} (excluded {len(dev_mods) - len(lite_mods)} visual/client mods)")
        print(f"========================================================")
    else:
        lite_mods = resolve_and_verify_mods(lite_mods_dir, edition_label=f"PEAK Lite ({version})", update_registry=False)

    verify_cross_play_network_parity(dev_mods, lite_mods)
    print_release_diff(lite_mods, version, is_lite=True)

    if audit_only:
        return lite_mods

    lite_out_zip = os.path.join(PACK_EXPORTS_DIR, f"Peak-Lite-{version}.zip")
    lite_staged_zip = os.path.join(TEMP_DIR, f"Peak-Lite-{version}.zip")
    print(f"\nBuilding CurseForge Export: Peak-Lite-{version}.zip ({len(lite_mods)} mods, NeoForge {neoforge_ver})...")

    lite_manifest = {
        "minecraft": {
            "version": mc_ver,
            "modLoaders": [{"id": f"neoforge-{neoforge_ver}", "primary": True}],
            "recommendedRam": 6348
        },
        "manifestType": "minecraftModpack",
        "manifestVersion": 1,
        "name": "Peak Lite",
        "version": version,
        "author": "eldodoron",
        "files": [
            {"projectID": m["projectID"], "fileID": m["fileID"], "required": True}
            for m in lite_mods
        ],
        "overrides": "overrides"
    }

    manifest_bytes = json.dumps(lite_manifest, indent=2).encode("utf-8")
    assert manifest_bytes[0] == ord("{"), "Manifest must start with '{' (no BOM)"

    modlist_bytes = build_modlist_html(lite_mods)
    logo_bytes = load_logo_bytes()

    print("Collecting overrides from PEAK-Lite...")
    overrides = collect_overrides(LITE_MC, is_lite=True)
    print(f"Collected {len(overrides)} override files for Lite.")

    os.makedirs(PACK_EXPORTS_DIR, exist_ok=True)
    temp_zip = lite_out_zip + ".tmp"
    with zipfile.ZipFile(temp_zip, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        zout.writestr("manifest.json", manifest_bytes)
        zout.writestr("modlist.html", modlist_bytes)
        if logo_bytes:
            zout.writestr("profileImage/logo_square_preview.png", logo_bytes)
        for name, content in overrides.items():
            zout.writestr(name, content)

    if os.path.exists(lite_out_zip):
        os.remove(lite_out_zip)
    shutil.move(temp_zip, lite_out_zip)
    print(f"Export ZIP written to: {lite_out_zip} ({os.path.getsize(lite_out_zip) / (1024*1024):.2f} MB)")

    shutil.copy2(lite_out_zip, lite_staged_zip)
    print(f"Staged ZIP for browser agent at: {lite_staged_zip}")

    with zipfile.ZipFile(lite_out_zip, "r") as zver:
        man_raw = zver.read("manifest.json")
        assert man_raw[0] == ord("{")
        man = json.loads(man_raw.decode("utf-8"))
        assert man["name"] == "Peak Lite"
        assert man["version"] == version
        assert man["author"] == "eldodoron"
        assert man["minecraft"]["modLoaders"][0]["id"] == f"neoforge-{neoforge_ver}"
        assert man["minecraft"]["recommendedRam"] == 6348
        assert len(man["files"]) == len(lite_mods)
        jars = [n for n in zver.namelist() if n.endswith(".jar") or n.endswith(".jar.disabled")]
        assert len(jars) == 0, f"Found loose jars in Lite overrides: {jars}"
        dh_raw = zver.read("overrides/config/DistantHorizons.toml").decode("utf-8")
        assert "lodChunkRenderDistanceRadius = 32" in dh_raw, "DH radius in Lite is not 32!"
        bc_raw = zver.read("overrides/config/bettercombat/client.json5").decode("utf-8")
        assert '"firstPersonAnimations": "YES"' in bc_raw, "Better Combat first person animations not enabled in Lite!"

    print(f"[VERIFIED] Peak-Lite-{version}.zip ({len(lite_mods)} mods) passed all integrity and cross-play checks!")
    return lite_mods


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Official Mistake-Proof PEAK Modpack Export & Audit Engine")
    parser.add_argument("--version", type=str, default="alpha3", help="Target release version string (e.g. alpha3)")
    parser.add_argument("--audit", action="store_true", help="Run full 1-to-1 disk audit, Lite sync check, and network parity check without writing ZIPs")
    parser.add_argument("--lite", action="store_true", help="Also synchronize and build PEAK Lite export")
    parser.add_argument("--only-lite", action="store_true", help="Synchronize and build only PEAK Lite export")
    parser.add_argument("--server", action="store_true", help="Also build or verify PEAK Dedicated Server Pack")
    parser.add_argument("--all", action="store_true", help="Build/audit all three editions: PEAK, PEAK Lite, and PEAK Server Pack")
    parser.add_argument("--map", action="append", help="Register/update a manual/Modrinth JAR: <filename.jar>=<projectID>:<fileID>")
    args = parser.parse_args()

    if args.map:
        reg = load_master_registry()
        apply_cli_mappings(reg, args.map)

    run_lite = args.lite or args.only_lite or args.all or args.audit
    run_server = args.server or args.all or args.audit

    dev_mods = build_dev_pack(version=args.version, audit_only=(args.audit or args.only_lite))
    if run_lite:
        build_lite_pack(dev_mods, version=args.version, audit_only=args.audit)
    if run_server:
        import build_server_pack
        if args.audit:
            exclusions = build_server_pack.load_exclusions(dry_run=True)
            src_mods = os.path.join(DEV_MC, "mods")
            active = [f for f in os.listdir(src_mods) if f.endswith(".jar") and os.path.isfile(os.path.join(src_mods, f))]
            srv_mods = [f for f in active if not build_server_pack.is_excluded(f, exclusions)]
            excl_mods = [f for f in active if build_server_pack.is_excluded(f, exclusions)]
            server_only_dir = os.path.join(BASE_DEV, "scrapped_tools", "server_only_mods")
            srv_only_mods = [f for f in os.listdir(server_only_dir) if f.endswith(".jar")] if os.path.isdir(server_only_dir) else []
            total_srv_count = len(srv_mods) + len(srv_only_mods)
            print(f"\n[SERVER PACK AUDIT] Active client/common mods: {len(active)} | Server mods: {total_srv_count} ({len(srv_mods)} common + {len(srv_only_mods)} server-only) | Excluded client/dev mods: {len(excl_mods)}")
        else:
            build_server_pack.stage_server_pack(version=args.version)
            build_server_pack.compress_and_verify(version=args.version)
