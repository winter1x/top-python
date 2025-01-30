import json

with open('ingredients.json', 'r', encoding='utf-8') as f1, \
        open('ingredients2.json', 'r', encoding='utf-8') as f2, \
        open('ingredients3.json', 'r', encoding='utf-8') as f3:
    ingredients1 = json.load(f1)
    ingredients2 = json.load(f2)
    ingredients3 = json.load(f3)

with open('question.json', 'r', encoding='utf-8') as fq:
    question_data = json.load(fq)

excluded_names = set(question_data.keys())

all_ingredients = ingredients1 + ingredients2 + ingredients3

filtered_ingredients = [
    ingredient for ingredient in all_ingredients
    if len(ingredient['effects']) == 4 and ingredient['name'] not in excluded_names
]

unique_ingredients = []
seen = {}

for ingredient in filtered_ingredients:
    key = (ingredient['name'], frozenset(ingredient['effects']))
    if key[0] not in seen:
        seen[key[0]] = key[1]
        unique_ingredients.append(ingredient)
    elif seen[key[0]] != key[1]:
        unique_ingredients.append(ingredient)

with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(unique_ingredients, outfile, ensure_ascii=False, indent=4)


