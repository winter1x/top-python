"""Известно, что на доске 8×8 можно расставить 8 ферзей так
, чтобы они не били друг друга. Вам дана расстановка 8
ферзей на доске, определите, есть ли среди них пара бьющих
друг друга. Программа получает на вход восемь пар чисел,
каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи
не бьют друг друга, выведите слово NO, иначе выведите YES."""
queens = []
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