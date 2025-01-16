list1 = [1, 2, 3, 4, 5]
for i in range(len(list1)):
    if i % 2 == 0 and i != 0:
        print(list1[i])
list1 = [list1[i] for i in range(len(list1))
         if i % 2 == 0 and i != 0]
print(list1)