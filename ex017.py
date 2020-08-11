# ESCREVA UM PROGRAMA QUE LEIA UM VALOR
# EM METROS E EXIBA CONVERTIDO EM
# CENTÍMETROS E MILÍMETROS

n1 = float(input('Digite um valor em metros: '))
c = n1 * 100
m = n1 * 1000
print('> {:.0f} metros vale: \n {:.0f} centímetros \n {:.0f} milímetros'.format(n1, c, m))