

#######################################################################
# BIBLIOTECAS
#######################################################################

from app import app
from dash.dependencies import Input, Output
from dash import html, dcc
import pandas as pd
import numpy as np
from dash_iconify import DashIconify

########################################################################
# LAYOUT
########################################################################

navbar_contents = [

    # seção contas bancárias -------------------------------------

    html.Div([

        html.Div([
            html.Span("Contas bancárias")
        ], id = 'titulo1', className='titulo-navbar'),

        html.Div([
            html.Div("Inter"),
            html.Div(id = 'total-inter')
        ], className='total-inter-nav'),

         html.Div([
            html.Div("Nubank"),
            html.Div(id = 'total-nubank')
        ], className='total-nubank-nav'),

         html.Div([
            html.Div("Cash"),
            html.Div(id = 'total-cash')
        ], className='total-cash-nav'),

         html.Div([
            html.Div("Banco do Brasil"),
            html.Div(id = 'total-bb')
        ], className='total-bb-nav'),
            
    ]),

    # seção próximas faturas -------------------------------------

    html.Div([
         
         html.Div([
            html.Span("Contas bancárias")
        ], id = 'titulo1', className='titulo-navbar'),

        html.Div([
            html.Div("Cartão Inter"),
            html.Div(id = 'total-cartão-inter')
        ], className='total-c-inter-nav'),

         html.Div([
            html.Div("Nubank"),
            html.Div(id = 'total-cartao-nubank')
        ], className='total-c-nubank-nav'),
    ])

]