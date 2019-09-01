import folium
import os
import pandas as pd

class locality:
    def __init__(self):
        self.locality = pd.DataFrame({'Nation':[], 'Location':[], 'Latitude':[], 'Longitude':[], 'Mineral':[], 'Age':[],'Reference':[]})
        self.zmap = folium.Map(location=[0, 0], zoom_start=3)

    def set_default(self,latitude,longitude,zoom):
        self.zmap = folium.Map(location=[latitude, longitude], zoom_start=zoom)

    def manual_collect(self,nation,location,latitude,longitude,mineral,age,reference):
        add_locality = pd.DataFrame({'Nation':[nation], 'Location':[location], 'Latitude':[latitude], 'Longitude':[longitude], 'Mineral':[mineral], 'Age':[age],'Reference':[reference]},index=[len(self.locality)+1])
        self.locality  = pd.concat([self.locality,add_locality],sort=False)

    def read_spreadsheet(self,url):
        pass

    def google_map(self,latitude,longitude):
        url_bridge = 'https://www.google.com/maps/place/'+str(latitude)+'+'+str(longitude)
        return url_bridge

    def add_map(self,num):
        ind = 'index == '+str(num)
        latitude,longitude = self.locality.query(ind)['Latitude'],self.locality.query(ind)['Longitude']
        link = self.google_map(float(latitude), float(longitude))
        pop = str(float(self.locality.query(ind)['Age']))+' (GA)\n'+link
        folium.Marker([latitude, longitude], popup=pop).add_to(self.zmap)
        self.zmap.save('mineral_age.html')

    def marker(self,num):
        if num == 'all':
            for i in range(len(self.locality)):
                self.add_map(i+1)
        else:
            self.add_map(num)

    def output(self):
        return self.locality
