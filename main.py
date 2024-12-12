"""number1 = 1
number2 = 1.1
str1 = '123'
flag1 = True
flag2 = False
print(number1, type(number1).__name__, 2 + 2, sep='', end='')
print(number2, type(number2).__name__)
print(str1, type(str1).__name__)
print(flag1, type(flag1).__name__)
print(flag2, type(flag2).__name__)

# 8093454
"""
from math import trunc

from listGuide import list1

"""qwd
qwwwww"""
"""

'''
qwd
qwd
dw
'''"""
"""num = int(input())
num = str(num)
num = float(num)
num = bool(num)
print(type(num))
print(num)"""
"""flag = 5 > 3 and 6 > 2 and not False or False
print(flag)"""
# >
# <
# >=
# >=
# ==
# !=
"""
if False:
    print(True)
    print(True)
else:
    print(False)
    if True:
        print(True)"""

"""if False:
    print()
elif False:
    print()
elif False:
    print()
else:
    print("finally")"""
"""i = 0
while 5 > 3 and 6 > 2 and not False or False:
    i += 1
else:
    print("done")    
    """
"""str1 = 'vfj2'
numbers = '1234567890'
list1 = [0, 4, 6, 74, '2', True]
for i in list1:
    if type(i) != int:
        print(i, 'это не число')"""
"""i = 0 
while True:
    i += 1
    if i == 10:
        break
        
for i in range(10):
    if i == 5:
        continue
    print(i)"""

"""try:
    print(1 / 0)
except Exception as ex:
    print(ex)
except ZeroDivisionError:
    print(ZeroDivisionError)
else:
    print('ошибок не возникло')
finally:
    print("тест завершен")"""

"""name = input()
print('Hello, ' + name + '!')"""
"""print('!' * 10)"""
"""print(1, 2, 3)
print(1, 2, 3)
print(1, 2, 3, sep='', end='')
print(1, 2, 3, sep='', end='')"""
# min
# max
# abs
# len
# pow
# hex
# round
import math
"""sum1 = sum([1, 2, 3, 4, 5, 6, 7])
max1 = max(1, 2, 3, 4)
min1 = min(1, 2, 4, 5)
abs1 = abs(-1)
someStr = '123z121saf253'
length1 = len([1, 2, 3])
length2 = len(someStr)

sorted1 = sorted(someStr)
print(''.join(sorted1))
sorted2 = sorted([1, 2, 3])

print(any([True, False, False])) # или во множестве
print(all([True, True, True]))  # и во множестве

list1 = []
for i in range(10):
    list1.append(i)
print(list1)"""

import time
import time as t
from time import *
list1 = [1, 2, 3]
start = time()
for i in range(100000):
    list1.extend([5, 5])
end = time()
print(end - start)
list2 = [1, 2, 3]
start = time()
for i in range(100000):
    list2 += [5, 5]
end = time()
print(end - start)
# на выборке из 100 определить какой из методов работает быстрее с указанием количества раз для каждого