import pandas as pd
from matplotlib import pyplot as plt
from pymongo import MongoClient


def read_data(type_, year):
    """
    Return traffic record for the specified type and year
    :param type_: a string of either 'Vol' for traffic volume or 'Accident' for traffic accidents
    :param year: a string for year '2016', '2017' or '2018'
    :return: traffic records stored in a dataframe
    """
    client = MongoClient()
    db = client['CalgaryTraffic' + type_ + year]
    df = pd.DataFrame(list(db[type_ + year].find()))
    return df


def sort_data(df, type_):
    """
    Sort the dataframe in descending order of volume for traffic volume and count for traffic accidents
    :param df: dataframe
    :param type_: a string of either 'Vol' for traffic volume or 'Accident' for traffic accidents
    :return: dataframe sorted in descending order of volume or count
    """
    if type_ == 'Vol':
        return df.sort_values(by='volume', ascending=False)
    else:
        return df.groupby(['incident info'])['count'].value_counts().sort_values(ascending=False)\
            .rename_axis(['incident info', 'incident']).to_frame().reset_index().drop(columns = 'incident')


def yearly_sum(type_, year):
    """
    Return the sum of volume for traffic volume, or count for traffic accidents
    :param type_: a string of either 'Vol' for traffic volume or 'Accident' for traffic accidents
    :param year: a integer: 2016, 2017, or 2018
    :return: integer sum of volume or count
    """
    client = MongoClient()
    db = client['CalgaryTraffic' + type_ + str(year)]
    df = pd.DataFrame(list(db[type_ + str(year)].find()))
    return df['volume'].sum() if type_ == 'Vol' else df['count'].sum()


# def analyze_yearly(type_):
#     """
#     Plot yearly traffic record from 2016 to 2017
#     :param type_: a string of either 'Vol' for traffic volume or 'Accident' for traffic accidents
#     :return: None
#     """
#     y = []
#     for year in range(2016, 2019):
#         y.append(yearly_sum(type_, year))
#     #something about adding subplots
#
#     plt.figure()
#
#     plt.plot(range(2016, 2019), y)
#     plt.xlabel('Year')
#     plt.xticks(range(2016, 2019))
#     plt.ylabel('Traffic ' + type_)
#     plt.title('Traffic ' + type_ + ' from 2016 - 2018')


def get_most_vol_coordinate(sorted_df):
    """
    Return the name and map coordinate of the road with most traffic volume
    :param sorted_df: dataframe sorted in descending order of volume or count
    :return: road name, and coodinates in a tuple
    """
    try:
        index_name = sorted_df.columns.get_loc('segment_name')
    except:
        index_name = sorted_df.columns.get_loc('secname')
    try:
        index_coord = sorted_df.columns.get_loc('the_geom')
    except:
        index_coord = sorted_df.columns.get_loc('multilinestring')
    return sorted_df.iloc[0, index_name], sorted_df.iloc[0, index_coord]


def get_most_accident_coord(df, sorted_df):
    """
    Return the name and map coordinate of the road with most traffic incidents
    :param df: unsorted traffic incident dataframe
    :param sorted_df: dataframe sorted in descending order of incident count
    :return: road name, and coodinates in a tuple
    """
    loc = sorted_df.iloc[0,0]
    coord = df[df['incident info'] == loc]['location'].to_frame().iloc[0,0]

    return loc, coord

"""
def main():
    pd.options.display.max_columns = None
    pd.options.display.width = None

    # df_volume2016 = read_data('Vol', '2016')
    # sorted_df_volume2016 = sort_data(df_volume2016, 'Vol')
    # print(df_volume2016)
    # print(sorted_df_volume2016)
    # print(get_most_vol_coordinate(sorted_df_volume2016))
    #
    # df_volume2017 = read_data('Vol', '2017')
    # sorted_df_volume2017 = sort_data(df_volume2017, 'Vol')
    # print(df_volume2017)
    # print(sorted_df_volume2017)
    # print(get_most_vol_coordinate(sorted_df_volume2017))
    #
    # df_volume2018 = read_data('Vol', '2018')
    # sorted_df_volume2018 = sort_data(df_volume2018, 'Vol')
    # print(df_volume2018)
    # print(sorted_df_volume2018)
    # print(get_most_vol_coordinate(sorted_df_volume2018))
    #
    # df_incident2016 = read_data('Accident', '2016')
    # sorted_df_incident2016 = sort_data(df_incident2016, 'Accident')
    # print(df_incident2016)
    # print(sorted_df_incident2016)
    # print(get_most_accident_coord(df_incident2016, sorted_df_incident2016))
    #
    # df_incident2017 = read_data('Accident', '2017')
    # sorted_df_incident2017 = sort_data(df_incident2017, 'Accident')
    # print(df_incident2017)
    # print(sorted_df_incident2017)
    # print(get_most_accident_coord(df_incident2017, sorted_df_incident2017))
    #
    # df_incident2018 = read_data('Accident', '2018')
    # sorted_df_incident2018 = sort_data(df_incident2018, 'Accident')
    # print(df_incident2018)
    # print(sorted_df_incident2018)
    # print(get_most_accident_coord(df_incident2018, sorted_df_incident2018))

    # analyze_yearly('Vol')
    # analyze_yearly('Accident')


if __name__ == '__main__':
    main()
"""