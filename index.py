import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from app import server
from app import app

from portfolio import experience,certificate
from blogs import blogspython,blogsds
from englishtutorial import engtutds,engtutba
from hinditutorial import hintutpython
from home import home

portfolio_dropdown = dbc.DropdownMenu(
	children = [
	dbc.DropdownMenuItem('Experience',href='/experience'), #dbc.DropdownMenuItem("More pages", header=True)
	dbc.DropdownMenuItem('Certificate',href='/certificate'),
	],
	nav = True,
	in_navbar = True,
	label = 'Portfolio',
	)
blogs_dropdown = dbc.DropdownMenu(
	children = [
	dbc.DropdownMenuItem('Python',href='/blogspython'),
	dbc.DropdownMenuItem('Data Science',href='/blogsds'),
	],
	nav = True,
	in_navbar = True,
	label = 'MY Blogs',
	)
english_tutorial = dbc.DropdownMenu(
	children = [
	dbc.DropdownMenuItem('Data Science',href='/engtutds'),
	dbc.DropdownMenuItem('Business Analytics',href='/engtutba'),
	],
	nav = True,
	in_navbar = True, 
	label = 'English Tutorial',
	)
hindi_tutorial = dbc.DropdownMenu(
	children = [
	dbc.DropdownMenuItem('Python',href='/hintutpython'),
	],
	nav = True,
	in_navbar = True,
	label = 'Hindi Tutorial',
	)
#Ref: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
navbar = dbc.Navbar(
	dbc.Container(
		[
			html.A(
				dbc.Row(
					[	
						dbc.Col(html.Img(src='assets/deepakphoto.jpg',height = '30px')),
						dbc.Col(dbc.NavbarBrand('DK',className='ml-2')),
					],
					align = 'center',
					no_gutters = True,
					),
					href='/home',
				),
				dbc.NavbarToggler(id='navbar-toggler-porfolio'),
				dbc.Collapse(dbc.Nav([portfolio_dropdown],className='port-auto',navbar=True),
                id="navbar-collapse-port",
                navbar=True,),

				dbc.NavbarToggler(id='navbar-toggler-blogs'),
				dbc.Collapse(dbc.Nav([blogs_dropdown],className='blogs-auto',navbar=True),
                id="navbar-collapse-blogs",
                navbar=True,),

				dbc.NavbarToggler(id='navbar-toggler-engtut'),
				dbc.Collapse(dbc.Nav([english_tutorial],className='eng-auto',navbar=True),
                id="navbar-collapse-eng",
                navbar=True,),

				dbc.NavbarToggler(id='navbar-toggler-hintut'),
				dbc.Collapse(dbc.Nav([hindi_tutorial],className='hin-auto',navbar=True),
                id="navbar-collapse-hin",
                navbar=True,),
		]
		),
		color='dark',
		dark=True,
		className='mb-4',
	)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
	Output(f"navbar-collapse-port",'is_open'),
	[Input(f"navbar-toggler-porfolio",'n_clicks')],
	[State(f"navbar-collapse-port",'is_open')]
	)(toggle_navbar_collapse)

@app.callback(
	Output(f"navbar-collapse-blogs",'is_open'),
	[Input(f"navbar-toggler-blogs",'n_clicks')],
	[State(f"navbar-collapse-blogs",'is_open')]
	)(toggle_navbar_collapse)

@app.callback(
	Output(f"navbar-collapse-eng",'is_open'),
	[Input(f"navbar-toggler-engtut",'n_clicks')],
	[State(f"navbar-collapse-eng",'is_open')]
	)(toggle_navbar_collapse)

@app.callback(
	Output(f"navbar-collapse-hin",'is_open'),
	[Input(f"navbar-toggler-hintut",'n_clicks')],
	[State(f"navbar-collapse-hin",'is_open')]
	)(toggle_navbar_collapse)

app.layout = html.Div([
	dcc.Location(id='url',refresh=False),
	navbar,
	html.Div(id='page-content')
	])

@app.callback(Output('page-content','children'),
	[Input('url','pathname')])
def display_page(pathname):
    if pathname == '/experience':
        return experience.layout
    elif pathname == '/certificate':
        return certificate.layout
    elif pathname == '/blogspython':
        return blogspython.layout
    elif pathname == '/blogsds':
        return blogsds.layout
    elif pathname == '/engtutds':
        return engtutds.layout
    elif pathname == '/engtutba':
        return engtutba.layout
    elif pathname == '/hintutpython':
        return hintutpython.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)