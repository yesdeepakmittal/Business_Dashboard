import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from app import server
from app import app

from product import piecategory,regionwisesubcategory,salesprofitsubcategory
from order import salescitywise,salespermonth,salesperweek
from geography import map
from customer import salesprofitbestcustomer,segment
from home import home

product_dropdown = dbc.DropdownMenu(
	children = [
	dbc.DropdownMenuItem('Pie Category',href='/piecategory'), #dbc.DropdownMenuItem("More pages", header=True)
	dbc.DropdownMenuItem('Region-wise',href='/regionwisesubcategory'),
	dbc.DropdownMenuItem('Sales Sub-Category',href='/salesprofitsubcategory'),
	],
	nav = True,
	in_navbar = True,
	label = 'Product',
	)
order_dropdown = dbc.DropdownMenu(
	children = [
	dbc.DropdownMenuItem('City-wise',href='/salescitywise'),
	dbc.DropdownMenuItem('Sales Per Week',href='/salesperweek'),
	dbc.DropdownMenuItem('Sales Per Month',href='/salespermonth'),
	],
	nav = True,
	in_navbar = True,
	label = 'Order',
	)
customer_dropdown = dbc.DropdownMenu(
	children = [
	dbc.DropdownMenuItem('Segment',href='/segment'),
	dbc.DropdownMenuItem('Best Customer',href='/salesprofitbestcustomer'),
	],
	nav = True,
	in_navbar = True, 
	label = 'Customer',
	)
geography_dropdown = dbc.DropdownMenu(
	children = [
	dbc.DropdownMenuItem('Map',href='/map'),
	],
	nav = True,
	in_navbar = True,
	label = 'Geography',
	)
#Ref: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
navbar = dbc.Navbar(
	dbc.Container(
		[
			html.A(
				dbc.Row(
					[	
						dbc.Col(dbc.NavbarBrand('Home')),
					],
					align = 'center',
					no_gutters = True,
					),
					href='/home',
				),
				dbc.NavbarToggler(id='navbar-toggler-product'),
				dbc.Collapse(dbc.Nav([product_dropdown],navbar=True),
                id="navbar-collapse-product",
                navbar=True,),

				dbc.NavbarToggler(id='navbar-toggler-order'),
				dbc.Collapse(dbc.Nav([order_dropdown],navbar=True),
                id="navbar-collapse-order",
                navbar=True,),

				dbc.NavbarToggler(id='navbar-toggler-customer'),
				dbc.Collapse(dbc.Nav([customer_dropdown],navbar=True),
                id="navbar-collapse-customer",
                navbar=True,),

				dbc.NavbarToggler(id='navbar-toggler-geography'),
				dbc.Collapse(dbc.Nav([geography_dropdown],navbar=True),
                id="navbar-collapse-geography",
                navbar=True,),
		]
		),
		color='dark',
		dark=True,
			)

@app.callback(
	Output(f"navbar-collapse-product",'is_open'),
	[Input(f"navbar-toggler-product",'n_clicks')],
	[State(f"navbar-collapse-product",'is_open')]
	)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
	Output(f"navbar-collapse-order",'is_open'),
	[Input(f"navbar-toggler-order",'n_clicks')],
	[State(f"navbar-collapse-order",'is_open')]
	)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
	Output(f"navbar-collapse-customer",'is_open'),
	[Input(f"navbar-toggler-customer",'n_clicks')],
	[State(f"navbar-collapse-customer",'is_open')]
	)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
@app.callback(
	Output(f"navbar-collapse-geography",'is_open'),
	[Input(f"navbar-toggler-geography",'n_clicks')],
	[State(f"navbar-collapse-geography",'is_open')]
	)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
 
app.layout = html.Div([
	dcc.Location(id='url',refresh=False),
	navbar,
	html.Div(id='page-content')
	])

@app.callback(Output('page-content','children'),
	[Input('url','pathname')])
def display_page(pathname):
    if pathname == '/piecategory':
        return piecategory.layout
    elif pathname == '/regionwisesubcategory':
        return regionwisesubcategory.layout
    elif pathname == '/salesprofitsubcategory':
        return salesprofitsubcategory.layout
    elif pathname == '/salescitywise':
        return salescitywise.layout
    elif pathname == '/salespermonth':
        return salespermonth.layout
    elif pathname == '/salesperweek':
        return salesperweek.layout
    elif pathname == '/map':
        return map.layout
    elif pathname == '/salesprofitbestcustomer':
        return salesprofitbestcustomer.layout
    elif pathname == '/segment':
        return segment.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)
