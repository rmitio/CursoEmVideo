#DESAFIO0100 Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anteior.

from random import randint
from time import sleep

números = list()


def sortear():
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        num = randint(0, 10)
        números.append(num)
        sleep(1)
        print(num, end=' ')
    print('PRONTO!')


def somaPar():
    s = 0
    for n in números:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {números}, temos {s}', end='')


sortear()
somaPar()



