"""def add(a: int, b: int) -> int:
    return a + b

def print_sum(a, b):
    print(a + b)

def some_func2():
    print("some")

def many_returns():
    return 1, 2, 3, 4, 5

print(add(1, 2))
print_sum(1, 2)

a, b, c, d, e = many_returns()
print(a, b, c, d, e)



def some_func():
    pass


a = input()
print(a)

def add(a=0, b=0):
    print(a + b)

add(b=5)"""

"""
рекурсия - функция вызывает саму себя
базовый случай - условие прекращения вызовов
"""
# прямая - f вызывает саму себя
# косвенная - f вызывает другую функцию, которая затем вызывает первую
# линейная - f вызывает себя один раз при вычислении результата
# каскадная - f вызывает себя несколько раз

# каскадная - f вызывает себя несколько раз
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# n!
# прямая - f вызывает саму себя
# линейная - f вызывает себя один раз при вычислении результата
#abs - модуль числа
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
#              5 * f(5 - 1) = 4 * f(4 - 1) = 3
#               5 *         4       *       3
#5*4*3*2 factorial(2 - 1) =1
#5*4*3*2*1
n = 5
result = factorial(n)
print(result)

# линейная - f вызывает себя один раз при вычислении результата

def collatz(n):
    if n == 1:
        return True
    if n % 2 == 0:
        return collatz(n // 2)
    return collatz(n * 3 + 1)

def nod(a, b):
    if b == 0:
        return a
    if a < b:
        return nod(b, a)
    return nod(b, a % b)

"""
принимает целое число n и выводит все целые от n до 1 включительно
"""
#базовый случай - если n = 1, то функция просто выводит 1 и завершает работу(рекурсию)
#рекурсивный случай - если n > 1,