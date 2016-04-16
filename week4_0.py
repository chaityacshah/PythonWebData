import urllib
from bs4 import BeautifulSoup
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
s = 0

for tag in tags:
    x = int(tag.contents[0])
    s += x
print s
