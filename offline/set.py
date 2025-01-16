inp = [1, 1, 2, 2]
print(set(inp)) # делает множество уникальных значений
some_set = {1, 2, 3, 3}
print(some_set)
zero2_set = set()
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3) # добавление
print(zero2_set)
zero2_set.update(range(5))
print(zero2_set)
zero2_set.discard(1)
print(zero2_set)
zero2_set.remove(2)
print(zero2_set)
popped = zero2_set.pop()
print(zero2_set)
print(popped)
zero2_set.clear()
print(zero2_set)
union_set = {1, 2, 3}.union({13, 2})
union2_set = {1, 2, 3} | {13, 2}
print(union_set)

intersection_set = {1, 2, 3}.intersection({13, 2})
intersection2_set = {1, 2, 3} & {13, 2}
print(intersection_set)

difference_set = {1, 2, 3}.difference({3, 4, 5})
difference2_set = {1, 2, 3} - {3, 4, 5}
print(difference_set)
print(difference2_set)

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

print(fs1 | fs2)
print(fs1 & fs2)
print(fs1 - fs2)
print(fs1 ^ fs2)
print(fs1 <= fs2)
print(fs1 >= fs2)

d = {
    frozenset([1, 2, 3]): "value1",
    frozenset([4, 5, 6]): "value2",
}

"""
на вход города
сгруппировать по уникальным наборам букв без учета регистра и повторений
возврщаем словарь по ключу из букв города
значение список городов с таким же набором букв
"""
cities = ['Moskov', 'Tokyo', 'Kyoto']
"""
{
    frozenset({'m', 's', 'c', 'o', 'w'}): ['Moskov'],
    frozenset({'t', 'k', 'y', 'o'}): ['Tokyo', 'Kyoto']
}
"""