
#######################################################################
# BIBLIOTECAS
#######################################################################

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
# import dash_html_components

# from app import app
from views import home, nubank, inter, details, sidebar
from callbacks import callbacks_gerais

pd.options.mode.chained_assignment = None

#######################################################################
# APP
#######################################################################

app = Dash(
    __name__,
    external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    update_title = "Atualizando ...",
    # suppress_callback_exceptions = True
)

app.title = "Planejamento Financeiro"
server = app.server

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
        return home.layout

    if pathname == '/fatura-nubank':
        return nubank.layout

    if pathname == '/fatura-inter':
        return inter.layout

    if pathname == '/detalhamento-categorias':
        return details.layout


#######################################################################
# PORT / HOST
#######################################################################

if __name__ == '__main__':
    app.run_server(debug=True)

