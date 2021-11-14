import folium 

class Drawer:
    def __init__(self, **args):
        self.markedPoints = []
        self.m = folium.Map(**args)
    
    def markDest(self, destPoint):
        self.markedPoints.append((destPoint.latitude, destPoint.longitude))
        folium.Marker(location=[destPoint.latitude, destPoint.longitude],popup=destPoint.address,tooltip=destPoint.address, icon=folium.Icon(color="red", icon="info-sign")).add_to(self.m)

    def markPrkgLots(self, prkgLots):
        for lot in prkgLots:
            self.markedPoints.append((lot.point.latitude, lot.point.longitude))
            folium.Marker(location=[lot.point.latitude, lot.point.longitude],popup=lot.getRateCard(),tooltip=lot.name, icon=folium.Icon(color="green")).add_to(self.m)
    def markPrkgBlocks(self, prkgBlocks):
        for block in prkgBlocks:
            pass

    def draw(self, save_to=None):
        if save_to:
            self.m.fit_bounds(self.markedPoints)
            self.m.save(save_to)