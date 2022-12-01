array = []

with open("C:/Git Stuff/advent-of-code/Day10/Day10Input.txt") as f:
    for s in f:
        toAdd = []
        s = s.rstrip()
        for char in s:
            toAdd.append(char)
        array.append(toAdd)

def isStart(chr):
    if chr not in ['{','<','(','[']:
        return False
    return True

def isEnd(chr):
    if chr not in ['}','>',')',']']:
        return False
    return True

def getOther(chr):
    startChr = ['{','<','(','[']
    endChr = ['}','>',')',']']
    if chr in startChr:
        return endChr[startChr.index(chr)]
    else:
        return startChr[endChr.index(chr)]

endingToAdd = []

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
                endingToAdd.append(ending[0])
                break

sum = 0
for i in endingToAdd:
    if i == ')':
        sum += 3
    elif i == ']':
        sum += 57
    elif i == '}':
        sum += 1197
    else:
        sum += 25137

print(sum)