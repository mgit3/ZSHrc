#%%
from email import header
from regex import D
from tabulate import tabulate
import pandas as pd
from matplotlib import pyplot as plt

#%%
folderName = 'dataset_speedtest'
excelFile = folderName + '/speedTest.xlsx'
df = pd.read_excel(excelFile, parse_dates=True)
#%%
print(df.columns)

lstCln = ['Sponsor', 'Server Name', 'Timestamp',
       'Distance', 'Ping', 'Download', 'Upload'] 
#%%
df = df [lstCln]
show = tabulate(df, headers='keys',tablefmt="grid")
print(show)
#%%
dw =df['Download']
tm =df['Timestamp']
#%%


plt.plot(tm, dw)
plt.show()

