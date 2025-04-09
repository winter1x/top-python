def visualize_heap(arr, heap_size=None):
    """Печатает массив в виде дерева (по уровням)"""
    import math
    if heap_size is None:
        heap_size = len(arr)
    levels = int(math.log2(heap_size)) + 1 if heap_size > 0 else 0
    index = 0
    for level in range(levels):
        count = 2 ** level
        line = arr[index:index+count]
        print(" " * (2 ** (levels - level)), *line)
        index += count
        if index >= heap_size:
            break
    print("-" * 40)


def heapify(arr, n, i, ascending, stats):
    """Функция поддержания свойства кучи"""
    stats["iterations"] += 1  # Считаем итерацию (вызов heapify)
    largest_or_smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Выбираем наибольший/наименьший элемент среди родителя и потомков
    if ascending:
        if left < n and arr[left] > arr[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and arr[right] > arr[largest_or_smallest]:
            largest_or_smallest = right
    else:
        if left < n and arr[left] < arr[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and arr[right] < arr[largest_or_smallest]:
            largest_or_smallest = right

    # Если найден элемент, нарушающий свойство кучи — меняем местами
    if largest_or_smallest != i:
        arr[i], arr[largest_or_smallest] = arr[largest_or_smallest], arr[i]
        stats["swaps"] += 1
        print(f"Перестановка: {arr[i]} <--> {arr[largest_or_smallest]}")
        visualize_heap(arr, n)  # Визуализация после каждой перестановки
        heapify(arr, n, largest_or_smallest, ascending, stats)


def heap_sort(arr, ascending=True):
    n = len(arr)
    stats = {"swaps": 0, "iterations": 0}

    print("🔹 Строим кучу:")
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, ascending, stats)

    print("🔹 Сортировка:")
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        stats["swaps"] += 1
        print(f"Ставим {arr[i]} на место, меняем с {arr[0]}")
        visualize_heap(arr, i)
        heapify(arr, i, 0, ascending, stats)

    return arr, stats["iterations"], stats["swaps"]


numbers = list(map(int, input("Введите числа через пробел: ").split()))
order = input("asc - по возрастанию / desc - по убыванию: ").strip().lower()
ascending = True if order == 'asc' else False

sorted_list, iterations, swaps = heap_sort(numbers, ascending)

print("✅ Отсортированный список:", sorted_list)
print("📊 Кол-во итераций (вызовов heapify):", iterations)
print("🔁 Кол-во перестановок:", swaps)
