# fin-planning-dash-2023

*criação de um dashboard que resume os gastos e as entradas mensais em 2023*

## 🖼️ imagens 
enquanto o dash não está disponível para acesso, seguem algumas imagens do desenho da estrutura:

```tela home``` - mostra o quanto tem em cada banco, o valor das próximas faturas, os maiores gastos de acordo com as categorias e, para cada mês, os gastos previstos, as entradas previstas e o quanto está sobrando (ou faltando)

<p align = "left">
  <img src = "https://github.com/leticiafaria7/fin-planning-dash-2023/blob/main/assets/home.png?raw=true" width = "700>
</p>
<br clear="all" />

```tela fatura nubank``` - mostra um gráfico com o valor das faturas de cada mês, e selecionando o mês, é possível ver todos os gastos da fatura com as categorias específicas (valores fictícios)

<p align = "left">
  <img src = "https://github.com/leticiafaria7/fin-planning-dash-2023/blob/main/assets/fatura-nubank.png?raw=true" width = "700>
</p>
<br clear="all" />

```tela fatura inter``` - igual à tela de fatura do nubank, mas com os gastos no cartão inter (valores fictícios)

<p align = "left">
  <img src = "https://github.com/leticiafaria7/fin-planning-dash-2023/blob/main/assets/fatura-inter.png?raw=true" width = "700>
</p>
<br clear="all" />

```tela detalhamento``` - mostra os gastos específicos dentro de cada categoria macro mostradas na tela home

<p align = "left">
  <img src = "https://github.com/leticiafaria7/fin-planning-dash-2023/blob/main/assets/detalhamento.png?raw=true" width = "700>
</p>
<br clear="all" />


## 📊 bases de dados necessárias
para o funcionamento do dash, seguem as estruturas das bases de dados, que devem estar na pasta ```📂 assets```
<br>
o arquivo deve se chamar ```fluxo-caixa.xlsx``` e as abas devem ter os seguintes nomes:

```despesas``` <br>
- base com todas as despesas, sejam recorrentes ou únicas, no cartão ou como boletos

VARIÁVEL | DESCRIÇÃO
:--- | :---
data | data de pagamento, ou uma data no mês em que o gasto deverá ser pago
categoria | categoria específica da despesa, mais abaixo há uma lista de exemplo
valor | valor da despesa, em reais
canal | por onde será pago, ex: banco inter, nubank, cartão de crédito x
pago | se foi pago ou não, tem que estar no formato de ```sim``` ou ```não```
mes_num | colocar a fórmula ```=month()``` para pegar o mês da data imputada - vai estar como numérico
mes | descrever o mês numérico - ex: se mes_num for ```1```, nesta coluna deverá estar ```janeiro```
ano | colocar a fórmula ```=year()``` para pegar o ano da data imputada
macro | colocar a fórmula ```=vlookup()``` para pegar a macro categoria da categoria específica da tabela de categorias

```ent_transf``` <br>
- base para colocar todas as entradas e transferências de um banco para outro

VARIÁVEL | DESCRIÇÃO
:--- | :---
data | data de recebimento ou de transferência
valor | valor recebido ou transferido
banco de origem | se for transferência, colocar banco de origem. se for recebimento, deixar em branco
banco de destino | qual banco recebeu o dinheiro
mes_num | colocar a fórmula ```=month()``` para pegar o mês da data imputada - vai estar como numérico
mes | descrever o mês numérico - ex: se mes_num for ```1```, nesta coluna deverá estar ```janeiro```
ano | colocar a fórmula ```=year()``` para pegar o ano da data imputada

```pg_faturas``` <br>
- lista todos os meses de cada ano para cada cartão (inter e nubank neste caso) e informa se está paga a fatura daquele mês <br>
- a coluna ```pago``` tem um checkbox que, ao subir a base para tratar em python, fica como "True" ou "False"
- ao informar que a fatura foi paga, todas as despesas daquela fatura ficarão como "pagas" na aba de ```despesas```

VARIÁVEL | DESCRIÇÃO
:--- | :---
ano | ano de referência
mes | mês de referência
cartão | cartão (aqui no caso temos inter e nubank apenas)
pago | se a fatura daquele cartão naquele ano e naquele mês foi paga
total | valor total da fatura

```categorias``` <br>
- lista de categorias específicas e suas respectivas categorias macro. exemplo:

CATEGORIA ESPECÍFICA | CATEGORIA MACRO
:--- | :---
mercado/padaria | alimentação
restaurantes | alimentação
aposentadoria | investimentos
comprar casa | investimentos
medicamentos | saúde
consultas médicas | saúde
netflix | streamings
spotify | streamings
combustível | transporte
estacionamento | transporte
