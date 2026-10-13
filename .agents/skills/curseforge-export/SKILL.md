---
name: curseforge-export
description: Procedures and verification scripts for packaging, sanitizing manifest.json (BOM stripping, loose jar migration, dead ID purging), and uploading CurseForge modpacks.
---

# CurseForge Modpack Export & Validation Guide

This skill provides the required procedures, verification scripts, and automated upload patterns for publishing modpack ZIP exports to CurseForge without ingestion rejections.

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

