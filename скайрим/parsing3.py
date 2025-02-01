import json


def process_file_to_json(effects_file, input_file, output_file, additional_effects_file):
    with open(effects_file, encoding='utf-8') as ef:
        all_effects = {effect.strip() for item in json.load(ef) for effect in item['effects']}

    with open(additional_effects_file, encoding='utf-8') as additional_ef:
        additional_effects = {effect.strip() for item in json.load(additional_ef) for effect in item['effects']}

    all_effects.update(additional_effects)

    tags_to_remove = {"CC", "DB", "HF", "DG"}
    data, lines = [], open(input_file, encoding='utf-16').read().splitlines()

    for effect in all_effects:
        for i, line in enumerate(lines):
            if line == effect:
                ingredients = []
                for j in range(i + 3, len(lines)):
                    if not lines[j].strip(): break
                    ingredient = lines[j].strip()
                    for tag in tags_to_remove:
                        ingredient = ingredient.replace(tag, "").strip()
                    if ingredient:
                        ingredients.append(ingredient)

                for ingredient in ingredients:
                    existing = next((item for item in data if item['name'] == ingredient), None)
                    if existing:
                        existing['effects'].append(effect)
                    else:
                        data.append({"name": ingredient, "effects": [effect]})

    for item in data:
        item['effects'] = sorted(set(item['effects']))

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

process_file_to_json('ingredients.json', 'Книга3.txt', 'ingredients2.json', 'ingredients3.json')