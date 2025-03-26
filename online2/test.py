"""
multiply_numbers
- принимает произвольное колво чисел
- возрвращет произведение
"""
"""
format_person_info
- принимает именованные name, age, city
- return "имя <>..."
"""
"""
список, передаем в multiply_numbers
словарь с info о person, передать в format_person_info
"""
"""
output
объединение двух списков чисел с использованием * и передадите в multiply_numbers
объединение двух словарей с разными данными и передадите в format_person_info
"""

def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result

def format_person_info(**kwargs):
    return f"Имя: {kwargs['name']}, Возраст: {kwargs['age']}, Город: {kwargs['city']}"

numbers1 = [2, 3, 4]
numbers2 = [5, 6]

person1 = {'name': 'ivan', 'age':23}
person2 = {'city': "moscow"}

print(multiply_numbers(*numbers1, *numbers2))

print(format_person_info(**person1, **person2))