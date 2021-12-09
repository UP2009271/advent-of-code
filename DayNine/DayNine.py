import numpy as np

array = []

def adjIsSmallerUp(grid, x, y):
    if y+1 != 100:
        if grid[x][y]<grid[x][y+1]:
            print(grid[x][y], "largest up")
            return True
        else:
            return False
    return True
def adjIsSmallerDown(grid, x, y):
    if y-1 != -1:
        if grid[x][y]<grid[x][y-1]:
            print(grid[x][y], "largest down")
            return True
        else:
            return False
    return True
def adjIsSmallerLeft(grid, x, y):
    if x+1 != 100:
        if grid[x][y]<grid[x+1][y]:
            print(grid[x][y], "largest left", grid[x+1][y])
            return True
        else:
            return False
    return True
def adjIsSmallerRight(grid, x, y):
    if x-1 != -1:
        if grid[x][y]<grid[x-1][y]:
            print(grid[x][y], "largest right")
            return True
        else:
            return False
    return True


def adjIsSmaller(grid, x, y):
    if adjIsSmallerUp(grid, x ,y):
        if adjIsSmallerDown(grid, x ,y):
            if adjIsSmallerLeft(grid, x ,y):
                if adjIsSmallerRight(grid, x ,y):
                    return True
    print("false")
    return False

with open("C:/Git Stuff/advent-of-code/DayNine/DayNineInput.txt") as f:
    for s in f:
        s = s.rstrip('\n')
        for k in s:
            array.append(int(k))

arraynp = np.reshape(array, (-1, 100))
smallestArr = []

for y in range(100): # #of columns
    for x in range(100): # # of rows
        print(y,x)
        isSmallest = adjIsSmaller(arraynp, y, x)
        if isSmallest:
            smallestArr.append(arraynp[y][x])

ans = 0

for i in smallestArr:
    ans += i + 1

print(ans)