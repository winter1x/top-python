"""
proxy
суррогат или заместитель

структура:
subject - общий интерфейс
realSubject - реальный объект
proxy - заместитель

+
не нарушает принцип открытости/закрытости
расширяемость
ленивая инициализация

-
новый уровень косвенности
может запутать, если сильно отличается
нужно соблюдать интерфейс

decorator
"""

class Image:
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"[Image] загрузка {self.filename}")

    def display(self):
        print(f"[Image] отображение {self.filename}")

class ImageProxy:
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = Image(self.filename)
        self._real_image.display()

img = ImageProxy("1.jpg")
print('объект создан без загрузки')
img.display()

class Document:
    def delete(self):
        print('док удален')

class SecureDocumentProxy:
    def __init__(self, real_doc, user_role):
        self._real_doc = real_doc
        self._user_role = user_role

    def delete(self):
        if self._user_role != 'admin':
            print('запрещено')
        else:
            self._real_doc.delete()


doc = Document()
proxy = SecureDocumentProxy(doc, 'guest')
proxy.delete()

"""
клиент обращается к бд через прокси
прокси проверяет авторизован ли, далее к реальному объекту

DataServer
SecureProxy
Client
"""

class DataServerInterface:
    def get_data(self):
        pass

class DataServer(DataServerInterface):
    def get_data(self):
        print('секретные данные получены')

class SecureProxy(DataServerInterface):
    _USERS = {
        'admin': 'admin',
        'editor': 'editor',
    }

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._real_server = None

    def _authenticate(self):
        return self._USERS.get(self._username) == self._password

    def get_data(self):
        if not self._authenticate():
            return 'нет доступа'
        if self._real_server is None:
            self._real_server = DataServer()
        return self._real_server.get_data()

proxy1 = SecureProxy('admin', 'admin')
print(proxy1.get_data())

proxy2 = SecureProxy('guest', 'guest')
print(proxy2.get_data())

proxy3 = SecureProxy('editor', 'editor2')
print(proxy3.get_data())

"""
прокси-доступ к дорогим операциям - генерация отчетов
RealReport - долгая инициализация/дорогой
    display()

ReportProxy реализует тот же интерфейс, создает настоящий отчет только при первом вызове display()

Report - интерфейс
    display()
"""