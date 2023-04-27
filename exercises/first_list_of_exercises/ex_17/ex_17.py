# Составьте функцию season_events(number_of_month, year), которая принимает номер месяца вашего рождения (число) и год
# и сохраняет в текстовый файл “wiki.txt” на диске в той же папке где код, следующее:
# «Вы родились в <НАЗВАНИЕ_МЕСЯЦА> в <Year> году. <ОПИСАНИЕ_СОБЫТИЙ>».
# В качестве ОПИСАНИЯ_СОБЫТИЙ можно взять 5 первых (или случайных) названий статей из русскоязычной википедии
# со страницы по категории этого месяца и года: например ноябрь 1999 https://ru.wikipedia.org/wiki/Категория:Ноябрь_1999_Года
# используйте библиотеку requests
# для поиска статей можно искать в html тексте страницы ссылки по подстроке “<a href=\"/wiki” и далее брать из ссылки title


import calendar # to transform number of month to its name
import random

from googletrans import * # to translate english to russian
from bs4 import *
import urllib.parse
import requests

print("ЕСЛИ ВЫЛЕЗАЕТ КРАСНАЯ ОШИБКА, ВВЕДИТЕ ДРУГУЮ ДАТУ ПОТОМ, ХЗ КАК ЭТО ФИКСИТЬ :)")

language = "Russian"

year = int(input("Insert the year when you were born"))
year = str(year)
month = int(input("Insert number of the month when you were born"))
monthString = calendar.month_name[month]

translator = Translator()
monthRus = translator.translate(monthString, src = 'en', dest = language)

monthRus = str(monthRus.text)

def season_events(number_of_month, number_of_year):
    # create list of articles
    nameOfArticle = []

    # wiki link and transform it
    urlConst = 'https://ru.wikipedia.org/wiki/Категория:'
    url = urlConst + monthRus + "_" + year + '_года'
    transformedUrl = urllib.parse.quote_plus(url,safe=':/')

    # get request
    response = requests.get(transformedUrl)
    bs = BeautifulSoup(response.text, "lxml")
    articles = bs.find_all("div")

    for article in articles:
        titles = article.find_all("a")

        for title in titles:
            nameOfArticle.append(title.get('title'))

    # work with files
    file = open('wiki.txt', 'w+')
    file.write("In " + str(year) + ", in " + monthString + " these five random articles were written \n")

    for i in nameOfArticle:
        nameOfArticle.remove(i)

    # sorting of list by its symbols and words to get only names of articles
    finalList = []
    number = 0
    while number < 5:
        index = random.randint(1,len(nameOfArticle))
        if nameOfArticle[index].__contains__("Категория") or nameOfArticle[index].__contains__("Category") or nameOfArticle[index].__contains__("Категоризация" or
            nameOfArticle[index].__contains__("Скачать") or nameOfArticle[index].__contains__("j") or nameOfArticle[index].__contains__("i") or nameOfArticle[index].__contains__("t") or
            nameOfArticle[index].__contains__("h") or nameOfArticle[index].__contains__("r") or nameOfArticle[index].__contains__("v") or nameOfArticle[index].__contains__("Править") or
            nameOfArticle[index].__contains__("فوریه") or nameOfArticle[index].__contains__("[g]")):
            nameOfArticle.remove(nameOfArticle[index])
        else:
            finalList.append(nameOfArticle[index])
            nameOfArticle.remove(nameOfArticle[index])
            number += 1

    for line in finalList:
        file.write(line + "\n")

season_events(month,year)