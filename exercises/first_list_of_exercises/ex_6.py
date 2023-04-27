# Алиса, Боб и Чарли хотят скинуться и купить подписку на Netflix.
# Однако Netfix позволяет использовать подписку только двум пользователям.
# Учитывая, что Алиса, Боб и Чарли имеют X, Y, Z денег соответственно и стоимость подписки на Netflix задана как COST денег.
# Напишите функцию, с определением кто может купить подписку (сумма каких двух чисел дает максимальное приближение к  COST).
# Известно, что X+Y+Z точно больше COST.

# подписку получит тот, чье значение (сумма троих - деньги двух) будет меньше
x = int(input("Insert Alice's money: "))
y = int(input("Insert Bob's money: "))
z = int(input("Insert Charlie's money: "))
COST = int(input("Insert Cost of subscription: "))


sum = x+y+z
list = []

def who():
    if sum - (x+y) < sum - (x+z) and sum - (x+y) < sum - (y+z):
        list.append("Alice")
        list.append("Bob")
    if sum - (x+z) < sum - (x+y) and sum - (x+z) < sum - (y+z):
        list.append("Alice")
        list.append("Charlie")
    else:
        list.append("Bob")
        list.append("Charlie")

    print(list)

who()
        

        



