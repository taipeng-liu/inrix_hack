from src.parking import *
from src.drawer import Drawer
from src.auth import getToken

def main(departAddr=None, startAddr=None, destAddr=None, radius=0, parkOffStreet=True):
    if not destAddr:
        return
    token = getToken()
<<<<<<< HEAD
    destPoint = Point(address=destAddr)
    mapDrawer = Drawer(location=[destPoint.latitude, destPoint.longitude])
    
    # if departAddr:
    #     departPoint = Point(address=departAddr)
    #     response = reqRoutes(departPoint, destPoint, token)
=======
    print(token)
    # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6InlneXNjb3FyeGEiLCJ0b2tlbiI6eyJpdiI6ImRhZjc0NDJjMjdmYmUzMmI1ZmQ5NzJmZjcyODRmODAwIiwiY29udGVudCI6ImI2YzZiZWNhNjAwZWJmNTNkN2E4YzBmN2RkYzI1MzczZWVlZDA3MGJiOTEyZjY0YWVlNWJmZWE3ZTY1NTIwZjNlMTAwMTliYzkzMGExMzI0OGE2NTQ2YTk2MmNmMTM4MTI5YzMxNWU2ZmYxZTc0ZTVlNzM5MzgzYWJmNTIzNjRlNDBmNTkwNzZhZDU2NjRlOGQ4NGZlZmM1YjA4NTc2YjE4YWRmNTkyMTdjNjU0ZDYxZjNkMGExNTVlZmU0OGI3YmVkYzlhZWQ3NDc3YzU1ZjlmZWU0M2U2MTUxNTg0MjFhZTJmMjk0ZWNmMzI4MzU5MjI1YmM3YzI0MGQwYTRhMmYzYTJmYjM5ODQxZDkzODg5MjM3Zjc2Zjg3YzUzZjAyOGFlMDMwMzNmYWM0NjY0MzhhMzNmNjJhZmYwMjRjOWNjNjA2MGIwOGFjZjY3MzRhOTdkNzU1OWFmNWFhMDEwN2NjMmI4OTJkODE1ZTNjZGQ1ZmJhMTkxYjI4MzMzNTgwZGZlZDM1YjM2MjUzODBmMWFhOTVhODUwMzVhNTNjM2Q0NTUyMDgzNmIyMGRlYmJmMTcyOWU1NjkyYmQyNGIyZjg5NTRjZGE5ODM2ODExNzU4NDZjNGQzOGJmNzg4ZWVlODY1N2ZkZDU5MDc3YjllOTNiMDk5MDM2ZjViODE2M2FjM2IxMzVhY2QyMjI0ZjgyNWMyYWUxZmE1ZDNiY2U3YWQ5ZDJlMmMzMTIwNGYwNDQ1N2NjY2I0NDEwODE1NmRiMGQ0NzY1MjBiOGI0NmYxNDQ2YTJmM2YwNWFjNjAwM2IzNjEyOGE2MjY2MGFiOTNjOGZkMGQwZjUzNjg5MWRmZWNiM2FjNWYwYTkzODAwMjNlODI5MTJjIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJkYWY3NDQyYzI3ZmJlMzJiNWZkOTcyZmY3Mjg0ZjgwMCIsImNvbnRlbnQiOiJlNmVmYjBlZDZjMmM4ZTA4ZGNhY2Y5ZjdkYWUxNWUyYmQ2YjEzNDRmYjkzMGMyMWJlNjVhZjNlOWZhNTMyOGY5ODAwMjY3YzBkZjM1M2ExOGE2NmY1Zjk3In0sImp0aSI6ImQwYmU5ZDc5LTlmNDAtNGNjMS1hOTRmLWE4ZmFmMjY0MzdlOSIsImlhdCI6MTYzNjg0Nzg2MSwiZXhwIjoxNjM2ODUxNDYxfQ.njzLY9NF-lYpo5kdkaUsoZhjUp2a1pX6nEiimJZfBVI'
    getParkingLots(destPoint, radius, token, parkOffStreet=True)
>>>>>>> main
    
    lots = parsePrkgLot(reqPrkg(destPoint, radius, token, prkOffStreet=True, save_to='results/prkgLots.json')['result'])
    # blocks = parsePrkgBlock(reqPrkg(destPoint, radius, token, parkOffStreet=False, save_to='prkgBlocks.json')['result'])
    mapDrawer.markPrkgLots(lots)
    mapDrawer.markDest(destPoint)
    mapDrawer.draw(save_to='results/map.html')


if __name__ == '__main__':
    departAddr = "1600 Guerrero St, San Francisco, CA 94110"
    destAddr = "74-98 Duncan St, San Francisco, CA 94110"
    main(departAddr=departAddr, destAddr=destAddr, radius=300, parkOffStreet=False)
    