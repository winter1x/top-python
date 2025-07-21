"""
put - обновление данных
создать или заменить ресурс на сервере
идемпотентен

post на /users - создание пользователя
put на /users/{id} - обновление пользователя

когда используем put
    - обновление существующего объекта
    - создание нового объекта по конкретному адресу
    - сохранение состояния

особенности
    - требуется точное указание ресурса
    - полное обновление

учесть/не забываем
    - передаем полный объект
    - статус коды
    - учитываем особенности автоматизации (put может перезаписать)
    - лучше вместе с https

для передачи данных
    - json
    - data

+headers
+cookies
+сессии
+timeout
+retries (urllib3 / requests.adapters.HTTPAdapter)
+обработка ошибок (try / except)
"""

import requests
url = 'https://httpbin.org/put'
#url = 'https://site.com/api/users/5
data = {'name': 'John Doe', 'age': 25}

response = requests.put(url, json=data)
print(response.status_code)
print(response.text)


url = 'https://example.com/api/tasks/101'
data = {
    'title': 'Finish homework',
    'status': 'in_progress',
    'priority': 'high',
}

response = requests.put(url, json=data)

headers = {
    "Authorization": "Bearer 1234567890",
    "Content-Type": "application/json",
}

requests.put(url, json=data, headers=headers)

try:
    response = requests.put(url, json=data, timeout=5)
except requests.exceptions.Timeout:
    print("Request timed out")