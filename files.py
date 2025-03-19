reg = -1
nat = []
amount = 0

with open('txts/region.txt', 'w') as file:
    lines = file.readlines()
    print(lines)

with open('txts/nation.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

with open('txts/customer.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

print(amount)
