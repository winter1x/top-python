"""
patch - частичное обновление ресурса

{
    'name': 'anna',
    'email': 'anna@gmail.com',
    'age': 25
}

{
    'age': 26
}

PATCH /tasks/42
{
    'done': true
}

PATCH /account
{
    'balance': "+100"
}

+json
+data
+заголовки
+сессии
+cookies
+обработка ошибок
+таймауты
+повторные попытки
"""

import requests

url = 'https://httpbin.org/patch'
data = {"email": "anna@gmail.com",}

response = requests.patch(url, json=data)

print(response.status_code)
print(response.text)

