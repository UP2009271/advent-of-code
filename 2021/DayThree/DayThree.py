gamma = ""
epsilon = ""

for x in range (0, 5):
    f = open(r"C:\\Git Stuff\advent-of-code\DayThree\dayThreeInput.txt")
    zeroCount = 0
    oneCount = 0
    kek = 0
    bob = 0
    for line in f:
        line = line.replace('\n','')
        if "0" in line[x]:
            zeroCount += 1
        else:
            oneCount += 1
    if zeroCount < oneCount:
        kek = 1
    else:
        kek = 0
    if (kek == 0):
        bob = 1
    else:
        bob = 0
    print(x, kek, bob)
    gamma += str(kek)
    epsilon += str(bob)
    f.close()

print(int(gamma,2), int(epsilon,2)