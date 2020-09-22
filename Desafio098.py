'''DESAFIO098 Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C)Uma contagem personalizada
'''
from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    if i > f and p > 0:
        p -= (p + p)
    if p < 0:
        print(f'Contagem de {i} até {f} de {-p} em {-p}')
    else:
        print(f'Contagem de {i} até {f} de {p} em {p}')
    for a in range(i, f, p):
        sleep(0.5)
        print(f'{a} ', end='')
    print()


contador(1, 11, 1)
contador(10, 0, -2)
print("Agora é sua vez de personalizar a contagem! ")
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
