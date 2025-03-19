def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # подсчитываем кол-во элементов для каждый цифры
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    # обновляем массив count[i], чтобы он содержал только позицию этой цифры в output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # заполняем выходной массив output
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # копируем output обратно в arr
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
        
    return arr

numbers = [45, 3, 23, 78, 98, 23, 56, 87, 320, 630, 76]
#numbers = [630, 320, 45, 3, 23, 78, 98, 23, 56, 87, 76]
sorted_numbers = radix_sort(numbers)
print(sorted_numbers)