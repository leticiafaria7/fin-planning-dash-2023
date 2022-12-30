
#######################################################################
# BIBLIOTECAS
#######################################################################

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

#######################################################################
# LAYOUT
#######################################################################

layout = dbc.Col([

    html.Br(), # espaço em branco acima do navbar
    
    dbc.Row([

        dbc.Col(width=1),

        # espaço na faixa do navbar ----------------------------------------------
        dbc.Row([
            html.Br(),
        ]),

        # contas bancárias --------------------------------------------------------
        dbc.Col([
            dbc.Row([
                html.Div([
                    html.Span("Contas bancárias")
                ], id = 'titulo1', className='titulo-navbar'),
                html.Hr(
                    style={'background-color': '#ffffff', 'height': '2px', 'border': 'none'}
                )
            ]),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.Div("Inter"),
                        html.Div(id = 'total-inter')
                    ], className='total-inter-nav')
                ], width=3),
                dbc.Col([
                    html.Div([
                        html.Div("Nubank"),
                        html.Div(id = 'total-nubank')
                    ], className='total-nubank-nav')
                ], width=3),
                dbc.Col([
                    html.Div([
                        html.Div("Banco do Brasil"),
                        html.Div(id = 'total-bb')
                    ], className='total-bb-nav')
                ], width=4),
                dbc.Col([
                    html.Div([
                        html.Div("Cash"),
                        html.Div(id = 'total-cash')
                    ], className='total-cash-nav')
                ], width=2),
            ])

        ], id = 'contas-bancarias'),

        dbc.Col([], width=1),

        # próximas faturas --------------------------------------------------------

        dbc.Col([
            dbc.Row([
                html.Div([
                    html.Span("Próximas faturas")
                ], id = 'titulo1', className='titulo-navbar'),
                html.Hr(
                    style={'background-color': '#ffffff', 'height': '2px', 'border': 'none'}
                )
            ]),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.Div("Cartão Inter"),
                        html.Div(id = 'total-cartao-inter')
                    ], className='total-c-inter-nav')
                ], width=6),
                dbc.Col([
                    html.Div([
                        html.Div("Cartão Nubank"),
                        html.Div(id = 'total-cartao-nubank')
                    ], className='total-c-nubank-nav')
                ], width=6)
            ])
        ], width=4),

        dbc.Col([], width=1),

        dbc.Row([
            html.Br(),
        ]),

    ], id = 'navbar'),

    html.Br(),

    # dashboard -------------------------------------------------------------------

    dbc.Row([

        dbc.Col([

            ## selecionar ano -------------------------------------------------
            dcc.Dropdown(
                id='ano-home',
                placeholder = "2023",
                persistence=True,
                persistence_type='session'
            ),
        ], width = 2),

        dbc.Col([
            ## selecionar mês -------------------------------------------------
            dcc.Dropdown(
                id='mes-home',
                placeholder = "Selecionar o mês",
                persistence=True,
                persistence_type='session'
            ),
        ], width = 4),

        dbc.Col([], width = 6)
    ]),

    dbc.Row([
        # gráfico ------------------------------------------------
        dbc.Col([
            dcc.Graph(
                id='grafico-cat',
                config={'displayModeBar': False}
            )
        ], width=9),

        # cards ------------------------------------------------
        dbc.Col([
            dbc.Row([
                html.Div("Gastos previstos"),
                html.Div(id = 'card1')
            ], className='cards'),
            dbc.Row([
                html.Div("Entradas previstas"),
                html.Div(id = 'card2')
            ], className='cards'),
            dbc.Row([
                html.Div("Leftovers"),
                html.Div(id = 'card3')
            ], className='cards')
        ], width=3)

    ]),
])