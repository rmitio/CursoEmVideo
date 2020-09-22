#DESAFIO025 Crie um programa que leia o nome de uma pessoa e diga se ela tem o nome "SILVA" no nome.
nome = input('Digite seu nome completo: ').strip()
print('SILVA' in nome.upper())

'''
if 'SILVA' in nome.upper():
    print('Você tem Silva no nome!')
else:
    print('Você não tem Silva no nome!')
'''
