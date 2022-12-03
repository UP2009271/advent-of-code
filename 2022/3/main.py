# files won't auto update in side nav
# check using correct input data

def load_file(path):
    lines = []
    with open(path, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert_let_to_numb(letter):
    alphabet = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alphabet.index(letter)

def most_common(lst):
    return max(set(lst), key=lst.count)

packs = load_file("input.txt")

seen = []
for pack in packs:
    seenTemp = []
    for i in (pack[:len(pack)//2]):
        seenTemp.append(i)
    for i in (pack[len(pack)//2:]):
        if i in seenTemp:
            seen.append(i)
            break

running = 0
for let in seen:
    running += convert_let_to_numb(let)

print(running) #P1 answer

seen = []
for i in range(0, len(packs), 3):
    setA = set(packs[i])
    setB = set(packs[i+1])
    setC = set(packs[i+2])
    if (setA & setB & setC):
        seen.append(most_common(list(setA & setB & setC)))

running = 0
for i in seen:
    running += convert_let_to_numb(i)

print(running) #P2 answer
