#%%
from click import style
from matplotlib.pyplot import margins
from sqlalchemy import create_engine
from sqlalchemy import MetaData 
from sqlalchemy import Table
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import dash_table
import plotly.express as px
from datetime import datetime as dt

#%%
tableName ='speedtest' 
engine = create_engine("sqlite:///dataset_speedtest/main.db")
query = "select * from speedtest"; df = pd.read_sql(query,engine)
#%%
#using the plotly modelu to produce a graph
graphColor = 'rgb(240, 245, 245)'
bluePlotly = 'rgb(99, 110, 250)'
redPlotly = 'rgb(239, 85, 59)'
fig_scatter = px.scatter(df,
            x=df.Timestamp, 
            y=[df.Download,df.Upload], 
            labels={'x':'Timestamp', 'y':['Download','Upload']},
            title="Download and Upload Speed")


fig_boxPlot = go.Figure()
# Use x instead of y argument for horizontal plot
fig_boxPlot.add_trace(go.Box(x=df['Download'], name='DOWNLOAD',marker_color = bluePlotly))
fig_boxPlot.add_trace(go.Box(x=df['Upload'],  name='UPLOAD',marker_color = redPlotly))

df.Download = df.Download.apply(lambda x:round(x,2))
df.Upload = df.Upload.apply(lambda x:round(x,2))


from dash import Dash, Input, Output, callback, dash_table
import pandas as pd
import dash_bootstrap_components as dbc



app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Label('Click a cell in the table:'),
    dash_table.DataTable(df.to_dict('records'),[{"name": i, "id": i} for i in df.columns], id='tbl'),
    dbc.Alert(id='tbl_out'),
    ])

@callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
def update_graphs(active_cell):
    return str(active_cell) if active_cell else "Click the table"

if __name__ == "__main__":
    app.run_server(debug=True)