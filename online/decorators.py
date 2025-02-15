"""def decorator(func):
    def wrapper():
        print("декоратор сработал до вызова функции")
        func()
        print("после вызова")
    return wrapper

@decorator
def say_hello():
    print('функция')

say_hello()"""

"""def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"вызывается {func.__name__} с аргументами {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"функция {func.__name__} завершила выполнение")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(3, 5))"""
"""
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print('hi')

say_hi()"""

"""def methor_decorator(func):
    def wrapper(self, *args, **kwargs):
        print(f"вызов метода {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class Example:
    @methor_decorator
    def greet(self):
        print("привет от класса")

obj = Example()
obj.greet()
"""
"""from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("выполняетя декорированная функция")
        return func(*args, **kwargs)
    return wrapper

@decorator
def example():
    """"""эта функция возвращает hello""""""
    return "hello"

print(example.__name__)
print(example.__doc__)"""