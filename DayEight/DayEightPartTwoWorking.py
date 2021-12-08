import itertools

digits = {
        0: 'abcefg',
        1: 'cf',
        2: 'acdeg',
        3: 'acdfg',
        4: 'bcdf',
        5: 'abdfg',
        6: 'abdefg',
        7: 'acf',
        8: 'abcdefg',
        9: 'abcdfg',
}

with open("C:/Git Stuff/advent-of-code/DayEight/DayEightInput.txt") as f:
    for line in f:
        before, after = line.split('|')
        before = before.split()
        after = after.split()

val = 0

returnString = ''

for perm in itertools.permutations(list(range(0, 9))):
    canExit = True
    dict = {}
    for i in range(0, 7):
        dict[chr(97+i)] = chr((97+perm[i]))
    for i in before:
        permString = ''
        for j in i:
            permString += dict[j]
        permString = ''.join(sorted(permString))
        if permString not in digits.values():
            canExit = False
    if canExit:
        break

for word in after:
    permString = ''
    for letter in word:
#appends numerical value of a word to a string which is printed after finishing line
        permString += dict[letter]
    permString = ''.join(sorted(permString))
    i = 0
    for k,v in digits.items():
        if v == permString:
            i = k
    returnString += str(i)
    val += int(returnString)

print(val)