import pandas as pd

def extract_accidents(filename, year):
    """
    Extract traffic accident data from file for a given year and return a dataframe
    :param filename: name of data file
    :param year: year in a string
    :return: a dataframe with accident info, longitude, latitude, and date
    """
    data = pd.read_csv(filename)
    data = data[data['id'].str.startswith(year)]
    data['START_DT'] = pd.to_datetime(data['START_DT'])
    data['Date'] = data['START_DT'].dt.date
    data = data.drop(['DESCRIPTION', 'QUADRANT', 'START_DT', 'MODIFIED_DT',
                                'Count', 'id'], axis=1).reset_index(drop=True)
    data.columns = data.columns.str.lower()
    return data

def get_accident_counts_by_day():
    """
    Get the accident count by date in Calgary 2018 as a dataframe
    :return:
    """
    accidents = extract_accidents('Traffic_Incidents.csv', '2018')
    return accidents['date'].value_counts().to_frame().rename(columns={'date': 'Accident Count'})

def get_accident_counts_by_location():
    """
    Get the accident count by location in Calgary 2018 as a dataframe
    :return:
    """
    accidents = extract_accidents('Traffic_Incidents.csv', '2018')
    return accidents['location'].value_counts().to_frame().rename(columns={'location': 'Accident Count'})