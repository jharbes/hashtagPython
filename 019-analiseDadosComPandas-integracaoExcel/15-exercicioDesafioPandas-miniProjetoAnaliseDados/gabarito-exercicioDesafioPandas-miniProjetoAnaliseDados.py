"""

# Exercício - Mini Projeto de Análise de Dados

Vamos fazer um exercício completo de pandas para um miniprojeto de análise de dados.

Esse exercício vai obrigar a gente a usar boa parte dos conhecimento de pandas e até de outros módulos que já aprendemos ao longo do curso.

### O que temos?

Temos os dados de 2019 de uma empresa de prestação de serviços. 

- CadastroFuncionarios
- CadastroClientes
- BaseServiçosPrestados

Obs1: Para ler arquivos csv, temos o read_csv<br>
Obs2: Para ler arquivos xlsx (arquivos em excel normais, que não são padrão csv), temos o read_excel

### O que queremos saber/fazer?

1. Valor Total da Folha Salarial -> Qual foi o gasto total com salários de funcionários pela empresa? <br>
    Sugestão: calcule o salário total de cada funcionário, salário + benefícios + impostos, depois some todos os salários
    
    
2. Qual foi o faturamento da empresa?<br>
    Sugestão: calcule o faturamento total de cada serviço e depois some o faturamento de todos
    
    
3. Qual o % de funcionários que já fechou algum contrato?<br>
    Sugestão: na base de serviços temos o funcionário que fechou cada serviço. Mas nem todos os funcionários que a empresa tem já fecharam algum serviço.<br>
    . Na base de funcionários temos uma lista com todos os funcionários<br>
    . Queremos calcular Qtde_Funcionarios_Fecharam_Serviço / Qtde_Funcionários_Totais<br>
    . Para calcular a qtde de funcionários que fecharam algum serviço, use a base de serviços e conte quantos funcionários tem ali. Mas lembre-se, cada funcionário só pode ser contado uma única vez.<br><br>
    Dica: se você aplicar o método .unique() em uma variável que é apenas 1 coluna de um dataframe, ele vai excluir todos os valores duplicados daquela coluna.<br>
    Ex: unicos_colunaA = dataframe['colunaA'].unique() te dá como resposta uma lista com todos os itens da colunaA aparecendo uma única vez. Todos os valores repetidos da colunaA são excluidos da variável unicos_colunaA 
    
    
4. Calcule o total de contratos que cada área da empresa já fechou


5. Calcule o total de funcionários por área


6. Qual o ticket médio mensal (faturamento médio mensal) dos contratos?<br>
    Dica: .mean() calcula a média -> exemplo: media_colunaA = dataframe['colunaA'].mean()

Obs: Lembrando as opções mais usuais de encoding:<br>
encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' ou então encoding='cp1252'

Observação Importante: Se o seu código der um erro na hora de importar os arquivos:<br>
- CadastroClientes.csv
- CadastroFuncionarios.csv

Use separador ";" (ponto e vírgula) para resolver

"""

import pandas as pd

funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')

funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)
print(funcionarios_df)
print(clientes_df)
print(servicos_df)




# 1. Valor Total da Folha Salarial -> Qual foi o gasto total com salários de funcionários pela empresa? <br>

# Sugestão: calcule o salário total de cada funcionário, salário + benefícios + impostos, depois some todos os salários

# como a coluna salario total nao existe ela sera criada
funcionarios_df['Salario Total'] = funcionarios_df['Salario Base'] + funcionarios_df['Impostos'] + funcionarios_df['Beneficios'] + funcionarios_df['VT'] + funcionarios_df['VR']
print('Total da Folha Salarial Mensal é de R${:,}'.format(funcionarios_df['Salario Total'].sum()))




# 2. Qual foi o faturamento da empresa?
# Sugestão: calcule o faturamento total de cada serviço e depois some o faturamento de todos

faturamentos_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente' ,'Valor Contrato Mensal']], on='ID Cliente')

faturamentos_df['Faturamento Total'] = faturamentos_df['Tempo Total de Contrato (Meses)'] * faturamentos_df['Valor Contrato Mensal']

print('Faturamento Total: R${:,}'.format(sum(faturamentos_df['Faturamento Total'])))



print()




# 3. Qual o % de funcionários que já fechou algum contrato?<br>

#    Sugestão: na base de serviços temos o funcionário que fechou cada serviço. Mas nem todos os funcionários que a empresa tem já fecharam algum serviço.<br>

#    . Na base de funcionários temos uma lista com todos os funcionários<br>

#    . Queremos calcular          Qtde_Funcionarios_Fecharam_Serviço / Qtde_Funcionários_Totais<br>  

#    . Para calcular a qtde de funcionários que fecharam algum serviço, use a base de serviços e conte quantos funcionários tem ali. Mas lembre-se, cada funcionário só pode ser contado uma única vez.<br><br>

#    Dica: se você aplicar o método .unique() em uma variável que é apenas 1 coluna de um dataframe, ele vai excluir todos os valores duplicados daquela coluna.<br>

 #   Ex: unicos_colunaA = dataframe['colunaA'].unique() te dá como resposta uma lista com todos os itens da colunaA aparecendo uma única vez. Todos os valores repetidos da colunaA são excluidos da variável unicos_colunaA 

qtde_funcionario_fecharamcontrato = len(servicos_df['ID Funcionário'].unique())

qtde_funcionario_total = len(funcionarios_df['ID Funcionário'])

print('Percentual Funcionários Fecharam Contrato: {:.2%}'.format(qtde_funcionario_fecharamcontrato / qtde_funcionario_total))




# 4. Calcule o total de contratos que cada área da empresa já fechou

# Areas da empresa: Administrativo, Logística, Financeiro, Operações, Comercial

contratos_area_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário')
contratos_area_qtde = contratos_area_df['Area'].value_counts()
print(contratos_area_qtde)

print()



# 5. Calcule o total de funcionários por área

# Areas da empresa: Administrativo, Logística, Financeiro, Operações, Comercial

areasEmpresa=cadastroFuncionarios['Area'].unique()
print(areasEmpresa)


totalFuncionariosAdministrativo=(cadastroFuncionarios[cadastroFuncionarios['Area']=='Administrativo'])['Area'].count()
print(f'{totalFuncionariosAdministrativo=}')

totalFuncionariosLogistica=(cadastroFuncionarios[cadastroFuncionarios['Area']=='Logística'])['Area'].count()
print(f'{totalFuncionariosLogistica=}')

totalFuncionariosFinanceiro=(cadastroFuncionarios[cadastroFuncionarios['Area']=='Financeiro'])['Area'].count()
print(f'{totalFuncionariosFinanceiro=}')

totalFuncionariosOperacoes=(cadastroFuncionarios[cadastroFuncionarios['Area']=='Operações'])['Area'].count()
print(f'{totalFuncionariosOperacoes=}')

totalFuncionariosComercial=(cadastroFuncionarios[cadastroFuncionarios['Area']=='Comercial'])['Area'].count()
print(f'{totalFuncionariosComercial=}')

print()




# 6. Qual o ticket médio mensal (faturamento médio mensal) dos contratos?<br>
#    Dica: .mean() calcula a média -> exemplo: media_colunaA = dataframe['colunaA'].mean()

ticketMedioMensal=cadastroClientes['Valor Contrato Mensal'].mean()
print(f'{ticketMedioMensal=:.2f}')