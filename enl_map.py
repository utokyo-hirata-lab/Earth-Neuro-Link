import os
import folium
import sqlite3
import pandas as pd
from httplib2 import Http
import gspread
from df2gspread import gspread2df as g2d
from oauth2client.service_account import ServiceAccountCredentials

class locality:
    def __init__(self):
        self.locality = pd.DataFrame({'Nation':[], 'Location':[], 'Latitude':[], 'Longitude':[], 'Mineral':[], 'Age':[],'Reference':[]})
        self.zmap = folium.Map(location=[0, 0], zoom_start=3)
        self.conn = ""

    def set_default(self,latitude,longitude,zoom):
        self.zmap = folium.Map(location=[latitude, longitude], zoom_start=zoom)

    def download_as_df(self,sheet_id, sheet_name):
        scopes      = ['https://www.googleapis.com/auth/spreadsheets']
        json_file   = 'Earth-Neuro-Link-09b51be6f905.json'#Json Cliant ID for OAuth
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scopes=scopes)
        http_auth   = credentials.authorize(Http())
        df = g2d.download(sheet_id, wks_name=sheet_name, col_names=True, row_names=False, credentials=credentials)
        return df

    def sql(self,path):
        df = self.download_as_df(path, 'form1')
        dbname = "enl.db"
        self.conn = sqlite3.connect(dbname)
        df.to_sql("enl_data", self.conn, if_exists="replace")
        self.conn.close()

    def auto_collect(self,path):
        self.sql(path)
        dbname = "enl.db"
        self.conn = sqlite3.connect(dbname)
        c = self.conn.cursor()
        sql = 'select * from enl_data'
        for row in c.execute(sql):
            self.manual_collect(row[2],row[3],row[4],row[5],row[6],row[7],row[8])
        self.conn.close()


    def manual_collect(self,nation,location,latitude,longitude,mineral,age,reference):
        add_locality   = pd.DataFrame({'Nation':[nation], 'Location':[location], 'Latitude':[latitude], 'Longitude':[longitude], 'Mineral':[mineral], 'Age':[age],'Reference':[reference]},index=[len(self.locality)+1])
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
