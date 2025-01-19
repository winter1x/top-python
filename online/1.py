# Задание 1
#  Пользователь вводитсклавиатурыстроку.Проверьте
# является ли введенная строка палиндромом. Палин
# слева направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба.
#  Задание 2
#  Пользователь вводитсклавиатурынекоторыйтекст,
# послечегопользовательвводитсписокзарезервированных
# слов. Необходимонайтивтекстевсезарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.
# Задание 3
#  Есть некоторый текст. Посчитайте в этом тексте ко
# личество предложенийивыведитенаэкранполученный
# результат
from numpy.ma.core import append

# import re
# x = input()
# x = re.sub(r'[^а-яА-ЯёЁ]', '', x).lower()
# if x == x[::-1]:
#     print("Верно")
# else:
#     print("wrong")


# text = input("Введите текст: ")
#
# reserved_words = input("Введите зарезервированные слова через запятую: ").split(',')
#
# reserved_words = [word.strip().upper() for word in reserved_words]
#
# for word in reserved_words:
#     text = text.replace(word.upper(), word)
# print("Измененный текст:", text)

from gettext import textdomain
from pdb import runctx
from random import sample, choice, shuffle
from re import match
from string import *
from re import *
import re

email = 'qweqw@tu.riu'
phone1 = '+7(123)123-23-23'
phone2 = '+7(666)666-66-66'
phone3 = '+7(123)123-23'

pattern_email = r'^\w+[\.\w-]*@\w+[\.\w-]*\.\w+[\.\w-]*$'
pattern_phone = r'^\+?\d{1}[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'

print(bool(re.match(pattern_email, email)))
print(bool(re.match(pattern_phone, phone1)))
print(bool(re.match(pattern_phone, phone2)))
print(bool(re.match(pattern_phone, phone3)))