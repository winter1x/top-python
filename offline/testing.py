def capitalize(text):
    if text == '':
        return ''

    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'


if capitalize('hello') != 'Hello':
    raise Exception("функция работает неверно")

if capitalize('') != '':
    raise Exception("функция работает неверно")

"""
''
None
int
"""

def get_by_index(elements, index, default):
    return elements[index] if index < len(elements) else default

print(get_by_index(['zero', 'one'], 2, 'value'))
