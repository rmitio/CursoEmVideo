#DESAFIO022 Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas. O nome Com todas letras Minúsculas. Quantas letras ao todo sem considerar espaços. Quantas letras tem o primeiro nome.

nome = input('Digite seu nome: ')
print('O nome completo com todas letras Maiúsculas: {}'.format(nome.upper()))
print('O nome completo com todas letras Minúsculas: {}'.format(nome.lower()))
print('O seu nome tem {} caracteres no total.(contando com espaços)!'.format(len(nome)))
dividido = nome.split()
print('O seu nome tem {} letras no total.'.format(len(''.join(dividido))))
print('O seu primeiro nome tem {} letras'.format(len(dividido[0])))
