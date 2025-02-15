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

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"вызывается {func.__name__} с аргументами {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"функция {func.__name__} завершила выполнение")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(3, 5))