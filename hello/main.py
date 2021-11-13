# This is a sample Python script.
import string
import json
import requests
import urllib.parse
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    address = "573 San Jose Avenue, San Francisco, CA 94110"
    locationUrl = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    addressResponse = requests.get(locationUrl).json()
    latitude = addressResponse[0]["lat"]
    longitude = addressResponse[0]["lon"]
    offUrl = "https://api.iq.inrix.com/lots/v3?point=" + latitude + "%7C" + longitude + "&radius=150"
    onUrl = "https://api.iq.inrix.com/blocks/v3?point=" + latitude + "%7C" + longitude + "&radius=50"
    payload = {}
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6InBxN2pncWFrN2IiLCJ0b2tlbiI6eyJpdiI6IjRkMmRjZTZmZGVhNDJkZDExMDM3NjQ1NDYxNGY5MjVhIiwiY29udGVudCI6ImZlNDM4OGViYjMwZTc5ZWM1NzNjNmYzOWI2NDBhMzM0ZDFmNjkyMTExNTBhYjAzZjY2OTU5NTM5NGQ0ZDYwMWVlNWNkYjkzNTVhNzFlNDI1ZGFjYTA3OWViOWRjOGY0NjAxODU5ZDZkNmMzMTNjZTMxOTQwNGE5OGUzZjU5NmNhZDY2MDg2MTk3MjAyYWM1MGNmYjYxYjEzNzZjNWI5OTdiMWMxOWY1NWNhODc0ZjAwZWVmMWM3NjhlZmEyMmYwNDAyYjA0YWY1ODc1MzU0ZTNiZmRkOGZiMTJlNzQyYmI3OTNkMzJmMDJlMDU4MjFhMGMyZGYxNWJkNjlhOWIyMDJmOWEyYjAxMDdhYTU1NjM3MWM1ZjgxMjFjMWI4YjBhZjAyNDJiYWNjNTNlYWM0ZjUxMzhiYTMyNzhjYjExODViMDcyYWZiM2NlMTYzNzg4YTBhNTg5MWJhNTZlZDE1YjFkZTNlMGJmNDUyYmI5NGE2MWRhMmUxMTJiNTUzODc4MzY0NWU1ZTYwY2U1MDQyM2NmNmVkODhjZjUzM2EyZTQxM2FjMmJkY2QyZGM3ODdlYjA5ZWFlYzg4NTE5M2RhOTk2YzZiMzgzNTgzZDYxZjBjMWZmOTA5NTk2NWNlN2Y3M2Q2Nzc1NDhiNWM1ZTBmMjViYzY0NzdlOThlNjE3ZDc1ZDZlZjBkZDUyN2UxODU5YzJlYmMyNmI4NDQwMzIwMzI1MjQ1ZWMzODU4ZTIxMDhiYjc0MDdiOGFiYjVjOWRhNTA4YWM1MjFiZTZkMTVlMmUwOGQwNmQxYTM2ZDYxYjAxMjkzZDc2ODBhYjAxYTJkZTdiNjBiODkwZjEzNmQzZWNjYzliNDEzYzkxNjg5YWQyYWU0NzVkIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI0ZDJkY2U2ZmRlYTQyZGQxMTAzNzY0NTQ2MTRmOTI1YSIsImNvbnRlbnQiOiJkZjE3OTFkNjgzNjQyOWZkNmMwMzZmMDZiNzQ4ZDM2Y2ZjZGJiZTJkMTYxZGI4NjMzZDkzOTA0MzMxNTY0NzEwZmZjMTgzNDMzMTQ1ZDUwMTgxYzgwNmEwIn0sImp0aSI6ImE2OGU4NDQ2LTkyNDktNDcyZS1iNmY1LTk0NTY4YTgzMDkwZSIsImlhdCI6MTYzNjgzNDE4NywiZXhwIjoxNjM2ODM3Nzg2fQ.uFRR0Lt370XkNZtnc4DalwGR_2nmOJOI3StunxFZVoQ'
    }
    offResponse = requests.request("GET", offUrl, headers=headers, data=payload)
    onResponse = requests.request("GET", onUrl, headers=headers, data=payload)

    print(offResponse.text)
    print(onResponse.text)





