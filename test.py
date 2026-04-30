import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    # Task 1: Dropdown will go here
    dcc.Dropdown(
        id = 'site-dropdown', 
        options=[{'label': 'All Sites', 'value': 'ALL'}]+[{'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()],
        value = 'ALL',
        placeholder = "Select Launch site",
        searchable = True
    ),

    html.Br(),

    # Task 2: Pie chart will go here
    html.Div(dcc.Graph(id='success-pie-chart')),

    html.Br(),

    html.P("Payload range (Kg):"),

    # Task 3: Slider will go here
    dcc.RangeSlider(
       id='payload-slider',
       min= 0, max=10000,step=1000,
        marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500'},
       value=[min_payload,max_payload]

    ),

    # Task 4: Scatter chart will go here
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)

def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig =  px.pie(
            spacex_df,
            values='class',
            names='Launch Site',
            title='Total Successful Launches by Site'
        )
    else:
        filtered_df = spacex_df[spacex_df['Launch Site']==entered_site]
        fig = px.pie(
            filtered_df,
            names='class',
            title=f'Total Successful/Unsuccessful Launches by {entered_site}'
        )
    return fig    


@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'), Input(component_id="payload-slider", component_property="value")]
)
def get_scatter_chart(entered_site,payload_range):
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)']>= payload_range[0]) & (spacex_df['Payload Mass (kg)']<=payload_range[1])]
    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color="Booster Version Category",title='Correlation between Payload and Success for All Sites')
    else:
        filtered_df = filtered_df[filtered_df['Launch Site']== entered_site]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color="Booster Version Category",title=f'Correlation between Payload and Success for {entered_site}')
    return fig      

if __name__ == '__main__':
    app.run()
