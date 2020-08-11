# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO
# E MOSTRE SEU NOVO SALÁRIO COM 15% DE AUMENTO

salario = float(input('Digite seu salario atual: R$'))
aumento = 0.15 * salario
saumento = salario + aumento
print('Você merece!', end=' ')
print('Agora seu salário é R${:.2f}'.format(saumento))