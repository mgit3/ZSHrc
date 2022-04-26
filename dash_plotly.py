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
fig_scatter_dw_up = px.scatter(df,
            x=df.Timestamp, 
            y=[df.Download,df.Upload], 
            labels={'x':'Timestamp', 'y':['Download','Upload']},
            title="Download and Upload Speed").update_layout(paper_bgcolor=graphColor)


fig_boxPlot = go.Figure()
# Use x instead of y argument for horizontal plot
fig_boxPlot.add_trace(go.Box(x=df['Download'], name='DOWNLOAD',marker_color = bluePlotly))
fig_boxPlot.add_trace(go.Box(x=df['Upload'],  name='UPLOAD',marker_color = redPlotly))


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

    html.Div(children=[
    dash_table.DataTable(
      id='table',
      data = df.tail(12).to_dict('records'),
      style_cell={'padding': '5px','backgroundColor':myColor,'font_size': '14px',},
      style_header={'backgroundColor':tableHeaderColor,'fontWeight': 'bold'})
    ],style={'color':textColor,'margin':marginSize}),

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

# html.Img(src=logo_link, style={'width':30,'height':30}),
