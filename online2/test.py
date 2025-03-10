list1 = [1, 2, 3, 4, 5]
list2 = list(range(1, 6))

list3 = []
for i in range(1, 6):
    list3.append(i)

list4 = [i for i in range(1, 6)]

list5 = list(i for i in range(1, 6))

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

list6 = [i for i in range(1, 60) if i % 2 == 0]
list7 = [i for i in range(1, 60) if i % 2 == 0 if i % 7 == 0]

list8 = [i if i % 2 == 0 else None for i in range(1, 60)]


list9 = [[i + j for i in range(5)] for j in range(5)]
print(list9)
