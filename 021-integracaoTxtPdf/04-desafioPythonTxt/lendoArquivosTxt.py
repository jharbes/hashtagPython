"""
# Integração do Python com Arquivos txt

Como quase tudo no Python, existem várias formas de ler um arquivo no Python.

Aprendemos em módulos passadas a ler arquivos em Excel ou csv com o Pandas, minha recomendação é que, sempre que possível, use o pandas para isso porque ele é um módulo feito para análise de dados e tem muita coisa pronta dentro dele.

Caso queira ler um arquivo txt simplesmente ou escrever um, vamos ver agora como fazer.

### Estrutura:

1. Método open: -> Abre um arquivo txt

arquivo = open('NomeArquivo.txt', 'r')

Usamos 'r' para abrir o arquivo para ler (read) e 'w' quando estamos abrindo o arquivo para escrever (write) ou 'a' se formos adicionar (append) uma informação no arquivo



- Com o arquivo aberto, agora podemos efetivamente ler o arquivo com os métodos:

2. Método read():

texto_arquivo = arquivo.read()

3. Método readlines():

lista_linhas = arquivo.readlines()



- Para escrever alguma coisa no arquivo teremos o método write:

4. Método write():

arquivo.write('Texto que quero escrever')



- Obs: Quando você abre um arquivo, ele permanece aberto no Python até você fechar. Existem 2 formas de fazer isso:

5. Método close():

arquivo.close()

6. Usando a estrutura with: -> ao final do with, a própria estrutura with fecha automaticamente o arquivo

with open('NomeArquivo.txt', 'w') as arquivo:
    arquivo.write()
    ...

"""


### 1. Método open: -> Abre um arquivo txt

# Usamos 'r' para abrir o arquivo para ler (read) e 'w' quando estamos abrindo o arquivo para escrever (write) ou 'a' se formos adicionar (append) uma informação no arquivo
arquivo=open('Alunos.txt','r')




### - Com o arquivo aberto, agora podemos efetivamente ler o arquivo com os métodos:

print(arquivo.read()) # imprime exatamente como o arquivo se encontra no bloco de notas

print(arquivo.readlines()) # transforma o arquivo em uma lista python onde cada linha é um elemento da lista

print(type(arquivo.readlines())) # <class 'list'>

print(len(arquivo.readlines())) # 0

arquivo.close()
print('--------------------------------')




### - Para escrever alguma coisa no arquivo teremos o método write:

# ***IMPORTANTE: o parametro 'w' ao abrir o arquivo cria o arquivo caso ele nao exista, no caso dele ja existir ele APAGA todo o conteudo existente do arquivo e comeca do zero a edição, para continuar a edição de um arquivo com algo já escrito, preservando o texto existente devemos usar o parametro 'a' de append (adição)
novoArquivo=open('resumo.txt','w')


# caso nao seja utilizado o \n na edição não havera pulo de linhas
novoArquivo.write('Testando edição de arquivo')
novoArquivo.write('Escrevendo mais\npulando linha')
novoArquivo.writelines('teste')
novoArquivo.writelines('teste novo')


# ao editar se faz necessário fechar o arquivo para que as mudanças no arquivo sejam salvas, caso contrario nada será salvo no arquivo
novoArquivo.close()




### Método with para Txt: Usando a estrutura with: -> ao final do with, a própria estrutura with fecha automaticamente o arquivo, torna-se desnecessario o .close ao final para salvar o arquivo

with open('resumo2.txt','w') as novoArquivo2:
    novoArquivo2.write('Segundo teste,\ntestando agora edição de txt com o método with\n')
    novoArquivo2.write('continuando o texto')

print('fim do codigo de edição com metodo with')




"""
### Desafio onde vamos aprender:

- Na Hashtag, sempre analisamos o nosso "Funil de Vendas". Para isso, rastreamos de onde veio os alunos por meio de um código, do tipo:
    - hashtag_site_org -> Pessoas que vieram pelo site da Hashtag
    - hashtag_yt_org -> Pessoas que vieram pelo Youtube da Hashtag
    - hashtag_ig_org -> Pessoas que vieram pelo Instagram da Hashtag
    - hashtag_igfb_org -> Pessoas que vieram pelo Instagram ou Facebook da Hashtag

Os códigos diferentes disso, são códigos de anúncio da Hashtag.

- Queremos analisar quantos alunos vieram de anúncio e quantos vieram "orgânico".
- Qual a melhor fonte "orgânica" de alunos

Obs: orgânico é tudo aquilo que não veio de anúncios.

No nosso sistema, conseguimos exportar um txt com as informações dos alunos, conforme o arquivo Alunos.txt

(Os dados foram gerados aleatoriamente para simular uma situação real, já que não podemos fornecer os dados reais dos alunos por questões de segurança)

- No final, para treinar, vamos escrever todas essas respostas em um novo arquivo txt

"""

arquivoAlunos=open('Alunos.txt','r')

listaArquivoAlunos=arquivoAlunos.readlines()

print(listaArquivoAlunos)


clientesOrganico=0
clientesAnuncio=0
clientesSite=0
clientesYoutube=0
clientesInstagram=0
clientesFbOuInstagram=0
for linha in listaArquivoAlunos:
    if 'origemurl:' in linha:
        if '_org' in linha:
            clientesOrganico+=1
            if 'hashtag_site_org' in linha:
                clientesSite+=1
            if 'hashtag_yt_org' in linha:
                clientesYoutube+=1
            if 'hashtag_ig_org' in linha:
                clientesInstagram+=1
            if 'hashtag_igfb_org' in linha:
                clientesFbOuInstagram+=1
        else:
            clientesAnuncio+=1

totalClientes=clientesAnuncio+clientesOrganico

print(f'{totalClientes=}')
print(f'{clientesAnuncio=}')
print(f'{clientesOrganico=}')
print('--------------------')
print(f'{clientesSite=}')
print(f'{clientesYoutube=}')
print(f'{clientesInstagram=}')
print(f'{clientesFbOuInstagram=}')

with open('indicadores.txt','w') as arquivoIndicadores:
    arquivoIndicadores.write(f'{totalClientes=}\n')
    arquivoIndicadores.write(f'{clientesAnuncio=}\n')
    arquivoIndicadores.write(f'{clientesOrganico=}\n')
    arquivoIndicadores.write('--------------------\n')
    arquivoIndicadores.write(f'{clientesSite=}\n')
    arquivoIndicadores.write(f'{clientesYoutube=}\n')
    arquivoIndicadores.write(f'{clientesInstagram=}\n')
    arquivoIndicadores.write(f'{clientesFbOuInstagram=}\n')

arquivoAlunos.close()