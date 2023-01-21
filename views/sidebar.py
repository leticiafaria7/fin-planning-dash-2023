
#######################################################################
# BIBLIOTECAS
#######################################################################

# from index import app

from dash.dependencies import Input, Output
from dash import html, dcc
import pandas as pd
import numpy as np
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc

########################################################################
# LAYOUT
########################################################################

layout = dbc.Col([

    html.Br(),
    # html.Div(["."], className='space-sidebar'),
    # html.Div(["."], className='space-sidebar'),
    # html.Div(["."], className='space-sidebar'),
    # html.Div(["."], className='space-sidebar'),
    # html.Div(["."], className='space-sidebar'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
    # fatura nubank ----------------------------------------------------

    dbc.NavLink(
        children=[
            DashIconify(
                icon='icon-park-twotone:bill',
                color= '#9400d3',
                width= 20
            ),
            html.Span(
                "Fatura Nubank",
                className = 'sidebar-texto'
            )
        ],
        href = '/fatura-nubank',
        active = 'exact',
        id = 'fatura-nubank'
    ),

    # fatura inter -----------------------------------------------------

    dbc.NavLink(
        children=[
            DashIconify(
                icon='icon-park-twotone:bill',
                color= '#ff7900',
                width= 20
            ),
            html.Span(
                "Fatura Inter",
                className = 'sidebar-texto'
            )
        ],
        href = '/fatura-inter',
        active = 'exact',
        id = 'fatura-inter'
    ),

    # detalhamento -----------------------------------------------------

    dbc.NavLink(
        children=[
            DashIconify(
                icon='ph:magnifying-glass-duotone',
                color= '#4d4d4d',
                width= 20
            ),
            html.Span(
                "Detalhamento",
                className = 'sidebar-texto'
            )
        ],
        href = '/detalhamento-categorias',
        active = 'exact',
        id = 'detalhamento'
    ),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br()

], id='sidebar-completa')