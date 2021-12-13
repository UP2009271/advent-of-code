import numpy as np
from copy import deepcopy

zeroArray = []
array = []

with open("C:/Git Stuff/advent-of-code/DayNine/DayNineInput.txt") as f:
    for s in f:
        s = s.rstrip('\n')
        toAdd = []
        for k in s:
            toAdd.append(int(k))
        array.append(toAdd)

def floodFill(fillArray, y, x):
    if fillArray[y][x] == 9:
        return True
    if fillArray[y][x] == 0:
        fillArray[y][x] = 5
        for j in [-1, 1]:
            try:
                if not(y+j > 5 or y+j < 0):
                    floodFill(fillArray, y+j, x)
            except:
                pass
            try:
                if not(x+j > 10 or x+j < 0):
                    floodFill(fillArray, y, x+j)
            except:
                pass

def printArray(parsed):
    for y in parsed:
        print(y)

def checkDiffs(one, two):
    count = 0
    for y in range(5):
        for x in range(10):
            if one[y][x] != two[y][x]:
                count += 1
    return count

for y in range(5):
    for x in range(10):
        if array[y][x] != 9:
            array[y][x] = 0

zeroArray = deepcopy(array)

tempList = []

for y in range(5):
    for x in range(10):
        floodFill(zeroArray,y, x)
        tempList.append(checkDiffs(zeroArray, array))

unique = []

for i in tempList:
    if i not in unique:
        unique.append(i)

print(unique)
tempList = []
tempList.append(unique[0])
for i in range(len(unique)-1):
    tempList.append(abs(unique[i]-unique[i+1]))

print(tempList)