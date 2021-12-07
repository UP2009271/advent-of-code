import numpy as np

array = []

with open("C:/Git Stuff/advent-of-code/DaySeven/DaySevenInput.txt") as f:
    line = f.readline()
    array = [int(s) for s in line.split(',') if s.isdigit()]

print(array)
lowestCount = 0
lowestNumber = 0
lowestArray = []

#sets each number in the lists length to brute force it
for i in range(len(array)-1):
    count = 0
    for j in array:
        count += abs(j - i)
    lowestArray.append(count)

lowestArray.sort()
lowestArray.reverse()

print(array)
print(count)
print(lowestArray)
