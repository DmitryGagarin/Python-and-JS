# Составьте функцию season_events(number_of_month, year), которая принимает номер месяца вашего рождения (число) и год
# и сохраняет в текстовый файл “wiki.txt” на диске в той же папке где код, следующее:
# «Вы родились в <НАЗВАНИЕ_МЕСЯЦА> в <Year> году. <ОПИСАНИЕ_СОБЫТИЙ>».
# В качестве ОПИСАНИЯ_СОБЫТИЙ можно взять 5 первых (или случайных) названий статей из русскоязычной википедии
# со страницы по категории этого месяца и года: например ноябрь 1999 https://ru.wikipedia.org/wiki/Категория:Ноябрь_1999_Года
# используйте библиотеку requests
# для поиска статей можно искать в html тексте страницы ссылки по подстроке “<a href=\"/wiki” и далее брать из ссылки title

# TODO: make normal deleting
# TODO: make links by these strings
# TODO: make a loop for a deleting trash
# TODO: make a condition for an inserting month

import calendar # to transform number of month to its name
import random

from googletrans import * # to translate english to russian
from bs4 import *
import urllib.parse
import requests

language = "Russian"

year = int(input("Insert year when you were born"))
year = str(year)
month = int(input("Insert number of month when you were born"))
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

    unnecessary_values = [nameOfArticle[0],nameOfArticle[1], nameOfArticle[2], nameOfArticle[3], nameOfArticle[4], nameOfArticle[5],
                          nameOfArticle[6],nameOfArticle[10],nameOfArticle[14],nameOfArticle[18],nameOfArticle[22],nameOfArticle[26],
                          nameOfArticle[7],nameOfArticle[11],nameOfArticle[15],nameOfArticle[19],nameOfArticle[23],nameOfArticle[27],
                          nameOfArticle[8],nameOfArticle[12],nameOfArticle[16],nameOfArticle[20],nameOfArticle[24],nameOfArticle[28],
                          nameOfArticle[9],nameOfArticle[13],nameOfArticle[17],nameOfArticle[21],nameOfArticle[25],nameOfArticle[29],
                          nameOfArticle[30],nameOfArticle[34],nameOfArticle[38],nameOfArticle[42],nameOfArticle[46],nameOfArticle[49],
                          nameOfArticle[31],nameOfArticle[35],nameOfArticle[39],nameOfArticle[43],nameOfArticle[47],nameOfArticle[50],
                          nameOfArticle[32],nameOfArticle[36],nameOfArticle[40],nameOfArticle[44],nameOfArticle[48],nameOfArticle[51],
                          nameOfArticle[33],nameOfArticle[37],nameOfArticle[41],nameOfArticle[45],nameOfArticle[52],nameOfArticle[53],
                          nameOfArticle[54],nameOfArticle[55]]

    for value in unnecessary_values:
        nameOfArticle.remove(value)

    finalList = []
    for i in range (1,6):
        index = random.randint(1,30)
        finalList.append(nameOfArticle[index])

    for line in finalList:
        file.write(line + "\n")

season_events(month,year)