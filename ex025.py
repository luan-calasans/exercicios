# CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER
# PELO TECLADO E MOSTRE A SUA PORÇÃO INTEIRA

# E X E M P L O ::
# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

from math import trunc
real = float(input('Digite um número: '))
print('O número {} tem a porção inteira {}'.format(real, trunc(real)))

# 1 - PODE SER FEITO TAMBÉM::

# import math
# real = float(input('Digite um número: '))
# print('O número {} tem a porção inteira {}'.format(real, math.trunc(porcao)))

# 2 - PODE SER FEITO TAMBÉM::

# real = float(input('Digite um número: '))
# print('O número {} tem a porção inteira {}'.format(real, int(real)))