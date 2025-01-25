"""Реализуйте функцию print_table_of_squares(first, last),
которая печатает на экран квадраты чисел.
Она первое first и последнее last число печатает строку square of <число> is <результат>

Примеры вызова:
"""
def print_table_of_squares(first, last):
    result = []
    for number in range(first, last + 1):
        square = number ** 2
        result.append(f'square of {number} is {square}')
    print('\n'.join(result))

def print_table_of_squares2(first, last):
    for i in range(first, last + 1):
        square = i * i
        print(f"square of {i} is {square}")

print_table_of_squares(1, 3)
# => square of 1 is 1
# => square of 2 is 4
# => square of 3 is 9