import numpy as np

array = []


with open("C:/Git Stuff/advent-of-code/DaySix/DaySixInput.txt") as f:
    line = f.readline()
    line = line.replace(',','')
    line = line.rstrip('\n')
    for i in line:
        if i.isdigit():
            array.append(int(i))
            print(i)


for j in range(0, 18):
    count = 0
    for count in range(len(array)):
        k = array[count]
        if k == 0:
            array.append(8)
            array[count] = 6
        else:
            array[count] -= 1
    print(j, array)

print(array)

print(len(array))

