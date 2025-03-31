from functools import reduce

#lambda filter map reduce
"""
оставить нечетные числа
возвести их в куб
найти сумму
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_of_cubes = reduce(
    lambda x, y: x + y,
    map(
        lambda x: x ** 3,
        filter(lambda x: x % 2 == 0, numbers)
    )
)
"""
оставить те где длина >3 

Если
    начинается с гласной, то превратить в заглавные все буквы
    противный - первая заглавной, остальные строчные

объединить все в строку через пробел
"""
words = ['qwe', 'wer', 'rty', 'asd', 'ert', 'uio']