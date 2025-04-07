"""
запрашивает список через пробел
1 2 3 4 5 5 -> в список целых чисел - в одну строчку
подсчитать количество перестановок, итераций

добавить возможность выбора пользователем в каком порядке сортировать
"""

def merge_sort(arr, ascending=True):
    # Базовый случай: массив из одного элемента
    if len(arr) <= 1:
        return arr, 0, 0

    mid = len(arr) // 2

    # Рекурсивно сортируем левую и правую половины, не забываем передавать ascending
    left, iter_left, swap_left = merge_sort(arr[:mid], ascending)
    right, iter_right, swap_right = merge_sort(arr[mid:], ascending)

    # Сливаем отсортированные половины
    merged, merge_iters, merge_swaps = merge(left, right, ascending)

    # Суммируем статистику
    total_iters = iter_left + iter_right + merge_iters
    total_swaps = swap_left + swap_right + merge_swaps

    return merged, total_iters, total_swaps


def merge(left, right, ascending):
    result = []
    i = j = 0
    swaps = 0
    iterations = 1  # Считаем 1 итерацию на каждый merge

    # Пока есть элементы в обоих массивах
    while i < len(left) and j < len(right):
        # Сравниваем в зависимости от направления сортировки
        if (ascending and left[i] <= right[j]) or (not ascending and left[i] >= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        swaps += 1

    # Добавляем оставшиеся элементы из левой части
    while i < len(left):
        result.append(left[i])
        i += 1
        swaps += 1

    # Добавляем оставшиеся элементы из правой части
    while j < len(right):
        result.append(right[j])
        j += 1
        swaps += 1

    return result, iterations, swaps


# Ввод от пользователя
numbers = list(map(int, input("Введите числа через пробел: ").split()))
order = input("asc - по возрастанию / desc - по убыванию: ").strip().lower()
ascending = True if order == 'asc' else False

# Сортировка
numbers, iterations, swaps = merge_sort(numbers, ascending)

# Вывод
print("Отсортированный список:", numbers)
print("Итераций (слияний):", iterations)
print("Перестановок (вставок):", swaps)
