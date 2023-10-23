"""
Algumas maneiras de voltar a um commit antigo:


- No GitHub Desktop:

Imediatamente embaixo do repositório escolhido clicar em 'History', depois ir
no ultimo commit existente e clicar com o segundo botão do mouse e ir na opção
'Revert changes in commit'
OBS**: Só conseguirá fazer um commit de cada vez


Podemos também ir no commit da versão desejada criar uma nova Branch, para isso 
vamos até o commit desejado clicamos com o segundo botão do mouse e vamos na opção
'Create branch from commit' e seguimos ultilizando essa branch, após feitas todas as
alterações podemos fazer um 'merge' novamente com a origin fazendo com que assim a
branch origin tenha os valores desejados do commit em questão



- No GitBash:

Primeiramente teremos duas opçoes:
1a - Retroceder o branch main ao commit desejado
2a - Fazer um merge do branch desejado com o branch main levando ao estado desejado

No terminal usaremos o seguinte comando:

git reset --hard 342105d578af43734260005b788b652ef6438805 (codigo recuperado do commit desejado, podemos
conseguir ele pela opção 'Copy SHA' clicando com o segundo botão do mouse no commit respectivo no próprio
GitHub Desktop ou pelo GitHub achando o commit em questão e apertando na opção 'Copy the full SHA')

ou

git reset --hard <nome_da_branch_desejada_para_fazer_merge> (no caso de fazer um merge do main com a branch
desejada)


Após feitas as alterações será necessário fazer um 'push' dos arquivos atualizados do PC para o
repositório levando as alterações desejadas para o GitHub (a principio só foram feitos na máquina local),
para isso utilizaremos o comando:

git push -f origin main


IMPORTANTE***: O histórico antigo que foi voltado é perdido de maneira definitiva.


"""