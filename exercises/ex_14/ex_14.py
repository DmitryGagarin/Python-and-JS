#компьютер будет загадывать случайное число от 1 до 100. Пользователь пытается угадать число.
# После каждой неудачной попытки, компьютер будет давать подсказку: задуманное число больше или меньше вашего ответа.
# Если число угадано, надо записать количество попыток и имя пользователя в текстовый файл ‘game.txt’ в той же папке где и игра.
import random

num = random.randrange(1,101)
attempts = []

print("I have a number and you have to guess it")
username = input("Firstly input your name: ")
print("Make your anticipation by inserting a number from 1 to 100")

less = "My number is less"
more = "My number is more"
equals = "You win!"
def guess():
    user_num = int(input())
    win = 0
    while win < 1:
        if user_num < num:
            print(more)
            attempts.append(user_num)
            guess()
            break
        if user_num > num:
            print(less)
            attempts.append(user_num)
            guess()
            break
        if user_num == num:
            print(equals)
            win += 1
            break

guess()

file = open("game.txt", "a+")
file.write("Username is:" + username + '      ')
file.write("Number of attempts are: " + str(len(attempts)) + "\n")
file.close()

with open('game.txt', 'r') as f:
    last_line = f.readlines()[-1]

print("Your name and number of attempts below 👇")
print(last_line)






