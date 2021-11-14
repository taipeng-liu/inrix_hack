import requests
import json
import urllib.parse
import datetime
APPID = "ygyscoqrxa"
APPKEY = "mUCJkmhAUu3JDAw2YjnWc8JmlOZzJhF85TSmA177"
HASHKEY = 'eWd5c2NvcXJ4YXxtVUNKa21oQVV1M0pEQXcyWWpuV2M4Sm1sT1p6SmhGODVUU21BMTc3'
locationUrl = "https://nominatim.openstreetmap.org/search/'{}'?format=json"
tokenUrl = "https://api.iq.inrix.com/auth/v1/appToken?appId={}&hashToken={}"
offStreetUrl = "https://api.iq.inrix.com/lots/v3?point={}%7C{}&radius={}"
onStreetUrl = "https://api.iq.inrix.com/blocks/v3?point={}%7C{}&radius={}"

class Point:
    def __init__(self, address):
        addressResponse = requests.get(locationUrl.format(urllib.parse.quote(address))).json()
        self.latitude = addressResponse[0]["lat"]
        self.longitude = addressResponse[0]["lon"]
        print(self.latitude, self.longitude)

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

def getParkingLots(point, radius, token, parkOffStreet=True):
    head = {
        'Authorization': ' '.join(['Bearer', token])
    }
    url = offStreetUrl if parkOffStreet else onStreetUrl
    response = requests.get(url.format(point.latitude, point.longitude, radius), headers=head)
    response_text = response.text
    with open('response.json', 'w') as f:
        f.write(response_text)

def main(destAddr=None, radius=0):
    if not destAddr:
        return
    destPoint = Point(destAddr)
    token = getToken()
    # print(token)
    getParkingLots(destPoint, radius, token, parkOffStreet=True)
    


if __name__ == '__main__':
    address = "74-98 Duncan St, San Francisco, CA 94110"
    main(destAddr=address, radius=150)