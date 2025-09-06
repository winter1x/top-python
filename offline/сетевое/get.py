"""
get
все параметры передаются в url (query string, не безопасно)
кэшируется браузером и прокси



не изменяют данные на сервере (индемпотентность - не влияет на состояние сервера)
вся информация передается в url

кэшируемость
идемпонентность

<2000 - символов
не безопасно (не безопасно для передачи паролей)
безопасность (не меняет данные на сервере)
"""
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

пример сырого запроса
GET /products?sort=price&order=asc HTTP/1.1
Host: api.example.com
User-Agent: curl/7.64.1
Accept: text/html

пример ответа
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 123

<html></html>


/api/products

<button id="load-products">Загрузить товары</button>
<script>
    document.getElementById('load-products').addEventListener('click', () => {
        fetch('/api/products')
            .then(response => response.json())
            .then(data => {
                console.log(data);
            });
    });
</script>
"""

import requests

url = "https://api.example.com/products"
params = {'sort': 'price', 'order': 'asc'}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.RequestException as err:
    print(f"ошибка {err}")
"""
params = {
    'course': 'networking',
    'task': 'get_request'
}

response = requests.get("https://api.example.com/products", params=params)

if response.status_code == 200:
    products = response.json()
    print('получены задания', products)"""


"""response = requests.get('https://example.com/search?q=python')
print(response.text)"""

"""response = requests.get('https://api.agify.io/?name=alex')
data = response.json()
print(data)"""

"""params = {
    'name': 'anna',
    'county_id': "US"
}

response = requests.get('https://api.agify.io/', params=params) #?name=anna&county_id=US
data = response.json()
print(data)"""

"""response = requests.get('https://example.com/search?q=python')

if response.status_code == 200:
    print('все хорошо')
else:
    print(f"ошибка {response.status_code}")

try:
    response = requests.get('https://example.com/search?q=python')
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"http ошибка {err}")"""

"""response = requests.get('https://example.com/image.jpg')

with open('image.jpg', 'wb') as f:
    f.write(response.content)"""

"""
response = requests.get("https://api.github.com/users")
print(response.status_code)
print(response.headers)
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
"""response = requests.get("https://httpbin.org/get", params={'course': "networking"})
print(response.json())
"""
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
"""
"""try:
    response = requests.get("https://api.github.com")
    print(response.status_code)
    print(response.url)
    print(response.headers)
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"произошла ошибка при выполнении запроса{e}")"""
"""
2
https://httpbin.org/
передать ваше имя, course=networking task=get_request
вывести факт юрл
"""
"""try:
    params = {
        'name': "Name",
        'course': 'networking',
        'task': 'get_request'
    }
    response = requests.get("https://httpbin.org/get", params=params)
    print(response.url)

except requests.exceptions.RequestException as e:
    print(f"произошла ошибка при передаче параметров{e}")"""
"""
3
https://api.github.com/users/tsenturion
вывести логин login, ссылку на профиль html_url, количество репозиториев public_repos
"""
"""try:
    response = requests.get("https://api.github.com/users/tsenturion")
    response.raise_for_status()
    data = response.json()
    print(data.get("login"))
    print(data.get("html_url"))
    print(data.get('public_repos'))

except requests.exceptions.RequestException as e:
    print(f"произошла ошибка при получении данных пользователя{e}")
except ValueError:
    print('ошибка преобразования ответа в json')"""
"""
4
https://httpbin.org/headers
передать юзерагент любой
вывести тело
"""
"""try:
    headers = {
        'User-Agent': "my-app/0.0.1"
    }
    response = requests.get("https://httpbin.org/headers", headers=headers)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"произошла ошибка при отправке заголовков{e}")"""
"""
https://api.github.com/dfbdpfmds
обработка ошибок, таймаут
"""
"""try:
    response = requests.get("https://api.github.com/dfbdpfmds", timeout=5)
    response.raise_for_status()
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP ошибка {http_err}")
except requests.exceptions.ConnectionError:
    print("ошибка соединения")
except requests.exceptions.Timeout:
    print("время ожидания истекло")
except requests.exceptions.RequestException as err:
    print(f"другая ошибка {err}")"""

#except requests.exceptions.ConnectionError: - не может установить соединение с сервером

#except requests.exceptions.Timeout: - запрос слишком долго ждет ответа от сервера

#    response.raise_for_status()
#except requests.exceptions.HTTPError as http_err: - неудачный код ответа от сервера

#TooManyRedirects - слишком много перенаправлений

#except requests.exceptions.RequestException as err: - поймать любую ошибку

"""
редирект перенаправление 300-399
301
302
303
307
308

сервер сообщает новый URL в заголовке Location
response.history - список всех промежуточных ответов

allow_redirects - переходить ли по новому адресу
"""

"""response = requests.get("http://github.com", allow_redirects=False)
print(response.url)
print(response.headers["Location"])
print(response.status_code)

print("история редиректов")
for resp in response.history:
    print(resp.status_code, resp.url)
"""

"""response = requests.get("http://github.com", allow_redirects=False)

if response.status_code in (301, 302, 303, 307, 308):
    new_url = response.headers['Location']
    print(f"перенаправляемся на {new_url}")
    new_response = requests.get(new_url)
    print(new_response.status_code)"""

#TooManyRedirects - слишком много перенаправлений (более 30)

"""from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = Session()
retries = Retry(total=5, redirect=5)
adapter = HTTPAdapter(max_retries=retries)
session.mount('http://', adapter)
session.mount("https://", adapter)

response = session.get("http://github.com")
print(response.url)"""
"""try:
    response = requests.get("зацикленный юрл")
except requests.exceptions.TooManyRedirects:
    print("слишком много перенаправлений")"""


"""
1
http://github.com
показать финальный url
список промежуточных переходов (статус и юрл)

2
http://github.com
с отключением автоматических 
получить статус и заголовок Location
показать адрес куда сервер предлагает перейти

3
добавить для 2 
вручную новый запрос на этот адрес
вывести финальный статус и юрл

4
https://httpbin.org/redirect/100
отправить запрос
перехватить ошибку
сообщение об ошибке

5
count_redirects(url: str) -> int
запрос к юрл
возвращает колво промежуточных редиректов
обработка искл
если ошибка return -1
"""
def count_redirects(url: str) -> int:
    try:
        response = requests.get(url, timeout=5)
        return len(response.history)
    except requests.exceptions.RequestException as e:
        print(f"ошибка запроса {e}")
        return -1


"""
указываем url
отправляем запрос
получаем ответ
"""

response = requests.get("https://httpbin.org/get")
print(response.text)

"""
параметры 
query string
начинается со знака ?
далее "ключ=значение", разделенные &
https://example.com/search?query=python&page=2
/search - ресурс
два параметра
    q=python - строка поиска
    page=2 - номер страницы

параметры с несколькими значениями
tags=python&tags=backend&tags=go

параметры с пробелами(%20 или +) и спецсимволами
"learn python now!"

пустые значения и логика по умолчания
params = {"debug": ""}

динамическая генерация параметров

слияние параметров и ручная сборка URL - ПЛОХО, ТАК НЕ ДЕЛАЕМ 
url = f"https://httpbin.org/get?q={query}&page={page}" - не безопасно
правильно - params

проверка отправленых параметров
response.url
response.json()['args']

сочетается и используется вместе с другими возможностями (headers, cookies, session)

расширенные параметры (вложенные словари/структуры)


параметры и кэширование
https://example.com/api/items?page=1
https://example.com/api/items?page=2
"""

params = {'q', 'python', 'page': 2}
response = requests.get("https://httpbin.org/get", params=params)
#https://httpbin.org/get?q=python&page=2
print(response.url)

"""
параметры с несколькими значениями
tags=python&tags=backend&tags=go
"""

params = {'tags': ['python', 'backend', 'go']}
response = requests.get("https://httpbin.org/get", params=params)
print(response.url)
#https://httpbin.org/get?tags=python&tags=backend&tags=go

"""
параметры с пробелами(%20 или +) и спецсимволами
"learn python now!"
https://httpbin.org/get?q=learn+python+now%21
"""

params = {'q': 'learn python now!'}
response = requests.get("https://httpbin.org/get", params=params)
print(response.url)
#https://httpbin.org/get?q=learn+python+now%21

"""
пустые значения и логика по умолчания
params = {"debug": ""}
"""

params = {'debug': ''}
response = requests.get("https://httpbin.org/get", params=params)
print(response.url)
#https://httpbin.org/get?debug=

"""
динамическая генерация параметров
"""

def search_books(title: str, page=1, limit=10):
    params = {'title': title, 'page': page, 'limit': limit}
    response = requests.get("https://httpbin.org/get", params=params)
    return response.json()

result = search_books("python", page=2)
print(result['args'])
#{'limit': '10', 'page': '2', 'title': 'python'}

"""
расширенные параметры (вложенные словари/структуры)
"""

params = {
    'filter[category]': 'python',
    'filter[theme][title]': 'advanced'
}

#https://httpbin.org/get?filter%5Bcategory%5D=python&filter%5Btheme%5D%5Btitle%5D=advanced
response = requests.get("https://httpbin.org/get", params=params)
if response.status_code == 200:


# работа с заголовками
"""
http заголовки - метаинформация 
.get
.post
.put

ключи=заголовки значения=содержимое

User-Agent - кто мы такие
Accept - что мы хотим получить
    application/json
    text/html
    application/xml
Authorization - авторизация (токены, пароли и тд)
Content-Type - тип контента (актуален для POST и PUT и PATCH)
    application/json
    text/html
    application/xml
    application/octet-stream - файл (возможно)

при работе с Session
s.headers.update({"User-Agent": "my-app/0.0.1"})
s.headers.pop("User-Agent")

шаблонный словарь заголовков
"""
headers = {
    "User-Agent": "my-app/0.0.1", #кто мы такие
    "Accept": "application/json", #что мы хотим получить
}

response = requests.get("https://httpbin.org/get", headers=headers)
print(response.json())
#{'args': {}, 'headers': {'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'my-app/0.0.1', 'X-Amzn-Trace-Id': 'Root=1-687530c5-546131611cbb4adb2f2a599b'}, 'origin': '45.144.54.184', 'url': 'https://httpbin.org/get'}

s = requests.Session()
r = s.get("https://httpbin.org/headers")
print(r.json())
#{'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-6875333d-651ee5bc002a23fe3b5e6b04'}}

"""
шаблонный словарь заголовков
"""

DEFAULT_HEADERS = {
    "User-Agent": "my-app/0.0.1", #кто мы такие
    "Accept": "application/json", #что мы хотим получить
}

def get_data(url, token=None):
    headers = DEFAULT_HEADERS.copy()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return response.get(url, headers=headers)

#обработка ответа
"""
удался ли запрос
200 или .raise_for_status() - завершился ли запрос с ошибкой? 4xx 5xx
.json - преобразовать в json

следуем редиректам
301 запрашиваемый ресурс перенесен на другой адрес
302 тоже редирект
можно отключить
allow_redirects=False
"""
if response.status_code == 200:
    print('ok')
else:
    print('error', response.status_code)

try:
    data = response.json()
except ValueError:
    print('error json')

data = response.json()
if not data.get('results'):
    print('нет результатов')

for r in reponse.history:
    print(r.status_code, r.url)

response = requests.get("https://httpbin.org/get")
print("status code:", response.status_code)
print("text:", response.text[:100])
print('headers:', response.headers)

url = "https://httpbin.org/get"
params = {'q': 'python', 'page': 1}
headers = {
    'Accept': 'application/json',
    "User-Agent": "my-app/0.0.1",
}

try:
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(data['args'])
except requests.RequestException as e:
    print('ошибка', e)
except ValueError:
    print('ошибка json')

# обработка ошибок
"""
сервер не отвечает
неверный url
истек тайамут
ошибка соединения
4xx 5xx
ошибка в ответе

.raise_for_status() чтобы ловить 404 или 500 например


requests.exceptions.RequestException - родитель
ConnectionError - ошибка соединения - сервер не существует/неправильный домент/нет интернета

Timeout - истек таймаут при timeout=
HTTPError - ошибка http при .raise_for_status()
TooManyRedirects - слишком много редиректов - если больше 30 редиректов

    логирование
    print() с ошибкой
    print() с кодом ответа
    print() с url
    print() с телом ответа
"""
try:
    response = requests.get("https://httpbin.org/status/404", timeout=5)
    response.raise_for_status()
    response = requests.get("https://this-domain-does-not-exist.com", timeout=5)
except requests.exceptions.HTTPError as http_err:
    print(f"ошибка HTTP {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"ошибка соединения {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"таймаут {timeout_err}")
except requests.exceptions.RequestException as err:
    print(f"другая ошибка {err}")

# повторные попытки retry
import time

for i in range(3):
    try:
        response = requests.get("https://httpbin.org/status/500")
        response.raise_for_status()
        break
    except requests.exceptions.RequestException:
        print("попытка", i + 1, "неудачна")
        time.sleep(1)
else:
    print("все попытки неудачны")
#таймауты
"""
timeout=(3.0, 7.0)
connect_timeout=3.0 - сколько ждать подключения к серверу
read_timeout=7.0 - сколько ждать ответа от сервера
"""
try:
    response = requests.get("https://httpbin.org/delay/10", timeout=3)
except requests.exceptions.Timeout as err:
    print(f"сервер долго не отвечает {err}")

try:
    response = requests.get("https://httpbin.org/delay/10", timeout=(3.0, 7.0))
except requests.exceptions.Timeout as err:
    print(f"сервер долго не отвечает {err}")

# кеширование
import requests_cache
requests_cache.install_cache('my_cache', expire_after=60)  # кеширование в файл sqllite. 60 секунд
#                                       , expire_after=timedelta(hours=60)
#далее все вызовы будут кешироваться

requests_cache.install_cache(backend='memory') #кеширование только в памяти

requests_cache.clear() #очистить кеш
# rm my_cache.sqlite

with requests_cache.disabled():
    response = requests.get("https://httpbin.org/get")

response = requests.get(
    "https://httpbin.org/get",
    params={'a': 1},
    expire_after=30
)

from requests_cache import CachedSession

session = CachedSession('my_cache', expire_after=60)

response = session.get('https://httpbin.org/get')
print(response.from_cache)
# cookies
"""
response.cookies
<RequestsCookieJar[]>
get_dict() - чтобы получить словарь
requests.get(url, cookies=cookies) - передача вручную
requests.Session() - работа с сессией и cookies
pickle - хранение cookies между запусками
session.cookies.clear() - удаление cookies

заголовки 
print(response.request.headers.get('Cookie'))
print(response.headers.get('Set-Cookie'))
для установки и передачи cookies

session.cookies.update - для передачи несколько cookies
"""
response = requests.get("https://httpbin.org/cookies/set?theme=light&user=test")
response = requests.get("https://httpbin.org/cookies/") # не передает cookie потому что она не запомнилась
print(response.cookies)  # -> {}
print(response.cookies.get_dict())

url = "https://httpbin.org/cookies"
cookies = {'session_id': '1234567890', "user": "test"}
response = requests.get(url, cookies=cookies)
print(response.json())
print(response.cookies.get_dict())

cookies = {'session_id': '1234567890'}
response = requests.get('https://httpbin.org/cookies', cookies=cookies)
print(response.json())

session = requests.Session()
session.cookies.set("token", "1234567890")
response = session.get("https://httpbin.org/cookies")
print(response.json())

session = requests.Session()
session.get('https://httpbin.org/cookies/set/sessionid/1234567890')
response = session.get('https://httpbin.org/cookies')
print(response.json())  # -> {'sessionid': '1234567890'}

session.cookies.set('lang', 'ru', domain='httpbin.org', path='/cookies')

session.cookies.clear() # полная очистка
session.cookies.clear(domain='httpbin.org', path='/cookies', name='lang') 


print(response.request.headers.get('Cookie'))
print(response.headers.get('Set-Cookie'))


import pickle
session = requests.Session()
session.get('https://httpbin.org/cookies/set/sessionid/1234567890')

with open('cookies.pkl', 'wb') as f:
    pickle.dump(session.cookies, f)

with open('cookies.pkl', 'rb') as f:
    session.cookies.update(pickle.load(f))

response = session.get('https://httpbin.org/cookies')
print(response.json())

# Session
"""
хранить и переиспользовать cookies
автоматически передавать заголовки, параметры и другие настройки
сохранять соединение с сервером 
сессия сохранят информацию

session.close() - закрыть сессию

with requests.Session() as session:
    response = session.get('https://httpbin.org/get')
    print(response.json())
# сессия закрыта

сравнение           без session     с session
                        get - одинаковые
передача cookies    каждый раз      хранятся автоматически
общие заголовки     каждый раз      один раз задаются session.headers
авторизации/настро  сами            сессия запоминает
сохранение соединен|новое соединени|одно соединение повторно

в сессии не сохраняется
js

session.headers["User-Agent"] = None - ошибка
session.headers.update(...)          - верно


используем один объект session
"""
s = requests.Session()
s.headers.update({"User-Agent": "my-app/0.0.1"})

response1 = s.get("https://httpbin.org/headers")
response2 = s.get("https://httpbin.org/cookies/set?mycookie=value")
response3 = s.get("https://httpbin.org/cookies")

print(response3.json())


# session + headers
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
})

print(session.get('https://httpbin.org/headers', headers={'Accept': 'application/json'}).json())

session = requests.Session()
login_data = {
    'username': 'admin',
    'password': '1234567890',
}
session.post('https://httpbin.org/post', data=login_data)

response = session.get('https://httpbin.org/profile')
print(response.json())


session = requests.Session()
form_data = {"name": "John", "email": "john@example.com"}
session.post("https://httpbin.org/post", data=form_data)
response = session.get("https://httpbin.org/get")


session = requests.Session()
session.headers.update({"User-Agent": "my-app/0.0.1"})
session.get("https://httpbin.org/headers", headers={"User-Agent": "my-app/0.0.2"})
#стриминг
"""
stream=True - включает стриминг
тогда
response.content
response.text
response.json()
будут пустыми

работаем с
response.raw прямой доступ к сырым данным (в виде потока)
response.iter_lines() чтение потока по строкам
response.iter_content(chunk_size) чтение потока по байтам

response.close() - закрыть соединение
Content-Length: - заголовок с указанием размера файла

"""
response = requests.get("https://httpbin.org/stream/20", stream=True)
for line in response.iter_lines():
    print(line)

url = "https://nbg1-speed.hetzner.com/100MB.bin"

with requests.get(url, stream=True) as response:
    response.raise_for_status()
    # if response.status_code != 200:
    with open("100MB.bin", "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

print('done')

url = 'https://httpbin.org/stream/5'

response = requests.get(url, stream=True)
for line in response.iter_lines():
    if line:
        print(line.decode('utf-8'))

url = "https://nbg1-speed.hetzner.com/100MB.bin"

with requests.get(url, stream=True) as response:
    total_size = int(response.headers.get('content-length', 0))
    downloaded = 0

    with open("100MB.bin", "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
                downloaded += len(chunk)
                percent = downloaded * 100 / total_size
                print(f"Downloaded {downloaded} bytes ({percent:.2f}%)", end='\r')

print('done')

"""r = requests.get(url, stream=True)
try:
    ...
finally:
    r.close()"""

"""
1 часть
https://api.thecatapi.com/v1
получить случайное изображение кошки
    get https://api.thecatapi.com/v1/image/search
    статус код 
    полученные данные
    только ссылку на изображение из json ответа - список с одним словарем, внутри "url"

2 limit в параметках. 5 случайных изображений кошек, выводить только список ссылок
3 корректный код (timeout ошибки...)
"""
#import requests

url = "https://api.thecatapi.com/v1/images/search"
params = {"limit": 5}

try:
    response = requests.get(url, params=params, timeout=5)

    if response.status_code == 200:
        data = response.json()
        print("Ссылки на изображения:")
        for item in data:
            print(item["url"])
    else:
        print("Ошибка сервера. Код ответа:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Ошибка запроса:", e)



"""
with requests.Session() as session:
    создать сессию и установить cookie
    отпавить запрос и убедиться, что передается
    добавить заголовки в сессию

"""

#import requests

with requests.Session() as session:
    session.cookies.set("token", "1234567890")

    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    })

    cookies_response = session.get("https://httpbin.org/cookies")
    print(cookies_response.json())

    headers_response = session.get("https://httpbin.org/headers")
    print(headers_response.json()['headers'])