from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import calendar
import httplib2

language = "Russian"

year = int(input("Insert year when you were born"))
year = str(year)
month = int(input("Insert number of month when you were born"))
monthString = calendar.month_name[month]
monthString = str(monthString)

print(monthString)
print(type(monthString))

urlConst = "https://en.wikipedia.org/wiki/Special:Purge/Category:"

url = urlConst + monthString + "_" + year

http = httplib2.Http()

response, content = http.request(url)

links = []

for link in BeautifulSoup(content).find_all("a", href = True):
    links.append(link['href'])

for link in links:
    print(links)
