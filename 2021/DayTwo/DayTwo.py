f = open(r"C:\\Git Stuff\advent-of-code\DayTwo\dayTwoInput.txt")

x = 0 #horiz
y = 0 #depth
aim = 0 #aim
number = 0

for line in f:
    line = line.replace('\n','')
    number = [int(s) for s in line.split() if s.isdigit()]
    print(number, x, y)
    if "forward" in line:
        x = x + number[0]
        y = y + (number[0] * aim)
    elif "down" in line:
        aim = aim + number[0]
    elif "up" in line:
        aim = aim - number[0]
    print(line)

print(x, y, aim)