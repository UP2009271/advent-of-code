def transform(sn, size):
    return pow(sn, size, 20201227)

k1, k2 = 5099500, 7648211

l1 = 0
while transform(7, l1) != k1:
    l1 += 1

l2 = 0
while transform(7, l2) != k2:
    l2 += 1

print(l1, l2, transform(k1, l2))