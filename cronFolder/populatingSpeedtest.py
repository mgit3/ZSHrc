#%%
from email import header
from tabulate import tabulate
import pandas as pd
folderName = 'dataset_speedtest'
file = folderName + '/temp.csv'

columns = 'Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload,Share,IP Address';lst_columns = columns.split(',')
dfA = pd.read_csv(file, names=lst_columns)

showA = tabulate(dfA, headers='keys')
print(showA)
#%%
excelFile = folderName + '/speedTest.xlsx'
dfB = pd.read_excel(excelFile)

showB = tabulate(dfB, headers='keys')
print(showB)
#%%
newDf = pd.concat([dfA,dfB],axis=0)
newDf = newDf[lst_columns]
newDf.to_excel(excelFile)

# %%