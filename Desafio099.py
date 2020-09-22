#DESAFIO099 Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analizar todos valores e dizer qual deles é o maior
from time import sleep


def maior(*num):
    print('-='*30)
    maior = 0
    for n in num:
        if maior < n:
            maior = n
        print(n, end=' ')
        sleep(1)
    print(f' Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()