#Imports to make the maps and store json data
from pathlib import Path
import json
import plotly.express as px

#Read data as a string and convert to a python object
path = Path('gas_stations.geojson')
contents = path.read_text(encoding ='utf-8')
all_gas_data = json.loads(contents)

#Examine all gas stations in the dataset
all_gas_dicts = all_gas_data['elements']

#Create lists of latitudes and longitudes
#
lons, lats = [], []
for gas_dict in all_gas_dicts:
    lon = gas_dict['lon']
    lat = gas_dict['lat']
    lons.append(lon)
    lats.append(lat)

#Format the map
title = 'American Gas Stations'
fig = px.scatter_geo(lat = lats, lon = lons, title = title, scope = 'usa', template = 'ggplot2',)
def show_gas_station():
    fig.show()

#Create a more readable version of the data file
path = Path('gas_data/readable_gas_data.geojson')
readable_contents = json.dumps(all_gas_data, indent = 4, ensure_ascii = False)
path.write_text(readable_contents, encoding ='utf-8')

show_gas_station()