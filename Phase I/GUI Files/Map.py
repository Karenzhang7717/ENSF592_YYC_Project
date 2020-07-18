import folium
import os

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