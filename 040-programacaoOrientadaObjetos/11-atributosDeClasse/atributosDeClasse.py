
# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

#classes
class TV:

    # atributos de classe
    cor = 'preta'

    def __init__(self, tamanho):
        # atributos de instancia
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal


#programa
tv_sala = TV(55)
tv_quarto = TV(70)

print(tv_sala.tamanho) # 55
print(tv_quarto.tamanho) # 70

print(tv_sala.cor) # preta
print(tv_quarto.cor) # preta

tv_quarto.cor='amarela'

print(tv_quarto.cor) # amarela
print(tv_sala.cor) # preta

# altera o valor global, no entanto se ja tiver sido alterado apos a criacao da classe nao sera atingido por essa modificacao
TV.cor='branca'

print(tv_quarto.cor) # amarela
print(tv_sala.cor) # branca