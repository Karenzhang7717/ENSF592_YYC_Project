import folium

class Map:

    def __init__(self, data_list = None, data_kind = 'Traffic_Incidents', data_year = '2017', map_base_coordinates = [51.044270, -114.062019]):
        self.data_ = data_list
        self.kind_=data_kind
        self.year_=data_year
        self.base_coordinates_ = map_base_coordinates
        self.map_ = folium.Map(location=self.base_coordinates_)


    
    def create_Map(self):
        file_name = self.kind_+'_'+self.year_+'.html'
        

        # Call populate_Markers
        print("Populating markers")

    
        self.populate_Markers()

        

        # TODO: return file path.
        self.map_.save(file_name)
        print("Returning file name: ", file_name)
        return file_name

    def populate_Markers(self):

        # TODO: for loop or while loop that attaches markers to the map

        # First take data from list

        
        accident_coordinate = [51.03706737,-114.1123288]
        accident_location_name = "17 Avenue at Richmond Road SW"
        accident_description = "2 vehicle incident"

        # Then create a marker on map

        folium.Marker(accident_coordinate, popup=accident_location_name, tooltip=accident_description).add_to(self.map_)
