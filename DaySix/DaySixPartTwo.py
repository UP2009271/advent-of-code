import numpy as np

array = []


with open("C:/Git Stuff/advent-of-code/DaySix/DaySixInput.txt") as f:
    line = f.readline()
    line = line.replace(',','')
    line = line.rstrip('\n')
    for i in line:
        if i.isdigit():
            array.append(int(i))

#             0  1  2  3  4  5  6  7, 8
countArray = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#days until birth

for i in array:
    countArray[i] += 1

print(countArray)

for j in range(0, 256):
    temp = 0
    if countArray[0] != 0:
        temp = countArray[0]
        countArray[0] = 0
    tempVal = countArray[0]
    for k in range(8):
        countArray[k] = countArray[k+1]
    countArray[8] = tempVal
    print(countArray)
    countArray[6] += temp
    countArray[8] += temp

print(countArray)
count = 0

for i in countArray:
    count += i
print(count)
