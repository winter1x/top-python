# ?search=python
"""
https://api.github.com/data?type=student&id=123
параметры:
type=student
id=123

200 - успешно
301 запрашиваемый ресурс перенесен на другой адрес
404 не найдена
500 внутренняя ошибка сервера
"""
import requests

"""response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)

payload = {"q": 'python', 'sort': 'stars'}
response = requests.get(url="https://api.github.com/search/repositories", params=payload)
print(response.url)"""
#print(response.text)

"""headers = {'User-Agent': 'my-app/0.0.1'}
response = requests.get("https://api.github.com", headers=headers)
print(response.request.headers)"""

"""try:
    response = requests.get("https://api.github.com", timeout=5)
    response.raise_for_status()
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP ошибка {http_err}")
except requests.exceptions.ConnectionError:
    print("ошибка соединения")
except requests.exceptions.Timeout:
    print("время ожидания истекло")
except requests.exceptions.RequestException as err:
    print(f"другая ошибка {err}")
"""
"""
https://httpbin.org/
"""
response = requests.get("https://httpbin.org/get", params={'course': "networking"})
print(response.json())

#import requests

"""
requests.get(url, params=None, **kwargs)

объект ответа = экземпляр Response

response.status_code

response.text

response.content - данные в байтовом формате
with open('image.jpg', 'wb') as f:
    f.write(response.content)
    
response.json()
data = response.json()
print(data['name']

response.headers - заголовки ответа
print(response.headers)
словарь 
    print(response.headers["Content-Type"]) тип содержимого
    #print(response.headers["User-agent"]) информация о клиентском приложении
    #print(response.headers["Authorization"]) данные для авторизации
    Accept - что мы хотим получить
    Date дата ответа
    Server информация о сервере

response.url - фактический url
print(response.url)

response.cookies


методы управления ошибками
response.raise_for_status() - проверяет код ответа и вызывает исключение HTTPError (если 400 500)
try:
    response = requests.get("https://api.github.com")
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"Ошибка HTTP: {err}")


requests.get(url, params=None, **kwargs)
headers
timeout
auth
proxies
verify 
"""

"""
1
https://api.github.com
вывести код ответа, факт юрл, заголовки, тело

2
https://httpbin.org/
передать ваше имя, course=networking task=get_request
вывести факт юрл

3
https://api.github.com/users/tsenturion
вывести логин login, ссылку на профиль html_url, количество репозиториев public_repos

4
https://httpbin.org/headers
передать юзерагент любой
вывести тело

5
https://api.github.com/dfbdpfmds
обработка ошибок, таймаут

"""