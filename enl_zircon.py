import folium
import os
import pandas as pd

class locality:
    def __init__(self):
        self.locality = pd.DataFrame({'Nation':[], 'Location':[], 'Latitude':[], 'Longitude':[], 'Age(GA)':[],'Reference':[]})
        self.zmap = folium.Map(location=[0, 0], zoom_start=3)

    def set_default(self,latitude,longitude,zoom):
        self.zmap = folium.Map(location=[latitude, longitude], zoom_start=zoom)

    def collect(self,nation,location,latitude,longitude,age,reference):
        add_locality = pd.DataFrame({'Nation':[nation], 'Location':[location], 'Latitude':[latitude], 'Longitude':[longitude], 'Age':[age],'Reference':[reference]},index=[len(self.locality)+1])
        self.locality  = pd.concat([self.locality,add_locality],sort=False)

    def add_map(self,num):
        ind = 'index == '+str(num)
        latitude = self.locality.query(ind)['Latitude']
        longitude = self.locality.query(ind)['Longitude']
        pop = str(float(self.locality.query(ind)['Age']))+'(GA)'
        folium.Marker([latitude, longitude], popup=pop).add_to(self.zmap)
        self.zmap.save('zmap.html')

    def marker(self,num):
        if num == 'all':
            for i in range(len(self.locality)):
                self.add_map(i+1)
        else:
            self.add_map(num)

    def output(self):
        return self.locality
