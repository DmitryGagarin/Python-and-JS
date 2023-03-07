import json
from datetime import *

path = '/Users/dmitryfatsievich/Desktop/education/IT/semester 2/Fatsievich_Dmitry/exercises/Json/text.json'

with open(path,'r') as f:
    text = json.load(f)

dates = []

for i in range (4):
    dates.append(text[i]['birthday'])
    
date_str = dates[0]
date_object0 = datetime.strptime(date_str, '%d/%m/%Y').date()

date_str = dates[1]
date_object1 = datetime.strptime(date_str, '%d/%m/%Y').date()

date_str = dates[2]
date_object2 = datetime.strptime(date_str, '%d.%m.%Y').date()

date_str = dates[3]
date_object3 = datetime.strptime(date_str, '%Y-%d-%m').date()

today = date.today()

print("------------------")
print("вместо дней должны быть года")

print("Age of first: " , (today - date_object0)/365)
print("Age of second: ", (today - date_object1)/365)
print("Age of third: " ,(today - date_object2)/365)
print("Age of fourth: " , (today - date_object3)/365)

