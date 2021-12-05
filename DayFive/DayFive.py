import numpy as np

buildArray = []


with open("C:/Git Stuff/advent-of-code/DayFive/DayFiveInput.txt") as f:
    line = f.readline()
    for line in f:
        line = line.rstrip('\n')
        line = line.replace("->",'')
        line = line.split()
        buildArray.append(line)
        print(line)

array = np.array(buildArray)
#get largest values in array



largestX = 0
largestY = 0
for i in array:
    x, y = i[0].split(',')
    x1, y1 = i[1].split(',')
    x = int(x)
    y = int(y)
    x1 = int(x1)
    y1 = int(y1)
    if largestX < x:
        largestX = x
    elif largestX < x1:
        largestX = x1
    if largestY < y:
        largestY = y
    elif largestY < y1:
        largestY = y1

diagram = np.zeros(shape=(largestX+1, largestY+1))

for i in array:
    x1, y1 = i[0].split(',')
    x2, y2 = i[1].split(',')
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    if x1 == x2:
        if y1 > y2:
            smallest = y2
        else:
            smallest = y1
        for j in range(abs(y2-y1)+1):
            diagram[x1][smallest] += 1
            smallest += 1
    elif y1 == y2:
        if x1 > x2:
            smallest = x2
        else:
            smallest = x1
        for j in range(abs(x2-x1)+1):
            diagram[smallest][y1] += 1
            smallest += 1

print((2 <= diagram).sum())
