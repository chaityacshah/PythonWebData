import urllib
from bs4 import BeautifulSoup
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
count = int(raw_input('Count'))
pos = int(raw_input('Position'))
# Retrieve all of the anchor tags

for k in range(count):
    tags = soup('a')
    i = 0
    for tag in tags:
        i += 1
        #print tag.get('href', None)
        if( i == pos ):
            print tag.contents[0]
            link = tag.get('href', None)
            print link
            html = urllib.urlopen(link).read()
            soup = BeautifulSoup(html)

print 'over'
