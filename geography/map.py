import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px

from data.datafile import geography
df = geography()

fig = px.scatter_mapbox(
        df,
        title='Customer Location',
        lat="Latitude",
        lon="Longitude",
        color="Sales",
        size="Sales",
        size_max=60,
        hover_name="Profit",
        hover_data=["City", "Profit", "Sales"],
#         color_continuous_scale='Profit',
    )

fig.layout.update(
        margin={"r": 150, "t": 70, "l": 150, "b": 70},
        height=700,
        # width=700,
        coloraxis_showscale=False,
        mapbox_style='stamen-toner',
        mapbox=dict(center=dict(lat=39.7837304, lon=-100.4458825), zoom=3),
    )

fig.data[0].update(
        hovertemplate="Sales: ₹%{customdata[2]} <br>Profit: ₹%{customdata[1]}<br>City: %{customdata[0]}"
    )

layout = html.Div([
                html.H1(children='Where your customers are?'), 
                html.H6(children='Visualising customers across the world'), 
                dcc.Graph(id='dist-chart', figure=fig)],
                style={'color': 'navy', 'textAlign': 'center'})