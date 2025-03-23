N = int(input())
keys = [0] + [int(input()) for _ in range(N)]
visited = [False] * (N + 1)
count = 0

for i in range(1, N + 1):
    if not visited[i]:
        path = set()
        current = i
        while current not in path and not visited[current]:
            path.add(current)
            visited[current] = True
            current = keys[current]
        if current in path:
            count += 1

print(count)
