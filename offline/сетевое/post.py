"""
для отправки/передачи данных на сервер

данные передаются в теле запроса (request body), а не в url
обычно изменяет состояние сервера
не кэшируется
не должен быть повторен автоматически
безопаснее
не идемпотентный
сопровождаются заголовком Content-Type
    Content-Type: application/x-www-form-urlencoded
    Content-Type: application/json
    Content-Type: multipart/form-data
авторизация
    Basic Auth
    Token Auth (Bearer) - Authorization - токен авторизации
CSRF (Cross-Site Request Forgery)
User-Agent - описание клиента


используется когда:
    - нужно передать данные на сервер
    - нужно обновить состояние сервера
    - создать новый объект
    - отправить данные формы
    - загрузить файл
    - отправить json-данные 

request body:
    - json
    - ключи/значения
    - бинарные данные
    - потоковые данные 




получить
GET /notes

создать
POST /notes
Body:
    {
        "title": "Buy milk",
        "completed": false
    }

обновить
PUT /notes/1
Body:
    {
        "title": "Buy milk",
        "completed": true
    }

удалить
DELETE /notes/1


<form action="/submit" method="post">
    <input name="username">
    <input name="password" type="password">
    <button type="submit">Submit</button>
</form>

POST /login - получаем
POST /data - отправляем
POST /logout - аннулируем
"""

import requests

"""
url = 'https://httpbin.org/post'
data = {
    'username': "alice", 
    'password': 'secret'
}

# username=alice&password=secret - application/x-www-form-urlencoded
response = requests.post(url, data=data)
print(response.status_code)
print(response.text)

json_data = {'username': "alice", 'password': 'secret'}

response = requests.post(url, json=json_data)
print(response.json())
#application/json

data = {'key': 'value'}
headers = {'Content-Type': 'application/json', 'Authorization': 'token'}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
try:
    response = requests.post(url, json=data, timeout=5)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(e)"""
"""url = 'https://httpbin.org/post'
files = {'file': open('example.txt', 'rb')}
#multipart/form-data
response = requests.post(url, files=files)
print(response.text)"""
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import requests

session = requests.Session()

retries = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[500, 502, 503, 504]
)

adapter = HTTPAdapter(max_retries=retries)
session.mount("http://", adapter)
session.mount("https://", adapter)

response = session.post("https://httpbin.org/status/500", data={}, timeout=3)
print(response.status_code)


from requests.auth import HTTPBasicAuth

url = "https://httpbin.org/basic-auth/user/pass"
r = requests.post(url, auth=HTTPBasicAuth('user', 'pass'))

print(r.status_code)
print(r.text)


r = requests.post('https://example.com/api/token', json={'username': 'admin', 'password': '123456'})
token = r.json().get('token')

headers = {
    "Authorization": token
}

r = requests.post("https://httpbin.org/post", headers=headers, data={"a": 1, "b": 2})
print(r.text)


auth_data = {'username': 'admin', 'password': 'admin'}
r = requests.post('https://httpbin.org/post', json=auth_data)

token = 'my_example_token'

headers = {
    'Authorization': 'Bearer ' + token
}
data = {"text": "Hello, world!"}
r2 = requests.post('https://httpbin.org/post', headers=headers, json=data)

print(r2.status_code)
print(r2.text)
"""
payload = {"q": 'python', 'sort': 'stars'}
response = requests.get(url="https://api.github.com/search/repositories", params=payload)
"""
"""
rest - архитектура, опирается на http методы
get
post
put - полностью обновить объект
patch - частично обновить
delete -удалить

пример
POST /api/users HTTP/1.1
Host example.com
Content-Type: application/json

{
    'name': 'ivan',
    'email': 'ivan@example.com'
}
"""
"""url = 'https://example.com/api/users'
user = {
    'name': 'ivan',
    'email': 'ivan@example.com'
}

response = requests.post(url, json=user)
print(response.status_code)"""
#201 Created
#200 OK
#400 Bad Request
#401 Unauthorized/403 Forbidden нет доступа
#500 Internal Server Error


"""
data= (посмотреть form headers )
json= (Content-Type)
передача заголовков
с обработкой ответа от сервера 
https://reqres.in
"""

url = 'https://httpbin.org/post'
data = {
    'username': "alice",
    'password': 'secret'
}

"""resposne = requests.post(url, data=data)

print(resposne.status_code)
print(resposne.json())"""

user = {
    'username': 'alice123',
    'email': 'alice@example.com',
    'is_active': True
}

"""resposne = requests.post(url, json=user)
print(resposne.status_code)
print(resposne.json()['json'])
print(resposne.json())"""

payload = {'task': 'POST headers'}
headers = {
    'Authorization': '12345',
    'Custom-Header': 'CustomValue'
}

"""response = requests.post(url, json=payload, headers=headers)

print(response.json()['headers'])"""

"""url = 'https://reqres.in/api/register'
data = {
    'email': 'evo.holt@reqres.in',
    'password': 'pistol'
}
headers = {
    'x-api-key': 'reqres-free-v1'
}
response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response.json())
"""
"""
.post()
data= - отправка формы
data = {
    'email': 'evo.holt@reqres.in',
    'password': 'pistol'
}
resposne = requests.post(url, data=data)

json=
json_data = {'username': "alice", 'password': 'secret'}
response = requests.post(url, json=data)

headers= - кастомные заголовки
Authorization - токен авторизации
User-Agent - описание клиента
Content-Type - тип тела запроса
headers = {
    'x-api-key': 'reqres-free-v1'
}
response = requests.post(url, json=data, headers=headers)

files=
files = {'file': open('example.txt', 'rb')}
response = requests.post(url, files=files)
multipart/form-data

params= - если нужен url с параметрами
timeout= - защита от зависания
response.status_code 
response.json()
response.text
try:
    response.raise_for_status()
except

idempotency 
"""