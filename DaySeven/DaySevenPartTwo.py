import numpy as np

#returns the sum of all the numbers less than or equal to n
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact += num
    return fact

array = []

with open("C:/Git Stuff/advent-of-code/DaySeven/DaySevenInput.txt") as f:
    line = f.readline()
    array = [int(s) for s in line.split(',') if s.isdigit()]

print(array)
lowestCount = 0
lowestNumber = 0
lowestArray = []

for i in range(len(array)-1):
    count = 0
    jumpTracker = 0
    temp = 0
    for j in array:
        #there was a special case with function where if i == j, it would count it as 1
        #so added this clause to quickly catch it because didnt want to change the def
        if i != j:
            temp = abs(j-i)
            jumpTracker += abs(factorial(temp))
        else:
            jumpTracker += 0
    count += jumpTracker
    print(i, count)
    lowestArray.append(count)

lowestArray.sort()
lowestArray.reverse()

print(array)
print(count)
print(lowestArray)
#answers is the final item in list