gamma = ""
epsilon = ""

def removeFromArray(array, colu, number):
    for x in array:
        if x[colu]==[number]:
            array.remove(x)

def getToRemove(array, column):
    zCount = 0
    oCount = 0
    for y in array:
        if y[x] == "0":
            zCount += 1
        else:
            oCount += 1

    if zCount > oCount: #change to <= for
        return "0"
    else:
        return "1"

array = []

f = open(r"C:\\Git Stuff\advent-of-code\DayThree\dayThreeInput.txt")
for line in f:
    line = line.replace('\n','')
    array.append(line)
f.close()
print(array)

toRemove = 0

def sift(array, column):
    tempArray = array
    toRemove = getToRemove(array, column)

    for node in array[:]:
        if node[x] == toRemove:
            tempArray.remove(node)

    print(tempArray)
    return tempArray


for x in range (0, 12): #12
    array = sift(array, x)

print(int("100111110001",2)*int("000011100111",2))





print(array)
print(toRemove)
