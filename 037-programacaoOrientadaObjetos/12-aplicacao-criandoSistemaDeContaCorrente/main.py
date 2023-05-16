from contasBancos import *
from numerosConta import *

contasCorrentes=[]

c1=ContaCorrente('Jorge Nami Harbes',10231086741,500)
c2=ContaCorrente('Carolina Ferreira Alcantara',16242112752,1500)
c3=ContaCorrente('Elizabeth Barreto Ramos Ferreira Harbes',39634299768,500000)

print(c1.__dict__)

print(numerosConta.NumerosConta.numerosConta)

c1.saque(200)
c3.deposito(10000000000000)

print(c1.saldo)

c1.numero=55555

print(c1.numero)

print(vars(c3))

print(numerosConta.NumerosConta.numerosConta)


contasCorrentes.append(ContaCorrente('Jorge Nami Harbes',10231086741,500))


print(contasCorrentes)

for conta in contasCorrentes:
    print(conta.__dict__)