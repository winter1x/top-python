tuple1 = (4, 1, 2, 7, 5)
tuple2 = (3, 1, 5, 6, 7)
tuple3 = (5, 1, 7, 11, 9)

common_elements = set(tuple1) & set(tuple2) & set(tuple3)

set1, set2, set3 = set(tuple1), set(tuple2), set(tuple3)

unique1 = set1 - (set2 | set3)
unique2 = set2 - (set1 | set3)
unique3 = set3 - (set1 | set2)

result = tuple(common_elements)

result1 = tuple(unique1)
result2 = tuple(unique2)
result3 = tuple(unique3)

result4 = tuple(tuple1[i] for i in range(len(tuple1)) if tuple1[i] == tuple2[i] == tuple3[i])

print("Элементы, которые есть во всех кортежах: ", result)
print("\nУникальные элементы первого кортежа:", result1)
print("Уникальные элементы второго кортежа:", result2)
print("Уникальные элементы третьего кортежа:", result3)
print("\nЭлементы, совпадающие во всех кортежах на одинаковых позициях:", result4)