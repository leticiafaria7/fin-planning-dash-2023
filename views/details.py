
#######################################################################
# BIBLIOTECAS
#######################################################################

from dash import Dash, html, dcc, dash_table
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify
from dash.dash_table.Format import Format, Scheme, Trim

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
                placeholder = '2023',
                persistence=True,
                persistence_type='session',
                options=[
                    {'label': '2023', 'value': 2023}
                ]
            ),
        ], width = 2),

        dbc.Col([
            ## selecionar mês -------------------------------------------------
            dcc.Dropdown(
                id='mes-detalhamento',
                placeholder = "Todos os meses",
                persistence=True,
                persistence_type='session',
                options=[
                    {'label': 'Todos os meses', 'value': 'Todos os meses'},
                    {'label': 'Janeiro', 'value': 'Janeiro'},
                    {'label': 'Fevereiro', 'value': 'Fevereiro'},
                    {'label': 'Março', 'value': 'Março'},
                    {'label': 'Abril', 'value': 'Abril'},
                    {'label': 'Maio', 'value': 'Maio'},
                    {'label': 'Junho', 'value': 'Junho'},
                    {'label': 'Julho', 'value': 'Julho'},
                    {'label': 'Agosto', 'value': 'Agosto'},
                    {'label': 'Setembro', 'value': 'Setembro'},
                    {'label': 'Outubro', 'value': 'Outubro'},
                    {'label': 'Novembro', 'value': 'Novembro'},
                    {'label': 'Dezembro', 'value': 'Dezembro'},
                ]
            ),
        ], width = 4),

        dbc.Col([], width = 6),
    ], id = 'dropdown-details'),

    # tabela e gráfico ----------------------------------------------------------
    dbc.Row([

        # tabela ------------------------
        dbc.Col([
            dbc.Row([
                dash_table.DataTable(
                    style_cell={
                        'textAlign': 'center',
                        'font-size': '12px',
                        'font-family': 'Ubuntu',
                        'whiteSpace': 'pre-line'
                    },

                    style_data_conditional=[
                        {
                            'if': {'state': 'selected'},
                            'backgroundColor': '#edf3fb',
                            'border': '1px solid #edf3fb'
                        }
                    ], 
                    # style_as_list_view = True, 
                    style_header = {'fontWeight': 'bold'},
                    id = 'tabela-detalhamento'
                )
            ]),
            dbc.Row([
                dbc.Col([
                    html.Button("Limpar seleção", id = 'clear')
                ], width=5),

                dbc.Col([], width=7)
            ])
        ], width=5),

        # tabela ------------------------
        dbc.Col([
            dcc.Graph(
                id='grafico-detalhamento',
                figure={},
                config={'displayModeBar': False}
            )
        ], width=7)

    ], id = 'dash-details')

])