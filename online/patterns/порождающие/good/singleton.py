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