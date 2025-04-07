"""
бинарный поиск
"""

"""
по способу организации

внутренняя сортировка - в оперативке
внешняя - для больших данных, с записью во временные файлы
"""

"""
по устойчивости (стабильности)

стабильная сортировка- сохраняет порядок одинаковых элементов
нестабильная - может измениться
"""

"""
по принципу работы

обменные алгоритмы - пузырьковая - if else
выборочные - выбором - выбирается минимальный элемент
вставочные - вставками - новый элемент вставляется в отсортированную часть списка
разделяй и властвуй - быстрая, слиянием - рекурсия, части сортируются
"""

"""
.sort() - сортирует список на месте - изменяет его
sorted() - возвращает новый"""

numbers = [5, 4, 2, 6, 7, 8, 3, 5, 6, 9]
numbers.sort()
print(numbers)

numbers = [5, 4, 2, 6, 7, 8, 3, 5, 6, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

words = ['123', '1234', '12', '12334']
words.sort(key=len)
print(words)

students = [('иван', 20), ("анна", 18), ("петр", 22)]
students.sort(key=lambda x: x[1])
print(students)

numbers = [5, 4, 2, 6, 7, 8, 3, 5, 6, 9]
numbers.sort(reverse=True)
print(numbers)

numbers = [5, 4, 2, 6, 7, 8, 3, 5, 6, 9]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)
"""
O(n)
n - размер входных данных (сколько элементов)
"""

"""
простые O(n^2)
пузырьковая, вставками, выбором
"""

"""
продвинутые O(n log n)
слиянием быстрая 
"""

"""
гибридные
timsort: вставками + слиянием
"""

"""
пузырьковая (bubble sort)
"""

"""
1 проход

[5, 3, 8, 4, 2] 5 3 8 4 2
5 > 3
3 5
[3, 5, 8, 4, 2]
5 < 8
[3, 5, 8, 4, 2]
8 > 4
4 8
[3, 5, 4, 8, 2]
8 > 2
2 8
[3, 5, 4, 2, 8]
"""

def bubble_sort_bad(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#[3, 2, 4, 5, 8]
#[2, 3, 4, 5, 8]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

#выбором (selection sort)

"""
min из неотсортированной части массива
меняем этот минимальный e с первым e неотсортированной части
повторяем
"""

"""
1 проход

[5, 3, 8, 4, 2]
2 <-> 5
[2, 3, 8, 4, 5]

2 проход

[2, 3, 8, 4, 5]
3 <-> 5
[2, 3, 8, 4, 5]

3 проход

[2, 3, 8, 4, 5]
4 <-> 8
[2, 3, 4, 8, 5]

"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index] ,arr[i]

numbers = [5, 3, 8, 4, 2]
selection_sort(numbers)
print(numbers)

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
"""
[]
[4, 2, 5, 1]
min 1
[1, 2, 5, 4]
[1]

[1]
[1, 2, 5, 4]
min 2
[1, 2, 5, 4]
[1, 2]

[1, 2]
[1, 2, 5, 4]
min 4
[1, 2, 4, 5]

"""





"""
левая уже отсортирована
правая нет

[5, 2, 4, 6, 1, 3]
2 < 5
[2, 5, 4, 6, 1, 3]
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key



"""
[4, 3, 2, 1]
3 4
3 
[3 4 2 1]
2 < 4 
4
[3 4 4 1]
2 < 3
[3 3 4 1]
[2 3 4 1]

[2 3 4 4]
[2 3 3 4]
[2 2 3 4]
[1 2 3 4]
"""

"""
1: выбираем шаг
2: сортируем с шагом
3: уменьшаем шаг
4: дойдя до 1 = обычная вставками

[5, 2, 9, 1, 5, 6]
первые элементы:
i = 0 3 6
[5, 1]
вторые элементы:
i = 1, 4
[2, 5]
третьи элементы:
i = 2, 5
[9, 6]

[1, 2, 6, 5, 5, 9]

хиббарда
"""

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        gap //= 2