
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

def total_inter():
    ent_inter = ent_transf[ent_transf['banco de destino'] == 'inter']['valor'].sum()
    transf_inter = ent_transf[ent_transf['banco de origem'] == 'inter']['valor'].sum()
    saidas_inter = despesas[despesas['canal'] == 'inter']['valor'].sum()

    tot_inter = ent_inter - transf_inter - saidas_inter

    tot_inter2 = "R$ " + str("{:.2f}".format(tot_inter))

    return tot_inter2

# nubank ---------------------------------------------

def total_nubank():
    ent_nubank = ent_transf[ent_transf['banco de destino'] == 'nubank']['valor'].sum()
    transf_nubank = ent_transf[ent_transf['banco de origem'] == 'nubank']['valor'].sum()
    saidas_nubank = despesas[despesas['canal'] == 'nubank']['valor'].sum()

    tot_nubank = ent_nubank - transf_nubank - saidas_nubank

    tot_nubank2 = "R$ " + str("{:.2f}".format(tot_nubank))

    return tot_nubank2

# banco do brasil -------------------------------------

def total_bb():
    ent_bb = ent_transf[ent_transf['banco de destino'] == 'banco do brasil']['valor'].sum()
    transf_bb = ent_transf[ent_transf['banco de origem'] == 'banco do brasil']['valor'].sum()
    saidas_bb = despesas[despesas['canal'] == 'banco do brasil']['valor'].sum()

    tot_bb = ent_bb - transf_bb - saidas_bb

    tot_bb2 = "R$ " + str("{:.2f}".format(tot_bb))

    return tot_bb2

# cash ---------------------------------------------

def total_cash():
    ent_cash = ent_transf[ent_transf['banco de destino'] == 'cash']['valor'].sum()
    transf_cash = ent_transf[ent_transf['banco de origem'] == 'cash']['valor'].sum()
    saidas_cash = despesas[despesas['canal'] == 'cash']['valor'].sum()

    tot_cash = ent_cash - transf_cash - saidas_cash

    tot_cash2 = "R$ " + str("{:.2f}".format(tot_cash))

    return tot_cash2

#######################################################################
# PRÓXIMAS FATURAS
#######################################################################

#######################################################################
# DROPDOWNS HOME
#######################################################################

#######################################################################
# GRÁFICO HOME
#######################################################################

@app.callback(
    Output('grafico-cat', 'figure'),

    Input('mes-home', 'value'),
    Input('ano-home', 'value'),

    prevent_inicial_call = True
)

def grafico_cat(mes, ano):

    despesas2 = despesas

    if ano is None:
        ano2 = 2023

    else:
        ano2 = ano

    if mes == "Todos os meses" or mes is None:
        sum_cat = despesas2.groupby(['macro'])['valor'].sum().sort_values(ascending = True).reset_index()

    else:
        despesas2['mes'] = despesas2['mes'].str.capitalize()
        despesas2 = despesas2[despesas2['ano'] == ano2]
        despesas2 = despesas2[despesas2['mes'] == mes]

        sum_cat = despesas2.groupby(['macro'])['valor'].sum().sort_values(ascending = True).reset_index()

    fig = go.Figure([
        go.Bar(
            y = sum_cat['macro'],
            x = sum_cat['valor'],
            orientation = 'h',
            marker_color = '#d0e0e3',
            textposition = "outside",
            hovertemplate = 'R$ %{x:.2f}<extra></extra>',
            texttemplate = 'R$ %{x:.2f}',
            textfont = dict(color = '#4d4d4d', size = 10)
        )
    ])

    fig.update_yaxes(
        ticks = 'outside', 
        tickwidth = 2, 
        tickcolor='#fff',
        showline = True, 
        linewidth = 2, 
        linecolor = '#d4d4d4',
        tickfont = dict(size = 10, color = '#4d4d4d')
    )

    fig.update_traces(width = 0.7)

    fig.update_layout(
        yaxis = dict(title = '', showgrid = False),
        xaxis = dict(title = '', showgrid = False, showticklabels = False),
        xaxis_range=[0, max(sum_cat['valor'])*1.15],
        legend = dict(
            orientation = 'h',
            xanchor = 'center',
            yanchor = 'top',
            y = 1.2,
            x = 0.5,
            title_text = '',
            font_family = 'Ubuntu'
        ),
        paper_bgcolor = '#fff',
        plot_bgcolor = '#fff',
        margin_t = 30,
        margin_r = 30,
        height = 450,
    )

    return fig

#######################################################################
# CARDS HOME
#######################################################################

# gastos previstos ---------------------------


# entradas previstas ---------------------------


# leftovers ----------------------------------------