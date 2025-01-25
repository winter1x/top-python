"""Условие
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...)."""
# elements = input().split()
lst = list(map(int, input().split()))
for i in range(0, len(lst), 2):
    print(lst[i])

"""Условие
Выведите все четные элементы списка. 
При этом используйте цикл for, перебирающий элементы списка, а не их индексы!"""
# elements = input().split()
lst = list(map(int, input().split()))
for e in lst:
    if e % 2 == 0:
        print(e)
"""
Дан список чисел. 
Выведите все элементы списка, которые больше предыдущего элемента."""
lst = list(map(int, input().split()))
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        print(lst[i])
"""
Дан список чисел. 
Выведите значение наибольшего элемента в списке, 
а затем индекс этого элемента в списке. 
Если наибольших элементов несколько, выведите индекс первого из них."""
lst = list(map(int, input().split()))
max_value = max(lst)
max_index = lst.index(max_value)
print(max_value)
print(max_index)
"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
Если элементов нечетное число, то последний элемент остается на своем месте."""
lst = list(map(int, input().split()))
for i in range(0, len(lst) - 1, 2):
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
for i in lst:
    print(i, end=' ')
"""
В списке все элементы различны. 
Поменяйте местами минимальный и максимальный элемент этого списка."""
lst = list(map(int, input().split()))
max_index = lst.index(max(lst))
min_index = lst.index(min(lst))
lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
for i in lst:
    print(i, end=' ')
"""Дан список чисел. 
Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, 
которую необходимо посчитать."""
lst = list(map(int, input().split()))
count = 0
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            count += 1
print(count)