
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
    html.Br(),
    
    dbc.Row([
        dbc.Col([
            dbc.Row([
                html.Div([
                    html.Span("Contas bancárias")
                ], id = 'titulo1', className='titulo-navbar'),
                html.Hr()
            ]),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.Div("Inter"),
                        html.Div(id = 'total-inter')
                    ], className='total-inter-nav')
                ]),
                dbc.Col([
                    html.Div([
                        html.Div("Nubank"),
                        html.Div(id = 'total-nubank')
                    ], className='total-nubank-nav')
                ]),
                dbc.Col([
                    html.Div([
                        html.Div("Banco do Brasil"),
                        html.Div(id = 'total-bb')
                    ], className='total-bb-nav')
                ]),
                dbc.Col([
                    html.Div([
                        html.Div("Cash"),
                        html.Div(id = 'total-cash')
                    ], className='total-cash-nav')
                ]),
            ])

        ], width=8),
        dbc.Col([
            dbc.Row([
                html.Div([
                    html.Span("Próximas faturas")
                ], id = 'titulo1', className='titulo-navbar'),
                html.Hr()
            ]),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.Div("Cartão Inter"),
                        html.Div(id = 'total-cartao-inter')
                    ], className='total-c-inter-nav')
                ]),
                dbc.Col([
                    html.Div([
                        html.Div("Cartão Nubank"),
                        html.Div(id = 'total-cartao-nubank')
                    ], className='total-c-nubank-nav')
                ])
            ])
        ], width=4),
    ]),

    html.Br(),

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

    ]),
])