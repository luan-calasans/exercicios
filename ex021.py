# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E
# MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO

preco = float(input('Digite o preço do produto: R$'))
desconto = preco * 0.05
cdesconto = preco - desconto
# 5% = 0,05
print('O valor do produto com desconto é R${:.2f}'.format(cdesconto))

