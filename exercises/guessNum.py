
import random

num = random.randrange(101)

print("I have a number and you have to guess it")
print("Make your anticipation by inserting a number from 1 to 100")

less = "My number is less"
more = "My number is more"
equals = "You win!"    

def guess():
    attempt = 0
    user_num = int(input())
    while user_win <= 0:
        if user_num < num:
            print(more)
            attempt += 1 
            guess()
            break
        if user_num > num:
            print(less) 
            attempt += 1
            guess()
            break
        if user_num == num:
            print(equals)
            user_win += 1
        
guess()
