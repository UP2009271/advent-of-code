import numpy as np

with open("C:/Git Stuff/advent-of-code/DayFour/DayFourPicks.txt") as f:
    line = f.readline()
    inputs = [int(s) for s in line.split(',') if s.isdigit()]

f = open(r"C:/Git Stuff/advent-of-code/DayFour/DayFourInput.txt")
table = []
tempTable = []
counter = 0
for line in f:
    line = line.rstrip('\n')
    tempTable.append([int(s) for s in line.split(' ') if s.isdigit()])
    counter += 1
    if counter == 5:
        table.append(tempTable)
        tempTable = []
        counter = 0

toCheck = np.array(table)
safe = toCheck
matched = []

iteration = 0
lastX = 0
xCounter = 0
for x in inputs:
    tempLastX = x
    toCheck[toCheck == x] = -1
    tableNumber = 0
    for counter in range(0, 5):
        for x in toCheck[..., counter]:
            if np.all(x==-1):
                if tableNumber//5 not in matched:
                    matched.append(tableNumber//5)
                    lastX = tempLastX
                    print(toCheck[counter])
                    xCounter = counter
            tableNumber += 1
    tableNumber = 0
    for counter in range(100): # how many tables (lines / 5), 500 lines in data
        for y in toCheck[counter, ...]:
            if np.all(y==-1):
                if tableNumber//5 not in matched:
                    matched.append(tableNumber//5)
                    lastX = tempLastX
                    print(toCheck[counter])
            tableNumber += 1
    iteration += 1

print(table[xCounter-1])
print(matched)
print(lastX)