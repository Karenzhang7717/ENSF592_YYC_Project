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
    df = pd.DataFrame(list(db[type_ + year].find())).drop(columns = '_id')
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
        return df.groupby(['incident info'])['count'].value_counts().sort_values(ascending=False)


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
    if type_ == 'Vol':
        return df['volume'].sum()
    else:
        return df['count'].sum()


def analyze_yearly(type_):
    """
    Plot yearly traffic record from 2016 to 2017
    :param type_: a string of either 'Vol' for traffic volume or 'Accident' for traffic accidents
    :return: None
    """
    y = []
    for year in range(2016, 2019):
        y.append(yearly_sum(type_, year))
    plt.figure()
    plt.plot(range(2016, 2019), y)
    plt.xlabel('Year')
    plt.xticks(range(2016, 2019))
    plt.ylabel('Traffic ' + type_)
    plt.title('Traffic ' + type_ + ' from 2016 - 2018')
    plt.show()


def main():
    pd.options.display.max_columns = None
    pd.options.display.width = None

    df_volume2016 = read_data('Vol', '2016')
    print(df_volume2016)
    print(sort_data(df_volume2016, 'Vol'))

    df_volume2017 = read_data('Vol', '2017')
    print(df_volume2017)
    print(sort_data(df_volume2017, 'Vol'))

    df_volume2018 = read_data('Vol', '2018')
    print(df_volume2018)
    print(sort_data(df_volume2018, 'Vol'))

    df_incident2016 = read_data('Accident', '2016')
    print(df_incident2016)
    print(sort_data(df_incident2016, 'Accident'))

    df_incident2017 = read_data('Accident', '2017')
    print(df_incident2017)
    print(sort_data(df_incident2017, 'Accident'))

    df_incident2018 = read_data('Accident', '2018')
    print(df_incident2018)
    print(sort_data(df_incident2018, 'Accident'))

    # analyze_yearly('Vol')
    # analyze_yearly('Accident')


if __name__ == '__main__':
    main()
