from contasBancos import *

c1=ContaCorrente('Jorge Nami Harbes',10231086741,500)
c2=ContaCorrente('Carolina Ferreira Alcantara',16242112752,1500)
c3=ContaCorrente('Elizabeth Barreto Ramos Ferreira Harbes',39634299768,500000)

print(c1.__dict__)

print(numerosConta.NumerosConta.numerosConta)

c1.saque(200)

print(c1.saldo)

c1.numero=55555

print(c1.numero)

print(numerosConta.NumerosConta.numerosConta)
