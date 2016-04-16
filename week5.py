import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location: ')
uh = urllib.urlopen(address)
data = uh.read()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')

ans = 0

for i in lst:
    ans += int(i.find('count').text)

print ans
