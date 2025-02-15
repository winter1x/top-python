def decorator(func):
    def wrapper():
        print("декоратор сработал до вызова функции")
        func()
        print("после вызова")
    return wrapper

@decorator
def say_hello():
    print('функция')

say_hello()


