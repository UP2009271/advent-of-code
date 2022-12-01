import numpy as np

array = []

with open("C:/Git Stuff/advent-of-code/DayNine/DayNineInput.txt") as f:
    for s in f:
        s = s.rstrip('\n')
        for k in s:
            array.append(int(k))

def floodFill(fillArray, x, y):
    global count
    if fillArray[x][y] == 0:
        fillArray[x][y] = 5
        try:
            if x > 0:
                count += 1
                floodFill(fillArray, x-1, y)
            if x < len(fillArray[y]-1):
                count += 1
                floodFill(fillArray, x+1, y)
            if y > 0:
                count += 1
                floodFill(fillArray, x, y-1)
            if y < len(fillArray[y]-1):
                count += 1
                floodFill(fillArray, x, y+1)
        except:
            count += 1
            pass
        return count
    return count

count = 0

arraynp = np.reshape(array, (-1, 10))
nineDetect = np.zeros([5, 10])

for y in range(5):
    for x in range(10):
        if arraynp[y][x] == 9:
            nineDetect[y][x] = 9

for y in range(5):
    for x in range(10):
        floodFill(nineDetect, y, x)

print(nineDetect)
print(count)