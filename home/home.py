import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from app import app,server
from dash.dependencies import Input,Output,State

row = dbc.Row([
        dbc.Col(dbc.Jumbotron([
            html.H5(children="About Author"),
            html.P("Data Scientist"),
            html.Hr(),
            html.P("Treat Data & People equally"),
            html.A(dbc.Button("Follow Author on Github", color="primary"),href='https://github.com/yesdeepakmittal')],
            ), lg=4, md=4, xs=12),
        dbc.Col(dbc.Jumbotron([
            html.H5(children="For Demo Only"),
            html.P("You can use these tiles to show any important information \
                at the landing page or at any other page"),
            html.Hr(),
            html.P("Modify it depending upon your task  "),
            html.A(dbc.Button("Read here", color="primary"),href='https://github.com/yesdeepakmittal')],
            ), lg=4, md=4, xs=12),
        dbc.Col(dbc.Jumbotron([
            html.H5(children="Improve Application"),
            html.P("Feel free to open an issue in Github Repository for any Suggestion/Improvement"),
            html.Hr(),
            html.P("Click below button to open an issue"),
            html.A(dbc.Button("Open issue", color="primary"),href='https://github.com/yesdeepakmittal/Business_Dashboard/issues/new')],
            ), lg=4, md=4, xs=12)],justify='around')


layout = html.Div(children=[html.H1(children='Sample Superstore Data Analysis'),
                html.P(children='Python Web Application made using low-code framework, Dash'),
                html.Div(['Update Data👉',html.Button('Update-data', id='button')]),
                html.Br(),
                row,
                html.Div(id='Output',children='')],
                style={'marginTop': 0,'marginLeft':90, 'marginBottom': 0, 'font-size': 30, 
                          'color': 'navy', 'display': 'inline-block',})

from data.datafile import update,geography
@app.callback(Output('Output','children'),[Input('button', 'n_clicks')])
def update_data(n_clicks):
    update()
    # return print(n_clicks)
