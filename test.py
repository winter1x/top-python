P = int(input())
X = int(input())
Y = int(input())
X = X + Y * 0.01
X = X * (1 + P * 0.01)
print(int(X), int(X * 100 % 100))