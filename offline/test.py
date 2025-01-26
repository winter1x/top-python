from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
strs = ['123', '456']

# Найдите сумму всех элементов списка чисел.
sum_result = reduce(lambda x, y : x + y, numbers)
print(sum_result)

# Найдите произведение всех элементов списка чисел.
sum_result = reduce(lambda x, y : x * y, numbers)
print(sum_result)

# Найдите максимальный элемент в списке чисел.
sum_result = reduce(lambda x, y : x if x > y else y, numbers)
print(sum_result)

# Объедините все строки из списка в одну строку через пробел.
conc_result = reduce(lambda x, y : x + ' ' + y, strs)
print(conc_result)

# Найдите сумму квадратов всех элементов списка чисел.
sum_result = reduce(lambda x, y : x + y ** 2, numbers)
print(sum_result)

# Найдите наименьший элемент в списке чисел.
sum_result = reduce(lambda x, y : x if x < y else y, numbers)
print(sum_result)

# Вычислите факториал числа, используя список чисел от 1 до этого числа.
n = 5
fact = reduce(lambda x, y : x * y, range(1, n + 1))
print(fact)

# Подсчитайте количество чётных чисел в списке, используя reduce.
count = reduce(lambda acc, x : acc + 1 if x % 2 == 0 else acc, numbers, 0)
print(count)