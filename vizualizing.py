#%%
from datetime import datetime
from email import header
from regex import D
from tabulate import tabulate
import pandas as pd
import plotly.express as px
#%%

#giving the name of where the dataset is located
file = 'dataset_speedtest/speedTest.csv'
# reading the Dataset with pandas
df = pd.read_csv(file)

#%%

# filtering the columns
df = df [['Sponsor', 'Server Name', 'Timestamp','Distance', 'Ping', 'Download', 'Upload']] 

# using the tabulate module to show in a cool way the data on the terminal
# print(tabulate(df, headers='keys',tablefmt="grid"))

#%%
# transforming the 'Timestamp' column in a datatetime on Pandas
df['Timestamp'] = pd.to_datetime(df['Timestamp'],infer_datetime_format=True)

df['Download'] = df['Download'].astype('float')
df['Upload'] = df['Upload'].astype('float') 

#change the scale on of the value to be more readable
df['Download'] = df['Download'] / (100**3)
df['Upload'] = df['Upload'] / (100**3)

#%%

#using the plotly modelu to produce a graph
fig = px.scatter(df,
            x=df.Timestamp, 
            y=[df.Download,df.Upload], 
            labels={'x':'Timestamp', 'y':['Download','Upload']})


fig.show()
#transforming the graph into html
file = 'dataset_speedtest/graph.html'
fig.write_html(file)

