# https://buildin.ai/youit/share/817c2f62-dab0-4b06-8b2d-85037305a8a4?code=LHHZV7
from collections import deque


def min_recolor(n, k, s):

    if 'B' * k in s:
        return 0

    min_white = float('inf')
    white_count = 0
    dq = deque()

    for i in range(n):
        if s[i] == 'W':
            white_count += 1
            dq.append(i)

        if i >= k:
            if s[i - k] == 'W':
                white_count -= 1
                if dq and dq[0] == i - k:
                    dq.popleft()

        if i >= k - 1:
            min_white = min(min_white, white_count)
            if min_white == 0:
                break
    return min_white


print(min_recolor(5, 3, "BBWBW"))
print(min_recolor(5, 5, "BBWBW"))
print(min_recolor(5, 1, "BBWBW"))
print(min_recolor(1, 1, "W"))
