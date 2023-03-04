#Напишите функцию search_substr(subst, st), которая принимает 2 строки и определяет, имеется ли подстрока subst в строке st. 
#В случае нахождения подстроки, возвращается фраза «Есть контакт!», а иначе «Мимо!». 
#Должно быть найдено совпадение независимо от регистра обеих строк.

subst = str(input("Введите любой текст: "))
st = str(input("Введите любой текст: "))

bigger = subst if subst > st else st
new = []

def search_substy(subst, st):
    for i in range(len(bigger)): #это проверка по одинаковому индексу
        if subst[i] == st[i]:
            new.append(subst[i])
        else: #если индексы одинаковых букв не равны
            for x in range(len(st)):
                if subst[i] == st[x]:
                    new.append(subst[i])
    
    print("Есть контакт, а именно: " + str(new))
search_substy(subst,st)
                
    
#Задача сильнее меня - нужно как то сделать, что никогда не выходило за рамки и было сообщение, что не найдено
