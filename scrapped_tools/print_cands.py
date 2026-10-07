import sys
sys.path.append('.')
from scrapped_tools.find_more_candidates import candidates

for fn, info in candidates[:25]:
    print(f"{fn} | id: {info['mod_id']} | name: {info['name']} | c_mixins: {info['mixins_client']}, com_mixins: {info['mixins_common']}, pkts: {info['packet_classes']}")
