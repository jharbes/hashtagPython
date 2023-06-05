"""
### Dash

- Instalar o dash


Estrutura Básica
- plotly -> gráficos
- Flask -> aplicação



### Como funciona o Dash

- Layout (parte visual, frontend)

    - HTML -> textos, imagens, espaços
    - Dash Components (Core Components) -> gráficos, botões que mexem em gráficos, coisas do dashboard


- Callbacks (funcionalidades, backend)

"""

#### Primeiro Dashboard

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd



app = Dash(__name__) # criando o seu aplicativo Dash



# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# BACKEND
# PARTE DE CRIACAO DA LOGICA DO APLICATIVO
df = pd.read_excel('Vendas.xlsx')


# grafico criado com plotly
# tipos de graficos possiveis em plotly https://plotly.com/python/
# o barmode='group' faz com que cada cor esteja em uma coluna independente, facilita a visualizacao
# existem varios tipos de graficos como o px.bar (barra), px.line (linha), px.scatter
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
fig2= px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size='Valor Unitário',size_max=60)




# FRONTEND
# PARTE DA CRIACAO DO LAYOUT DO APLICATIVO

# observe que o abaixo temos uma lista de valores e cada um dos elementos de HTML podem ter outros elementos como itens de uma lista

# podemos utilizar CSS no html por meio do argumento style presente nos elementos HTML, os elementos de css formarão um dicionário nos argumentos, conforme abaixo
app.layout = html.Div(children=[
    html.H1(children='Hello Dash', style={'background-color':'lightgray', 'color':'brown'}),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    html.H2(children='Vendas de cada Produto por Loja'),

    dcc.Graph(id='vendas_por_loja',figure=fig),

    dcc.Graph(id='grafico2', figure=fig2)

], style={'text-align': 'center'})




# CALLBACKS




# colocando o seu site (dashboard) no ar
# caso ocorra bug no debug=True mudar para False
# o debug=True permite que qualquer alteracao no codigo se reflita automaticamente no dashboard que esteja sendo executada, de forma dinamica, mas geralmente essa funcao nao funciona bem no jupyter
if __name__ == '__main__':
    app.run_server(debug=True)
