# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE
# EM METROS, CALCULE SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA
# PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA A CADA 2m²

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = (area / 2)
# 1 litro de tinta -> pinta -> 1 área a cada 2m²
print('\n A área da parede é igual a: {:.3f}m² \n Sendo assim, você precisará de {:.3f} litros de tinta para pintar a parede'.format(area, tinta))
