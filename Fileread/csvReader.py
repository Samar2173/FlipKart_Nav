'''
Converting package csv files
to seperate lists according to 
Induct Stations.

~Flipkart GRiD 3
'''

import pandas as pd

def csv_to_list_seperate(filepath):
    '''
    Read csv from path, sort according to stations
    and return after converting to seperate lists.
    '''
    df = pd.read_csv(filepath)

    # Sorting according to Induct Stations
    station1 = df[df['Induct Station'] == 1]
    station2 = df[df['Induct Station'] == 2]

    # Cleaning Dataframe
    station1 = station1.drop(['Induct Station'], axis=1)
    station2 = station2.drop(['Induct Station'], axis=1)

    # Converting to List
    list_1 = station1.values.tolist()
    list_2 = station2.values.tolist()

    return list_1, list_2

if __name__ == '__main__':
    filepath = r'/home/rez3liet/Projects/Flipkart/FlipKart_Nav/Files/Sample Data - Sheet1.csv'
    station1_list, station2_list = csv_to_list_seperate(filepath)