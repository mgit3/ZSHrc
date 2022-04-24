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
logo_link = 'https://seeklogo.com/images/E/endless_knot-logo-1A4534EFCF-seeklogo.com.png'
myColor =   'rgb(54, 69, 99)'
textColor =   'white'

app.layout = html.Div(
  children=[
    html.Br(),
    html.Div(style={'width':10000,'height':10,'background-color':'white'}),
    html.H1(dashTitle),
    html.Br(),
    html.Span(children=[f"Prepared: {dt.now().date()} by {fullName} {profession}."]),
    html.Br(),html.Br(),
    dcc.Graph(id='scatter_dwUp',figure=fig_scatter_dw_up,style={'width':'900px', 'margin':'auto', 'background-color': myColor}),
    html.Br(),
    
    
    html.Span(children=[
    html.B('HIGHEST:'),
    html.Ol(children=[
      	# Add two list elements with the top category variables
        html.Li(children=[f"Download speed - {round(df['Download'].max(),2)} Mb/s."]),
        html.Li(children=[f"Upload speed - {round(df['Upload'].max(),2)} Mb/s."]),
        ],style={'width':'350px', 'margin':'auto'}),
    html.Br(),
    ]),

    html.Span(children=[
    html.B('LOWEST:'),
    html.Ol(children=[
      	# Add two list elements with the top category variables
        html.Li(children=[f"Download speed - {round(df['Download'].min(),2)} Mb/s."]),
        html.Li(children=[f"Upload speed - {round(df['Upload'].min(),2)} Mb/s."]),
        ],style={'width':'350px', 'margin':'auto'}),
    html.Br(),
    ]),

    html.Div(style={'width':10000,'height':10,'background-color':'white'}),
    html.Br(),
  ],style={'text-align':'center', 'font-size':22, 'background-color':myColor, 'color':textColor}
)

# Set the app to run in development mode
if __name__ == '__main__':
    app.run_server(debug=True)

#transforming the graph into html
file = 'dataset_speedtest/graph.html'
fig_scatter_dw_up.write_html(file)

    # html.Img(src=logo_link, style={'width':30,'height':30}),