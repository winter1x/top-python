"""
int - числа
str - строки
float - 1.1  плавающей (точкой)
bool - True False
"""
"""
number = 10
str1 = '112'
str_number = "34"""

"""num1 = input()
print(num1 + 1)"""

'''dceeve''' #многострочный
#92hrf9ejf39 - однострочный
"""
функции
int()
str()
float()
bool()
"""

"""num1 = int(input())
print(num1 + 1)
"""

"""try:
    num1 = input()
    print(1 / 0)
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex:
    print(ex)
else:
    print("тест не прошел")
finally:
    print("тест закончился")"""
""""""

#print(f'{number + 10}, что угодно {str1}')
"""print(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
average_grade = 1.111111111
print(f"{average_grade:.2f}")"""
"""average_grade = 1.111111111

#a = input()

flag1 = True
flag2 = False"""

"""
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

"""boolean_value = 6 > 2 and False or flag1
print(boolean_value)"""
"""number = int(input())
if number > 5:
    print(f"{number} > 5")
elif number < 5:
    print(f"{number} < 5")
else:
    print(f"{number} = 5")"""
count = 0
while count < 10 and True:
    if count == 5:
        count += 1
        continue
    if count == 8:
        break
    print(count)
    count += 1
else:
    print("цикл завершился")
