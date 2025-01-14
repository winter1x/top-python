N = int(input())
dictionary = {}
for _ in range(N):
    word = input().strip()
    lowercase_word = word.lower()
    if lowercase_word not in dictionary:
        dictionary[lowercase_word] = set()
    dictionary[lowercase_word].add(word)
text = input().strip().split()
errors = 0
for word in text:
    lowercase_word = word.lower()
    if lowercase_word in dictionary:
        if word not in dictionary[lowercase_word]:
            errors += 1
    else:
        uppercase_count = sum(1 for char in word if char.isupper())
        if uppercase_count != 1:
            errors += 1
print(errors)