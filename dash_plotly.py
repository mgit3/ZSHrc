#%%
from sqlalchemy import create_engine
from sqlalchemy import MetaData 
from sqlalchemy import Table
import pandas as pd
import plotly.express as px
import dash 
import dash_core_components as dcc
#%%
tableName ='speedtest' 
engine = create_engine("sqlite:///dataset_speedtest/main.db")
query = "select * from speedtest"; df = pd.read_sql(query,engine)
#%%
#using the plotly modelu to produce a graph
fig_scatter_dw_up = px.scatter(df,
            x=df.Timestamp, 
            y=[df.Download,df.Upload], 
            labels={'x':'Timestamp', 'y':['Download','Upload']},
            title="Total Sales by Country and Month"
            )
#%%

# Create the Dash app
app = dash.Dash(__name__)

# Set up the layout with a single graph
app.layout = dcc.Graph(
  id='download_and_upload_speed',
  # Insert the line graph
  figure=fig_scatter_dw_up)

# Set the app to run in development mode
if __name__ == '__main__':
    app.run_server(debug=True)

#transforming the graph into html
file = 'dataset_speedtest/graph.html'
fig_scatter_dw_up.write_html(file)
