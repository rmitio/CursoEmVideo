#DESAFIO054 Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. (Maioridade 21 anos)
from datetime import date

atual = date.today().year
menor = 0
maior = 0
for c in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = atual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('Tem {} pessoas menores que 21 anos. \n E {} maiores'.format(menor, maior))