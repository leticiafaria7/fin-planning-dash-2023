
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
    ], className='dropdown-faturas'),

    # título ----------------------------------------------------------
    dbc.Row([
        dbc.Col([
            html.Span("Detalhamento das categorias", className='titulo-texto')
        ], id='titulo1', className='titulo-secao', width=11)
    ]),

    # dropdowns ----------------------------------------------------------
    dbc.Row([

        dbc.Col([
            ## selecionar ano -------------------------------------------------
            dcc.Dropdown(
                id='ano-detalhamento',
                placeholder = "2023",
                persistence=True,
                persistence_type='session'
            ),
        ], width = 2),

        dbc.Col([
            ## selecionar mês -------------------------------------------------
            dcc.Dropdown(
                id='mes-detalhamento',
                placeholder = "Selecionar o mês",
                persistence=True,
                persistence_type='session'
            ),
        ], width = 4),

        dbc.Col([], width = 6),
    ], id = 'dropdown-details'),

    # tabela e gráfico ----------------------------------------------------------
    dbc.Row([

        # tabela ------------------------
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
                ], style_as_list_view = True, id = 'tabela-detalhamento'
            )
        ], width=6),

        # tabela ------------------------
        dbc.Col([
            dcc.Graph(
                id='grafico-detalhamento',
                config={'displayModeBar': False}
            )
        ], width=6)

    ], id = 'dash-details')





])