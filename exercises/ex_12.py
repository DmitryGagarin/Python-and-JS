#Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
#Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

def sum_range(start, end):
    if start > end:
        #start = end ; end = start
        start, end = end, start
    else:
        start, end = start, end
    print(sum(range(start, end+1)))


start = int(input("Insert start number"))
end = int(input("Insert end number"))

sum_range(start, end)
