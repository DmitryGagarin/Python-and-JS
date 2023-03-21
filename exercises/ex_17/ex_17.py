# Составьте функцию season_events(number_of_month, year), которая принимает номер месяца вашего рождения (число) и год
# и сохраняет в текстовый файл “wiki.txt” на диске в той же папке где код, следующее:
# «Вы родились в <НАЗВАНИЕ_МЕСЯЦА> в <Year> году. <ОПИСАНИЕ_СОБЫТИЙ>».
# В качестве ОПИСАНИЯ_СОБЫТИЙ можно взять 5 первых (или случайных) названий статей из русскоязычной википедии
# со страницы по категории этого месяца и года: например ноябрь 1999 https://ru.wikipedia.org/wiki/Категория:Ноябрь_1999_Года
# используйте библиотеку requests
# для поиска статей можно искать в html тексте страницы ссылки по подстроке “<a href=\"/wiki” и далее брать из ссылки title
import calendar
import googletrans
from googletrans import *

language = "Russian"

year = int(input("Insert year when you were born"))
month = int(input("Insert number of month when you were born"))
monthString = calendar.month_name[month]

translator = Translator()
monthRus = translator.translate(monthString, src = 'en', dest = language)

monthRus = str(monthRus.text)

articles = []

def season_events(number_of_month, number_of_year):
    print("You were born in", monthString, "in ", year, ". At that month wikipedia wrote this articles: ", articles)
    url = 'https://ru.wikipedia.org/wiki/Категория:' + monthRus + "_" + str(year) + '_года'
    print(url)

print(season_events(month, year))