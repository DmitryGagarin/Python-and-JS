#TODO make hints 

import random

num = random.randrange(101)

print("I have a number and you have to guess it")
print("Make your anticipation by inputing a number from 1 to 100")

less = "My number is less"
more = "My number is more"
equals = "You win!"    

def guess():
    attempt = 0
    userNum = int(input())
    userWin = 0
    while userWin <= 0:
        if userNum < num:
            print(more)
            attempt += 1 
            if attempt == 3:
                hints()
            guess()
            break
        if userNum > num:
            print(less) 
            attempt += 1
            if attempt == 3:
                hints()
            guess()
            break
        if userNum == num:
            print(equals)
            userWin += 1 
            
            def hints():
                if attempt == 3:
                    print("Do you want a hint? 1 - Yes; 2 - No")
                    decision = int(input())
                    if decision == 1:
                        if num % 5 == 0:
                            print("This number doesn't have the remainder of the division by 5")
                            guess()
                        if num % 2 == 0:
                            print("This is an even number")
                            guess()
                        if num % 3 == 0:
                            print("This number doesn't have the remainder of the division by 3")
                            guess()
                        else: 
                            print("This number is as weird as i can't help you D: ")
                            guess()
                    else:
                        print("Do what you want!!!")
                        guess()

        
guess()
