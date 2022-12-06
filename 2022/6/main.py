# files won't auto update in side nav
# check using correct input data

def load_file(path):
    lines = []
    with open(path, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def isUnique(str):
    seen = []
    for i in str:
        if i in seen:
            return False
        seen.append(i)
    return True

arr = load_file("input.txt")

for count in range(0, len(arr[0])):
    lastFour = arr[0][count:count+4]
    lastFourteen = arr[0][count:count+14]

    # P1 Answer
    if isUnique(lastFour):
        print(count+4)
        break

    # P2 Answer
    # if isUnique(lastFourteen):
    #     print(count+14)
    #     break
