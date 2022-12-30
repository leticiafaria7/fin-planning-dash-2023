
#######################################################################
# BIBLIOTECAS
#######################################################################

from dash import Dash, html, dcc, dash_table
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
        dbc.Col([
            ## selecionar ano -------------------------------------------------
            dcc.Dropdown(
                id='ano-inter',
                placeholder = "2023",
                persistence=True,
                persistence_type='session'
            ),
        ], width = 2),

        dbc.Col([
            ## selecionar mês -------------------------------------------------
            dcc.Dropdown(
                id='mes-inter',
                placeholder = "Selecionar o mês",
                persistence=True,
                persistence_type='session'
            ),
        ], width = 4),

        dbc.Col([], width = 4),

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
        ], width = 2)
    ], className='dropdown-faturas'),

    dbc.Row([

        # gráfico ------------------------------------------------------
        dbc.Col([
            dcc.Graph(
                id='grafico-inter',
                config={'displayModeBar': False}
            )
        ], width=8),

        # tabela gastos -------------------------------------------------
        dbc.Col([
            dash_table.DataTable(
                style_cell={
                    'textAlign': 'center',
                    'font-size': '13px',
                    'font-family': 'Ubuntu',
                    'whiteSpace': 'pre-line'
                },

                style_data_conditional=[
                    {
                        'if': {'state': 'selected'},
                        'backgroundColor': '#edf3fb',
                        'border': '1px solid #edf3fb'
                    }
                ], style_as_list_view = True, id = 'tabela-inter'
            )
        ], width=4)
    ])
])