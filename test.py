import math


numbers = []
while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)
n = len(numbers)
s = sum(numbers) / n
sum_of_squares = sum((x - s) ** 2 for x in numbers)
sigma = math.sqrt(sum_of_squares / (n - 1))
print(sigma)