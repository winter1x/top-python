"""
запрашивает список через пробел
1 2 3 4 5 5 -> в список целых чисел - в одну строчку
подсчитать количество перестановок, итераций

добавить возможность выбора пользователем в каком порядке сортировать
"""

def selection_sort(arr):
    n = len(arr)
    left, right = 0, n - 1
    while left < right:
        min_index = left
        max_index = right

        for i in range(left, right + 1):
            if arr[i] < arr[min_index]:
                min_index = i
            if arr[i] > arr[min_index]:
                max_index = i

        arr[left], arr[min_index] = arr[min_index], arr[left]

        if max_index == left:
            max_index = min_index

        arr[right], arr[max_index] = arr[max_index], arr[right]

        left += 1
        right -= 1