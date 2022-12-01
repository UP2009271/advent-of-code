array = []
digits = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}

numArray = ["cagedb", "ab", "gcdfa", "fbcad", "eafb", "cdfbe", "cdfgeb", "dab", "acedgfb", "cefadb"]
letterArray = ["a", "b", "c", "d", "e", "f", "g"]
comparisonArray = ["a", "b", "c", "d", "e", "f", "g"]
letters = ["a", "b", "c", "d", "e", "f", "g"]

letterArray = [0, 0, 0, 0, 0,0,0]

def notIn(s1, s2): #largest first
    chars = []
    for char in letters:
        if (char in s1) and (char not in s2):
            chars.append(char)
    return chars


with open("C:/Git Stuff/advent-of-code/DayEight/DayEightInput.txt") as f:
    for s in f:
        arrayCount = [0, 0 ,0 ,0 ,0 ,0 ,0]
        before, after = s.split('|')
        before = before.split(' ')
        after = after.split(' ')
        for w in before:
            if len(w) == 2:
                lenTwo = w
            if len(w) == 3:
                lenThree = w
            if len(w) == 4:
                lenFour = w
        letterArray[0] = ((notIn(lenThree, lenTwo)))[0]
        for w in before:
            for l in w:
                if l == 'a':
                    arrayCount[0] += 1
                if l == 'b':
                    arrayCount[1] += 1
                if l == 'c':
                    arrayCount[2] += 1
                if l == 'd':
                    arrayCount[3] += 1
                if l == 'e':
                    arrayCount[4] += 1
                if l == 'f':
                    arrayCount[5] += 1
                if l == 'g':
                    arrayCount[6] += 1
        set = True
        setOne = True
        for i in range(0, 7):
            if arrayCount[i] == 4:
                letterArray[4] = chr(97+i)
            if arrayCount[i] == 6:
                letterArray[1] = chr(97+i)
            if arrayCount[i] == 9:
                letterArray[5] = chr(97+i)
            #only wanna set these one time
            if set:
                if arrayCount[i] == 8:
                    for j in range(0, 7):
                        if arrayCount[j] == 8 and letterArray[j] == 0:
                            letterArray[2] = chr(97+i)
                            set = False
        print(letterArray, "ac")
        notUsed = []
        for i in range(len(comparisonArray)):
            if comparisonArray[i] not in letterArray:
                notUsed.append(comparisonArray[i])
        firstOne = ""
        lastOne = ""
        for i in range(len(notUsed)):
            print(notUsed, i, "nu")
            if notUsed[i] not in lenFour:
                print(notUsed[i], lenFour)
                lastOne = notUsed[i]
                firstOne = notUsed[0]

        for i in range(len(letterArray)):
            if letterArray[i] == 0 and firstOne != 0:
                letterArray[i] = firstOne
                firstOne = 0
            elif letterArray[i] == 0 and lastOne != 0:
                letterArray[i] = lastOne
                lastOne = 0

        print(arrayCount)
print(letterArray)