"""

"""
"""
pickle - объекты
json - 
marshal
csv (pandas для работы)
yaml, protobuf, msgpack
"""

"""
.dump
.dumps - байты
"""
import pickle
data = {'name': 'John', 'age': 30, 'skills': ['python', 'java', 'c++']}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

nums = [1, 2, 3, 4, 5]
with open('numbers.pkl', 'wb') as file:
    pickle.dump(nums, file)



"""
.dump
.dumps - строку
ensure_ascii= - позволяет сохранять кириллицу
indent= - форматирует json (отступы)
"""
import json

data = {'name': 'John', 'age': 30, 'skills': ['python', 'java', 'c++']}

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

"""
{
    "name": "John",
    "age": 30,
    "skills": [
        "python",
        "java",
        "c++"
    ]
}
"""

users = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
]
with open('users.json', 'w', encoding='utf-8') as file:
    json.dump(users, file, ensure_ascii=False, indent=4)


data = {'key1': 'value1'}
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)

data = {"x": 1, "y": 2}
binary_data = pickle.dumps(data)
print(binary_data)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)
with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)