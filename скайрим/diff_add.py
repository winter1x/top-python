import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def compare_json_files(*files):
    data = {file: load_json(file) for file in files}
    dicts = {file: {item['name']: sorted(item['effects']) for item in items} for file, items in data.items()}

    all_keys = set(dicts[files[0]].keys()).union(*[d.keys() for d in dicts.values()])

    main_ingredients = set()
    unique_in_ingredients = set()
    effects_differences = {}

    for file in files:
        only_in_file = set(dicts[file].keys()) - set.union(*[set(dicts[f].keys()) for f in files if f != file])
        for name in only_in_file:
            effects = dicts[file][name]
            if len(effects) < 4:
                unique_in_ingredients.add(name)
            else:
                main_ingredients.add(name)

    for name in all_keys:
        effects = {file: dicts[file].get(name, []) for file in files}

        if all(len(effect) == 0 for effect in effects.values()):
            continue

        if all(set(effects[files[2]]) >= set(effects[file]) for file in [files[0], files[1]] if effects[file]):
            main_ingredients.add(name)
            continue

        non_empty_effects = {file: effect for file, effect in effects.items() if effect}
        if len(non_empty_effects) == len(files) - 1:
            effect_tuples = {file: tuple(effect) for file, effect in non_empty_effects.items()}
            if len(set(effect_tuples.values())) == 1:
                continue

        common_effects = set.intersection(*map(set, effects.values()))
        diffs = {file: set(effect) - common_effects for file, effect in effects.items()}

        if any(diffs[file] for file in files):
            effects_differences[name] = {file: list(diff) for file, diff in diffs.items() if diff}

    data_for_questions = {}
    for name in effects_differences:
        data_for_questions[name] = effects_differences[name]

    with open('question.json', 'w', encoding='utf-8') as f:
        json.dump(data_for_questions, f, ensure_ascii=False, indent=4)

file1 = 'ingredients.json'
file2 = 'ingredients2.json'
file3 = 'ingredients3.json'

compare_json_files(file1, file2, file3)
