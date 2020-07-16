import json
import pandas as pd
from pymongo import MongoClient

def csv_to_dict(filename):
    data = pd.read_csv(filename)
    return data.to_dict('records')

def extract_2018_accidents(filename):
    data = pd.read_csv(filename)
    data = data[data['id'].str.startswith('2018')]
    return data.to_dict('records')

def main():

    client = MongoClient()
    database = client['CalgaryTraffic']
    collection1 = database['Traffic2016']
    collection1.insert_many(csv_to_dict('TrafficFlow2016_OpenData.csv'))
    collection2 = database['Traffic2017']
    collection2.insert_many(csv_to_dict('2017_Traffic_Volume_Flow.csv'))
    collection3 = database['Traffic2018']
    collection3.insert_many(csv_to_dict('Traffic_Volumes_for_2018.csv'))
    collection4 = database['Accident2016']
    collection4.insert_many(csv_to_dict('Traffic_Incidents_Archive_2016.csv'))
    collection5 = database['Accident2017']
    collection5.insert_many(csv_to_dict('Traffic_Incidents_Archive_2017.csv'))
    accident_2018 = extract_2018_accidents('Traffic_Incidents.csv')
    collection6 = database['Traffic2018']
    collection6.insert_many(accident_2018)

if __name__ == '__main__':
    main()