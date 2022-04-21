#%%

from email import header
from tabulate import tabulate
import pandas as pd

#%%

# setting the name of the columns
lst_columns = 'Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload,Share,IP Address'.split(",") 

#reading the new file with pandas
tempCSV = 'dataset_speedtest/temp.csv'
dfA = pd.read_csv(tempCSV, names=lst_columns)
#%%
# reading the main dataset with pandas
file = 'dataset_speedtest/speedTest.csv'
dfB = pd.read_csv(file)

#%%

# concatenating the new data to the main dataset
newDf = pd.concat([dfA,dfB],axis=0)
newDf = newDf[lst_columns]

# writing over to the the main dataset 
newDf.to_csv(file)

# %%
