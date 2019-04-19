
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('URL(FULL):    ')
find = input('Any HTML tags to be found?    ')
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)
title = soup.title
print(title)
if find != 'no' or 'No' or 'NO':
    print(soup.find_all(find))
    print('There are ' + str(len(soup.find_all(find))))
    if len(soup.find_all(find)) == 0:
        print('There are none')





