#filter_numbers принимает условие
"""
even - четные
odd - нечетные
positive - положительные
negative - отрицательные
"""

def filter_numbers(condition):
    def filter_list(numbers):
        if condition == "even":
            return [num for num in numbers if num % 2 == 0]
        elif condition == "odd":
            return [num for num in numbers if num % 2 != 0]
        elif condition == "positive":
            return [num for num in numbers if num > 0]
        elif condition == "negative":
            return [num for num in numbers if num < 0]
        elif callable(condition):
            return [num for num in numbers if condition(num)]
        else:
            raise ValueError("")
    return filter_list
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_filter = filter_numbers("even")
print(even_filter(test_list))

odd_filter = filter_numbers("odd")
print(odd_filter(test_list))

positive_filter = filter_numbers("positive")
print(positive_filter(test_list))

negative_filter = filter_numbers("negative")
print(negative_filter(test_list))

custom_filter = filter_numbers(lambda x : x > 5)
print(custom_filter(test_list))