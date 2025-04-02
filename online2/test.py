"""
запрашивает список через пробел
1 2 3 4 5 5 -> в список целых чисел - в одну строчку
подсчитать количество перестановок, итераций

добавить возможность выбора пользователем в каком порядке сортировать
"""

def bubble_sort(arr, ascending=True):
    n = len(arr)
    total_swaps = 0
    total_iterations = 0
    for i in range(n - 1):
        swapped = False
        swaps_in_pass = 0

        for j in range(n - i - 1):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                swaps_in_pass += 1
                total_swaps += 1

        total_iterations += 1
        print(f"шаг {i + 1}: {arr} перестановки {swaps_in_pass}")

        if not swapped:
            break

    return total_iterations, total_swaps

numbers = list(map(int, input().split()))
order = input("asc - по возрастания / decs - по убыванию").strip().lower()
ascending = True if order == 'asc' else False
iterations, swaps = bubble_sort(numbers, ascending)