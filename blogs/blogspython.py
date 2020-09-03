import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

'''https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/ 
Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has twelve columns(width <= 12), and five responsive tiers'''
'''https://medium.com/swlh/dashboards-in-python-for-beginners-using-dash-responsive-mobile-dashboards-with-bootstrap-css-2a0d05a53cf6'''
layout = html.Div([
    dbc.Container(
    	[
        dbc.Row([dbc.Col(html.H1(children='Thank you very much for reading my blogs!'), className="mb-2")]),
        dbc.Row([dbc.Col(html.H6(children='You will find informative blogs here'), className="mb-4")]),
        ]),

     dbc.Row([
        dbc.Col(dbc.Jumbotron([
            html.H5(children="Python Introduction", className="display-5"),
            html.P("One of the easiest and most widely used programming language in the world.",className="lead",),
            html.Hr(className="my-2"),
            html.P("Read the full blog at SolvProb"),
            html.A(dbc.Button("Read here", color="primary"), className="lead",href='https://github.com/yesdeepakmittal')],
            ), lg=4, md=4, xs=12),
        dbc.Col(dbc.Jumbotron([
            html.H5(children="Python Introduction", className="display-5"),
            html.P("One of the easiest and most widely used programming language in the world.",className="lead",),
            html.Hr(className="my-2"),
            html.P("Read the full blog at SolvProb"),
            html.A(dbc.Button("Read here", color="primary"), className="lead",href='https://github.com/yesdeepakmittal')],
            ), lg=4, md=4, xs=12),
        dbc.Col(dbc.Jumbotron([
            html.H5(children="Python Introduction", className="display-5"),
            html.P("One of the easiest and most widely used programming language in the world.",className="lead",),
            html.Hr(className="my-2"),
            html.P("Read the full blog at SolvProb"),
            html.A(dbc.Button("Read here", color="primary"), className="lead",href='https://github.com/yesdeepakmittal')],
            ), lg=4, md=4, xs=12)],justify='around'),

     dbc.Row([
        dbc.Col(dbc.Jumbotron([
            html.H5(children="Python Introduction", className="display-5"),
            html.P("One of the easiest and most widely used programming language in the world.",className="lead",),
            html.Hr(className="my-2"),
            html.P("Read the full blog at SolvProb"),
            html.A(dbc.Button("Read here", color="primary"), className="lead",href='https://github.com/yesdeepakmittal')],
            ), lg=4, md=4, xs=12),
        dbc.Col(dbc.Jumbotron([
            html.H5(children="Python Introduction", className="display-5"),
            html.P("One of the easiest and most widely used programming language in the world.",className="lead",),
            html.Hr(className="my-2"),
            html.P("Read the full blog at SolvProb"),
            html.A(dbc.Button("Read here", color="primary"), className="lead",href='https://github.com/yesdeepakmittal')],
            ), lg=4, md=4, xs=12),
        dbc.Col(dbc.Jumbotron([
            html.H5(children="Python Introduction", className="display-5"),
            html.P("One of the easiest and most widely used programming language in the world.",className="lead",),
            html.Hr(className="my-2"),
            html.P("Read the full blog at SolvProb"),
            html.A(dbc.Button("Read here", color="primary"), className="lead",href='https://github.com/yesdeepakmittal')],
            ), lg=4, md=4, xs=12)],justify='around')
    ])