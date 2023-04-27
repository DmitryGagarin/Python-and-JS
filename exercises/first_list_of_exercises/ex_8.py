#Алиса недавно узнала на уроке экономики, что рынок находится в равновесии, когда предложение равно спросу.
# У Алисы есть рыночные данные для
#N моментов времени в виде двух целочисленных массивов S и D. Где в массиве S спрос, а в D предложение. 
# определите количество моментов времени, когда рынок находился в равновесии (спрос равен предложению).
import random

#то есть надо определить сколько раз элементы одного массива рааны элементам другого
#возьмем 9 промежутков времени

S = []
D = []
coincidence = 0
N = []

for i in range(1,5):
    data1 = random.randint(1, 10)
    data2 = random.randint(1, 10)
    S.append(data1)
    D.append(data2)

for element in S:
    if element in D:
        N.append(element)
        coincidence += 1

print(D)
print(S)
print("Number of moments when the market is on balance is ", coincidence)