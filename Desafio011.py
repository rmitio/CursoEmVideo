#DESAFIO011 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

print('{0} LITROS DE TINTA POR PAREDE {0}'.format('#'*40))
a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede '))
area = a * l
print('A área da parede é {}m², portanto você precisa de {} litros de tinta para pinta-las!'.format(area, area/2))