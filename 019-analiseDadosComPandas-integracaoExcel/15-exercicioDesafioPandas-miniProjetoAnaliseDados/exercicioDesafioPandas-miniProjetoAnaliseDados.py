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

# 1. Valor Total da Folha Salarial -> Qual foi o gasto total com salários de funcionários pela empresa? <br>

# Sugestão: calcule o salário total de cada funcionário, salário + benefícios + impostos, depois some todos os salários

cadastroFuncionarios=pd.read_csv('CadastroFuncionarios.csv',sep=';',decimal=',',encoding='utf-8')

cadastroClientes=pd.read_csv('CadastroClientes.csv',sep=';',encoding='utf-8')

baseServicosPrestados=pd.read_excel('BaseServiçosPrestados.xlsx')

print(cadastroFuncionarios)
print()
print(cadastroClientes)

valorTotalFolhaSalarial=cadastroFuncionarios['Salario Base'].sum()+cadastroFuncionarios['Impostos'].sum()+cadastroFuncionarios['Beneficios'].sum()+cadastroFuncionarios['VT'].sum()+cadastroFuncionarios['VR'].sum()

print(f'{valorTotalFolhaSalarial=:.2f}')




# 2. Qual foi o faturamento da empresa?
# Sugestão: calcule o faturamento total de cada serviço e depois some o faturamento de todos

print(baseServicosPrestados)

faturamentoDf=baseServicosPrestados.merge(cadastroClientes, on='ID Cliente')

print(faturamentoDf)

somaFaturamento=0
for linha in faturamentoDf.index:
    somaFaturamento+=faturamentoDf.loc[linha,'Valor Contrato Mensal']*faturamentoDf.loc[linha,'Tempo Total de Contrato (Meses)']
print(f'{somaFaturamento=:.2f}')



print()
# 3. Qual o % de funcionários que já fechou algum contrato?<br>

#    Sugestão: na base de serviços temos o funcionário que fechou cada serviço. Mas nem todos os funcionários que a empresa tem já fecharam algum serviço.<br>

#    . Na base de funcionários temos uma lista com todos os funcionários<br>

#    . Queremos calcular          Qtde_Funcionarios_Fecharam_Serviço / Qtde_Funcionários_Totais<br>  

#    . Para calcular a qtde de funcionários que fecharam algum serviço, use a base de serviços e conte quantos funcionários tem ali. Mas lembre-se, cada funcionário só pode ser contado uma única vez.<br><br>

#    Dica: se você aplicar o método .unique() em uma variável que é apenas 1 coluna de um dataframe, ele vai excluir todos os valores duplicados daquela coluna.<br>

 #   Ex: unicos_colunaA = dataframe['colunaA'].unique() te dá como resposta uma lista com todos os itens da colunaA aparecendo uma única vez. Todos os valores repetidos da colunaA são excluidos da variável unicos_colunaA 

numeroFuncionariosFecharamContrato=baseServicosPrestados['ID Funcionário'].nunique()

numeroFuncionariosTotal=cadastroFuncionarios['ID Funcionário'].count()

print(f'{numeroFuncionariosFecharamContrato=}')
print(f'{numeroFuncionariosTotal=}')

print(f'Percentual de funcionarios que fecharam contrato = {numeroFuncionariosFecharamContrato/numeroFuncionariosTotal*100:.2f}%')




# 4. Calcule o total de contratos que cada área da empresa já fechou

# Areas da empresa: Administrativo, Logística, Financeiro, Operações, Comercial

baseContratosArea=baseServicosPrestados.merge(cadastroFuncionarios, on='ID Funcionário')

print(baseContratosArea)


totalAdministrativo=(baseContratosArea[baseContratosArea['Area']=='Administrativo'])['Area'].count()
print(f'{totalAdministrativo=}')

totalLogistica=(baseContratosArea[baseContratosArea['Area']=='Logística'])['Area'].count()
print(f'{totalLogistica=}')

totalFinanceiro=(baseContratosArea[baseContratosArea['Area']=='Financeiro'])['Area'].count()
print(f'{totalFinanceiro=}')

totalOperacoes=(baseContratosArea[baseContratosArea['Area']=='Operações'])['Area'].count()
print(f'{totalOperacoes=}')

totalComercial=(baseContratosArea[baseContratosArea['Area']=='Comercial'])['Area'].count()
print(f'{totalComercial=}')

print()

# ou

totalContratosArea=baseContratosArea['Area'].value_counts()
print(totalContratosArea)

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
# ou

funcionariosArea=cadastroFuncionarios['Area'].value_counts()
print(funcionariosArea)

print()




# 6. Qual o ticket médio mensal (faturamento médio mensal) dos contratos?<br>
#    Dica: .mean() calcula a média -> exemplo: media_colunaA = dataframe['colunaA'].mean()

ticketMedioMensal=cadastroClientes['Valor Contrato Mensal'].mean()
print(f'{ticketMedioMensal=:.2f}')