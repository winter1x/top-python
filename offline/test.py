"""Задание
В одном из предыдущих уроков мы уже написали функцию filter_string().
Напомним, она принимает на вход строку и символ и возвращает новую строку,
в которой удалён переданный символ во всех его позициях.
На этот раз реализуйте эту функцию с помощью цикла for.
Дополнительное условие: регистр исключаемого символа не имеет значения.

Пример вызова:
"""
text = 'If I look forward I win'

def filter_string(s, c):
    c = c.lower()
    result = []
    for i in s:
        if i.lower() != c:
            result.append(i)
    return ''.join(result)

def filter_string2(text, char):
    result = ''
    for current_char in text:
        if current_char.upper() != char.upper():
            result += current_char
    return result

print(filter_string(text, 'i'))  # 'f  look forward  wn'
print(filter_string(text, 'O'))  # 'If I lk frward I win'