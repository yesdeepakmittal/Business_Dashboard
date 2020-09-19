import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as go 

from data.datafile import complete
df = complete()

temp = df['Segment'].unique()
fig = go.Figure(data=go.Bar(x=temp,y=[df[df['Segment']==i]['Sales'].sum() for i in temp]))
fig.update_traces(marker_color='rgb(171,241,255)', marker_line_color='rgb(12,0,335)',
                  marker_line_width=2, opacity=0.6)
fig.update_layout(template='simple_white',title='Sales of each Segment')

layout = html.Div([
        html.H1(children='Customer Segmentation'),
        html.H6(children='Visualising different segments'),
        dcc.Graph(id='dist-chart', figure=fig)],
        style={'color': 'navy', 'textAlign': 'center'})