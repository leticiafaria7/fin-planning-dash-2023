
#######################################################################
# BIBLIOTECAS
#######################################################################

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
# import dash_html_components

from app import app
from views import home, nubank, inter, details, sidebar
from callbacks import callbacks_gerais

pd.options.mode.chained_assignment = None

#######################################################################
# LAYOUT
#######################################################################

content = html.Div(id='page-content')

app.layout = dbc.Container(
    children=[
        dbc.Row([

            # sidebar ---------------------------------------------------------------------
            dbc.Col([
                dcc.Location(id = 'url'),
                sidebar.layout
            ], md=2, style={'background-color': 'transparent', 'height': '1080px'}),

            # contents da page selecionada -------------------------------------------------
            dbc.Col([
                content
            ], md=10, style={'background-color': 'transparent', 'height': '1080px'})
        ])
    ],
    fluid=True
)

#######################################################################
# CALLBACKS - PAGES
#######################################################################

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)

def render_page(pathname):

    if pathname == '/' or pathname == '/home':
        return home.lagityout

    if pathname == '/fatura-nubank':
        return nubank.layout

    if pathname == '/fatura-inter':
        return inter.layout

    if pathname == '/detalhamento-categorias':
        return details.layout


#######################################################################
# PORT / HOST
#######################################################################

# rodar local
if __name__ == '__main__':
    app.run_server(debug=True)

# criar imagem
# if __name__ == '__main__':
#     app.run_server(port=8080, debug=False, host="0.0.0.0")

