"""
Here is quick test filed use to experiment with folium.
Refer to:
https://python-visualization.github.io/folium/
For information used to play with folium

https://www.lifewire.com/latitude-longitude-coordinates-google-maps-1683398
For getting coordinates
Author: Patrick Kwan
"""

import folium
"""

#Creates a base map and saves it in index.html, which can be access through google chrome
#Looks like Decimal Degrees
m = folium.Map(location=[45.5236, -122.6750])
m.save('index.html')

"""


"""
Folium uses stuff from leaflet.js like special graphical markers

m = folium.Map(
    location=[51.044270, -114.062019],
    zoom_start=12,
    tiles='Stamen Terrain'
)
"""
"""
Create a tooltip that appears over the marker. You add this to the map object. 


tooltip = 'Click me!'

folium.Marker([51.04831941917631, -114.06036700906716 ], popup='<i>Mt. Hood Meadows</i>', tooltip=tooltip).add_to(m)
folium.Marker([51.04824965329041, -114.05790835100508 ], popup='<b>Timberline Lodge</b>', tooltip=tooltip).add_to(m)

m.save('markers.html')
"""


"""
Basic methodology:
1. Create a map object with a start location, which is a list of coordinates or if you really wanted to a point object
base_location = [ Latitude, Longitude ] 

"""
base_coordinate = []
base_coordinate = [51.044270, -114.062019]

map_object = folium.Map(location=base_coordinate)


"""
2. Attach markers to the map using folium.Marker([ Latitude, Longitude ] , popup = description, tooltip = tooltip_string).add_to(map_object)
    a. access accident coordinate
    b. access accident location name
    c. access accident descriptor
"""
accident_coordinate = []
accident_coordinate = [51.03706737,-114.1123288]
accident_location_name = "17 Avenue at Richmond Road SW"
accident_description = "2 vehicle incident"


folium.Marker(accident_coordinate, popup=accident_location_name, tooltip=accident_description).add_to(map_object)

"""
3. Save the map to be accessed by GUI
"""
kind = "Traffic_Incidents"
year = 2017

map_object.save(kind+'_'+str(2017)+'.html')

# file path

