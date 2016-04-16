import urllib
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = raw_input('Enter location: ')

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})

uh = urllib.urlopen(url)
data = uh.read()
js = json.loads(str(data))

for item in js['results']:
    print item['place_id']
