f = open(r"C:\\Git Stuff\AOC\DayOne\aocDayOneData.txt")

def addThreeFromArray(start, array):
    return (int(array[start]) + int(array[start+1]) + int(array[start+2]))

array = []
for line in f:
    tempLine = line
    tempLine = tempLine.replace('\n','')
    array.append(tempLine)

arrayThree = []

for i in range(0, len(array)-2):
    arrayThree.append(addThreeFromArray(i, array))

count = 0
previous = None
for line in arrayThree:
    if previous == None:
        previous = line
    else:
        if previous < line:
            count += 1

    previous = line

print(count)