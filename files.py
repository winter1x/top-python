reg = -1
nat = []
with open('txts/region.txt', 'r') as file:
    lines = file.readlines()
    to_find = 'ASIA'
    # content = file.read()
    for line in lines:
        if to_find in map(lambda s : s.strip(), line.split('|')):
            reg = line[0]
            break
    """for line in lines:
        if line.find(to_find) > 0:
            reg2 = line[0]
            break"""
with open('txts/nation.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if reg in line.split('|')[2]:
            nat.append(line.split('|')[0])
print(nat)
with open('txts/customer.txt', 'r') as file:
    lines = file.readlines()
