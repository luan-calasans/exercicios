# Escreva um programa que converta uma temperatura digitando
# em graus Celsius e converta para graus Fahrenheit.

print('CONVERSOR DE CELSIUS PARA FAHRENHEIT')
grausc = float(input('Digite em Celsius para converter: '))
fahren = (grausc * 1.8) + 32
print('A temperatura convertida em Fahrenheit é {:.1f}ºF'.format(fahren))
