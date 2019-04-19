from bs4 import BeautifulSoup
from urllib.request import urlopen

url = input('Google search URL:     ')
html = urlopen(url)
sh = input('Would you like to see general information?     ')
if sh == 'Yes' or 'yes' or 'YES':
    print(html)
print('TITLE')
print('IMAGES')
print('LINKS')
print('TEXT')
print('TABLES')
ch = input('What would you like to change? Options above. Please enter in lowercase:      ')
if ch == 'title':
    titles = html.find_all('h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7')
    conf = input('There are ' + str(len(titles)) + 'titles, would you like to continue')
    if conf == 'yes' or 'Yes' or 'YES':
        breakpoint()

soup = BeautifulSoup(html, 'lxml')
type(soup)