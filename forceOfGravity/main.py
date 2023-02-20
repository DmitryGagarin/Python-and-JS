#F = G * m1 * m2 / R^2
#TODO сделать чтобы циферки сами рисовались
#TODO Красивый вывод циферов (без е)

import math

g = 6.6743 * math.pow(10,-11)
earthMass = 5.97600 * math.pow(10,24)  
listOfPlanets = ["(1) Mercury","(2) Venus","(3) Mars","(4) Jupiter","(5) Saturn","(6) Uranus","(7) Neptune","(8) Moon", "(9) Sun"]

def space(spaces):
    for i in range(spaces):
        print("")

def lines():
    print("_____________________________________")
    
def showList():
    for i in listOfPlanets:
        print(i)

def choosingPlanet():
    print ("")
    print("Choose a planet (satellite/star) by inputing a number from 1 to 8")
    num = int(input())
    correctNum = 0
    
    while correctNum <= 0:
        if (num < 1 or num > len(listOfPlanets)):
            print("Input correct number!")
            choosingPlanet()
            break
        else:
            correctNum += 1
            myPlanet = listOfPlanets[num-1]
            print("You chose: " + myPlanet)
            print("")
    
            def counting():
                if num == 1:
                    radious = 190350000000
                    secondMass = 3.285 * math.pow(10,23)
                if num == 2:
                    radious = 212010000000
                    secondMass = 4.867 * math.pow(10,24)
                if num == 3:
                    radious = 158790000000
                    secondMass = 6.39 * math.pow(10,23)
                if num == 4:
                    radious = 849940000000
                    secondMass = 1.898 * math.pow(10,27)
                if num == 5:
                    radious = 1.6153 * math.pow(10,12)
                    secondMass = 5.683 * math.pow(10,26)
                if num == 6:
                    radious = 2.9768 * math.pow(10,12)
                    secondMass = 8.681 * math.pow(10,25)
                if num == 7:
                    radious = 4.6088 * math.pow(10,12)
                    secondMass = 1.02 * math.pow(10,26)
                if num == 8:
                    radious = 384400000
                    secondMass = 7.348 * math.pow(10,22)
                if num == 9:
                    radious = 1.4792 * math.pow(10,11)
                    secondMass = 1.989 * math.pow(10,30)
    
                force = str(((g * earthMass *  secondMass) / math.pow(radious,2)))

                print ("Force of gravity between the Earth and " + myPlanet + " equals: " + force)
        
        counting()
    
space(15)
lines()
showList()
choosingPlanet()
space(1)
lines()

