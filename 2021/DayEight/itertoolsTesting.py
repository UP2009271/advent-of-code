import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f']

count = 0
for perm in itertools.permutations(letters):
    temp = []
    print(perm)
    count += 1

print(count)