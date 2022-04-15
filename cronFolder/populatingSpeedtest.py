#%%

from email import header
from tabulate import tabulate
import pandas as pd

#%%

# setting the name of the columns
lst_columns = ['Sponsor', 'Server Name', 'Timestamp','Distance', 'Ping', 'Download', 'Upload'] 

#reading the new file with pandas
tempCSV = 'dataset_speedtest/temp.csv'
dfA = pd.read_csv(tempCSV, names=lst_columns)

#%%

# reading the main dataset with pandas
excelFile = 'dataset_speedtest/speedTest.xlsx'
dfB = pd.read_excel(excelFile)

#%%

# concatenating the new data to the main dataset
newDf = pd.concat([dfA,dfB],axis=0)
newDf = newDf[lst_columns]

# writing over to the the main dataset 
newDf.to_excel(excelFile)
