#DESAFIO052 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cont = 0
n = int(input('Digite um número: '))

for c in range(1, n):
    r = n % c
    if r == 0:
        cont += 1

if cont > 1:
    print('Não é Número Primo')
else:
    print('Número Primo')



