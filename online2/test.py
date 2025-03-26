#filter_numbers принимает условие
"""
even - четные
odd - нечетные
positive - положительные
negative - отрицательные
"""

сигнатура
    сигнатура (если без партикал)
        если передано even
            фильтруем четные, ретерн
        если передано odd
            фильтруем нечетные, ретерн

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_filter = filter_numbers("even")
print(even_filter(test_list))

odd_filter = filter_numbers("odd")
print(odd_filter(test_list))

positive_filter = filter_numbers("positive")
print(positive_filter(test_list))

negative_filter = filter_numbers("negative")
print(negative_filter(test_list))
