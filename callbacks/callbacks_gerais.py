
#######################################################################
# BIBLIOTECAS
#######################################################################

from app import app

from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
import dash
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

#######################################################################
# BASES DE DADOS
#######################################################################

fluxo_caixa = 'assets/fluxo-caixa.xlsx'

despesas = pd.read_excel(fluxo_caixa, "despesas", engine = 'openpyxl')
ent_transf = pd.read_excel(fluxo_caixa, "ent_transf", engine = 'openpyxl')
tot_cat = pd.read_excel(fluxo_caixa, 'tot_cat', engine = 'openpyxl')
tot_mes = pd.read_excel(fluxo_caixa, 'tot_mes', engine = 'openpyxl')
categorias = pd.read_excel(fluxo_caixa, 'categorias', engine = 'openpyxl')

#######################################################################
# CONTAS BANCÁRIAS
#######################################################################

# inter ---------------------------------------------



# nubank ---------------------------------------------

# banco do brasil -------------------------------------

# cash ---------------------------------------------

#######################################################################
# PRÓXIMAS FATURAS
#######################################################################

#######################################################################
# DROPDOWNS HOME
#######################################################################

#######################################################################
# GRÁFICO HOME
#######################################################################

#######################################################################
# CARDS HOME
#######################################################################

# gastos previstos ---------------------------


# entradas previstas ---------------------------


# leftovers ---------------------------


