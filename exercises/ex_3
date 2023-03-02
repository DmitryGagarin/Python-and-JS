#с теми же списками чисел, нужно вернуть список, который состоит из элементов, общих для этих двух списков.

import random

firstList = []
secondList = []
finalList = []

for i in range(random.randrange(50,101)):
    firstList.append(random.randrange(0,10000))
    secondList.append(random.randrange(0,10000))

#count(x) - считает кол-во элементов x, которые встречаются в другом списке
for j in firstList:
    if secondList.count(j) != 0:
        finalList.append(j)

if len(finalList) == 0:
    print("There are not any variables that are similar in to different lists")
else:
    print("Similar variables are: " + str(finalList))
    




