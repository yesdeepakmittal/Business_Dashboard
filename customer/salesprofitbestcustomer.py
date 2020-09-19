import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as go 

from data.datafile import complete
df = complete()

temp = df.sort_values('Profit',ascending=False)[['Sales','Profit','Customer Name']].head(10)
fig = go.Figure(data=[go.Bar(name='Profit',x=temp['Profit'],y=temp['Customer Name'],orientation='h',marker_color='navy'),
                      go.Bar(name='Sales',x=temp['Sales'],y=temp['Customer Name'],orientation='h',marker_color='green')])
fig.update_layout(template='simple_white',title='Sales & Profit of 10 Best Customers',barmode='stack',
                 yaxis_categoryorder = 'total ascending')

layout = html.Div([
        html.H1(children='Top 10 Customers'), 
        html.H6(children='Visualising sales & profit'), 
        dcc.Graph(id='dist-chart', figure=fig)],
            style={'color': 'navy', 'textAlign': 'center'})