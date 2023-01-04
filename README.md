# fin-planning-dash-2023

*criação de um dashboard que resume os gastos e as entradas mensais em 2023*

## 🖼️ imagens 
enquanto o dash não está disponível, seguem algumas imagens do desenho da estrutura

## 📊 bases de dados necessárias
para o funcionamento do dash, seguem as estruturas das bases de dados, que devem estar na pasta ```📂 assets```
<br>
o arquivo deve se chamar ```fluxo-caixa.xlsx``` e as abas devem ter os seguintes nomes:

```despesas``` <br>
- base com todas as despesas, sejam recorrentes ou únicas, no cartão ou como boletos

variável | descrição
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

variável | descrição
:--- | :---
data | data de recebimento ou de transferência
valor | valor recebido ou transferido
banco de origem | se for transferência, colocar banco de origem. se for recebimento, deixar em branco
banco de destino | qual banco recebeu o dinheiro
mes_num | colocar a fórmula ```=month()``` para pegar o mês da data imputada - vai estar como numérico
mes | descrever o mês numérico - ex: se mes_num for ```1```, nesta coluna deverá estar ```janeiro```
ano | colocar a fórmula ```=year()``` para pegar o ano da data imputada

```pg_faturas``` <br>

```categorias``` <br>
- lista de categorias específicas e suas respectivas categorias macro. exemplo:

categoria especifica | categoria macro
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
