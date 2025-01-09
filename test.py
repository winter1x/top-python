N = int(input())
M = int(input())
x = int(input())
y = int(input())
result = min(x, y)
short = result
long = result
if y == result:
    short = min(N, M) - y
if x == result and max(N, M) - x < short:
    long = max(N, M) - x
if max(N, M) / 2 < x:
    long = max(N, M) - x
if long < 0:
    long += 100000
if short < 0:
    short += 100000
result = min(result, long, short)

print(result)