import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def remove_ingredients(data, ingredients_to_remove):
    return [item for item in data if item['name'] not in ingredients_to_remove]

ingredients_to_remove = {
    "Измельченная соль пустоты",
    "Корень жарницы",
    "Морозная соль Фаренгара",
    "Прах Берита"
}

file1 = 'ingredients.json'
file2 = 'ingredients2.json'

data1 = load_json(file1)
data2 = load_json(file2)

filtered_data1 = remove_ingredients(data1, ingredients_to_remove)
filtered_data2 = remove_ingredients(data2, ingredients_to_remove)

save_json(file1, filtered_data1)
save_json(file2, filtered_data2)


found_in_file1 = [item['name'] for item in data1 if item['name'] in ingredients_to_remove]
found_in_file2 = [item['name'] for item in data2 if item['name'] in ingredients_to_remove]

print("Удаленные ингредиенты из", file1, ":", set(found_in_file1))
print("Удаленные ингредиенты из", file2, ":", set(found_in_file2))