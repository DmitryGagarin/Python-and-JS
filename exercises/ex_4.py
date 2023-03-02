#Дана последовательность случайных чисел, от 0 до 9999, случайной длины (от 5 до 100) и положительное число Х, больше нуля. 
#Напишите функцию magic(), принимающую эти аргументы, и выясните, можно ли разделить сумму чисел 
#последовательности на число  Х без остатка. 
#В качестве ответа возвращается bool, если можно то True иначе False.

#есть случайные числа от 0 до 9999
#последовательность состоит минимум из 5 максимум из 100 чисел
#есть случайный положительный Х
#может ли сумма последовательности разделиться на Х без остатка?

import random

list = []
number = 0
result = False

def magic(number, x):
    print("Sum of list = " + str(number))
    print("x = " + str(x))
    if number % x == 0:
        result = True
        print("Number can be divided into x without the remainder of the division")

    else:
        result = False
        print("Number can't be divided into x without the remainder of the division")
    print(result)

for i in range(random.randrange(5,101)): #случайная длина последовательности
    list.append(random.randrange(0,10000)) #добавляем в лист случайный элемент
    
for element in list:
    number = number + element
    
x = random.randrange(number)

magic(number, x)
