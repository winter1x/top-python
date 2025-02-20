# 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half =arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half) and k < len(arr):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[i]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while i < len(right_half):
        arr[k] = right_half[i]
        i += 1
        k += 1



arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print(arr)
