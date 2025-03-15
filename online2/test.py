lst = list(map(int, input().split())) # ввод
"""
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""
a = [int(s) for s in input().split()]
index_of_min = 0
index_of_max = 0
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
    if a[i] < a[index_of_min]:
        index_of_min = i
a[index_of_min], a[index_of_max] = a[index_of_max], a[index_of_min]
print(' '.join([str(i) for i in a]))

#--------------------------------------
lst = list(map(int, input().split()))
max_index = lst.index(max(lst))
min_index = lst.index(min(lst))
lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
for i in lst:
    print(i, end=' ')


"""
Дан список чисел. 
Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, 
равные друг другу образуют одну пару, которую необходимо посчитать.
"""

a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)
#--------------------------------------
lst = list(map(int, input().split()))

element_counts = {}
for num in lst:
    if num in element_counts:
        element_counts[num] += 1
    else:
        element_counts[num] = 1

count = 0
for key in element_counts:
    n = element_counts[key]
    if n >= 2:
        count += n * (n - 1) // 2

print(count)

"""
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. 
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""
n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

correct = True
for i in range(n):
    for j in range(i + 1, n):
        if (x[i] == x[j] or y[i] == y[j]
                or abs(x[i] - x[j]) == abs(y[i] - y[j])):
            correct = False

if correct:
    print('NO')
else:
    print('YES')

#--------------------------------------
queens = []
[
    (x11, y12),
    (x23, y24),
    (5, 6),
    (7, 8)
]
for _ in range(8):
    x, y = map(int, input().split())
    queens.append((x, y))
attack = False
for i in range(8):
    for j in range(i + 1, 8):
        x1, y1 = queens[i]
        x2, y2 = queens[j]
        if x1 == x2 or y1 == y2:
            attack = True
            break
        if abs(x1 - x2) == abs(y2 - y1):
            attack = True
            break
if attack:
    print('YES')
else:
    print("NO")
#--------------------------------------
queens = []
for _ in range(8):
    x, y = map(int, input().split())
    queens.append((x, y))

found = False
for i in range(8):
    for j in range(i + 1, 8):
        x1, y1 = queens[i]
        x2, y2 = queens[j]
        if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            found = True
            break
    if found:
        break

print("YES" if found else "NO")
"""
Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
"""
s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)
#--------------------------------------
s = input()
result = ''
for i in range(len(s)):
    if i % 3 != 0:
        result += s[i]
print(result)


"""
Политическая жизнь одной страны очень оживленная. В стране действует K политических партий, 
каждая из которых регулярно объявляет национальную забастовку. Дни, когда хотя бы одна из партий объявляет забастовку, 
при условии, что это не суббота или воскресенье (когда и так никто не работает), наносят большой ущерб экономике страны.

i-я партия объявляет забастовки строго каждые b_i дней, начиная с дня с номером a_i. 
То есть i-я партия объявляет забастовки в дни a_i, a_i + b_i, a_i + 2 * b_i и т.д. 
Если в какой-то день несколько партий объявляет забастовку, то это считается одной общенациональной забастовкой.

В календаре страны N дней, пронумерованных, начиная с единицы. Первый день года является понедельником, 
шестой и седьмой дни года — выходные, неделя состоит из семи дней.

В первой строке даны числа N и K. Далее идет K строк, описывающие графики проведения забастовок. 
i-я строка содержит числа a_i и b_i. Вам нужно определить число забастовок, произошедших в этой стране в течении года.
"""
N, K = [int(s) for s in input().split()]
work_days = set([day for day in range(1, N + 1) if day % 7 not in (6, 0)])
no_strikes = set(work_days)
for party in range(K):
    a, b = [int(s) for s in input().split()]
    max_strikes = (N - a) // b + 1
    no_strikes -= {a + b*i for i in range(max_strikes)}
print(len(work_days) - len(no_strikes))
#--------------------------------------
N, K = map(int, input().split())
strikes = set()
for _ in range(K):
    a_i, b_i = map(int, input().split())
    current_day = a_i
    while current_day <= N:
        if current_day % 7 != 6 and current_day % 7 != 0:
            strikes.add(current_day)
        current_day += b_i
print(len(strikes))

"""
В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, 
сколько раз оно встречалось в этом тексте ранее.

Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов или символами конца строки.
"""