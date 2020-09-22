#DESAFIO008 Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
print('{0}METROS, CENTIMETROS E MILIMETROS {0}'.format('*'*30))
m = float(input('Digite o valor em metros:'))
print('Você digite o valor em metros: {}, que em centrimetors equivale a {} centimetros, e em milimetros equivale a {} milimetros'.format(m, int(m*100), int(m*1000)))