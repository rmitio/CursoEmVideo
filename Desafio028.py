#DESAFIO028 Esscreva um programa que faça o computador "pensar" em um númeri inteiro entre 0 e 5 e peça par ao usuário tentar  descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar ...')
print('-=-' * 20)
n = int(input('Em que número pensei?'))
pc = randint(0, 5)
if n == pc:
    print('GANHOU! Pensei no número {}'.format(pc))
else:
    print('PERDEU! Pensei no número {}'.format(pc))