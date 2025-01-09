N = int(input())
cards = set()
for _ in range(N - 1):
    cards.add(int(input()))
print(sum(set(list(range(1, N + 1))) - cards))