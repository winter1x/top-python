import json
import re


def clean_text(text):
    return re.sub(r'[\u200e\u200f\u200b\u200c\u200d]', '', text)


with open('data.txt', 'r', encoding='utf-16') as file:
    data = []

    for line in file:
        cleaned_line = clean_text(line.strip())

        parts = cleaned_line.split('\t')

        ingredient = {
            "name": parts[0],
            "effects": parts[1:]
        }

        data.append(ingredient)

with open('ingredients.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Файл успешно преобразован в JSON.")