#Imports to make the maps and store json data
from pathlib import Path
import json
import plotly.express as px

#Read data as a string and convert to a python object
path = Path('alt_fuel_stations_Jul_12_2023.geojson')
contents = path.read_text(encoding ='utf-8')
all_electric_data = json.loads(contents)

#Examine all elecric stations in the dataset
all_electric_dicts = all_electric_data['features']

#Create lists of latitudes and longitudes
lons, lats = [], []
for electric_dict in all_electric_dicts:
    lon = electric_dict['geometry']['coordinates'][0] 
    lat = electric_dict['geometry']['coordinates'][1] 
    lons.append(lon)
    lats.append(lat)

#Format the map
title = 'American Charging Stations'
fig = px.scatter_geo(lat = lats, lon = lons, title = title, scope = 'usa', template = 'seaborn')
def show_electric_map():
    fig.show()


show_electric_map()