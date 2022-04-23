#%%
from click import style
from sqlalchemy import create_engine
from sqlalchemy import MetaData 
from sqlalchemy import Table
import pandas as pd
import dash 
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from datetime import datetime as dt

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
            title="Download and Upload Speed"
            )
#%%

# Create the Dash app
app = dash.Dash(__name__)

author = "Roberto"; lastName = "Moreira Diniz"; fullName = f"{author} {lastName}"; profession = "Data Engineer"
dashTitle = f"{author}'s Dashboard"  


# Set up the layout with a single graph
app.layout = html.Div(children=[
    html.Div(style={'width':1000,'height':10,'background-color':'darkblue'}),
    html.H1(dashTitle),
    html.Br(),
    html.Span(children=[f"Prepared: {dt.now().date()} by {fullName}, {profession}."]),
    dcc.Graph(id='scatter_dwUp',figure=fig_scatter_dw_up)
    ]
)

# Set the app to run in development mode
if __name__ == '__main__':
    app.run_server(debug=True)

#transforming the graph into html
file = 'dataset_speedtest/graph.html'
fig_scatter_dw_up.write_html(file)
