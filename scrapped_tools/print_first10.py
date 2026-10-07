import sys
sys.path.append('.')
from scrapped_tools.audit_nodata_mods import nodata_included

for i, item in enumerate(nodata_included[:10], 1):
    ratio = f"{item['client_classes_count']}/{item['classes_count']}"
    print(f"{i:2d}. {item['filename']} | {item['name']} | {ratio} | mixins: {len(item['mixins'])}")
