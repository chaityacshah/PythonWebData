import json
import urllib

url = raw_input()
uh = urllib.urlopen(url)
data = uh.read()

info = json.loads(data)
s = 0
for item in info['comments']:
    x = int(item['count'])
    s += x

print s
