"""
Main_GUI
This file runs the Phase I GUI, which utilizes defintions from Map.py and traffic.py to analyze City of Calgary traffic Data.
The GUI:
1. Allows the user to select from two types of data (Traffic Accidents or Traffic Volume)
2. Allows the user to select of specific year of data (2016, 2017, 2018)
3. Read data based on the selected type and date
4. Sort the data from highest to least traffic accident/volume
5. Identify the street with the largest number of accidents/volume
6. Allow the user to generate a map (html) with a marker identifying the specific street with the highest accidents/volume

"""


"""
Here are the list of packages that need to be installed before running the program:
1. Pymongo:  https://api.mongodb.com/python/current/installation.html
2. Mongodb: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
3. Folium: https://python-visualization.github.io/folium/
4. Tkinter: https://realpython.com/python-gui-tkinter/
5. Matplotlib: https://matplotlib.org/
"""

"""Import"""
import pandas as pd
from pymongo import MongoClient
import folium
from tkinter import *
from tkinter import ttk

"""
The Map class contains all definitions required to generate a map based on the user's selection of year and type.
"""
class Map:

    def __init__(self, data_kind = 'Traffic_Incidents', data_year = '2017', marker_coordinates = [51.03706737,-114.1123288], location = "17 Avenue at Richmond Road SW",  map_base_coordinates = [51.044270, -114.062019]):

        self.kind_=data_kind
        self.year_=data_year
        self.base_coordinates_ = map_base_coordinates
        self.map_ = folium.Map(location=self.base_coordinates_)
        self.marker_coordinates_ = marker_coordinates
        self.location_ = location
        self.file_name = self.create_Map()


    
    def create_Map(self):
        file_name = self.kind_+'_'+self.year_+'.html'
        

        # Call populate_Markers
        # print("Populating markers")

        if(self.kind_ == 'Traffic Incidents'):
            marker_name = "Most Traffic Accidents"
            self.populate_Markers(self.marker_coordinates_,self.location_,marker_name)
        else:
            marker_name = "Most Traffic Volume"
            self.populate_Markers(self.marker_coordinates_,self.location_,marker_name)
        

        # TODO: return file path.
        self.map_.save(file_name)
        #print("Returning file name: ", file_name, "saved in directory: ", os.getcwd())
        return file_name

    def populate_Markers(self,marker_coordinates=[51.03706737,-114.1123288],marker_name="17 Avenue at Richmond Road SW", marker_description="Most accidents" ):

        folium.Marker(marker_coordinates, popup=marker_name, tooltip=marker_description).add_to(self.map_)

        # TODO: for loop or while loop that attaches markers to the map

        # First take data from list

        
       # accident_coordinate = [51.03706737,-114.1123288]
       # accident_location_name = "17 Avenue at Richmond Road SW"
       # accident_description = "2 vehicle incident"

        # Then create a marker on map

        #folium.Marker(accident_coordinate, popup=accident_location_name, tooltip=accident_description).add_to(self.map_)

    def get_File_Name(self):
        return self.file_name

"""
The Traffic class contains all definitions required to read, sort, analyze data. It is also responsible for providing the Map object with the coordinate and address of the street
with most traffic accidents/volume.
"""
class Traffic:

"""
The GUI class contains all interface definitions required to receive user input and to display data the user has selected or create a map if the user requests it.
The main loop is runned here.
"""
class GUI:


"""
Getter/Updater for type and year as selected by the user using combobox1 and combobox2
This is used whenever the program wants to take the user selection into function arguments
"""
def update_type_year:
    global selected_type = combobox1.get()
    global selected_year = combobox2.get()

    if(map_type is not "" and map_year is not ""):
        pass
    else:
        updateDepositLabel("Error: Select Type/Year")



def main():
    GUI()

if __name__ == "__main__":
    pass