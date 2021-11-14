import requests
import json
import urllib.parse
import datetime
import folium 
APPID = "ygyscoqrxa"
APPKEY = "mUCJkmhAUu3JDAw2YjnWc8JmlOZzJhF85TSmA177"
HASHKEY = 'eWd5c2NvcXJ4YXxtVUNKa21oQVV1M0pEQXcyWWpuV2M4Sm1sT1p6SmhGODVUU21BMTc3'
locationUrl = "https://nominatim.openstreetmap.org/search/'{}'?format=json"
tokenUrl = "https://api.iq.inrix.com/auth/v1/appToken?appId={}&hashToken={}"
offStreetUrl = "https://api.iq.inrix.com/lots/v3?point={}%7C{}&radius={}"
onStreetUrl = "https://api.iq.inrix.com/blocks/v3?point={}%7C{}&radius={}"
routeUrl = "https://api.iq.inrix.com/findRoute?wp_1={}%2C{}&wp_2={}%2C{}&format=json"
class Point:
    def __init__(self, address):
        addressResponse = requests.get(locationUrl.format(urllib.parse.quote(address))).json()
        self.latitude = addressResponse[0]["lat"]
        self.longitude = addressResponse[0]["lon"]
        print(self.latitude, self.longitude)

class outStreetStruct:
   def __init__(self, street, city, state, postal, country, struct_ratesList):
       self.address = street + " " + city + " " + state + " " + postal + " " + country
       self.outStreetList = struct_ratesList

class inStreetStruct:
   def __init__(self, name, rates):
       self.name = name
       self.ratesList = rates


def getToken():
    with open('.cache', 'w+') as f:
        cache = f.read()
        if len(cache) > 0:
            parsed_cache = json.loads(cache)
            token = parsed_cache['result']['token']
            expiry = parsed_cache['result']['expiry']
            expiry_time=datetime.datetime.strptime(expiry[:-1],"%Y-%m-%dT%H:%M:%S.%f")
            curr_time = datetime.datetime.utcnow()
            if expiry_time > curr_time:
                # Not expired
                return token
        response = requests.get(tokenUrl.format(APPID, HASHKEY))
        resp_text = response.text
        f.write(resp_text)
        parsed_resp_text = json.loads(resp_text)
        token = parsed_resp_text['result']['token']
        return token


def parse(jsonObj, parkOffStreet):
    onStreetList = []
    offStreetList = []
    if parkOffStreet:
        for street in jsonObj['result']:
            v1 = outStreetStruct(street['buildingAddress']['street'], street['buildingAddress']['city'],
                                 street['buildingAddress']['state'], street['buildingAddress']['postal'],
                                 street['buildingAddress']['country'], street['rateCard'])
            offStreetList.append(v1)
    else:
        for streets in jsonObj['result']:
            v2 = inStreetStruct(streets['name'], streets['rateCards'])
            onStreetList.append(v2)
    print(onStreetList)
    for offStreet in offStreetList:
        print(offStreet.address, offStreet.outStreetList)

def getParkingLots(point, radius, token, parkOffStreet=True):
    head = {
        'Authorization': ' '.join(['Bearer', token])
    }
    url = offStreetUrl if parkOffStreet else onStreetUrl
    response = requests.get(url.format(point.latitude, point.longitude, radius), headers=head)
    response_text = response.text
    with open('parking_info.json', 'w') as f:
        f.write(response_text)
    parse(json.loads(response_text), parkOffStreet)

# return routes between departure point to destination point
def getRoutes(departPoint, destPoint, token):
    head = {
        'Authorization': ' '.join(['Bearer', token])
    }
    response = requests.get(routeUrl.format(departPoint.latitude, departPoint.longitude, destPoint.latitude, destPoint.longitude), headers=head)
    response_text = response.text
    with open('routes.json', 'w') as f:
        f.write(response_text)



def main(departAddr=None, startAddr=None, destAddr=None, radius=0):
    if not destAddr:
        return
    token = getToken()
    destPoint = Point(destAddr)
    if departAddr:
        departPoint = Point(departAddr)
        getRoutes(departPoint, destPoint, token)
    # m = folium.Map(location=[destPoint.latitude, destPoint.longitude])
    # m.save("map.html")
    getParkingLots(destPoint, radius, token, parkOffStreet=True)
    


if __name__ == '__main__':
    departAddr = "1600 Guerrero St, San Francisco, CA 94110"
    destAddr = "74-98 Duncan St, San Francisco, CA 94110"
    main(departAddr=departAddr, destAddr=destAddr, radius=150)
    