# files won't auto update in side nav
# check using correct input data

def load_file(path):
    lines = []
    with open(path, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

arr = (load_file('input.txt'))

count = 0
secondCount = 0

for line in arr:
    first = line.split(",")[0]
    second = line.split(",")[1]
    first_low = int(first.split("-")[0])
    first_high = int(first.split("-")[1])
    second_low = int(second.split("-")[0])
    second_high = int(second.split("-")[1])

    if ((first_low <= second_low) & (first_high >= second_high)) | ((second_low <= first_low) & (second_high >= first_high)):
        count += 1

    for i in range(first_low, first_high + 1):
        if i in range(second_low, second_high + 1):
            secondCount += 1
            break

print(count) #P1 answer

print(secondCount) #P2 answer
