n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(' \n a soma é {}, \n a multiplicação é {}, \n a divisão é {:.3f} \n'.format(s, m, d), end=' ')
print('a divisão inteira é {} \n e a exponenciação é {}'.format(di, e))

#a função ( contra barra 'n' -> \n )
#serve para quebrar a linha em partes (nova linha)