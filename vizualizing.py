#%%
from sqlalchemy import create_engine
from sqlalchemy import MetaData 
from sqlalchemy import Table
import pandas as pd
import plotly.express as px
#%%
tableName ='speedtest' 
engine = create_engine("sqlite:///dataset_speedtest/main.db")
query = "select * from speedtest"
# Load entire weather table by table name
df = pd.read_sql(query,engine)

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
