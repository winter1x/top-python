"""подсчет перестановок и итераций"""
def quick_sort(arr, low, high, ascending=True, counters=None):
    if counters is None:
        counters = {"iterations": 0, 'swaps': 0}

    if low < high:
        pivot_index = partition(arr, low, high, ascending, counters)

        quick_sort(arr, low, pivot_index - 1, ascending, counters)
        quick_sort(arr, pivot_index + 1, high, ascending, counters)

    return counters

def partition(arr, low, high, ascending, counters):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        counters['iterations'] += 1
        if (ascending and arr[j] <= pivot) or (not ascending and arr[j] >= pivot):
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
                counters['swaps'] += 1

    if (i + 1) != high:
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        counters['swaps'] += 1

    return i + 1

numbers = list(map(int, input().split()))
order = input()
ascending = order == 'asc'
counters = quick_sort(numbers, 0, len(numbers) - 1, ascending)

print(numbers, counters['iterations'], counters['swaps'], sep='\n')