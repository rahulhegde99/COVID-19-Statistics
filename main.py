import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import resources as res

#User Interface parameters
colors = {
    'background':'#FFFFFF',
}

confirmed_color_list = ['#585858','#585858','#585858','#585858','#585858','#585858','#585858','#585858','#585858','#585858']
death_color_list = ['#ff0000','#ff0000','#ff0000','#ff0000','#ff0000','#ff0000','#ff0000','#ff0000','#ff0000','#ff0000']
recovered_color_list = ['#4bbf73','#4bbf73','#4bbf73','#4bbf73','#4bbf73','#4bbf73','#4bbf73','#4bbf73','#4bbf73','#4bbf73']
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
app.title = "COVID-19"
app.layout = html.Div(
    [
        dcc.Location(id="url"),
        dbc.NavbarSimple(
            children=[
                dbc.NavLink("Home", href="/page-1", id="page-1-link"),
                dbc.NavLink("Information", href="/page-2", id="page-2-link"),
                dbc.NavLink("About", href="/page-3", id="page-3-link"),
            ],
            brand="COVID-19",
            color="primary",
            dark=True,
        ),
        dbc.Container(id="page-content", className="pt-4"),
        dbc.NavbarSimple(style={'color':'white'},children=[
                dcc.Markdown('''
                    Built by &copy Rahul Hegde, 2020  [Github](https://github.com/rahulhegde99)

                    Data from Ministry of Health and Family Welfare  [https://www.mohfw.gov.in/](https://www.mohfw.gov.in/) 
                ''')
            ],
            brand="COVID-19",
            color="primary",
            dark=True,
        )
    ]
)

#Page1
page1 = html.Div(className="container",style={'textAlign':'center','backgroundColor':colors['background']},children=[
    html.H1("Case History of COVID-19"),
    html.Div(className="main",children=[
        html.Div(className="graphhead",children=[
            html.H3("Statistical Report of COVID-19 in India"),
        ]),
        html.P(html.Br()),

        dcc.Markdown('''
            #### **State-wise Bar Report**
        '''),

        html.Div(className="graph",children=[
            dcc.Graph(
                id='bar-graph',
                figure={
                    'data':[
                        {'x':res.state_list,'y':res.confirmed_list,'type':'bar','name':'Confirmed','marker': {'color':confirmed_color_list}},
                        {'x':res.state_list,'y':res.death_list,'type':'bar','name':'Deaths','marker':{'color':death_color_list}},
                        {'x':res.state_list,'y':res.recovered_list,'type':'bar','name':'Recovered','marker':{'color':recovered_color_list}},  
                    ],
                    'layout':{
                        'title': 'States with most COVID-19 reports',
                        'xaxis': dict(
                            title = ''
                        ),
                        'yaxis': dict(
                            title = 'Number of people'
                        ),  
                    }
                },
                config={'displayModeBar':False},
            ),
            html.P(html.Br()),
            html.P("The above graph shows the states with the highest confirmed COVID-19 cases. Interact with the legend to get better information."),
        ]),

        html.P(html.Br()),

        dcc.Markdown('''
            #### **State-wise Table Report**
        '''),

        html.Div(className="tablehead",style={'font-family':"Segoe UI"},children=[
            html.P("The below table gives us statewise reports"),
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in res.state_stats.columns],
                data=res.state_stats.to_dict('records'),
                style_cell={'textAlign': 'left','font-size':'16px'},
                style_header={
                    'backgroundColor': 'white',
                    'fontWeight': 'bold'
                },
                style_cell_conditional=[
                {
                    'if': {'column_id': 'Region'},
                    'textAlign': 'left',
                    'font-family':'"Lucida Console", Monaco, monospace'
                }
                ]
            ),
            html.P(html.Br()),
            html.P(html.Br())
        ]),
    ]),
])
#Page1 ends

#Page2
page2 = html.Div(className="container",style={'textAlign':'center','backgroundColor':colors['background']},children=[
    html.H1("Case History of COVID-19"),
    html.Div(className="main",children=[
        html.Div(className="graphhead",children=[
            html.H3("Detail Question and Answers on COVID-19 for Public"),
        ]),
        html.P(html.Br()),

        dcc.Markdown('''
            ##### What is corona virus?
            Corona viruses are a large family of viruses which may cause illness
            in animals or humans. In humans, several coronaviruses are known
            to cause respiratory infections ranging from the common cold to more
            severe diseases such as Middle East Respiratory Syndrome (MERS)
            and Severe Acute Respiratory Syndrome (SARS). The most recently
            discovered coronavirus causes coronavirus disease COVID-19.
            ##### What is COVID-19?
            COVID-19 is the infectious disease caused by the most recently
            discovered corona virus. This new virus and disease were unknown
            before the outbreak began in Wuhan, China, in December 2019.
            ##### What are the symptoms of COVID-19?
            The most common symptoms of COVID-19 are fever, tiredness, and
            dry cough. Some patients may have aches and pains, nasal
            congestion, runny nose, sore throat or diarrhea. These symptoms are
            usually mild and begin gradually. Some people become infected but
            don’t develop any symptoms and don't feel unwell. Most people
            (about 80%) recover from the disease without needing special
            treatment. Around 1 out of every 6 people who gets COVID-19
            becomes seriously ill and develops difficulty breathing. Older people,
            and those with underlying medical problems like high blood pressure,
            heart problems or diabetes, are more likely to develop serious illness.
            People with fever, cough and difficulty breathing should seek medical
            attention.  
            ##### How does COVID-19 spread?
            People can catch COVID-19 from others who have the virus. The
            disease can spread from person to person through small droplets from
            the nose or mouth which are spread when a person with COVID-19
            coughs or exhales. These droplets land on objects and surfaces
            around the person. Other people then catch COVID-19 by touching
            these objects or surfaces, then touching their eyes, nose or mouth.
            People can also catch COVID-19 if they breathe in droplets from a
            person with COVID-19 who coughs out or exhales droplets. This is
            why it is important to stay more than 1 meter (3 feet) away from a
            person who is sick.
        '''),
    ]),
])
#Page2ends

#Page3
page3 = html.Div(className="container",style={'textAlign':'center','backgroundColor':colors['background']},children=[
    html.H1("Case History of COVID-19"),
    html.Div(className="main",children=[
        html.Div(className="graphhead",children=[
            html.H3("Detail Question and Answers on COVID-19 for Public"),
        ]),
        html.P(html.Br()),

        dcc.Markdown('''
            ##### This application was built by Rahul Hegde.
            ##### The data for this application is scraped off of Ministry of Health and Family Welfare  [https://www.mohfw.gov.in/](https://www.mohfw.gov.in/) 
            ##### Check out my [GitHub](https://github.com/rahulhegde99) and my [LinkedIn](https://www.linkedin.com/in/rahul-hegde-0955391a5/)
        '''),
        html.P(html.Br()),
        html.P(html.Br()),
        html.P(html.Br()),
        html.P(html.Br()),
        html.P(html.Br()),
        html.P(html.Br()),
        html.P(html.Br())
    ]),
])
#Page3ends

# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return html.P(page1)
    elif pathname == "/page-2":
        return html.P(page2)
    elif pathname == "/page-3":
        return html.P(page3)
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)