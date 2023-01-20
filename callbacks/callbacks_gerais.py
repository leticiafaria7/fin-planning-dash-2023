
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
categorias = pd.read_excel(fluxo_caixa, 'categorias', engine = 'openpyxl')
pg_faturas = pd.read_excel(fluxo_caixa, 'pg_faturas', engine = 'openpyxl')

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

# fatura nubank -------------------------------------------------------

def fat_nubank():

    pg_faturas2 = pg_faturas[pg_faturas['cartão'] == 'cartão nubank']
    pg_faturas2 = pg_faturas2[pg_faturas2['pago'] == False].reset_index()

    prox_fat_nubank = "R$ " + str("{:.2f}".format(pg_faturas2.iloc[0]['total']))

    return prox_fat_nubank

# fatura inter -------------------------------------------------------

def fat_inter():

    pg_faturas2 = pg_faturas[pg_faturas['cartão'] == 'cartão inter']
    pg_faturas2 = pg_faturas2[pg_faturas2['pago'] == False].reset_index()

    prox_fat_inter = "R$ " + str("{:.2f}".format(pg_faturas2.iloc[0]['total']))

    return prox_fat_inter

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
            hoverlabel = dict(font = dict(size = 10, color = '#4d4d4d')),
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

@app.callback(
    Output('card1', 'children'),

    Input('mes-home', 'value'),
    Input('ano-home', 'value'),

    prevent_inicial_call = True
)

def card1(mes, ano):

    despesas2 = despesas

    if ano is None:
        ano2 = 2023

    else:
        ano2 = ano

    if mes == "Todos os meses" or mes is None:
        gastos_prev2 = "R$ --"

    else:
        despesas2['mes'] = despesas2['mes'].str.capitalize()
        despesas2 = despesas2[despesas2['ano'] == ano2]
        gastos_prev = despesas2[despesas2['mes'] == mes]['valor'].sum()

        gastos_prev2 = "R$ " + str("{:.2f}".format(gastos_prev))

    return gastos_prev2

# entradas previstas ---------------------------

@app.callback(
    Output('card2', 'children'),

    Input('mes-home', 'value'),
    Input('ano-home', 'value'),

    prevent_inicial_call = True
)

def card2(mes, ano):

    ent_transf2 = ent_transf

    if ano is None:
        ano2 = 2023

    else:
        ano2 = ano

    if mes == "Todos os meses" or mes is None:
        tot_entrada2 = "R$ --"

    else:
        ent_transf2['mes'] = ent_transf2['mes'].str.capitalize()
        ent_transf2 = ent_transf2[ent_transf2['ano'] == ano2]
        ent_prev = ent_transf2[ent_transf2['mes'] == mes]['valor'].sum()
        tot_transf = ent_transf2.loc[ent_transf2['banco de origem'].notnull()]
        tot_transf = tot_transf[tot_transf['mes'] == mes]['valor'].sum()

        tot_entrada = ent_prev - tot_transf

        tot_entrada2 = "R$ " + str("{:.2f}".format(tot_entrada))

    return tot_entrada2

# leftovers ----------------------------------------

@app.callback(
    Output('card3', 'children'),

    Input('mes-home', 'value'),
    Input('ano-home', 'value'),

    prevent_inicial_call = True
)

def card3(mes, ano):

    despesas2 = despesas
    ent_transf2 = ent_transf

    if ano is None:
        ano2 = 2023

    else:
        ano2 = ano

    if mes == "Todos os meses" or mes is None:
        leftovers2 = "R$ --"

    else:
        despesas2['mes'] = despesas2['mes'].str.capitalize()
        despesas2 = despesas2[despesas2['ano'] == ano2]
        gastos_prev = despesas2[despesas2['mes'] == mes]['valor'].sum()

        ent_transf2['mes'] = ent_transf2['mes'].str.capitalize()
        ent_transf2 = ent_transf2[ent_transf2['ano'] == ano2]
        ent_prev = ent_transf2[ent_transf2['mes'] == mes]['valor'].sum()
        tot_transf = ent_transf2.loc[ent_transf2['banco de origem'].notnull()]
        tot_transf = tot_transf[tot_transf['mes'] == mes]['valor'].sum()

        tot_entrada = ent_prev - tot_transf

        leftovers = tot_entrada - gastos_prev

        leftovers2 = "R$ " + str("{:.2f}".format(leftovers))

    return leftovers2

#######################################################################
# TABELA DETALHAMENTO
#######################################################################

@app.callback(

    Output('tabela-detalhamento', 'data'),

    Input('mes-detalhamento', 'value'),
    Input('ano-detalhamento', 'value'),

    prevent_inicial_call = True
)

def tabela_details(mes, ano):

    despesas2 = despesas

    if ano is None:
        ano2 = 2023

    else:
        ano2 = ano

    if mes == "Todos os meses" or mes is None:
        tabela_detalhamento = despesas2.groupby(['macro'])['valor'].sum().sort_values(ascending = False).reset_index()

    else:
        despesas2['mes'] = despesas2['mes'].str.capitalize()
        despesas2 = despesas2[despesas2['ano'] == ano2]
        despesas2 = despesas2[despesas2['mes'] == mes]

        tabela_detalhamento = despesas2.groupby(['macro'])['valor'].sum().sort_values(ascending = False).reset_index()

    tabela_detalhamento['valor'] = tabela_detalhamento['valor'].map('{:,.2f}'.format)
    
    tabela_detalhamento2 = tabela_detalhamento.rename(columns = {
        "macro": 'macro categorias',
    })

    tabela_detalhamento3 = tabela_detalhamento2.to_dict(orient = 'records')

    return tabela_detalhamento3

#######################################################################
# GRÁFICO DETALHAMENTO
#######################################################################

@app.callback(

    Output('grafico-detalhamento', 'figure'),

    Input('tabela-detalhamento', 'active_cell'),
    Input('tabela-detalhamento', 'data'),
    Input('mes-detalhamento', 'value'),
    Input('ano-detalhamento', 'value'),

    prevent_inicial_call = True
)

def graf_detalhamento(
    celula, data, 
    mes, ano
):

    despesas2 = despesas

    if ano is None:
        ano2 = 2023

    else:
        ano2 = ano

    if celula:
        row_aux = str(celula).split(' ')[1]
        coluna_aux = str(celula).split(' ')[3]

        if coluna_aux != "0,":
            
            if mes == "Todos os meses" or mes is None:
                sum_cat = despesas2.groupby(['categoria'])['valor'].sum().sort_values(ascending = True).reset_index()

            else:
                despesas2['mes'] = despesas2['mes'].str.capitalize()
                despesas2 = despesas2[despesas2['ano'] == ano2]
                despesas2 = despesas2[despesas2['mes'] == mes]

                sum_cat = despesas2.groupby(['categoria'])['valor'].sum().sort_values(ascending = True).reset_index()
        
        else:
            df = pd.DataFrame(data, columns = ['macro categorias', 'valor'])
            df['id'] = df.index
            row = row_aux.replace(',', '')
            df = df[df['id'] == int(row)]
            selected = str(df.iloc[0]['macro categorias'])
            despesas3 = despesas2[despesas2['macro'] == selected]

            if mes == "Todos os meses" or mes is None:
                sum_cat = despesas3.groupby(['categoria'])['valor'].sum().sort_values(ascending = True).reset_index()

            else:
                despesas3['mes'] = despesas3['mes'].str.capitalize()
                despesas3 = despesas3[despesas3['ano'] == ano2]
                despesas3 = despesas3[despesas3['mes'] == mes]

                sum_cat = despesas3.groupby(['categoria'])['valor'].sum().sort_values(ascending = True).reset_index()

    else:

        if mes == "Todos os meses" or mes is None:
            sum_cat = despesas2.groupby(['categoria'])['valor'].sum().sort_values(ascending = True).reset_index()

        else:
            despesas2['mes'] = despesas2['mes'].str.capitalize()
            despesas2 = despesas2[despesas2['ano'] == ano2]
            despesas2 = despesas2[despesas2['mes'] == mes]

            sum_cat = despesas2.groupby(['categoria'])['valor'].sum().sort_values(ascending = True).reset_index()

    sum_cat2 = sum_cat

    fig = go.Figure([
        go.Bar(
            y = sum_cat2['categoria'],
            x = sum_cat2['valor'],
            orientation = 'h',
            marker_color = '#d0e0e3',
            textposition = "outside",
            hovertemplate = 'R$ %{x:.2f}<extra></extra>',
            texttemplate = 'R$ %{x:.2f}',
            hoverlabel = dict(font = dict(size = 10, color = '#4d4d4d')),
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
        xaxis_range=[0, max(sum_cat2['valor'])*1.25],
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
# BOTÃO LIMPAR SELEÇÃO
#######################################################################

@app.callback(
    Output("tabela-detalhamento", 'selected_cells'),
    Output('tabela-detalhamento', 'active_cell'),

    Input('clear', 'n_clicks'),

    prevent_initial_call = True
)

def clear(n_clicks):
    return [], None

#######################################################################
# GRÁFICO NUBANK
#######################################################################

@app.callback(
    Output('grafico-nubank', 'figure'),

    Input('ano-nubank', 'value'),
    Input('mes-nubank', 'value'),

    prevent_inicial_call = True
)

def grafico_nubank(ano, mes):

    if ano is None:
        ano2 = 2023

    else:
        ano2 = ano

    despesas2 = despesas[despesas['canal'] == 'cartão nubank']
    despesas2 = despesas2[despesas2['ano'] == ano2]

    sum_cat = despesas2.groupby(['mes'])['valor'].sum().reset_index()
    depara_mes = categorias[['mes_num', 'mes']]
    sum_cat = sum_cat.merge(depara_mes, on = 'mes', how = 'left').sort_values(by = ['mes_num'], ascending=False)

    sum_cat['mes'] = sum_cat['mes'].str.capitalize()

    sum_cat['id'] = range(0, len(sum_cat))

    if(mes):

        if mes == 'Todos os meses':
            marker_color = "#b4a7d6"

        else:
            n_row_graf = len(sum_cat)
            colors = ['#d4d4d4'] * n_row_graf

            id_value = sum_cat[sum_cat.mes == mes]

            select = id_value.iloc[0]['id']
            colors[select] = "#b4a7d6"
            marker_color = colors

    else:
        marker_color = "#b4a7d6"

    fig = go.Figure([
        go.Bar(
            y = sum_cat['mes'],
            x = sum_cat['valor'],
            orientation = 'h',
            marker_color = marker_color,
            textposition = "outside",
            hovertemplate = 'R$ %{x:.2f}<extra></extra>',
            texttemplate = 'R$ %{x:.2f}',
            hoverlabel = dict(font = dict(size = 10, color = '#4d4d4d')),
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
        height = 600,
    )

    return fig

#######################################################################
# TABELA NUBANK
#######################################################################

@app.callback(

    Output('tabela-nubank', 'data'),

    Input('mes-nubank', 'value'),
    Input('ano-nubank', 'value'),

    prevent_inicial_call = True
)

def tabela_details(mes, ano):

    despesas2 = despesas[despesas['canal'] == 'cartão nubank']

    if ano is None:
        ano2 = 2023

    else:
        ano2 = ano

    if mes == "Todos os meses" or mes is None:
        tabela_nubank = despesas2.groupby(['categoria'])['valor'].sum().sort_values(ascending = False).reset_index()

    else:
        despesas2['mes'] = despesas2['mes'].str.capitalize()
        despesas2 = despesas2[despesas2['ano'] == ano2]
        despesas2 = despesas2[despesas2['mes'] == mes]

        tabela_nubank = despesas2.groupby(['categoria'])['valor'].sum().sort_values(ascending = False).reset_index()

    tabela_nubank['valor'] = tabela_nubank['valor'].map('{:,.2f}'.format)
    
    tabela_nubank2 = tabela_nubank.rename(columns = {
        "categoria": 'despesas',
    })

    tabela_nubank3 = tabela_nubank2.to_dict(orient = 'records')

    return tabela_nubank3

#######################################################################
# GRÁFICO INTER
#######################################################################

@app.callback(
    Output('grafico-inter', 'figure'),

    Input('ano-inter', 'value'),
    Input('mes-inter', 'value'),

    prevent_inicial_call = True
)

def grafico_inter(ano, mes):

    if ano is None:
        ano2 = 2023

    else:
        ano2 = ano

    despesas2 = despesas[despesas['canal'] == 'cartão inter']
    despesas2 = despesas2[despesas2['ano'] == ano2]

    sum_cat = despesas2.groupby(['mes'])['valor'].sum().reset_index()
    depara_mes = categorias[['mes_num', 'mes']]
    sum_cat = sum_cat.merge(depara_mes, on = 'mes', how = 'left').sort_values(by = ['mes_num'], ascending=False)

    sum_cat['mes'] = sum_cat['mes'].str.capitalize()
    sum_cat['id'] = range(0, len(sum_cat))

    if(mes):

        if mes == 'Todos os meses':
            marker_color = "#ffe599"

        else:
            n_row_graf = len(sum_cat)
            colors = ['#d4d4d4'] * n_row_graf

            id_value = sum_cat[sum_cat.mes == mes]

            select = id_value.iloc[0]['id']
            colors[select] = "#ffe599"
            marker_color = colors
        
    else:
        marker_color = "#ffe599"

    fig = go.Figure([
        go.Bar(
            y = sum_cat['mes'],
            x = sum_cat['valor'],
            orientation = 'h',
            marker_color = marker_color,
            textposition = "outside",
            hovertemplate = 'R$ %{x:.2f}<extra></extra>',
            texttemplate = 'R$ %{x:.2f}',
            hoverlabel = dict(font = dict(size = 10, color = '#4d4d4d')),
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
        height = 600,
    )

    return fig

#######################################################################
# TABELA INTER
#######################################################################

@app.callback(

    Output('tabela-inter', 'data'),

    Input('mes-inter', 'value'),
    Input('ano-inter', 'value'),

    prevent_inicial_call = True
)

def tabela_details(mes, ano):

    despesas2 = despesas[despesas['canal'] == 'cartão inter']

    if ano is None:
        ano2 = 2023

    else:
        ano2 = ano

    if mes == "Todos os meses" or mes is None:
        tabela_inter = despesas2.groupby(['categoria'])['valor'].sum().sort_values(ascending = False).reset_index()

    else:
        despesas2['mes'] = despesas2['mes'].str.capitalize()
        despesas2 = despesas2[despesas2['ano'] == ano2]
        despesas2 = despesas2[despesas2['mes'] == mes]

        tabela_inter = despesas2.groupby(['categoria'])['valor'].sum().sort_values(ascending = False).reset_index()

    tabela_inter['valor'] = tabela_inter['valor'].map('{:,.2f}'.format)
    
    tabela_inter2 = tabela_inter.rename(columns = {
        "categoria": 'despesas',
    })

    tabela_inter3 = tabela_inter2.to_dict(orient = 'records')

    return tabela_inter3
