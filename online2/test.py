"""
запрашивает список через пробел
1 2 3 4 5 5 -> в список целых чисел - в одну строчку
подсчитать количество перестановок, итераций

добавить возможность выбора пользователем в каком порядке сортировать
"""

def selection_sort(arr, ascending=True):
    n = len(arr)
    left, right = 0, n - 1
    total_swaps = 0
    total_iterations = 0

    while left < right:
        min_index = left
        max_index = right

        for i in range(left, right + 1):
            if (ascending and arr[i] < arr[min_index]) or (not ascending and arr[i] > arr[min_index]):
                min_index = i
            if (ascending and arr[i] > arr[max_index]) or (not ascending and arr[i] < arr[max_index]):
                max_index = i

        if min_index != left:
            arr[left], arr[min_index] = arr[min_index], arr[left]
            total_swaps += 1

            if max_index == left:
                max_index = min_index

        if max_index != right:
            arr[right], arr[max_index] = arr[max_index], arr[right]
            total_swaps += 1

        left += 1
        right -= 1
        total_iterations += 1

        print(f"шаг {total_iterations}: {arr}")

    return total_iterations, total_swaps

numbers = list(map(int, input().split()))
order = input("asc - по возрастания / decs - по убыванию").strip().lower()
ascending = True if order == 'asc' else False
iterations, swaps = selection_sort(numbers, ascending)

print(iterations, swaps)