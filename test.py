N = int(input())
M = int(input())
x = int(input())
y = int(input())
short = min(N, M)
long = max(N, M)

short2 = min(short - x, short - (short - x))
long2 = min(long - y, long - (long - y))

result = min(short2, long2)

print(result)