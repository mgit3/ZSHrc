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
df['Download'] = df['Download'] / (100**3)
df['Upload'] = df['Upload']  / (100**3)

#%%
fig = px.line(df,x=tm, y=[dw,up], labels={'x':'Timestamp', 'y':['Download','Upload']})

fig.show()

file = folderName + '/graph.html'
fig.write_html(file)
#%%

up = df['Upload']
up
# %%

# %%
