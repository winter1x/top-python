def greet(name):
    return f"привет, {name}"

say_hello = greet
print(say_hello('me'))

def to_upper_case(text):
    return text.upper()

def print_formatted(formatter, message):
    print(formatter(message))

print_formatted(to_upper_case, 'привет')

def outer(text):
    def inner():
        print(f"внутри {text}")
    return inner

func = outer('привет')
func()

def say_hi():
    print('привет')

def wrapper():
    print('лог')
    say_hi()

wrapper()

def wrapper(func):
    def inner(*args, **kwargs):
        print('до')
        result = func(*args, **kwargs)
        print('после')
        return result
    return inner

def say_hello():
    print('привет')

def decorator(func):
    def wrapper():
        print('функция вызывается')
        func()
    return wrapper

say_hello = decorator(say_hello)
say_hello()

@decorator
def say_hello():
    print('привет')

def greet(name):
    print(f'привет, {name}')

def decorator(func):
    def wrapper(*args, **kwargs):
        print('функция вызывается')
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet(name):
    print(f'привет, {name}')

greet('катя')

def decorator(func):
    def wrapper(*args, **kwargs):
        print('функция вызывается')
        result = func(*args, **kwargs)
        print('функция завершена')
        return result
    return wrapper

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"время выполнения {end - start:.4f} сек")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print('готово')

slow_function()

@decorator
def greet(name):
    """печатает приветствие"""
    print(f'привет, {name}')


print(greet.__name__)
print(greet.__doc__)

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("функция вызывается")
        return func(*args, **kwargs)
    return wrapper


"""@decorator1
@decorator2
def f():
    pass

f = decorator1(decorator2(f))"""



def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say():
    print('привет')


say()