#DESAFIO004 Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

a = input('Digite algo: ')
print('O Tipo primitivo é {}'.format(type(a)))
print('É Númerico: ', a.isnumeric())
print('É Letra: ', a.isalpha())
print('É Alfanúmerico: ', a.isalnum())
print('É Minúsculo: ', a.islower())
print('É Maiúsculo: ', a.isupper())
print('É Imprimível: ', a.isprintable())
print('É Capitalizado: ', a.istitle())
print('É Espaço: ', a.isspace())