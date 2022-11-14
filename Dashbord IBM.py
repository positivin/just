# python3 -m pip install pandas dash
# pip3 install httpx==0.20 dash plotly
# pip3 install pandas dash
# python3 dash_interactivity.py

#import pandas as pd
#import plotly.graph_objects as go
#import dash
#import dash_html_components as html
#import dash_core_components as dcc
#from dash.dependencies import Input, Output

## Read the airline data into pandas dataframe
#airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            #encoding = "ISO-8859-1",
                            #dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   #'Div2Airport': str, 'Div2TailNum': str})

##Next, we create a skeleton for our dash application. Our dashboard application layout has three components as seen before:

##Title of the application
##Component to enter input year inside a layout division
##Chart conveying the average monthly arrival delay inside a layout division
##Mapping to the respective Dash HTML tags:

##Title added using html.H1() tag
##Layout division added using html.Div() and input component added using dcc.Input() tag inside the layout division.
##Layout division added using html.Div() and chart added using dcc.Graph() tag inside the layout division.
##Copy the below code to the dash_interactivity.py script and review the structure.

## Create a dash application
#app = dash.Dash(__name__)

## Get the layout of the application and adjust it.
## Create an outer division using html.Div and add title to the dashboard using html.H1 component
## Add a html.Div and core input text component
## Finally, add graph component.
#app.layout = html.Div(children=[html.H1(),
                                #html.Div(["Input Year", dcc.Input(),], 
                                #style={}),
                                #html.Br(),
                                #html.Br(),
                                #html.Div(),
                                #])
##Application title
##Heading reference: Plotly H1 HTML Component (https://dash.plotly.com/dash-html-components/h1)
##Title as Airline Performance Dashboard
##Use style parameter and make the title center aligned, with color code #503D36, and font-size as 40. Check More about HTML section here.
##Input component
##Update dcc.Input component id as input-year, default value as 2010, and type as number. Use style parameter and assign height of the input box to be 50px and font-size to be 35.
##Use style parameter and assign font-size as 40 for the whole division.
##Output component
##Add dcc.Graph() component to the second division.
##Update dcc.Graph component id as line-plot.


##The core idea of this application is to get year as user input and update the dashboard in real-time. We will be using callback function for the same.

##Steps:

##Define the callback decorator
##Define the callback function that uses the input provided to perform the computation
##Create graph and return it as an output
##Run the application

## add callback decorator
#@app.callback(Output(),
               #Input())

## Add computation to callback function and return graph
#def get_graph(entered_year):
    ## Select data based on the entered year
    #df =  airline_data[airline_data['Year']==int(entered_year)]

    ## Group the data by Month and compute average over arrival delay time.
    #line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

    ## 
    #fig = go.Figure(data=)
    #fig.update_layout()
    #return fig

## Run the app
#if __name__ == '__main__':
    #app.run_server()

##Callback decorator
##Refer examples provided here
##Update output component id parameter with the id provided in the dcc.Graph() component and component property as figure.
##Update input component id parameter with the id provided in the dcc.Input() component and component property as value.
##Callback function
##Update data parameter of the go.Figure() with the scatter plot. Refer here. Sample syntax below:
#go.Scatter(x='----', y='----', mode='-----', marker='----)

##Update x as line_data['Month'], y as line_data['ArrDelay'], mode as lines, and marker as dict(color='green').

##Update fig.update_layout with title, xaxistitle, and yaxistitle parameters.

##Title as Month vs Average Flight Delay Time
##xaxis_title as Month
##yaxis_title as ArrDelay Refer the update layout function here (https://plotly.com/python/line-and-scatter/).

# Import required libraries
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})
# Create a dash application
app = dash.Dash(__name__)

app.layout = html.Div(children=[ html.H1('Airline Performance Dashboard',style={'textAlign': 'center', 'color': '#503D36','font-size': 40}),
                                html.Div(["Input Year: ", dcc.Input(id='input-year', value='2010', 
                                type='number', style={'height':'50px', 'font-size': 35}),], 
                                style={'font-size': 40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='line-plot')),
                                ])

# add callback decorator
@app.callback( Output(component_id='line-plot', component_property='figure'),
               Input(component_id='input-year', component_property='value'))

# Add computation to callback function and return graph
def get_graph(entered_year):
    # Select 2019 data
    df =  airline_data[airline_data['Year']==int(entered_year)]

    # Group the data by Month and compute average over arrival delay time.
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

    fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
    fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()