array = []

with open("C:/Git Stuff/advent-of-code/DayEight/DayEightInput.txt") as f:
    for s in f:
        temp = s.split('|')
        w = (temp[1])
        print(w)
        for k in w.split(' '):
            k = k.strip()
            print(k)
            array.append(len(k))

count = 0
count += array.count(2)
count += array.count(3)
count += array.count(7)
count += array.count(4)
print(count)
