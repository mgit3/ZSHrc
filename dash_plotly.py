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
            title="Download and Upload Speed")


fig_boxPlot = go.Figure()
# Use x instead of y argument for horizontal plot
fig_boxPlot.add_trace(go.Box(x=df['Download'], name='DOWNLOAD',marker_color = bluePlotly))
fig_boxPlot.add_trace(go.Box(x=df['Upload'],  name='UPLOAD',marker_color = redPlotly))

df.Download = df.Download.apply(lambda x:round(x,2))
df.Upload = df.Upload.apply(lambda x:round(x,2))


#%%

# Create the Dash app
app = dash.Dash(__name__)

#transforming the graph into html
author ="Roberto"; lastName = "Moreira Diniz"; fullName = f"{author} {lastName}"; profession = "Data Engineer"
dashTitle =f"{author}'s Dashboard"  
logo_link ='https://seeklogo.com/images/E/endless_knot-logo-1A4534EFCF-seeklogo.com.png'
colors = {
    'background': 'gray',
    'text': 'white'
}
marginSize = '20px'
fontSize = '14xp'

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
  html.H1(children= dashTitle,
      style={
          'textAlign': 'center',
          'color': colors['text'],
          'margin':'auto'}),

  html.Div(children=[f"Prepared: {dt.now().date()} by {fullName}, {profession}."], style={
      'textAlign': 'center',
      'margin': 'auto',
      'color': colors['text']}),

  html.Br(),

  html.Div(dcc.Graph(
      figure=fig_scatter_dw_up,
      style={}),
    style={'color':colors['text'], 
      'display':'inline-block', 
      'width':'1200xp',
      'margin':f'auto auto auto {marginSize}'}),
  
  html.Div(dcc.Graph(
      id='boxPLot',
      figure=fig_boxPlot),
    style={'color':colors['text'], 
      'display':'inline-block', 
      'width':'350xp'}),

  html.Span(children=[

    html.Ul(children=[
        html.B('HIGHEST:'),
        html.Li(children=[f"Download speed - {round(df['Download'].max(),2)} Mb/s."]),
        html.Li(children=[f"Upload speed - {round(df['Upload'].max(),2)} Mb/s."]),
        ],style={'width':'350px','display':'inline-block'}),
    html.Ul(children=[
        html.B('AVERAGE:'),
        html.Li(children=[f"Download speed - {round(df['Download'].mean(),2)} Mb/s."]),
        html.Li(children=[f"Upload speed - {round(df['Upload'].mean(),2)} Mb/s."]),
        ],style={'width':'350px','display':'inline-block'}),
    html.Ul(children=[
        html.B('LOWEST:'),
        html.Li(children=[f"Download speed - {round(df['Download'].min(),2)} Mb/s."]),
        html.Li(children=[f"Upload speed - {round(df['Upload'].min(),2)} Mb/s."]),
        ],style={'width':'350px','display':'inline-block'}),
    html.Ul(children=[
        html.B('STANDARD DESVIATION:'),
        html.Li(children=[f"Download speed - {round(df['Download'].std(),2)} Mb/s."]),
        html.Li(children=[f"Upload speed - {round(df['Upload'].std(),2)} Mb/s."]),
        ],style={'width':'350px','display':'inline-block'}),

    ],style={'font-size': fontSize,'display':'inline-block', 'margin':'auto','color':colors['text']}),

  html.Div(
    dash_table.DataTable(
    id='table',
    data = df.tail(10).to_dict('records'),
    style_cell={
      'padding': '5px',
      'textAlign': 'left',
      'backgroundColor':colors['text']},
    style_header={
      'backgroundColor':colors['text'],
      'fontWeight': 'bold'},
    ),style={'margin':marginSize}
  ),

    html.Div(children=[" "], style={
      'textAlign': 'center',
      'margin': 'auto',
      'height': marginSize,
      'color': colors['text']
  }),







])

# Set the app to run in development mode
if __name__ == '__main__':
    app.run_server(debug=True)

# html.Img(src=logo_link, style={'width':30,'height':30}),

    # html.Span(children=[
    # dcc.Graph(id='boxPLot',figure=fig_boxPlot,
    #   style={
    #   'width':'800px',
    #   'height':'350px', 
    #   'margin':'30PX', 
    #   }),html.Br()],style={'color':textColor, 'display':'inline-block','padding':'200px auto'}),
    
    
    # html.Span(children=[

    # html.Ul(children=[
    #     html.B('HIGHEST:'),
    #   	# Add two list elements with the top category variables
    #     html.Li(children=[f"Download speed - {round(df['Download'].max(),2)} Mb/s."]),
    #     html.Li(children=[f"Upload speed - {round(df['Upload'].max(),2)} Mb/s."]),
    #     ],style={'width':'350px'}),html.Br(),

    # html.Ul(children=[
    #     html.B('AVERAGE:'),
    #   	# Add two list elements with the top category variables
    #     html.Li(children=[f"Download speed - {round(df['Download'].mean(),2)} Mb/s."]),
    #     html.Li(children=[f"Upload speed - {round(df['Upload'].mean(),2)} Mb/s."]),
    #     ],style={'width':'350px'}),html.Br(),

    # html.Ul(children=[
    #     html.B('LOWEST:'),
    #   	# Add two list elements with the top category variables
    #     html.Li(children=[f"Download speed - {round(df['Download'].min(),2)} Mb/s."]),
    #     html.Li(children=[f"Upload speed - {round(df['Upload'].min(),2)} Mb/s."]),
    #     ],style={'width':'350px'}),html.Br(),

    # html.Ul(children=[
    #     html.B('STANDARD DESVIATION:'),
    #   	# Add two list elements with the top category variables
    #     html.Li(children=[f"Download speed - {round(df['Download'].std(),2)} Mb/s."]),
    #     html.Li(children=[f"Upload speed - {round(df['Upload'].std(),2)} Mb/s."]),
    #     ],style={'width':'350px'}),html.Br(),
    
    # ],style={'font-size':'18px','display':'inline-block', 'margin':'50px 50px 50px 100px'}), 


    # html.Div(style={'width':10000,'height':10,'background-color':'white'}),
    # html.Br(),