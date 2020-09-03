import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='Deepak Mittal'), className="mb-1")
        ]),
        dbc.Row([
            dbc.Col(html.P(children='Undergraduate student with focus in Engineering. \
            	Self-taught Business Analytics and Data Analysis specialist with more than a \
            	year of experience in helping others learn these skills.'), className="mb-4")
        ]),])])