from json import *
test_data_learn = {
    "name": 'alice',
    "age": '23',
}
"""
dumps - сериализация dict в .json
dump - сериализация dict в .json и запись в файл
loads - десериализация .json в dict
load - десериализация .json из файла в dict
"""
json_data = dumps(test_data_learn, indent=4, sort_keys=True, ensure_ascii=False)
print(json_data)