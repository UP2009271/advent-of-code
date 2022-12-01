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

iteration = 0
for x in inputs:
    print(x)
    toCheck[toCheck == x] = -1
    tableNumber = 0
    for counter in range(0, 5):
        for x in toCheck[..., counter]:
            if np.all(x==-1):
                print("found x")
                print(tableNumber, table[counter], iteration)
                exit()
            tableNumber += 1
    tableNumber = 0
    for counter in range(3): # how many tables (lines / 5), 500 lines in data
        for y in toCheck[counter, ...]:
            if np.all(y==-1):
                print("found y")
                print(tableNumber, table[counter], iteration)
                print(toCheck[counter])
                exit()
            tableNumber += 1
    iteration += 1

#if (toCheck[...,0]) all are x: where 0 is x iteratively
#or if  toCheck[0, ...] are all x: where 0 is y iteratively