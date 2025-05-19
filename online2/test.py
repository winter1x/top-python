"""
данные о человеке имя возраст
user.pkl

список чисел 
кортеж строк
.dumps - байты
print()

+json
user.json
"""

import pickle
user = {
    "name": "Alex",
    "age": 20,
    'skills': ['python', 'js']
    'active': True
}
with open("user.pkl", "wb") as f:
    pickle.dump(user, f)

numbers = [1, 2, 3, 4]
with open("numbers.pkl", "wb") as f:
    pickle.dump(numbers, f)

fruits = ("apple", "banana", "cherry")
with open("fruits.pkl", "wb") as f:
    pickle.dump(fruits, f)

binary_data = pickle.dumps(user)
print("сериализованные байты user: ", binary_data)

import json

with open("user.json", "w", encoding='utf-8') as f:
    json.dump(user, f, ensure_ascii=False, indent=4)

with open("numbers.json", "w", encoding='utf-8') as f:
    json.dump(numbers, f, ensure_ascii=False, indent=4)

with open("fruits.json", "w", encoding='utf-8') as f:
    json.dump(fruits, f, ensure_ascii=False, indent=4)

data = json.dumps(user, ensure_ascii=False, indent=4)
print("json строка для кортежа:", data)

