import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
from database.places_data import data

df = pd.DataFrame(data)

color_map = {
    "Joao": "red",
    "Mariana": "pink",
    "both": "green"
}

fig = go.Figure()

for group in df['visited_by'].unique():
    group_df = df[df['visited_by'] == group]
    fig.add_trace(go.Scattermap(
        lat=group_df['lat'],
        lon=group_df['lon'],
        mode='markers+text',
        marker=dict(size=10, color=color_map[group]),
        text=group_df['place'],
        textposition="top right",
        name=group.capitalize()
    ))

fig.update_layout(
    mapbox=dict(
        style="open-street-map",  # No token needed here
        zoom=5.5,
        center=dict(lat=39.5, lon=2.0),
        pitch=0,
    ),
    margin={"r":0,"t":0,"l":0,"b":0},
    legend=dict(y=0.99, x=0.01),
)

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("World Travel Dashboard"),
    dcc.Graph(figure=fig,
        config={
            "scrollZoom": True,
            "doubleClick": "reset",
            "displayModeBar": True,
        })
])

if __name__ == '__main__':
    app.run(debug=True, port=8051)