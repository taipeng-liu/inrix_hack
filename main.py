from ParkingLots.src.parking import *
from ParkingLots.src.drawer import Drawer
from ParkingLots.src.auth import getToken

def main(departAddr=None, startAddr=None, destAddr=None, radius=0, parkOffStreet=True):
    if not destAddr:
        return
    token = getToken()
    destPoint = Point(address=destAddr)
    mapDrawer = Drawer(location=[destPoint.latitude, destPoint.longitude])
    
    # if departAddr:
    #     departPoint = Point(address=departAddr)
    #     response = reqRoutes(departPoint, destPoint, token)
    
    lots = parsePrkgLot(reqPrkg(destPoint, radius, token, prkOffStreet=True, save_to='results/prkgLots.json')['result'])
    # blocks = parsePrkgBlock(reqPrkg(destPoint, radius, token, parkOffStreet=False, save_to='prkgBlocks.json')['result'])
    mapDrawer.markPrkgLots(lots)
    mapDrawer.markDest(destPoint)
    mapDrawer.draw(save_to='results/map.html')


if __name__ == '__main__':
    departAddr = "1600 Guerrero St, San Francisco, CA 94110"
    destAddr = "74-98 Duncan St, San Francisco, CA 94110"
    main(departAddr=departAddr, destAddr=destAddr, radius=300, parkOffStreet=False)
    