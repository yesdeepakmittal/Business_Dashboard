import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as go

from data.datafile import sales_sub
df = sales_sub()

fig = go.Figure(data=[go.Bar(name='Sales',x=df['Sales'],y=df['Sub-Category'],orientation='h',marker_color = 'green'),
                      go.Bar(name='Profit',x=df['Profit'],y=df['Sub-Category'],orientation='h',marker_color = 'navy')])
fig.update_layout(template='simple_white',title='Sales & Profit of each Sub-Category',height=700) #barmode='stack'



layout = html.Div([
        html.H1(children='Sales & Profit of Sub-category Products'),
        html.H6(children='Compare sales & profit'),
        dcc.Graph(id='dist-chart', figure=fig)],
        style={'color': 'navy', 'textAlign': 'center'})