
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
    num = str(input())
    correctNum = 0
    
    while correctNum <= 0:
        if (int(num) < 1 or int(num) > len(listOfPlanets)):
            print("Input correct number!")
            choosingPlanet()
            break
        else:
            correctNum += 1
            myPlanet = listOfPlanets[int(num)-1]
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
                
                radious = massAndRadious[num][0]
                secondMass = massAndRadious[num][1]
                
                force = str(((g * earthMass *  secondMass) / math.pow(radious,2)))

                print ("Force of gravity between the Earth and " + myPlanet + " equals: " + force + " N")
        
        counting()
    
space(15)
lines()
showList()
choosingPlanet()
space(1)
lines()

