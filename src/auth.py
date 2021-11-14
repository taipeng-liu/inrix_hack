import requests
import datetime
import json

APPID = "ygyscoqrxa"
APPKEY = "mUCJkmhAUu3JDAw2YjnWc8JmlOZzJhF85TSmA177"
HASHKEY = 'eWd5c2NvcXJ4YXxtVUNKa21oQVV1M0pEQXcyWWpuV2M4Sm1sT1p6SmhGODVUU21BMTc3'

tokenUrl = "https://api.iq.inrix.com/auth/v1/appToken?appId={}&hashToken={}"

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