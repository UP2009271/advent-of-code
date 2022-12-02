# files won"t auto update in side nav
# check using correct input data

def load_file(path):
    lines = []
    with open(path, "r") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def getPlay(them):
    if them == "A" or them == "X":
        return "R"
    elif them == "B" or them == "Y":
        return "P"
    elif them == "C" or them == "Z":
        return "S"

def getWin(them, me):
    if me == them:
        return "T"
    elif me == "R" and them == "P":
        return "L"
    elif me == "P" and them == "S":
        return "L"
    elif me == "S" and them == "R":
        return "L"
    else:
        return "W"

def rigged(them, me):
    if me == "R":
        if them == "R":
            return "S"
        elif them == "P":
            return "R"
        elif them == "S":
            return "P"
    elif me == "P":
        if them == "R":
            return "R"
        elif them == "P":
            return "P"
        elif them == "S":
            return "S"
    else:
        if them == "R":
            return "P"
        elif them == "P":
            return "S"
        elif them == "S":
            return "R"

def rockPaperScissorsScore(them, me):
    score = 0
    # me = rigged(them, me) # toggle comment for P1 / P2
    if getWin(them, me) == "W":
        score += 6
    elif getWin(them, me) == "L":
        score += 0
    elif getWin(them, me) == "T":
        score += 3
    if me == "R":
        score += 1
    elif me == "P":
        score += 2
    else:
        score += 3
    return score

inp = load_file("input.txt")
score = 0
for i in range(len(inp)):
    them, me = inp[i].split(" ")
    them = getPlay(them)
    me = getPlay(me)
    score += rockPaperScissorsScore(them, me)

print(score)
