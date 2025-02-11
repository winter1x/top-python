import json

with open("effects.json", "r", encoding="utf-8") as file:
    data = json.load(file)

data.sort(key=lambda x: x["effect"])
for item in data:
    item["ingredients"].sort()

with open("effects.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Данные успешно отсортированы и сохранены в effects.json")
