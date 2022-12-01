f = open(r"C:\\Git Stuff\AOC\DayOne\aocDayOneData.txt")

count = 0
previous = None
for line in f:
    if previous == None:
        previous = line
    else:
        if previous < line:
            count += 1
    previous = line

print(count)