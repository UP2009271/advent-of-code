def floodfill(nineArr, x, y):
    global count
    if nineArr[x][y] == 0:
        nineArr[x][y] = 5
        #recursively call floodfill on all surrounding cells:
        if x > 0:
            floodfill(nineArr,x-1,y)
            count += 1
        if x < len(nineArr) - 1:
            floodfill(nineArr,x+1,y)
            count += 1
        if y > 0:
            floodfill(nineArr,x,y-1)
            count += 1
        if y < len(nineArr):
            floodfill(nineArr,x,y+1)
            count += 1

import numpy as np

array = []

with open("C:/Git Stuff/advent-of-code/DayNine/DayNineInput.txt") as f:
    for s in f:
        s = s.rstrip('\n')
        for k in s:
            array.append(int(k))
arraynp = np.reshape(array, (-1, 10))
nineDetect = np.zeros([5, 10])

for y in range(5):
    for x in range(10):
        if arraynp[y][x] == 9:
            nineDetect[y][x] = 9

print(nineDetect)
total = 0
for y in range(5):
    count = 0
    countt = 0
    for x in range(10):
        temp = nineDetect
        floodfill(nineDetect, y, x)
        if temp  nineDetect:
            print(changed)
            countt += 1
    print(count)
    total += count

print(nineDetect)
print(count)
print(countt)
print(total)