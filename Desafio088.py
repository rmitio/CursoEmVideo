#DESAFIO088 Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programavai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
jogos = int(input('Quantos Jogos? '))

for j in range(0, jogos):
    jogo = []
    for n in range(0, 6):
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
        else:
            n -= 1
    sleep(2)
    jogo.sort()
    print(f'Jogo {j+1}: {jogo}')
