"""
запрашивает список через пробел
1 2 3 4 5 5 -> в список целых чисел - в одну строчку
подсчитать количество перестановок, итераций

добавить возможность выбора пользователем в каком порядке сортировать
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result


numbers = list(map(int, input().split()))
order = input("asc - по возрастания / decs - по убыванию").strip().lower()
ascending = True if order == 'asc' else False
iterations, swaps = merge_sort(numbers, ascending)

print(numbers)
print(iterations, swaps)