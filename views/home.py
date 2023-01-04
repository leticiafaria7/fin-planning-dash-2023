
#######################################################################
# BIBLIOTECAS
#######################################################################

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from callbacks import callbacks_gerais

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
                        html.Div(children = callbacks_gerais.total_inter(), id = 'total-inter')
                    ], className='total-inter-nav')
                ], width=3),
                dbc.Col([
                    html.Div([
                        html.Div("Nubank"),
                        html.Div(children = callbacks_gerais.total_nubank(), id = 'total-nubank')
                    ], className='total-nubank-nav')
                ], width=3),
                dbc.Col([
                    html.Div([
                        html.Div("Banco do Brasil"),
                        html.Div(children = callbacks_gerais.total_bb(), id = 'total-bb')
                    ], className='total-bb-nav')
                ], width=4),
                dbc.Col([
                    html.Div([
                        html.Div("Cash"),
                        html.Div(children = callbacks_gerais.total_cash(), id = 'total-cash')
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
                        html.Div(children = callbacks_gerais.fat_inter(), id = 'total-cartao-inter')
                    ], className='total-c-inter-nav')
                ], width=6),
                dbc.Col([
                    html.Div([
                        html.Div("Cartão Nubank"),
                        html.Div(children = callbacks_gerais.fat_nubank(), id = 'total-cartao-nubank')
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

        html.Br(),

        dbc.Col([
            ## selecionar ano -------------------------------------------------
            dcc.Dropdown(
                id='ano-home',
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
                id='mes-home',
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

        dbc.Col([], width = 6)
    ], id='dropdown-home'),

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

            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            dbc.Row([
                html.Div("Gastos previstos"),
                html.Div(id = 'card1')
            ], className='cards-gastos'),

            dbc.Row([
                html.Div("Entradas previstas"),
                html.Div(id = 'card2')
            ], className='cards-entradas'),

            dbc.Row([
                html.Div("Leftovers"),
                html.Div(id = 'card3')
            ], className='cards-leftovers')
        ], width=3)

    ]),
])