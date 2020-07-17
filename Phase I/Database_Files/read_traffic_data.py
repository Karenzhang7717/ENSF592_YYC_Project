import pandas as pd
from matplotlib import pyplot as plt
from pymongo import MongoClient

def read_data(type, year):
    client = MongoClient()
    db = client['CalgaryTraffic' + type + year]
    df = pd.DataFrame(list(db[type + year].find()))
    return df

def sort_data(df, type, year):
    if type == 'Vol':
        return df.sort_values(by='volume', ascending = False)
    else:
        return df.groupby(['incident info'])['count'].value_counts().sort_values(ascending=False)

def analyze_yearly(df, type):
    return None

def main():
    df_volume2016 = read_data('Vol', '2016')
    print(df_volume2016)
    print(sort_data(df_volume2016, 'Vol', '2016'))

    df_volume2017 = read_data('Vol', '2017')
    print(df_volume2017)
    print(sort_data(df_volume2017, 'Vol', '2017'))

    df_volume2018 = read_data('Vol', '2018')
    print(df_volume2018)
    print(sort_data(df_volume2018, 'Vol', '2018'))

    df_incident2016 = read_data('Accident', '2016')
    print(df_incident2016)
    print(sort_data(df_incident2016, 'Accident', '2016'))

    df_incident2017 = read_data('Accident', '2017')
    print(df_incident2017)
    print(sort_data(df_incident2017, 'Accident', '2017'))

    df_incident2018 = read_data('Accident', '2018')
    print(df_incident2018)
    print(sort_data(df_incident2018, 'Accident', '2018'))

if __name__ == '__main__':
    main()

