tup = (1, 2, 4, '123')
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
    print(i)
