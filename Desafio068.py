#DESAFIO068 Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
n = v = 0
while True:
    n = int(input('Digite um valor: '))
    pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    c = randint(0, 10)
    soma = c + n
    if soma % 2 == 0:
        r = 'P'
    else:
        r = 'I'
    print(f'Você jogou {n} e o computador jogou {c}. Total de {soma}.')
    if r == pi:
        print('Você VENCEU!')
        v += 1
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {v} vezes.')

