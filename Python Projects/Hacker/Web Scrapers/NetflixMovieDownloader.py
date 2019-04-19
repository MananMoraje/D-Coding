from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://netflix.com/watch/' + input('http://netflix.com/watch/: ')
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)
divs = soup.find_all('div')
for div in divs:
    classes = div.get('class')
    print(classes)

