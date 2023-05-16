# Criando nossa 1ª Classe em Python

# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

class TV:
    def __init__(self) -> None:
        self.cor='preta'
        self.ligada=False
        self.tamanho=55
        self.canal='Netflix'
        self.volume=10


tvSala=TV()
tvQuarto=TV()

print(tvSala.__dict__) # {'cor': 'preta', 'ligada': False, 'tamanho': 55, 'canal': 'Netflix', 'volume': 10}