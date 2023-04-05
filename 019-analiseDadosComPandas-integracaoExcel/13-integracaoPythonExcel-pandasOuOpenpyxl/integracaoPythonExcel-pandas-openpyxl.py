"""

# Integração Python + Excel

### 2 formas:

1. Pandas
    - Mais usada no geral
    - Trata o Excel como uma base de dados
    - Faz o que quiser com o arquivo
    - Pode desfazer a estrutura original do arquivo, caso queira editar
    
2. Openpyxl
    - Trata o Excel como uma planilha mesmo que pode ter várias coisas
    - Edita "como se fosse um VBA"
    - Menos eficiente
    - Mantém mais a estrutura original do arquivo, mas cuidado porque não necessariamente tudo, então tem que testar

"""

### Desafio

# - Temos uma planilha de produtos e serviços. Com o aumento de imposto sobre os serviços, temos que atualizar o preço dos produtos impactados pela mudança.

# Novo Multiplicador Imposto: 1.5

# pandas

