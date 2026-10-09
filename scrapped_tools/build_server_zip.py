import os
import zipfile
import time

staging_dir = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\ServerPackStaging"
output_zip = r"C:\Users\chris\Desktop\PEAK DEV MULTIMEDIA\PackExports\Peak-Server-alpha1.zip"

print(f"Starting Step 3: Compressing Server Pack...")
print(f"Source: {staging_dir}")
print(f"Destination: {output_zip}")

start_time = time.time()
file_count = 0

with zipfile.ZipFile(output_zip, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
    for root, dirs, files in os.walk(staging_dir):
        for f in files:
            full_path = os.path.join(root, f)
            # Relative path inside zip (must NOT contain ServerPackStaging root folder)
            rel_path = os.path.relpath(full_path, staging_dir).replace("\\", "/")
            zout.write(full_path, arcname=rel_path)
            file_count += 1

elapsed = time.time() - start_time
zip_size = os.path.getsize(output_zip)

print(f"\nCompression complete in {elapsed:.1f} seconds!")
print(f"Total Files in ZIP: {file_count}")
print(f"Archive Size: {zip_size / (1024*1024):.2f} MB ({zip_size:,} bytes)")

# Integrity verification
print("Verifying archive integrity...")
with zipfile.ZipFile(output_zip, 'r') as zver:
    corrupt = zver.testzip()
    if corrupt:
        print(f"ERROR: Corrupt file detected: {corrupt}")
    else:
        root_items = set(n.split('/')[0] for n in zver.namelist())
        print(f"Archive test passed! Root items directly in ZIP: {sorted(list(root_items))}")
