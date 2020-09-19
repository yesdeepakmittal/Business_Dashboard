import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as go

from data.datafile import regionwise
df = regionwise()

fig = go.Figure(data=[go.Bar(name=region,x=df['Sub-Category'],y=df[df['Region']==region]['Sales'],marker_color=color) for region,color in zip(df.Region.unique(),['red','navy','green','brown'])])
fig.update_layout(barmode='group',template='simple_white',title='Region-wise Sub-Category products Sales')



layout = html.Div([html.H1(children='Sales in each region'), 
        html.H6(children='Compare sales of different sub-category in each region'), 
        dcc.Graph(id='dist-chart', figure=fig)],
        style={'color': 'navy', 'textAlign': 'center'})