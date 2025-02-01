"""from time import *
print(pow(2, 3))
from math import pow
"""
"""print(1, 2, 3, 4, '123' + '123', 5 % 2, 5 // 2, 2 ** 3)
number = input()  # ввод str с консоли
number = bool(number)
print(number)  # вывод в консоль
"""
"""
str   строки "123" '123'
int   целые числа 123 34554435435 35 53 534 53 334 345 53 453 345 43
float дробные 123.3 5.4 6.0
bool  булевы True/1 False/0
list список (не массив, но похож)
перевод в другое тип
str()
int()
float()
bool()

>
<
>=
<=
==
!=
and и/умножение
or или/сложение
not отрицание
"""
"""flag = 5 > 2 and 4 < 3 or True

if 5 > 2:
    print("правда")
else:
    print("ложь")

if flag:
    print("правда")
else:
    print("ложь")
    """
"""if False:
    print()
elif False:
    print()
elif False:
    print()

if True:
    print()
start = time()
end = time()
while end - start < 1:
    end = time()
    print(1)
else:
    print('цикл закончился')
"""
"""str1 = '123456789'
for index, element in enumerate(str1):
    print(index, element)"""

"""for i in range(0, 51, 2):
    print(i)"""
"""
for _ in range(5):
    print('hi')

str1 = '123456789'
print(str1[::-1])  # перевернуть строку

str1 = '123456789'
print(str1[2:5])

list1 = []
list2 = [123, 345, 6, True, 'sdc']
list3 = list(range(5))
print(list3)
print(range(5))

for e in list3:
    if e % 2 == 0:
        print(e)

chetnie = [i for i in list3 if i % 2 == 0]
b = None
print(type(b).__name__)
print(chetnie)"""
"""
length = int(input())
list1 = []
for _ in range(length):
    list1.append(int(input()))

for index, element in enumerate(list1):
    print(index, element)

print(f'длина: {length}\nсписок: {list1}')"""

"""
chr() символ по юникод коду
hex() 16x
len() длина 
abs() модуль
max()
min()
sum()

in
"""

"""print(chr(65))
print(chr(97))

print(hex(255))"""
"""
str1 = '1234'
str2 = '235'"""
"""list1 = list(range(5))
print(len(str1), len(list1))
print(1, abs(-1))

print(max(list1), min(list1), sum(list1))"""
"""for c in str2:
    if c not in str1:
        print(c)"""

"""
console.log(Math.round(num)); //до ближайшего целого
console.log(Math.floor(num)); //округление вниз до ближайшего целого
console.log(Math.ceil(num)); //вверх до ближайшего целого
console.log(Math.trunc(num)); //убрать дробную часть
console.log(num.toFixed(2)); //определенное количество знаков после запятой"""

"""import math
from math import *
from math import pi, ceil, trunc, floor"""
"""
import math as m
from math import *
from math import pi as p, ceil as c, trunc, floor

print(list1)
print(custom_add(1, 2))

print(m.pi)
print(round(pi))
print(round(pi, 2))
print(f'{pi:.3}')
print(ceil(pi))
print(trunc(pi))
print(floor(pi))

print(c(p))
"""
"""import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from offline.main import list1
print(list1)"""

"""
12
12
"""
'''
34
34
'''
# 213
# 123

"""x = None
if x is None:
    print(True)"""

"""x = Null было раньше
x = Nil в go
"""

"""list1 = [False, True, False]
if any(list1):
    print(True)
list1 = [True, True, True]
if all(list1):
    print(True)
"""
""""x = 8 if 5 > 2 else 5
"""""""значение если правда условие значение если ложь"""
"""print(x)
"""
"""number = 0
match number:
    case 0:
        print(0)
    case 2:
        print(2)
    case _:
        print('другое число')
number = str(number)
match number:
    case int():
        print('int')
    case str():
        print('str')
    case _:
        print('другой тип')
tuple1 = 2, 3

match tuple1:
    case (0, 0):
        print('начало координат')
    case (2, 3):
        print(f'точка {tuple1}')
    case _:
        print('другая точка')
list1 = [1, 2, 3]
match list1:
    case []:
        print(None)
    case [1, 2, 3]:
        print(list1)
    case _:
        print("other")

"""
"""для js
loop1: for(,,)
    loop2: for(,,)
        break loop2"""
"""
for i in range(5):
    if i == 1:
        print(f'прерывание {i}')
        continue
    print(i)
    if i == 2:
        print(f'остановка {i}')
        break

str1 = '123'"""
"""print('frffr', 'ererferfer', 'erfr')
print()
print()
print('frffr', 'ererferfer', 'erfr', sep='0123')
print('frffr', 'ererferfer', 'erfr', sep='\t')
print('frffr', 'ererferfer', 'erfr', sep=' ')
print('frffr', 'ererferfer', 'erfr', sep='??')
print('frffr', 'ererferfer', 'erfr', end='\n')
print('frffr', 'ererferfer', 'erfr', end='\t')
print('frffr', 'ererferfer', 'erfr', end=' ')
print('frffr', 'ererferfer', 'erfr', end='??')
"""
"""def custom_add_print(a, b):
    print(a + b)

def custom_add_return(a, b):
    return a + b

def get_user_info():
    name = "matvey"
    age = 23
    return name, age

myName, myAge = get_user_info()
print(myAge, myName)

custom_add_print(1, 2)
a = custom_add_return(1, 2)
print(a)


list1 = []
list2 = [1, 2, {234, 234, 12}, (123, 32), '1231', [123, 123, 123]]
for i in range(2, 10, 2):
    list1.append(i)
    print(i)

print(list1)
for i in list1:
    print(i)

print(list1[-1])
print(list1.pop())
"""
"""# lst = [int(s) for s in input().split()]
list1 = [i for i in range(5)]
print(list1)
list1 = list(range(5))
print(list1)
list1 = [i ** 4 if i % 4 == 0 else i ** 2 for i in range(10) if i % 2 == 0]
print(list1)
list1 = [i * j for i in range(5) for j in range(5)]
print(list1)
list1 = [[i * j for i in range(5)] for j in range(5)]
print(list1)

# квадраты чисел от 3 до 50 с шагом 7
list1 = [i * i for i in range(3, 50, 7)]

# создать список четных чисел от 0 до 20
list1 = [i for i in range(20) if i % 2 == 0]

list2 = ['123', '123', '123', '123', '123f', '1234']
# создать список слов, длина которых больше 3
list2 = [word for word in list2 if len(word) > 3]
print(list2)
list3 = [1, 2, 3]
list4 = [100, 1000]
# создать список со всеми возможными суммами двух элементов из двух списков
list1 = [i + j for i in list3 for j in list4]
print(list1)
"""
"""
try:
    a = float(input())
    b = float(input())
    print(a / b)

except ZeroDivisionError:
    print("нельзя / на 0")
except ValueError:
    print("введено не число")

except Exception as ex:
    print(ex)
    print("неизвестная ошибка")

else:
    print('ошибок не возникло')
finally:
    print("тест завершен")"""

"""
вводим а б
попробуем поделить а на б
ZeroDivisionError если делим на 0. печать нельзя на 0
ValueError если не число. печать введено не число
в остальных случаях печать неизвестная ошибка
"""

"""def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))"""


"""def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter1 = make_counter()
print(counter1())
print(counter1())
print(counter1())"""
"""
функция умножения
"""
"""def make_multiplier(x):
    def inner_function(y):
        return x * y
    return inner_function

times3 = make_multiplier(3)
print(times3(9)) # 27
print(times3(9)) # 27

def outer_function(name):
    return lambda: f'Hello, {name}'

greet = outer_function('alice')
print(greet())
greet = outer_function('112')
print(greet())

multipliers = []
for x in range(1, 4):
    multipliers.append(lambda y : x * y)

m1, m2, m3 = multipliers
print(m1(10))
print(m2(10))
print(m3(10))

multipliers = []
for x in range(1, 4):
    multipliers.append(lambda y, real_x=x : real_x * y)

m1, m2, m3 = multipliers
print(m1(10))
print(m2(10))
print(m3(10))
"""
"""def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter"""
"""def make_counter():
    count = [0]
    return lambda: (count.append(count[-1] + 1) or count[-1])

# 1 счетчик
counter1 = make_counter()
print(counter1()) # 1
print(counter1()) # 2
print(counter1()) # 3

def make_multiplier(n):
    return lambda x : x * n
# умножение на число. Принимает число, возвращает замыкание
times5 = make_multiplier(5)
print(times5(10)) # 50
print(times5(3)) # 15

def filter_by_threshold(threshold):
    return lambda numbers: [n for n in numbers if n > threshold]
# фильтрация списка. Принимает пороговое значение, возвращает замыкание для фильтрации списка чисел
filter_above_10 = filter_by_threshold(10)
print(filter_above_10([5, 10, 15, 20])) # [15, 20]

def create_functions(numbers):
    return [lambda x, n=n: x * n for n in numbers]
# создание множества функций. Принимает список чисел, возвращает список функций. Кажая функция умножает входное на соответствующее из списка
functions = create_functions([2, 3, 4])
print(functions[0](10)) # 20
print(functions[1](10)) # 30
print(functions[2](10)) # 40"""

def count_up_to(max1):
    count = 1
    while count <= max1:
        yield count
        count += 1

"""list1 = list(count_up_to(3))
print(list1)"""
for number in count_up_to(3):
    print(number)
# ----------------------------------------------------------------

def get_even(list_of_nums):
    for i in list_of_nums:
        if i % 2 == 0:
            yield i

list_of_nums = [1, 2, 3, 8, 15, 42]
for i in get_even(list_of_nums):
    print(i, end=' ')

print()
# ----------------------------------------------------------------

def nextCube():
    acc = 1
    while True:
        yield acc ** 3
        acc += 1

count = 1
for num in nextCube():
    if count > 15:
        break
    print(num)
    count += 1

# ----------------------------------------------------------------

str1 = '1234589'
iter1 = iter(str1)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
# ----------------------------------------------------------------

list1 = [1, 2, 3]
iter2 = iter(list1)
try:
    print(next(iter2))
    print(next(iter2))
    print(next(iter2))
    print(next(iter2))
except StopIteration:
    print('конец')
# ----------------------------------------------------------------

def number_generator():
    for i in range(1, 6):
        yield i

gen = number_generator()
print(next(gen))
print(next(gen))
print(next(gen))
# ----------------------------------------------------------------

import random

def random_number_generator():
    while True:
        yield random.randint(1, 100)

gen = random_number_generator()
print(next(gen))
print(next(gen))
print(next(gen))
# ----------------------------------------------------------------

# фибоначчи

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)
# ----------------------------------------------------------------

from itertools import chain, cycle, count

combined = list(chain(iter([1, 2]), iter(['a', 'b'])))
print(combined)
# ----------------------------------------------------------------
cyclic_iterator = cycle([10, 20, 50])
for i in range(20):
    print(next(cyclic_iterator), end=' ')
# ----------------------------------------------------------------

for i in count(10):
    if i > 15:
        break
    print(i)