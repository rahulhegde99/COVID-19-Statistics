import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd
import json, urllib

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
tickFont = {'size':12, 'color':"rgb(30,30,30)", 'family':"Courier New, monospace"}

#Get Indian data from Ministry of Health
URL = "https://raw.githubusercontent.com/covid19india/covid19india/master/docs/data.json"
response = urllib.request.urlopen(URL)
data_dict = json.loads(response.read())
data = pd.DataFrame.from_dict(data_dict,orient='index')
data.to_csv("data.csv",index=None)

#Statewise data
statewise = data.iloc[0,:]
statewise = statewise.dropna()
statewise = pd.json_normalize(statewise)
statewise.columns = statewise.columns.map(lambda x: x.split(".")[-1])
statewise = statewise.drop([0])
statewise = statewise.drop(columns=['lastupdatedtime','confirmeddeltayesterday','deceaseddelta','recovereddelta','statesdelta'])
statewise.to_csv("statewise.csv",index=None)
#Statewise data to feed the graph(only top 5 data fed)
state = statewise['state'].head(10)
confirmed = statewise['confirmed'].head(10)
deaths = statewise['deaths'].head(10)
recovered = statewise['recovered'].head(10)
active = statewise['active'].head(10)

#Case Time Series data
case_time_series = data.iloc[1,:]
case_time_series = case_time_series.dropna()
case_time_series = pd.json_normalize(case_time_series)
case_time_series.columns = case_time_series.columns.map(lambda x: x.split(".")[-1])
case_time_series = case_time_series.drop(columns=['confirmeddeltayesterday','recovereddelta','deceaseddelta'])
case_time_series.to_csv("case_time_series.csv",index=None)
#Case Time Series data to feed the graph(only last 10 days fed)
date = case_time_series['date'].tail(20)
dailyconfirmed = case_time_series['dailyconfirmed'].tail(20)
dailyrecovered = case_time_series['dailyrecovered'].tail(20)
dailydeceased = case_time_series['dailydeceased'].tail(20)
totalconfirmed = case_time_series['totalconfirmed'].tail(20)
totalrecovered = case_time_series['totalrecovered'].tail(20)
totaldeceased = case_time_series['totaldeceased'].tail(20)

#Key Value data
key_value = data.iloc[2,:]
key_value = key_value.dropna()
key_value = pd.json_normalize(key_value)
key_value.columns = key_value.columns.map(lambda x: x.split(".")[-1])
key_value.to_csv("key_value.csv",index=None)

#User Interface parameters
colors = {
    'background':'#EEEEEE',
}

#User Interface using Dash and Plotly
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
app.title = "COVID-19"
app.layout = html.Div(className="container",style={'font-family':"sans-serif",'textAlign':'center','backgroundColor':colors['background']},children=[
    html.H1("Case History of COVID-19"),
    html.Div(className="main",children=[
        html.Div(className="graphhead",children=[
            html.H5("Statistical Report of COVID-19 in India"),
            html.P("-By Rahul Hegde")
        ]),

        html.Div(className="graph",children=[
            dcc.Graph(
                id='bar-graph',
                figure={
                    'data':[
                        {'x':state,'y':confirmed,'type':'bar','name':'Confirmed',},
                        {'x':state,'y':deaths,'type':'bar','name':'Deaths',},
                        {'x':state,'y':recovered,'type':'bar','name':'Recovered',},
                        {'x':state,'y':active,'type':'bar','name':'Active',},   
                    ],
                    'layout':{
                        'title': 'State-wise Bar Report',
                        'xaxis': dict(
                            title = ''
                        ),
                        'yaxis': dict(
                            title = 'Number of people'
                        )    
                    }
                },
                config={'displayModeBar':False},
            ),
            html.P("The above graph tells us statewise reports"),
            dcc.Graph(
                id='line-graph',
                figure={
                    'data':[
                        {'x':date,'y':dailyconfirmed,'type':'line','name':'Confirmed',},
                        {'x':date,'y':dailydeceased,'type':'line','name':'Deaths',},
                        {'x':date,'y':dailyrecovered,'type':'line','name':'Recovered',}, 
                    ],
                    'layout':{
                        'title': 'Daily Case Time Series Report',
                        'xaxis': dict(
                            title = ''
                        ),
                        'yaxis': dict(
                            title = 'Number of people'
                        )    
                    }
                },
                config={'displayModeBar':False},
            ),
            html.P("The above graph tells us daily report"),
            dcc.Graph(
                id='line-graph-cum',
                figure={
                    'data':[
                        {'x':date,'y':totalconfirmed,'type':'line','name':'Confirmed',},
                        {'x':date,'y':totaldeceased,'type':'line','name':'Deaths',},
                        {'x':date,'y':totalrecovered,'type':'line','name':'Recovered',}, 
                    ],
                    'layout':{
                        'title': 'Cumulative Case Time Series Report',
                        'xaxis': dict(
                            title = ''
                        ),
                        'yaxis': dict(
                            title = 'Number of people'
                        )    
                    }
                },
                config={'displayModeBar':False},
            ),
            html.P("The above graph tells us cumulative daily report"),
        ])
    ])
])

if __name__ == "__main__":
    app.run_server(debug=False)

server = app.server

"""@app.callback(
    Output(component_id='bar-graph',component_property='children'),
    [Input(component_id=,component_property=)]
)"""
