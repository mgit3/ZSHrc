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
fig_scatter_dw_up = px.scatter(df,
            x=df.Timestamp, 
            y=[df.Download,df.Upload], 
            labels={'x':'Timestamp', 'y':['Download','Upload']},
            title="Download and Upload Speed").update_layout(paper_bgcolor=graphColor)


fig_boxPlotDW = px.box(df['Download']).update_layout(paper_bgcolor=graphColor)        
fig_boxPlotUP= px.box(df['Upload']).update_layout(paper_bgcolor=graphColor)        

#%%

# Create the Dash app
app = dash.Dash(__name__)


#transforming the graph into html
author ="Roberto"; lastName = "Moreira Diniz"; fullName = f"{author} {lastName}"; profession = "Data Engineer"
dashTitle =f"{author}'s Dashboard"  
logo_link ='https://seeklogo.com/images/E/endless_knot-logo-1A4534EFCF-seeklogo.com.png'
myColor ='rgb(15, 33, 62)'
textColor ='white'
tableHeaderColor = 'rgb(91, 138, 215)'

app.layout = html.Div(
  children=[
    html.Br(),
    html.Div(style={'width':10000,'height':10,'background-color':'white'}),
    
    html.H1(dashTitle),
    html.Span(children=[f"Prepared: {dt.now().date()} by {fullName} {profession}."]),
    html.Br(),

        
    html.Span(children=[
    dcc.Graph(id='scatter_dwUp',figure=fig_scatter_dw_up,
    style={
    'width':'900px', 
    'margin':'auto', 
    }),html.Br()],style={'color':textColor, 'display':'inline-block','margin':'100px'}),

    dash_table.DataTable(
      id='table',
      data = df.to_dict('records'),
      style_cell={'padding': '5px','backgroundColor':myColor},
      style_header={'backgroundColor':tableHeaderColor,'fontWeight': 'bold'},
      ),

    html.Span(children=[
    dcc.Graph(id='boxPLotDW',figure=fig_boxPlotDW,
      style={
      'width':'500px', 
      'margin':'auto', 
      }),html.Br()],style={'color':textColor, 'display':'inline-block','margin':'100px'}),
    
    html.Span(children=[
    dcc.Graph(id='boxPLotUP',figure=fig_boxPlotUP,
      style={
      'width':'500px', 
      'margin':'auto', 
      }),html.Br()],style={'color':textColor, 'display':'inline-block','margin':'100px'}),

    
    html.Span(children=[

    html.Ul(children=[
        html.B('HIGHEST:'),
      	# Add two list elements with the top category variables
        html.Li(children=[f"Download speed - {round(df['Download'].max(),2)} Mb/s."]),
        html.Li(children=[f"Upload speed - {round(df['Upload'].max(),2)} Mb/s."]),
        ],style={'width':'350px'}),html.Br(),

    html.Ul(children=[
        html.B('AVERAGE:'),
      	# Add two list elements with the top category variables
        html.Li(children=[f"Download speed - {round(df['Download'].mean(),2)} Mb/s."]),
        html.Li(children=[f"Upload speed - {round(df['Upload'].mean(),2)} Mb/s."]),
        ],style={'width':'350px'}),html.Br(),

    html.Ul(children=[
        html.B('LOWEST:'),
      	# Add two list elements with the top category variables
        html.Li(children=[f"Download speed - {round(df['Download'].min(),2)} Mb/s."]),
        html.Li(children=[f"Upload speed - {round(df['Upload'].min(),2)} Mb/s."]),
        ],style={'width':'350px'}),html.Br(),

    html.Ul(children=[
        html.B('STANDARD DESVIATION:'),
      	# Add two list elements with the top category variables
        html.Li(children=[f"Download speed - {round(df['Download'].std(),2)} Mb/s."]),
        html.Li(children=[f"Upload speed - {round(df['Upload'].std(),2)} Mb/s."]),
        ],style={'width':'350px'}),html.Br(),
    
    ],style={'text-align':'top','display':'inline-block', 'margin':'10px 10px 30px 100px'}), 


    html.Div(style={'width':10000,'height':10,'background-color':'white'}),
    html.Br(),
  ],style={
    'text-align':'center', 
    'font-size':22, 
    'background-color':myColor, 
    'color':textColor},
)

# Set the app to run in development mode
if __name__ == '__main__':
    app.run_server(debug=True)

# html.Img(src=logo_link, style={'width':30,'height':30}),
