from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import time
url = input('Google search URL:     ')
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)
all_image = soup.find_all('img')
src = []
j = 0
for image in all_image:
    src.append(image.get('src'))
while j != len(src):
    path = 'D:\Coding\Python Projects\Hacker\Web Scrapers\Images\ImageDownloader(' + str(j) + ').jpg'
    urllib.request.urlretrieve(src[j], path)
    j += 1
input('Press ENTER to exit  ')
#  ---------------------------------------------------------------------------------------------------------------------
#  =====================================================================================================================
#  ---------------------------------------------------------------------------------------------------------------------


