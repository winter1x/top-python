"""
http hyper text transfer protocol
методы
    GET получение
    POST отправка
    PUT обновление
    DELETE

заголовки - метаданные информация о клиенте
тело - фактический контент
requests

status_code - код ответа
200 - успешно
301 запрашиваемый ресурс перенесен на другой адрес
302 тоже редирект
401 не авторизован
403 - доступ запрещен
404 не найдена
500 внутренняя ошибка сервера

get methods у объекта Response
.status_code - код ответа
.headers - заголовки ответа (CaseInsensitiveDict)
.text - текст ответа str
.url - фактический юрл (вдруг был редирект)
.encoding - кодировка
.elapsed - время выполнения запроса
.json - преобразовать в json
.content - бинарные данные bytes
.history - история редиректов
.from_cache - получен ли из кеша True/False
"""
import requests
response = requests.get("http://google.com/")
"""data = response.json()
print(data)"""
print(response.status_code)
print(response.headers["Content-Type"])
#print(response.headers["User-agent"]) #информация о клиентском приложении
#print(response.headers["Authorization"]) данные для авторизации
#print(response.text)
"""data = {'username': 'myusername', 'password': 'mypassword'}
response = requests.post("http://example.com/login", data=data)
print(response.text)

"""


import json
headers = {"Content-Type": "application/json"}
data = {'name': 'Jhon', 'age': 30}
response = requests.post('http://example.com/api', headers=headers, json=data)
print(response.text)

"""response = requests.get("https://api/openweathermap.org/data/2.5/weater?q=London&appid=")
data = response.json()
print(data)"""


#задание 1
"""
agify.io
запрашивает ввод имени
get http://api.agify.io?name=<вееденное имя>
получает json ответ
вывод
try except
обработка корректного ввода имени
"""
print('-' * 50)
#import requests

import requests  

name = input("Введите имя: ").strip()

if not name:
    print("Имя не должно быть пустым.")
    exit()


params = {
    'name': name  
}

try:
    response = requests.get('https://api.agify.io', params=params)

    if response.status_code != 200:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        exit()

    data = response.json()

    name_from_api = data.get('name', 'Неизвестно')
    age = data.get('age', '—')  
    count = data.get('count', 0)

    print(f"Имя: {name_from_api}, Предполагаемый возраст: {age}, Кол-во людей в выборке: {count}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при выполнении запроса: {e}")
