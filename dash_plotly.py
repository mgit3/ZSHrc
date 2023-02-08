import os
import redis
import json
import redis
import pandas as pd
from useful_fuctions import  *


from click import style
from matplotlib.pyplot import margins
from datetime import datetime as dt
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

def get_df():
    # Get data from Redis
    data = get_speedtest_data_from_redis()
    print(data)
    # Create a Pandas dataframe from the data
    df = pd.DataFrame.from_dict(data['speedtest_data'], orient='index', columns=['download', 'upload'])
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'datetime'}, inplace=True)
    return df

df = get_df() 

#using the plotly modelu to produce a graph
graphColor = 'rgb(240, 245, 245)'
bluePlotly = 'rgb(99, 110, 250)'
redPlotly = 'rgb(239, 85, 59)'

fig_scatter_dw_up = px.scatter(df,
            x=df["datetime"],
            y=[df["download"],df["upload"]],
            labels={'x':'datetime', 'y':['download','upload']},
            title="DOWNLOAD & UPLOAD SPEED").update_layout(paper_bgcolor=graphColor)


fig_boxPlot = go.Figure()

# Use x instead of y argument for horizontal plot
fig_boxPlot.add_trace(go.Box(x=df['download'], name='DOWNLOAD',marker_color = bluePlotly))
fig_boxPlot.add_trace(go.Box(x=df['upload'],  name='UPLOAD',marker_color = redPlotly))


# Create the Dash app
app = dash.Dash(__name__)


#transforming the graph into html
author ="Roberto"; lastName = "Moreira Diniz"; fullName = f"{author} {lastName}"; profession = "Data Engineer"
dashTitle =f"{author}'s Dashboard"  
myColor ='#282a36'
textColor ='white'
tableHeaderColor = '#44475a'
marginSize = "20px"

app.layout = html.Div(
  children=[
    html.Br(),
    html.H3(dashTitle),
    html.Span(children=[f"Prepared: {dt.now().date()} by {fullName}, {profession}."]),
    html.Br(),

        
html.Div(children=[
    dcc.Graph(id='scatter_dwUp',figure=fig_scatter_dw_up,
    style={'margin':'auto','height':'400px'})], style={'color': textColor, 'margin': marginSize}),

    html.Span(children=[

      html.P(children=[f"Last download Rate: {round(df['download'].iloc[-1],2)} Mb/s."],style={'width':'350px','display':'inline-block'}),
      html.P(children=[f"Last upload Rate: {round(df['upload'].iloc[-1],2)} Mb/s."],style={'width':'350px','display':'inline-block'}),
    
    ],style={'font-size':'18px','display':'inline-block', 'margin':'0px auto'}), 


html.Div(children=[
    dash_table.DataTable(
        id='table',
        data=df.tail(10).to_dict('records'),
        style_cell={
            'padding': '5px',
            'backgroundColor': myColor,
            'font_size': '14px',
            'textAlign': 'center'  # add this line to center the text
        },
        style_header={
            'backgroundColor': tableHeaderColor,
            'fontWeight': 'bold',
            'textAlign': 'center'  # add this line to center the text
        }
    )
], style={'color': textColor, 'margin': marginSize}),

html.Div(children=[
    dcc.Graph(id='boxPLot',figure=fig_boxPlot,
      style={
      'width':'1260px',
      'height':'460px', 
      'margin':'auto', 
      }),html.Br()],style={'color':textColor, 'display':'inline-block','padding':'200px auto'}),
    
    
    html.Span(children=[

    html.Ul(children=[
        html.B('HIGHEST:'),
      	# Add two list elements with the top category variables
        html.Li(children=[f"download speed - {round(df['download'].max(),2)} Mb/s."]),
        html.Li(children=[f"upload speed - {round(df['upload'].max(),2)} Mb/s."]),
        ],style={'width':'350px'}),html.Br(),

    html.Ul(children=[
        html.B('AVERAGE:'),
      	# Add two list elements with the top category variables
        html.Li(children=[f"download speed - {round(df['download'].mean(),2)} Mb/s."]),
        html.Li(children=[f"upload speed - {round(df['upload'].mean(),2)} Mb/s."]),
        ],style={'width':'350px'}),html.Br(),

    html.Ul(children=[
        html.B('LOWEST:'),
      	# Add two list elements with the top category variables
        html.Li(children=[f"download speed - {round(df['download'].min(),2)} Mb/s."]),
        html.Li(children=[f"upload speed - {round(df['upload'].min(),2)} Mb/s."]),
        ],style={'width':'350px'}),html.Br(),

    html.Ul(children=[
        html.B('STANDARD DESVIATION:'),
      	# Add two list elements with the top category variables
        html.Li(children=[f"download speed - {round(df['download'].std(),2)} Mb/s."]),
        html.Li(children=[f"upload speed - {round(df['upload'].std(),2)} Mb/s."]),
        ],style={'width':'350px'}),html.Br(),
    
    ],style={'font-size':'18px','display':'inline-block', 'margin':f'50px 50px 50px {marginSize}'}), 


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
