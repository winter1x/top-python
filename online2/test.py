"""
запрашивает список через пробел
1 2 3 4 5 5 -> в список целых чисел - в одну строчку
подсчитать количество перестановок, итераций

добавить возможность выбора пользователем в каком порядке сортировать
"""
def insertion_sort(arr, ascending=True):
    swaps = 0
    iterations = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        iterations += 1

        while j >= 0 and ((ascending and arr[j] > key) or (not ascending and arr[j] < kay)):
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1

        arr[j + 1] = key

    return iterations, swaps

numbers = list(map(int, input().split()))
order = input("asc - по возрастания / decs - по убыванию").strip().lower()
ascending = True if order == 'asc' else False
iterations, swaps = insertion_sort(numbers, ascending)

print(numbers)
print(iterations, swaps)