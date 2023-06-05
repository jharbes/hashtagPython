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




# FRONTEND
# PARTE DA CRIACAO DO LAYOUT DO APLICATIVO
app.layout = html.Div(children=[
    html.H1(children='My Dashboard'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])




# colocando o seu site (dashboard) no ar
# caso ocorra bug no debug=True mudar para False
# o debug=True permite que qualquer alteracao no codigo se reflita automaticamente no dashboard que esteja sendo executada, de forma dinamica, mas geralmente essa funcao nao funciona bem no jupyter
if __name__ == '__main__':
    app.run_server(debug=True)
