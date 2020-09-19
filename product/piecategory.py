import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px

from data.datafile import complete
df = complete()

pie = px.sunburst(df, path=['Country','Category','Sub-Category'],
                        values='Sales',color='Category',
                        hover_data =['Sales','Quantity','Profit'])
pie.update_layout(margin=dict(t=40, l=0, r=0, b=0),
                            title='Sales Distribution',
                            height=700,
                            # width=410,
                            paper_bgcolor='#ffffff',
                            font={'size': 16}
                            )
pie.data[0].update(
            hovertemplate="Sales: $%{customdata[0]}")

layout = html.Div(children=[
                html.H1(children='Total Sales Distribution'),
                html.H6(children='Compare Categories'), 
                html.Br(),
                dcc.Graph(id='dist-chart', figure=pie)],
                style={'textAlign': 'center','color':'navy'}
                # style={'marginTop': 0,'marginLeft':90, 'marginBottom': 0, 'font-size': 30, 
                #         'color': 'navy', 'display': 'inline-block','textAlign': 'right',
                # 'vertical-align': 'middle','horizontal-align':'middle'}
                        ),