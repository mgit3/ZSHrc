
import pandas as pd 

lst_columns = ['Sponsor', 'Server Name', 'Timestamp','Distance', 'Ping', 'Download', 'Upload']

df = pd.read_csv('dataset_speedtest/temp.csv', names=lst_columns)

df.to_excel('dataset_speedtest/speedTest.xlsx')
