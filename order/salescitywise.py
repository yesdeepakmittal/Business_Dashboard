import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px

from data.datafile import complete
df = complete()

temp = df[['State','City','Sales']].groupby(['State','City'])['Sales'].sum().reset_index()
fig = px.treemap(temp,path=['State','City'], values='Sales')
fig.update_layout(height=1000,title='City-wise Sales',)
                 #color_discrete_sequence = px.colors.qualitative.Plotly)
fig.data[0].textinfo = 'label+text+value'

layout = html.Div([
        html.H1(children='Sales in each City'), 
        html.H6(children='Visualising sales across different cities'), 
        dcc.Graph(id='dist-chart', figure=fig)],
        style={'color': 'navy', 'textAlign': 'center'}),