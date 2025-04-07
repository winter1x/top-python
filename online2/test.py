"""
запрашивает список через пробел
1 2 3 4 5 5 -> в список целых чисел - в одну строчку
подсчитать количество перестановок, итераций

добавить возможность выбора пользователем в каком порядке сортировать
"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

numbers = list(map(int, input().split()))
order = input("asc - по возрастания / decs - по убыванию").strip().lower()
ascending = True if order == 'asc' else False
iterations, swaps = insertion_sort(numbers, ascending)

print(iterations, swaps)