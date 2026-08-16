import glob
import zipfile
import json
import os

books_to_check = [
    'wind_spellbooks:wind_spell_book',
    'ess_requiem:spellblade_spellbook',
    'irons_spellbooks:villager_spell_book',
    'irons_spellbooks:evoker_spell_book',
    'irons_spellbooks:blaze_spell_book',
    'irons_spellbooks:druidic_spell_book',
    'irons_spellbooks:ice_spell_book',
    'irons_spellbooks:cursed_doll_spell_book',
    'irons_spellbooks:necronomicon_spell_book',
    'firesenderexpansion:endchiridion',
    'irons_spellbooks:dragonskin_spell_book',
    'enigmatic_arcana:antonomos',
    'irons_spellbooks:netherite_spell_book',
    'darkermagic:volume_of_the_deep',
    'allthewizardgear:allthemodium_spell_book',
    'cataclysm_spellbooks:abyss_spell_book',
    'cataclysm_spellbooks:ignis_spell_book',
    'cataclysm_spellbooks:codex_of_malice_spell_book',
    'cataclysm_spellbooks:desert_spell_book',
    'allthewizardgear:vibranium_spell_book',
    'allthewizardgear:unobtainium_spell_book'
]

results = {}

jars = glob.glob('minecraft/mods/*.jar')
for jar in jars:
    try:
        with zipfile.ZipFile(jar, 'r') as z:
            for file in z.namelist():
                if file.startswith('data/') and '/recipes/' in file and file.endswith('.json'):
                    data = json.loads(z.read(file))
                    
                    if 'result' in data:
                        res = data['result']
                        res_id = res.get('id', res.get('item', '')) if isinstance(res, dict) else res
                        
                        if res_id in books_to_check:
                            if res_id not in results:
                                results[res_id] = []
                            results[res_id].append({'file': f'{os.path.basename(jar)} -> {file}', 'recipe': data})
    except Exception as e:
        pass

for k, v in results.items():
    print(f'Found recipes for {k}:')
    for r in v:
        print(f"  Source: {r['file']}")
        print(f"  Type: {r['recipe'].get('type', 'Unknown')}")
