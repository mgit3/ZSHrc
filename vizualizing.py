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

