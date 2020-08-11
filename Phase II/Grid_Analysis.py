import numpy as np
import folium

# Define Calgary Border Boundaries
lower_left = [50.842822,-114.315796]
upper_right = [51.212425,-113.859905]

# Divide Calgary into a list of 10x10 girds and fine list of latitudes and longitudes for grid boundaries
lats = np.linspace(lower_left[0], upper_right[0], 11)
longs = np.linspace(lower_left[1], upper_right[1], 11)

def find_grid_col(long):
    """
    Return the column index for the given longitude in a 10x10 grid for Calgary.
    :param long: longitude as a float
    :return: the column index
    """
    for i in range(10):
        if long >= longs[i] and long < longs[i+1]:
            return i


def find_grid_row(lat):
    """
    Return the row index for the given latitude in a 10x10 grid for Calgary.
    :param lat: latitude as a float
    :return: the row index
    """
    for j in range(10):
        if lat >= lats[j] and lat < lats[j+1]:
            return j


def populate_grid(df):
    """
    Find and return the counts based on the map coordinates in a 10x10 grid for Calgary.
    :param df: a dataframe with columns 'longitude' and 'latitude'
    :return: a 2D array (10,10) with counts
    """
    grid = np.zeros((10, 10))

    for idx, row in df.iterrows():
        col = find_grid_col(row['longitude'])
        row = find_grid_row(row['latitude'])

        if col is not None and row is not None:
            grid[9-row, col] += 1

    return grid


def populate_grid_ms(df, label):
    """
    Find the return the averages based on th map coordinates in a 10x10 grid for Calgary.
    :param df: a dataframe row contain column 'multiline' which is a string containing a sequence of comma-delimited
    longitudes and latitudes.
    :param label: label for the column used for grid averages
    :return: a 2D array (10, 10) with the averages
    """
    grid_sum = np.zeros((10, 10))
    grid_count = np.zeros((10, 10))

    df['multiline'] = df['multiline'].apply(lambda x: str(x).split(','))

    for idx, row in df.iterrows():
        value = row[label]
        crossed_grids = []
        for str_coordinates in row['multiline']:
            coordinates = str_coordinates.strip().split(' ')
            long, lat = float(coordinates[0]), float(coordinates[1])
            col = find_grid_col(long)
            row = find_grid_row(lat)

            crossed_grids.append((col, row))

        for unique_grid in set(crossed_grids):
            if unique_grid[0] is not None and unique_grid[1] is not None:
                grid_sum[9-unique_grid[0], unique_grid[1]] += value
                grid_count[9-unique_grid[0], unique_grid[1]] += 1

    #this was indented left            
    grid = grid_sum / grid_count
    nans = np.isnan(grid)
    grid[nans] = 0


   
    return grid


def get_geojson_grid(upper_right, lower_left):
    """Returns a grid of geojson rectangles, and computes the exposure in each section of the grid based on the vessel
    data.

    Parameters
    ----------
    upper_right: array_like
        The upper right hand corner of "grid of grids" (the default is the upper right hand [lat, lon] of the USA).

    lower_left: array_like
        The lower left hand corner of "grid of grids"  (the default is the lower left hand [lat, lon] of the USA).

    n: integer
        The number of rows/columns in the (10,10) grid.

    Returns
    -------

    list
        List of "geojson style" dictionary objects
    """

    all_boxes = []

    lat_stride = lats[1] - lats[0]
    lon_stride = longs[1] - longs[0]

    for lat in lats[:-1]:
        for lon in longs[:-1]:
            # Define dimensions of box in grid
            upper_left = [lon, lat + lat_stride]
            upper_right = [lon + lon_stride, lat + lat_stride]
            lower_right = [lon + lon_stride, lat]
            lower_left = [lon, lat]

            # Define json coordinates for polygon
            coordinates = [upper_left, upper_right, lower_right, lower_left, upper_left]

            geo_json = {"type": "FeatureCollection",
                        "properties":{"lower_left": lower_left, "upper_right": upper_right},
                        "features":[]}

            grid_feature = {"type":"Feature",
                            "geometry":{"type":"Polygon", "coordinates": [coordinates]}}

            geo_json["features"].append(grid_feature)

            all_boxes.append(geo_json)

    return all_boxes


def display_grid_on_map(grid_values, label):
    """
    Display grid on map with the specified grid values and labels
    :param grid_values: 1D array of grid values (100,)
    :param label: label for map popup
    :return: Calgary map with 10x10 grid
    """
    base_coordinates = [51.044270, -114.062019]
    map = folium.Map(location=base_coordinates)

    grid = get_geojson_grid(lower_left, upper_right)

    for i, geo_json in enumerate(grid):
        gj = folium.GeoJson(geo_json)
        popup = folium.Popup(label+str(grid_values[i]))
        gj.add_child(popup)

        map.add_child(gj)

    return map

def display_grid_on_map_combined(grid_values, label):
    """
    Display grid on map with the specified grid values and labels
    :param grid_values: 1D array of grid values (100,)
    :param label: label for map popup
    :return: Calgary map with 10x10 grid
    """
    base_coordinates = [51.044270, -114.062019]
    map = folium.Map(location=base_coordinates)

    grid = get_geojson_grid(lower_left, upper_right)

    for i, geo_json in enumerate(grid):
        gj = folium.GeoJson(geo_json)
        popup_str = ''
        for j in range(len(label)):
            popup_str += label[j] + ": " + str(grid_values[j][i]) + "\n"
        popup = folium.Popup(popup_str)
        gj.add_child(popup)

        map.add_child(gj)

    return map

