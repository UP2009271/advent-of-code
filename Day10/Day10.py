array = []

with open("C:/Git Stuff/advent-of-code/Day10/Day10Input.txt") as f:
    for s in f:
        toAdd = []
        s = s.rstrip()
        for char in s:
            toAdd.append(char)
        array.append(toAdd)

def getOther(chr):
    startChr = ['{','<','(','[']
    endChr = ['}','>',')',']']
    if chr in startChr:
        return endChr[startChr.index(chr)]
    else:
        return startChr[endChr.index(chr)]

def getScore(charr):
    if charr == '(':
        return 1
    elif charr == '[':
        return 2
    elif charr == '{':
        return 3
    else:
        return 4

corruptLines = []
incompleteLines = []
arrayEnding = []

for column in range(len(array)):
    start = []
    ending = []
    for i in array[column]:
        if isStart(i):
            start.append(i)
        else:
            ending.append(i)
        if len(ending) != 0:
            if start[-1] == getOther(ending[0]):
                start.pop()
                ending.pop(0)
            else:
                corruptLines.append(column)
                break
    start.reverse()
    arrayEnding.append(start)

for i in range(100): # no of lines
    if (i not in corruptLines):
        incompleteLines.append(i)

total = []
for i in incompleteLines:
    sum = 0
    for j in arrayEnding[i]:
        sum *= 5
        sum += getScore(j)
    total.append(sum)

total.sort()
middle = int((len(total) - 1) / 2)
print(total[middle])