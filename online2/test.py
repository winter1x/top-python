"""
1
декоратор log
Вызвана функция имя_функции с аргументами: аргументы
"""


def log(func):
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция {func.__name__} с аргументами: {args}")
        return func(*args, **kwargs)
    return wrapper

@log
def greet(name, age):
    print(f'привет, {name, age}')

greet("иван", 25)
"""
2
декоратор timer
Время выполнения функции имя_функции: время секунд
"""

"""
3
декоратор repeat

4
декоратор check_permissions
будет проверять имеет ли пользователь доступ к вызову функции
если не имеет прав, то декоратор должен выводить нет доступа
принимает список
"""
def check_permissions(allowed_users):
    def decorator(func):
        def wrapper(user):
            if user not in allowed_users:
                print('нет доступа')
            else:
                return func(user)
        return wrapper
    return decorator

@check_permissions(['admin', 'manager'])
def access_admin_area(user):
    print(f'добро пожаловать в админ-панель, {user}')

access_admin_area("admin")
access_admin_area("user")
"""
5
декоратор check_types
проверяет соответствуют ли аргументы функции заданным типам
декоратор принимает словарь
ключи - имена параметров
значения - типы

"""

def check_types(types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for (arg, (param, expected_type)) in zip(args, types.items()):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"ожидался тип {expected_type} для параметра {param}, но {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@check_types({'name': str, 'age': int})
def greet(name, age):
    print(f'привет, {name, age}')



"""
retry
количество попыток

если ф выбрасивает исключение, повторить ее выполнение до указанного количества раз
"""
import random

def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"ошибка {e}")
        return wrapper
    return decorator



@retry(3)
def usable_function():
    if random.choice([True, False]):
        raise ValueError("ошибка")
    print('успешно')

usable_function()
