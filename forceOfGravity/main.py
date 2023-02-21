
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
    space(1)
    for i in listOfPlanets:
        print(i)

def choosingPlanet():
    print ("")
    print("Choose a planet (satellite/star) by inputing a number from 1 to 9")
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
                massAndRadious = {
                    "1" : [190350000000, 3.285 * math.pow(10,23)],
                    "2" : [212010000000, 4.867 * math.pow(10,24)],
                    "3" : [158790000000, 6.39 * math.pow(10,23)],
                    "4" : [849940000000, 1.898 * math.pow(10,27)],
                    "5" : [1.6153 * math.pow(10,12), 5.683 * math.pow(10,26)],
                    "6" : [2.9768 * math.pow(10,12), 8.681 * math.pow(10,25)],
                    "7" : [4.6088 * math.pow(10,12), 1.02 * math.pow(10,26)],
                    "8" : [384400000, 7.348 * math.pow(10,22)],
                    "9" : [1.4792 * math.pow(10,11), 1.989 * math.pow(10,30)],
                }
                
                if num == 1:
                    radious = massAndRadious["1"][0]
                    secondMass = massAndRadious["1"][1]
                if num == 2:
                    radious = massAndRadious["2"][0]
                    secondMass = massAndRadious["2"][1]
                if num == 3:
                    radious = massAndRadious["3"][0]
                    secondMass = massAndRadious["3"][1]
                if num == 4:
                    radious = massAndRadious["4"][0]
                    secondMass = massAndRadious["4"][1]
                if num == 5:
                    radious = massAndRadious["5"][0]
                    secondMass = massAndRadious["5"][1]
                if num == 6:
                    radious = massAndRadious["6"][0]
                    secondMass = massAndRadious["6"][1]
                if num == 7:
                    radious = massAndRadious["7"][0]
                    secondMass = massAndRadious["7"][1]
                if num == 8:
                    radious = massAndRadious["8"][0]
                    secondMass = massAndRadious["8"][1]
                if num == 9:
                    radious = massAndRadious["9"][0]
                    secondMass = massAndRadious["9"][1]

                force = str(((g * earthMass *  secondMass) / math.pow(radious,2)))

                print ("Force of gravity between the Earth and " + myPlanet + " equals: " + force + " N")
        
        counting()
    
space(15)
lines()
showList()
choosingPlanet()
space(1)
lines()

