"""
singleton
один экземпляр класса

(+)
экономия ресурсов
централизованное управление
глобальный доступ
упрощение логики

(-)
нарушение srp
глобальное состояние
трудности тестирования
скрытые зависимости

factory method
builder
"""
print('#------------------------------------------------------------------------------')
class Singleton():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('создаем новый экземпляр класса Singleton')
            cls._instance = super().__new__(cls)
        else:
            print('возвращаем ранее созданный экземпляр класса Singleton')
        return cls._instance

obj1 = Singleton()
print(id(obj1))
obj2 = Singleton()
print(id(obj2))

print(obj1 is obj2)


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, "value"):
            self.value = value

obj1 = Singleton("первый")
obj2 = Singleton("второй")

print(obj1 is obj2) # True

print(obj1.value)
print(obj2.value)
print('#------------------------------------------------------------------------------')
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            print(f'создаем новый экземпляр класса {cls.__name__}')
            instances[cls] = cls(*args, **kwargs)
        else:
            print(f'возвращаем ранее созданный экземпляр класса {cls.__name__}')
        return instances[cls]
    return get_instance
"""
def singleton(cls):
    instances = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance
"""
@singleton
class Logger:
    def __init__(self):
        self.log = []

logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)
print(id(logger1))
print(id(logger2))

logger1.log.append("Первое сообщение")


print('#------------------------------------------------------------------------------')
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f'создаем новый экземпляр класса {cls.__name__} через метакласс')
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            print(f'возвращаем ранее созданный экземпляр класса {cls.__name__} (метакласс)')
        return cls._instances[cls]

"""
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
"""
class Configuration(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {}

conf1 = Configuration()
conf2 = Configuration()

print(conf1 is conf2)
print('#------------------------------------------------------------------------------')

"""
Система настроек приложения
class AppSettings:
    dict настройки
    set_param
    get_param
    get_instance - для получения экземпляра класса

settings1
settings2
указывают на один и тот же экземпляр класса - при создании через get_instance
"""

class AppSetting:
    _instance = None

    def __init__(self):
        print('инициализация экземпляра класса')
        self._settings = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        else:
            print('возвращаем ранее созданный экземпляр класса')
        return cls._instance

    @classmethod
    def reset_instance(cls):
        print('сброс экземпляра класса')
        cls._instance = None

    def set_param(self, key, value):
        self._settings[key] = value
        print(f'установлен параметр {key} = {value}')

    def get_param(self, key, default=None):
        value = self._settings.get(key, default)
        print(f'получен параметр {key} => {value}')
        return value

    def show_all(self):
        print('все параметры:')
        for key, value in self._settings.items():
            print(f'  {key}: {value}')

s1 = AppSetting.get_instance()
s1.set_param('language', 'ru')
s1.set_param('theme', 'dark')

s2 = AppSetting.get_instance()
s2.get_param('theme')
s2.get_param('language', default='en')

print(s1 is s2)

s2.show_all()

AppSetting.reset_instance()
s3 = AppSetting.get_instance()
s3.show_all()
s3.set_param('language', 'en')
s3.show_all()