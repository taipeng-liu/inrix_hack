from django.shortcuts import render, redirect
from django.http import HttpResponse

from .src.parking import *
from .src.drawer import Drawer
from .src.auth import getToken

def main(departAddr=None, startAddr=None, destAddr=None, radius=0, parkOffStreet=True):
    if not destAddr:
        return
    
    token = getToken()
    destPoint = Point(address=destAddr)
    mapDrawer = Drawer(location=[destPoint.latitude, destPoint.longitude])
    print('Im here')
    # if departAddr:
    #     departPoint = Point(address=departAddr)
    #     response = reqRoutes(departPoint, destPoint, token)
    
    lots = parsePrkgLot(reqPrkg(destPoint, radius, token, prkOffStreet=True)['result'])
    # blocks = parsePrkgBlock(reqPrkg(destPoint, radius, token, parkOffStreet=False, save_to='prkgBlocks.json')['result'])
    mapDrawer.markPrkgLots(lots)
    mapDrawer.markDest(destPoint)
    mapDrawer.draw(save_to='ParkingLots/templates/map.html')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def findPrkg(request):
    # Would do routing from depart->dest if get more time...
    departAddr = request.POST.get('departAddr', None)
    destAddr = request.POST.get('destAddr', None)
    radius = int(request.POST.get('radius', None))
    main(departAddr=departAddr, destAddr=destAddr, radius=radius, parkOffStreet=False)

    return render(request, 'map.html')


def detail(request):
    first_name = 'a'
    context = {'name': first_name}
    return render(request, 'index.html', context)
