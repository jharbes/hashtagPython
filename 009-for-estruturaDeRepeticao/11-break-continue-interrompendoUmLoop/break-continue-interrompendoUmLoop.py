# Formas de interromper um for

### 2 Opções:

# - break -> interrompe e finaliza o for
# - continue -> interrompe e vai para o próximo item do for

vendas = [100, 150, 1500, 2000, 120]




# - Caso 1: Se todas as vendas forem acima da meta, a loja ganha bônus

meta = 110

mensagem_bonus='Loja ganhou o bônus'
for venda in vendas:
    if venda<=110:
        mensagem_bonus='Loja não ganhou o bônus'
        break
print(mensagem_bonus)




# - Caso 2: Exiba quem bateu a meta

vendedores = ['João', 'Julia', 'Ana', 'José', 'Maria']
meta = 130

for i,vendedor in enumerate(vendedores):
    if vendas[i]>=meta:
        print(vendedor,'bateu a meta.')