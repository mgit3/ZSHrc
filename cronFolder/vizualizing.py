#%%
from datetime import datetime
from email import header
from regex import D
from tabulate import tabulate
import pandas as pd
import plotly.express as px
#%%
folderName = 'dataset_speedtest'
excelFile = folderName + '/speedTest.xlsx'
df = pd.read_excel(excelFile)
#%%
print(df.columns)

lstCln = ['Sponsor', 'Server Name', 'Timestamp',
       'Distance', 'Ping', 'Download', 'Upload'] 
#%%
df = df [lstCln]
show = tabulate(df, headers='keys',tablefmt="grid")
print(show)
#%%
df['Timestamp'] = pd.to_datetime(df['Timestamp'],infer_datetime_format=True)
df['Download'] = df['Download']/ (100**3)

#%% 

dw =df['Download']
tm =df['Timestamp']

fig = px.scatter(x=tm, y=dw, labels={'x':'Time', 'y':'Timestamp'})
fig.show()


# %%

# %%
