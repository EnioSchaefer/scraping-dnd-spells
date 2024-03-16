import json

with open('spells.json', 'r+', encoding='utf8') as json_file:
    loaded_dict = json.load(json_file)

    spell_list = loaded_dict.copy()

    for spell in spell_list:
        spell['description'] = spell['description'].replace('\n', '<br>')
        spell['at_higher_level'] = spell['at_higher_level'].replace('\n', '<br>')

    json_file.seek(0)
    json_file.truncate()
    json.dump(spell_list, json_file, indent=4)
