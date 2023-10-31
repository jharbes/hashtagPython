"""
### Operadores


    [] – conjunto de  caracteres;
    \ – sequência especial de caracteres;
    ^ – buscar elementos no início da string;
    $ – buscar elementos no final da string;
    * – buscar zero ou mais repetições de uma substring;
    + – uma ou mais aparições de uma substring;
    ? – zero ou uma aparição;
    | – busca um caractere ou outro.
    {} - quantidade específica de caracteres
    [^] - diferente de um caractere especificado logo após o ^
    () - apenas para agrupar regras e definir ordem de aplicação (igual matemática)

    
### Especificando caracteres:
    . - qualquer caractere
    \d - qualquer dígito
    \D - não é dígito
    \w - qualquer alfanumérico
    \W - não é alfanumérico
    \s - espaço em branco
    \S - não é espaço em branco

    
#### obs: lembre de usar a string como raw string


### Funções
#### Lembre sempre de importar a biblioteca re

- re.compile('padrao_regex') -> compilar um padrão regex
- re.search(padrao_compilado, texto) -> procura uma ocorrência do padrão no texto (re.match só procura na 1ª linha do texto)
- re.findall(padrao_compilado, texto) -> encontra todas as ocorrencias do padrão em um texto - armazena em uma lista
- re.finditer(padrao_compilado, texto) -> encontra todas as ocorrencias e armazena em um iterador

"""

texto = """
Bom dia,

Seguem os orçamentos solicitados:


Cerveja importada (330 ml) - R$12,30598615178 - bebida
Cerveja nacional (0,5 litros) - R$6,10 - bebida
Garrafa de vinho (750ml) - R$39,90 - bebida
Água (garrafa de 1,5 litros) - R$3,30 - bebida
Alface (1 unidade) - R$3,50 - comida
Cebolas (1kg) - R$5,10 - comida
Batatas (1 kg) - R$5,20 - comida
Tomates (1 kg) - R$7,90 - comida
Laranjas (1 kg) - R$4,70 - comida
Bananas (1kg) - R$5,50 - comida
Maçãs (1 kg) - R$8,30 - comida
Queijo fresco (1 kg) - R$42,90 - comida
Uma dúzia de ovos(12) - R$9,80 - comida
Arroz (1 kg) - R$5,70 - comida
Um quilo de pão (1 kg) - R$7,20 - comida
Leite (1 litro) - R$5,20 - bebida
Azeite (1 unidade) - R$20 - tempero
Pimenta Reino (20g) - R$5 - tempero


Favor informar as quantidades desejadas 
para emissão da Nota Fiscal.

Att.,"""


#### Ex: Quantos itens

# importando a biblioteca REGEX
import re

# quantas comidas
# o metodo re.compile() passa o padrao que desejamos que seja procurado
padrao=re.compile('comida')
resultado=re.findall(padrao, texto)

print(resultado) # ['comida', 'comida', 'comida', 'comida', 'comida', 'comida', 'comida', 'comida', 'comida', 'comida', 'comida']

print(len(resultado)) # 11




# quantas bebidas
padrao2=re.compile('bebida')
resultado2=re.findall(padrao2, texto)

print(resultado2) # ['bebida', 'bebida', 'bebida', 'bebida', 'bebida']

print(len(resultado2)) # 5




# o metodo re.compile() passa o padrao que desejamos que seja procurado
padrao=re.compile('comida')

# o metodo re.search() retorna um objeto com a primeira ocorrencia desse padrao, mostra o que encontrou e a posicao encontrada (caractere inicial e caractere final em relacao a string inteira) 
resultado=re.search(padrao, texto)

print(resultado) # <re.Match object; span=(271, 277), match='comida'>

print(resultado.group(0)) # comida




# o metodo re.compile() passa o padrao que desejamos que seja procurado
padrao=re.compile('comida')

# o metodo re.finditer() cria um objeto iterador, onde nele cada um dos elementos serão todos os resultados para o padrao procurado
resultado=re.finditer(padrao, texto)

print(resultado) # <callable_iterator object at 0x000002CDA83B2FE0>

for item in resultado:
    print(item)
"""
<re.Match object; span=(271, 277), match='comida'>
<re.Match object; span=(303, 309), match='comida'>
<re.Match object; span=(336, 342), match='comida'>
<re.Match object; span=(369, 375), match='comida'>
<re.Match object; span=(403, 409), match='comida'>
<re.Match object; span=(435, 441), match='comida'>
<re.Match object; span=(466, 472), match='comida'>
<re.Match object; span=(506, 512), match='comida'>
<re.Match object; span=(546, 552), match='comida'>
<re.Match object; span=(577, 583), match='comida'>
<re.Match object; span=(618, 624), match='comida'>
"""




# quantos itens

# para todos os caracteres especiais que sao usados como operadores do regex (o $ por exemplo) utilizaremos uma contra barra ('\') antes dele
padrao3=re.compile('\$')

resultado3=re.findall(padrao3,texto)

print(resultado3) # ['$', '$', '$', '$', '$', '$', '$', '$', '$', '$', '$', '$', '$', '$', '$', '$', '$', '$']

print(len(resultado3)) # 18