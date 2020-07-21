import pandas as pd
from pymongo import MongoClient

def csv_to_dict(filename):
    """
    Convert a csv file to a collection of dictionaries
    :param filename: name of data file
    :return: a collection of dictionaries
    """
    data = pd.read_csv(filename)
    data.columns = [x.lower() for x in data.columns]
    return data.to_dict('records')

def extract_2018_accidents(filename):
    """
    Extract 2018 traffic accident data from file and return a collection of dictionaries
    :param filename: name of data file
    :return: a collection of dictionaries
    """
    data = pd.read_csv(filename)
    data = data[data['id'].str.startswith('2018')]
    data.columns = [x.lower() for x in data.columns]
    return data.to_dict('records')

def main():
    #Read 2016 - 2018 traffic volume and accident records into mongodb
    client = MongoClient()
    database1 = client['CalgaryTrafficVol2016']
    collection1 = database1['Vol2016']
    collection1.insert_many(csv_to_dict('TrafficFlow2016_OpenData.csv'))
    
    database2 = client['CalgaryTrafficVol2017']
    collection2 = database2['Vol2017']
    collection2.insert_many(csv_to_dict('2017_Traffic_Volume_Flow.csv'))
    
    database3 = client['CalgaryTrafficVol2018']
    collection3 = database3['Vol2018']
    collection3.insert_many(csv_to_dict('Traffic_Volumes_for_2018.csv'))
    
    database4 = client['CalgaryTrafficAccident2016']
    collection4 = database4['Accident2016']
    collection4.insert_many(csv_to_dict('Traffic_Incidents_Archive_2016.csv'))
    
    database5 = client['CalgaryTrafficAccident2017']
    collection5 = database5['Accident2017']
    collection5.insert_many(csv_to_dict('Traffic_Incidents_Archive_2017.csv'))
    
    database6 = client['CalgaryTrafficAccident2018']
    accident_2018 = extract_2018_accidents('Traffic_Incidents.csv')
    collection6 = database6['Accident2018']
    collection6.insert_many(accident_2018)

if __name__ == '__main__':
    main()