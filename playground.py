import requests
import json

class Point:
    def __init__(self, longitude, lattitude):
        self.longitude = longitude
        self.lattitude = lattitude

def getToken(appid, hashkey):
    response = requests.get("https://api.iq.inrix.com/auth/v1/appToken?appId={}&hashToken={}".format(appid, hashkey))
    resp_text = response.text
    parsed_resp_text = json.loads(resp_text)
    return parsed_resp_text['result']['token']

def getParkingLots(point, token):
    head = {
        'Authorization': ' '.join(['Bearer', token])
    }
    url = 'https://api.iq.inrix.com/lots/v3?point={}%7C{}&radius=150'.format(point.longitude, point.lattitude)
    response = requests.get(url, headers=head)
    response_text = response.text
    with open('response.json', 'w') as f:
        f.write(response_text)

APPID = "ygyscoqrxa"
APPKEY = "mUCJkmhAUu3JDAw2YjnWc8JmlOZzJhF85TSmA177"
HASHKEY = 'eWd5c2NvcXJ4YXxtVUNKa21oQVV1M0pEQXcyWWpuV2M4Sm1sT1p6SmhGODVUU21BMTc3'
TOKEN = getToken(APPID, HASHKEY)


# point = Point('37.74638779388551', '-122.42209196090698')
# getParkingLots(point, TOKEN)
