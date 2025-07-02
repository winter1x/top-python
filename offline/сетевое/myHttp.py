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
404 не найдена
500 внутренняя ошибка сервера

get methods
.headers - заголовки ответа
.text - текст ответа
.url - фактический юрл (вдруг был редирект)
.encoding - кодировка
.elapsed - время выполнения запроса
.json - преобразовать в json
.content - бинарные данные
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