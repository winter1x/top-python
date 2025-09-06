from itertools import permutations

# Шаг 1: Ввод данных
data = input("Введите числа через запятую: ")  # Например: 22,44,05

# Шаг 2: Разделяем по запятой
numbers = data.split(",")  # ['22', '44', '05']

# Шаг 3: Находим все перестановки
# permutations(numbers) создаёт все возможные перестановки списков
# set(...) убирает дубликаты, если числа повторяются
unique_perms = set(permutations(numbers))

# Шаг 4: Выводим результат без запятых
for perm in unique_perms:
    print("".join(perm))
