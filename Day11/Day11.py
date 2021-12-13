array = []
toAdd = []

with open("C:/Git Stuff/advent-of-code/Day11/input.txt") as f:
    for s in f:
        toAdd = []
        s = s.rstrip()
        for char in s:
            toAdd.append(int(char))
        array.append(toAdd)

def flash(array, x, y):
    global counter
    counter += 1
    array[y][x] = -1000
    for j in [-1, 0, 1]:
        for i in [-1, 0, 1]:
            if 0<=y+j<=9 and 0<=x+i<=9:
                array[j+y][i+x] += 1
                if array[y+j][x+i] > 0:
                    if array[y+j][i+x] >= 10:
                        flash(array, x+i, y+j)

def turn(array):
    for y in range(len(array)):
        for x in range(len(array[y])):
            array[y][x] += 1
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] == 10:
                flash(array, x, y)
    setZero(array)

def setZero(array):
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] < 0:
                array[y][x] = 0
counter = 0

for i in range(100):
    turn(array)

print(counter)