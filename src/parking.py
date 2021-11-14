import requests
import json
import urllib.parse

locationUrl = "https://nominatim.openstreetmap.org/search/'{}'?format=json"

offStreetUrl = "https://api.iq.inrix.com/lots/v3?point={}%7C{}&radius={}"
onStreetUrl = "https://api.iq.inrix.com/blocks/v3?point={}%7C{}&radius={}"
routeUrl = "https://api.iq.inrix.com/findRoute?wp_1={}%2C{}&wp_2={}%2C{}&format=json"


class Point:
    # For the bay area, latitude 33, longitude -122
    def __init__(self, latitude=None, longitude=None, address=None):
        if latitude and longitude:
            self.latitude = latitude
            self.longitude = longitude
            self.address = None
            return
        elif address:
            addressResponse = requests.get(locationUrl.format(urllib.parse.quote(address))).json()
            self.address = address
            self.latitude = addressResponse[0]["lat"]
            self.longitude = addressResponse[0]["lon"]
            return
        self.latitude = None
        self.longitude = None
        self.address = None

class prkgLot:
    def __init__(self, attrs):
        self.id = attrs['id']
        self.type = attrs['type']
        self.constIndex = attrs['costIndex']
        self.hrs = attrs['hrs']
        self.rateCard = attrs['rateCard']
        self.peps = attrs['peps']
        self.pmtTypes = attrs['pmtTypes']
        self.name = attrs['name']
        self.note = attrs['note']
        self.point = Point(latitude=attrs['point']['coordinates'][1], longitude=attrs['point']['coordinates'][0])
        self.navigationAddress = attrs['navigationAddress']
        self.distance = attrs['distance']
        self.buildingAddress = attrs['buildingAddress'] 
    def getBuildingAddress(self):
        return ' '.join([self.buildingAddress["street"],self.buildingAddress["city"],self.buildingAddress["state"],self.buildingAddress["postal"]])

    def getRateCard(self):
        return '/n'.join(self.rateCard)

class prkgBlock:
   def __init__(self, attrs):
       self.name = attrs['name']
       self.probability = attrs['name']
       self.reservations = attrs['reservations']
       self.segments = attrs['segments']

def parsePrkgLot(result):
    return [prkgLot(lotAttrs) for lotAttrs in result]

def parsePrkgBlock(result):
    return [prkgBlock(blockAttrs) for blockAttrs in result]

# return json response
def reqPrkg(destPoint, radius, token, prkOffStreet=True, save_to=None):
    head = {
        'Authorization': ' '.join(['Bearer', token])
    }
    url = offStreetUrl if prkOffStreet else onStreetUrl
    response = requests.get(url.format(destPoint.latitude, destPoint.longitude, radius), headers=head)
    response_text = response.text
    if save_to:
        with open(save_to, 'w') as f:
            f.write(response_text)
    return json.loads(response_text)

# return json response
def reqRoutes(departPoint, destPoint, token, save_to=None):
    head = {
        'Authorization': ' '.join(['Bearer', token])
    }
    response = requests.get(routeUrl.format(departPoint.latitude, departPoint.longitude, destPoint.latitude, destPoint.longitude), headers=head)
    response_text = response.text
    if save_to:
        with open(save_to, 'w') as f:
            f.write(response_text)
    return json.loads(response_text)

