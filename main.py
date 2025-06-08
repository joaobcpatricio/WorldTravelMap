import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd

# Data
data = [
    # Portugal
    {"place": "Coimbra, Portugal", "lat": 40.2033, "lon": -8.4103, "visited_by": "both"},
    {"place": "Viseu, Portugal", "lat": 40.6610, "lon": -7.9097, "visited_by": "both"},

    # Spain
    {"place": "Barcelona, Spain", "lat": 41.3851, "lon": 2.1734, "visited_by": "both"},
    {"place": "Madrid, Spain", "lat": 40.4168, "lon": -3.7038, "visited_by": "both"},
    {"place": "Valencia, Spain", "lat": 39.4699, "lon": -0.3763, "visited_by": "both"},
    {"place": "Ibiza, Spain", "lat": 38.9089, "lon": 1.4329, "visited_by": "both"},
    {"place": "Palma de Mallorca, Spain", "lat": 39.5696, "lon": 2.6502, "visited_by": "both"},

    # France
    {"place": "Marseille, France", "lat": 43.2965, "lon": 5.3698, "visited_by": "both"},
    {"place": "Paris, France", "lat": 48.8566, "lon": 2.3522, "visited_by": "both"},

    # Italy
    {"place": "Milan, Italy", "lat": 45.4642, "lon": 9.1900, "visited_by": "both"},
    {"place": "Verona, Italy", "lat": 45.4384, "lon": 10.9916, "visited_by": "both"},
    {"place": "Venice, Italy", "lat": 45.4408, "lon": 12.3155, "visited_by": "both"},
    {"place": "Genoa, Italy", "lat": 44.4056, "lon": 8.9463, "visited_by": "both"},
    {"place": "Civitavecchia, Italy", "lat": 42.0921, "lon": 11.7955, "visited_by": "both"},
    {"place": "Palermo, Italy", "lat": 38.1157, "lon": 13.3615, "visited_by": "both"},

    # Germany
    {"place": "Hamburg, Germany", "lat": 53.5511, "lon": 9.9937, "visited_by": "both"},
    {"place": "Berlin, Germany", "lat": 52.5200, "lon": 13.4050, "visited_by": "both"},
    {"place": "Frankfurt, Germany", "lat": 50.1109, "lon": 8.6821, "visited_by": "both"},
    {"place": "Bremen, Germany", "lat": 53.0793, "lon": 8.8017, "visited_by": "both"},

    # Finland
    {"place": "Turku, Finland", "lat": 60.4518, "lon": 22.2666, "visited_by": "both"},
    {"place": "Helsinki, Finland", "lat": 60.1699, "lon": 24.9384, "visited_by": "both"},
    {"place": "Tampere, Finland", "lat": 61.4978, "lon": 23.7610, "visited_by": "both"},

    # Estonia
    {"place": "Tallinn, Estonia", "lat": 59.4370, "lon": 24.7535, "visited_by": "both"},

    # Latvia
    {"place": "Riga, Latvia", "lat": 56.9496, "lon": 24.1052, "visited_by": "both"},

    # Lithuania
    {"place": "Vilnius, Lithuania", "lat": 54.6872, "lon": 25.2797, "visited_by": "both"},
    {"place": "Klaipeda, Lithuania", "lat": 55.7033, "lon": 21.1443, "visited_by": "both"},
    {"place": "Kaunas, Lithuania", "lat": 54.8985, "lon": 23.9036, "visited_by": "both"},

    # Poland
    {"place": "Warsaw, Poland", "lat": 52.2297, "lon": 21.0122, "visited_by": "both"},
    {"place": "Gdansk, Poland", "lat": 54.3520, "lon": 18.6466, "visited_by": "both"},

    # Austria
    {"place": "Vienna, Austria", "lat": 48.2082, "lon": 16.3738, "visited_by": "both"},

    # USA
    {"place": "New York City, USA", "lat": 40.7128, "lon": -74.0060, "visited_by": "both"},
    {"place": "New Jersey, USA", "lat": 40.0583, "lon": -74.4057, "visited_by": "both"},
    {"place": "Rockaway Beach, USA", "lat": 40.5830, "lon": -73.8207, "visited_by": "both"},

    # Angola
    {"place": "Luanda, Angola", "lat": -8.8390, "lon": 13.2894, "visited_by": "both"},
    {"place": "Calandula, Angola", "lat": -9.1333, "lon": 15.3667, "visited_by": "both"},
    {"place": "Malanje, Angola", "lat": -9.5407, "lon": 16.3408, "visited_by": "both"},
    {"place": "Lobito, Angola", "lat": -12.3525, "lon": 13.5611, "visited_by": "both"},
    {"place": "Benguela, Angola", "lat": -12.5797, "lon": 13.4072, "visited_by": "both"},
    {"place": "Lubango, Angola", "lat": -14.9172, "lon": 13.4925, "visited_by": "both"},
    {"place": "Namibe, Angola", "lat": -15.1961, "lon": 12.1526, "visited_by": "both"},

    # Peru
    {"place": "Lima, Peru", "lat": -12.0464, "lon": -77.0428, "visited_by": "both"},
    {"place": "Cusco, Peru", "lat": -13.5319, "lon": -71.9675, "visited_by": "both"},
    {"place": "Moray, Peru", "lat": -13.3045, "lon": -72.1917, "visited_by": "both"},
    {"place": "Maras Salt Mines, Peru", "lat": -13.3150, "lon": -72.1570, "visited_by": "both"},
    {"place": "Chinchero, Peru", "lat": -13.3927, "lon": -72.0432, "visited_by": "both"},
    {"place": "Rainbow Mountain, Peru", "lat": -13.8694, "lon": -71.3020, "visited_by": "both"},

    # Bolivia
    {"place": "La Paz, Bolivia", "lat": -16.4897, "lon": -68.1193, "visited_by": "both"},
    {"place": "Train Cemetery, Bolivia", "lat": -20.4686, "lon": -66.8267, "visited_by": "both"},
    {"place": "Colchani, Bolivia", "lat": -20.2940, "lon": -66.9530, "visited_by": "both"},
    {"place": "Eyes of Salt, Bolivia", "lat": -20.4600, "lon": -66.8250, "visited_by": "both"},
    {"place": "Flags Square & Salt Hotel, Bolivia", "lat": -20.3330, "lon": -67.1630, "visited_by": "both"},
    {"place": "Salar de Uyuni, Bolivia", "lat": -20.1338, "lon": -67.4891, "visited_by": "both"},
    {"place": "Incahuasi Island, Bolivia", "lat": -20.2427, "lon": -67.6250, "visited_by": "both"},
    {"place": "San Juan Town, Bolivia", "lat": -20.5727, "lon": -67.7764, "visited_by": "both"},
    {"place": "Ollagüe Volcano, Bolivia", "lat": -21.3086, "lon": -68.1833, "visited_by": "both"},
    {"place": "Laguna Cañapa, Bolivia", "lat": -20.9414, "lon": -67.6186, "visited_by": "both"},
    {"place": "Laguna Hedionda, Bolivia", "lat": -21.0170, "lon": -67.8340, "visited_by": "both"},
    {"place": "Laguna Chiarcota, Bolivia", "lat": -21.0330, "lon": -67.8370, "visited_by": "both"},
    {"place": "Laguna Honda, Bolivia", "lat": -21.2030, "lon": -67.6300, "visited_by": "both"},
    {"place": "Siloli Desert, Bolivia", "lat": -22.0150, "lon": -67.8117, "visited_by": "both"},
    {"place": "Stone Tree, Bolivia", "lat": -22.1871, "lon": -67.8291, "visited_by": "both"},
    {"place": "Eduardo Avaroa National Reserve, Bolivia", "lat": -22.4567, "lon": -67.9712, "visited_by": "both"},
    {"place": "Sol de Mañana Geysers, Bolivia", "lat": -22.4333, "lon": -67.7600, "visited_by": "both"},
    {"place": "Dali Desert, Bolivia", "lat": -22.7333, "lon": -67.3833, "visited_by": "both"},
    {"place": "Laguna Verde, Bolivia", "lat": -22.7929, "lon": -67.8340, "visited_by": "both"},
    {"place": "Licancabur Volcano, Bolivia", "lat": -22.8333, "lon": -67.8833, "visited_by": "both"},
    {"place": "Valley of the Rocks, Bolivia", "lat": -21.7846, "lon": -67.7122, "visited_by": "both"},

    # Chile
    {"place": "San Pedro de Atacama, Chile", "lat": -22.9087, "lon": -68.1990, "visited_by": "both"},
    {"place": "Calama, Chile", "lat": -22.4560, "lon": -68.9279, "visited_by": "both"},
    {"place": "Isla Magdalena, Chile", "lat": -52.9167, "lon": -70.8333, "visited_by": "both"},
    {"place": "Puerto Montt, Chile", "lat": -41.4717, "lon": -72.9369, "visited_by": "both"},
    {"place": "Puerto Varas, Chile", "lat": -41.3176, "lon": -72.9854, "visited_by": "both"},
    {"place": "Punta Arenas, Chile", "lat": -53.1638, "lon": -70.9171, "visited_by": "both"},
    {"place": "Puerto Natales, Chile", "lat": -51.7290, "lon": -72.5060, "visited_by": "both"},
    {"place": "Torres del Paine National Park, Chile", "lat": -51.0814, "lon": -73.0899, "visited_by": "both"},
    {"place": "Santiago, Chile", "lat": -33.4489, "lon": -70.6693, "visited_by": "both"},
    {"place": "Valparaiso, Chile", "lat": -33.0472, "lon": -71.6127, "visited_by": "both"},

    # Argentina
    {"place": "El Calafate, Argentina", "lat": -50.3370, "lon": -72.2648, "visited_by": "both"},
    {"place": "Perito Moreno Glacier, Argentina", "lat": -50.4950, "lon": -73.1456, "visited_by": "both"},

    # Brazil
    {"place": "Rio de Janeiro, Brazil", "lat": -22.9068, "lon": -43.1729, "visited_by": "both"},

    # United Kingdom
    {"place": "London, United Kingdom", "lat": 51.5072, "lon": -0.1276, "visited_by": "both"}
]


df = pd.DataFrame(data)

# Color mapping
color_map = {
    "you": "blue",
    "wife": "pink",
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
        showcountries=True,         # ✅ Show country borders
        countrycolor="gray",        # Line color for country borders
        landcolor="rgb(230, 230, 230)",
        showocean=True,
        oceancolor="lightblue",
        lakecolor="lightblue",
        showlakes=True
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
