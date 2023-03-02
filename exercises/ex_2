#Напишите программу, которая создает два списка чисел, (случайной длины от 50 до 100), 
#(заполняя списки случайными числами от 0 до 9999). 
#И выводит все элементы первого, которых нет во втором.
import random

firstList = []
secondList = []
finalList = []

for i in range(random.randrange(50,101)):
    firstList.append(random.randrange(0,10000))
    secondList.append(random.randrange(0,10000))

#count(x) - считает кол-во элементов x, которые встречаются в другом списке
for j in firstList:
    if secondList.count(j) == 0:
        finalList.append(j)

if len(firstList) == len(finalList):
    print("First list has only unique variables")


print(finalList)

    



