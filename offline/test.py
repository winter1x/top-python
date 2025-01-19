"""
Задание 1
 Пользователь вводитсклавиатурыстроку.Проверьте
является ли введенная строка палиндромом. Палин
слева направо и справа налево. Например, кок; А роза
упала на лапу Азора; доход; А буду я у дуба.
"""
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

user_input = input()
print("Это палиндром!" if is_palindrome(user_input) else "Это не палиндром.")
"""
 Задание 2
 Пользователь вводитсклавиатурынекоторыйтекст,
послечегопользовательвводитсписокзарезервированных
слов. Необходимонайтивтекстевсезарезервированные
слова и изменить их регистр на верхний. Вывести на
экран измененный текст.
"""
def replace_reserved_words(text, reserved_words):
    for word in reserved_words:
        text = text.replace(word, word.upper())
    return text

text = input()
reserved_words = input().split()
modified_text = replace_reserved_words(text, reserved_words)
print("Измененный текст:", modified_text)
"""
Задание 3
 Есть некоторый текст. Посчитайте в этом тексте ко
личество предложенийивыведитенаэкранполученный
результат
"""
import re

def count_sentences(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

text = input()
sentence_count = count_sentences(text)
print("Количество предложений в тексте:", sentence_count)
"""
Задание 1
 Пользователь вводит с клавиатуры число в диапа
зоне от 1 до 100. Если число кратно 3 (делится на 3 без
остатка) нужно вывести слово Fizz. Если число кратно 5
нужновывестисловоBuzz.Есличислократно3и5нужно
вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
вывести само число.
Еслипользователь ввел значение не вдиапазонеот1
до 100 требуется вывести сообщение об ошибке.
"""
number = int(input())

if 1 <= number <= 100:
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
else:
    print("Ошибка: число должно быть от 1 до 100.")
"""
 Задание 2
 Написать программу, которая по выбору пользова
теля возводит введенное им число в степень от нулевой
до седьмой включительно.
"""
number = float(input())
power = int(input())

if 0 <= power <= 7:
    result = number ** power
    print(result)
else:
    print("Ошибка: степень должна быть от 0 до 7.")
"""
 Задание 3
 Написать программу подсчета стоимости разговора
для разныхмобильныхоператоров.Пользовательвводит
стоимость разговора и выбирает с какого на какой опе
ратор он звонит. Вывести стоимость на экран
"""
cost = float(input())
operators = {
    1: "Оператор A",
    2: "Оператор B",
    3: "Оператор C"
}

from_operator = int(input())
to_operator = int(input())

if from_operator in operators and to_operator in operators:
    print(cost)
else:
    print("Ошибка: выбран неверный оператор.")
"""
Задание 4
 Зарплатаменеджерасоставляет200$+процентотпро
даж, продажидо500$—3%,от500до1000—5%,свыше
1000 — 8%. Пользователь вводит с клавиатуры уровень
продаж для трех менеджеров. Определить их зарплату,
определить лучшего менеджера, начислить ему премию
200$, вывести итоги на экран
"""
def calculate_salary(sales):
    if sales < 500:
        return 200 + sales * 0.03
    elif 500 <= sales < 1000:
        return 200 + sales * 0.05
    else:
        return 200 + sales * 0.08

manager_sales = [float(input()) for _ in range(3)]
salaries = [calculate_salary(sales) for sales in manager_sales]

best_manager_index = salaries.index(max(salaries))
salaries[best_manager_index] += 200

for salary in salaries:
    print(salary)

print(best_manager_index + 1)
"""
---------------------------------------------------------------------------
Задание 1
 Показать на экран все простые числа в диапазоне,
указанном пользователем. Число называется простым,
если оноделитсябезостаткатольконасебяинаединицу.
Например, три — это простое число, а четыре нет.
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input())
end = int(input())

for num in range(start, end + 1):
    if is_prime(num):
        print(num)
"""
 Задание 2
 Показатьнаэкранетаблицуумножениядлявсехчисел
от 1 до 10. Например:
 1 * 1 = 1          1 * 2 = 2   …..  1 * 10  = 10
 .........................................................................
 10 * 1 = 10    10 * 2 = 20 …. 10 * 10 = 100.
 """
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()
"""
 Задание 3
 Показать на экран таблицу умножения в диапазоне,
указанном пользователем. Например, если пользователь
указал 3 и 5, таблица может выглядеть так
 3*1 = 3    3*2 = 6       3*3 = 9       ...     3 * 10 = 30
.....................................................................................
 5*1 = 5    5 *2 = 10    5 *3 = 15    ...     5 * 10 = 50
"""
start = int(input())
end = int(input())

for i in range(start, end + 1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()