
#######################################################################
# BIBLIOTECAS
#######################################################################

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

#######################################################################
# LAYOUT
#######################################################################

layout = dbc.Col([

    html.Br(),

    dbc.Row([
        dbc.Col(width=10),
        dbc.Col([
            dbc.NavLink(
                children=[
                    DashIconify(
                        icon='fluent-emoji-high-contrast:house-with-garden',
                        color= '#4d4d4d',
                        width= 20
                    ),
                    html.Span(
                        "Home",
                        className = 'to-home'
                    )
                ],
                href = '/',
                active = 'exact',
                id = 'home-button'
            ),
        ])
    ]),

    dbc.Row([
        dbc.Col([
            html.Span("Detalhamento das categorias", className='titulo-texto')
        ], id='titulo1', className='titulo-secao', width=11)
    ])





])