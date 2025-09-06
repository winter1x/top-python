"""
delete - удалять ресурс на сервере
действие, а не запрос на данные
идемпотентен

CRUD
create - post
read - get
update - put/patch
delete - delete

+статус коды
+сессии

DELETE /notes/52
DELETE /users/1
"""

import requests

response = requests.delete('https://httpbin.org/delete')

print(response.status_code)
print(response.text)