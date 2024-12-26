
dict1 = {'name': 'alice', 'city': 'new york'}
set1 = set()
dict1 = dict(name='bob', age=30)
zero_dict = {}
zero_dict['age'] = 30
zero_dict['name'] = 'bob'
print(zero_dict['name'])
print(zero_dict.get('name', 'age'))
zero_dict['age'] = 31
del zero_dict['name']
print(zero_dict)
for key, value in zero_dict.items():
    print(f'{key}: {value}')
"""
keys() - список ключей
values() - значений
items() - пары
get(key, default) возвр значение по ключу и default если ключ отсутствует
pop(key, default) удаление и возвр значения
popitem() удаляет и возвр последнюю добавл пару
clear()
copy()

"""

a = {
    "name": "alice",
    "age": 243,
    'address': {
        "city": "new york",
        "zip": '10101'
    }
}
