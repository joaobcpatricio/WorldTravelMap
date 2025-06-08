import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd

# Sample data
data = [
    {"place": "New York, USA", "lat": 40.7128, "lon": -74.0060, "visited_by": "you"},
    {"place": "Paris, France", "lat": 48.8566, "lon": 2.3522, "visited_by": "wife"},
    {"place": "Tokyo, Japan", "lat": 35.6895, "lon": 139.6917, "visited_by": "both"}
]

df = pd.DataFrame(data)

# Color mapping
color_map = {
    "you": "blue",
    "wife": "red",
    "both": "green"
}

fig = go.Figure()

# Add each category separately for custom colors and legend
for group in df['visited_by'].unique():
    group_df = df[df['visited_by'] == group]
    fig.add_trace(go.Scattergeo(
        lon=group_df['lon'],
        lat=group_df['lat'],
        text=group_df['place'],
        mode='markers',
        marker=dict(size=10, color=color_map[group]),
        name=group.capitalize()
    ))

fig.update_layout(
    geo=dict(
        projection_type='natural earth',
        showland=True,
        landcolor="rgb(217, 217, 217)",
        countrycolor="rgb(204, 204, 204)"
    ),
    margin={"r":0,"t":0,"l":0,"b":0}
)

# Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("World Travel Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
