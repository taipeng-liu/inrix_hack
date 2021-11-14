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
    response = requests.get(url.format(point.longitude, point.latitude, radius), headers=head)
    response_text = response.text
    with open('response.json', 'w') as f:
        f.write(response_text)

def main(destAddr=None, radius=0):
    if not destAddr:
        return
    destPoint = Point(destAddr)
    token = getToken()
    print(token)
    # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6InlneXNjb3FyeGEiLCJ0b2tlbiI6eyJpdiI6ImRhZjc0NDJjMjdmYmUzMmI1ZmQ5NzJmZjcyODRmODAwIiwiY29udGVudCI6ImI2YzZiZWNhNjAwZWJmNTNkN2E4YzBmN2RkYzI1MzczZWVlZDA3MGJiOTEyZjY0YWVlNWJmZWE3ZTY1NTIwZjNlMTAwMTliYzkzMGExMzI0OGE2NTQ2YTk2MmNmMTM4MTI5YzMxNWU2ZmYxZTc0ZTVlNzM5MzgzYWJmNTIzNjRlNDBmNTkwNzZhZDU2NjRlOGQ4NGZlZmM1YjA4NTc2YjE4YWRmNTkyMTdjNjU0ZDYxZjNkMGExNTVlZmU0OGI3YmVkYzlhZWQ3NDc3YzU1ZjlmZWU0M2U2MTUxNTg0MjFhZTJmMjk0ZWNmMzI4MzU5MjI1YmM3YzI0MGQwYTRhMmYzYTJmYjM5ODQxZDkzODg5MjM3Zjc2Zjg3YzUzZjAyOGFlMDMwMzNmYWM0NjY0MzhhMzNmNjJhZmYwMjRjOWNjNjA2MGIwOGFjZjY3MzRhOTdkNzU1OWFmNWFhMDEwN2NjMmI4OTJkODE1ZTNjZGQ1ZmJhMTkxYjI4MzMzNTgwZGZlZDM1YjM2MjUzODBmMWFhOTVhODUwMzVhNTNjM2Q0NTUyMDgzNmIyMGRlYmJmMTcyOWU1NjkyYmQyNGIyZjg5NTRjZGE5ODM2ODExNzU4NDZjNGQzOGJmNzg4ZWVlODY1N2ZkZDU5MDc3YjllOTNiMDk5MDM2ZjViODE2M2FjM2IxMzVhY2QyMjI0ZjgyNWMyYWUxZmE1ZDNiY2U3YWQ5ZDJlMmMzMTIwNGYwNDQ1N2NjY2I0NDEwODE1NmRiMGQ0NzY1MjBiOGI0NmYxNDQ2YTJmM2YwNWFjNjAwM2IzNjEyOGE2MjY2MGFiOTNjOGZkMGQwZjUzNjg5MWRmZWNiM2FjNWYwYTkzODAwMjNlODI5MTJjIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJkYWY3NDQyYzI3ZmJlMzJiNWZkOTcyZmY3Mjg0ZjgwMCIsImNvbnRlbnQiOiJlNmVmYjBlZDZjMmM4ZTA4ZGNhY2Y5ZjdkYWUxNWUyYmQ2YjEzNDRmYjkzMGMyMWJlNjVhZjNlOWZhNTMyOGY5ODAwMjY3YzBkZjM1M2ExOGE2NmY1Zjk3In0sImp0aSI6ImQwYmU5ZDc5LTlmNDAtNGNjMS1hOTRmLWE4ZmFmMjY0MzdlOSIsImlhdCI6MTYzNjg0Nzg2MSwiZXhwIjoxNjM2ODUxNDYxfQ.njzLY9NF-lYpo5kdkaUsoZhjUp2a1pX6nEiimJZfBVI'
    getParkingLots(destPoint, radius, token, parkOffStreet=True)
    


if __name__ == '__main__':
    address = "573 San Jose Avenue, San Francisco, CA 94110"
    main(destAddr=address, radius=150)