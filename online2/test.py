"""
словарь с данными пользователя
список чисел
кортеж строк

сохранить в один .pkl
в .json

считать .pkl (load) + print
считать .json (load) + print

pickle.dumps() + pickle.loads()
json.dumps() + json.loads()
"""
import pickle
import json

user = {
    "name": "Иван",
    "age": 25,
    "city": "Москва"
}
numbers = [1, 2, 3, 4, 5]
strings = ("Hello", "World", "Python")

with open("data.pkl", "wb") as file:
    pickle.dump((user, numbers, strings), file)

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(
        {
            "user": user,
            "numbers": numbers,
            "strings": strings
        }, 
        file,
        ensure_ascii=False,
        indent=4
    )

with open("data.pkl", "rb") as file:
    loaded_user, loaded_numbers, loaded_strings = pickle.load(file)

print(loaded_user)
print(loaded_numbers)
print(loaded_strings)

with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print(loaded_data["user"])
print(loaded_data["numbers"])
print(loaded_data["strings"])

pickle_bytes = pickle.dumps(user)
user_from_bytes = pickle.loads(pickle_bytes)
print(user_from_bytes)

json_str = json.dumps(user, ensure_ascii=False)
user_from_json = json.loads(json_str)
print(user_from_json)