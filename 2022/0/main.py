# files won't auto update in side nav
# check using correct input data

def main(path):
    totals = []
    largest = 0
    running = 0
    with open(path, 'r') as f:
        for line in f:
            if line == "\n":
                totals.append(running)
                running = 0
            else:
                running += int(line.strip())
                if running > largest:
                    largest = running
    return totals

arr = main("input.txt")
arr.sort()

# P1 solution is last num in array
print(arr)

# P2 solution is last output
print(arr[-1]+arr[-2]+arr[-3])
