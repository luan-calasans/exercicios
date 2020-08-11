# FAÇA UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA
# TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES
# ELA PODE COMPRAR - COTAÇÃO HOJE (US$1,00 = R$5,44)

n1 = int(input('Digite quantos reais você tem na carteira: '))
c = n1 / 5.44
print('Seu dinheiro atualmente vale {:.2f} dólares'.format(c))
