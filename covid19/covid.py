#=================================#
# Import das bibliotecas do projeto
#=================================#

import json

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
#from dash import dash_core_components as dcc
#from dash import dash_html_components as html

#=================================#
# leitura dos dados
#=================================#

df_states = pd.read_csv("df_states.csv")
df_brasil = pd.read_csv("df_brasil.csv")

brasil_states = json.load(open("geojson/brazil_geo.json", "r"))

df_states = df_states[df_states['data'] == '2020-05-13']

#=================================#
# instaciando o dash
#=================================#

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

fig = px.choropleth_mapbox(df_states, locations='estado', color='casosNovos', geojson=brasil_states, 
                            center={'lat': -16.95,'lon': -47.78 },
                            color_continuous_scale='Redor', opacity=0.4, 
                            hover_data={'casosAcumulado':True, 'casosNovos':True, 'obitosNovos':True, 'estado':True})

fig.update_layout(
    mapbox_style='carto-dakmatter'
)

#=================================#
# layout do dash
#=================================#

app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='choropleth_mapbox', figure=fig)
        ])
    ])
)

if __name__ == "__main__":
    app.run_server(debug=True)

