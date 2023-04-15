
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
            guess()
            break
        if userNum > num:
            print(less) 
            attempt += 1
            guess()
            break
        if userNum == num:
            print(equals)
            userWin += 1 
        
guess()
