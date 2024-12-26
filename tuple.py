"""tup = (1, 2, 4, '123')
print(tup)
print(type(tup).__name__)
tup2 = ([], 1, 2, 4, '123')
print(tup)
tup2[0].append(1)

print(tup * 2)

print(tup[1:3])

print(tup + tup2)
print(2 in tup)
print(len(tup))
for i in tup:
    print(i)"""

"""to_search = input()
data = ("banana", "apple", "bananamango", "mango", "strawberry-banana")
amount = 0
for e in data:
    if e == to_search or e.find(to_search) > 0:
        amount += 1
print(amount)"""
data = ("qwe", "qwer", "qwert", "qwerty", "qwer", "qwert", "qwerty", "qwerty")
title = input()
to_replace = input()
result = tuple(map(lambda x : to_replace if x == title else x, data))
print(result)