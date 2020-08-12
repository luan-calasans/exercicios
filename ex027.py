# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA
# TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO

from math import sin, cos, tan, radians
sct = int(input('Digite o ângulo que você deseja: '))
s = sin(radians(sct))
c = cos(radians(sct))
t = tan(radians(sct))
print(' \n O ângulo {} tem SENO igual a {:.2f} \n O ângulo {} tem COSSENO igual a {:.2f} \n O ângulo {} tem TANGENTE igual a {:.2f}'.format(sct, s, sct, c, sct, t))