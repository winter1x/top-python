"""
подсчет количества перестановок и итераций
визуализация дерева кучи на каждом этапе
"""
def heapify(arr, n, i, ascending):
    largest_or_smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if ascending:
        if left < n and arr[left] > arr[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and arr[right] > arr[largest_or_smallest]:
            largest_or_smallest = right
    else:
        if left < n and arr[left] < arr[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and arr[right] < arr[largest_or_smallest]:
            largest_or_smallest = right

    if largest_or_smallest != i:
        arr[i], arr[largest_or_smallest] = arr[largest_or_smallest], arr[i]
        heapify(arr, n, largest_or_smallest, ascending)


def heap_sort(arr, ascending=True):
    n = len(arr)

    #строим кучу
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, ascending)

    #сортируем, вытаскивая корень и уменьшая размер кучи
    for i in range(n - 1, 0, -1):

        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, ascending)

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
