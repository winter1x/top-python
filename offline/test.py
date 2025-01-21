# https://buildin.ai/youit/share/817c2f62-dab0-4b06-8b2d-85037305a8a4?code=LHHZV7
def min_recolor(n, k, s):
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + (1 if s[i] == 'W' else 0)
    
    min_white = float('inf')
    
    for i in range(n - k + 1):
        white_count = prefix[i + k] - prefix[i]
        min_white = min(min_white, white_count)
        if min_white == 0:
            break
    
    return min_white

"""
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    result = min_recolor(n, k, s)
    print(result)
"""

"""
t = int(input())
test_cases = []
results = []

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    test_cases.append((n, k, s))

for case in test_cases:
    n, k, s = case
    result = min_recolor(n, k, s)
    results.append(result)

for res in results:
    print(res)
"""

print(min_recolor(5, 3, "BBWBW"))
print(min_recolor(5, 5, "BBWBW"))
print(min_recolor(5, 1, "BBWBW"))
print(min_recolor(1, 1, "W"))
