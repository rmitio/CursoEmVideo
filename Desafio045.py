#DESAFIO045 Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''[0] PEDRA
[1] PAPEL 
[2] TESOURA
''')
j = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

print('-='*11)
print('O Computador Escolhe {}'.format(itens[computador]))
print('Jodador jogou {}'.format(itens[j]))
print('-='*11)
if computador == 0:
    if j == 0:
        print('EMPATE')
    elif j == 1:
        print('JOGADOR VENCE')
    elif j == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if j == 0:
        print('COMPUTADOR VENCE')
    elif j == 1:
        print('EMPATE')
    elif j == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if j == 0:
        print('JOGADOR VENCE')
    elif j == 1:
        print('COMPUTADOR VENCE')
    elif j == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
