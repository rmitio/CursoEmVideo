#DESAFIO0106 Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS: Use cores.
#\033[0;33;44m
from time import sleep

def Ajuda(com):
    print('\033[7;30m', end='')
    help(com)
    print('\033[m', end='')


def Imprimir(txt, cores='\033[m'):
    print(cores, end='')
    print(f'~' * len(txt))
    print(txt)
    print(f'~' * len(txt))
    print('\033[m', end='')

comando = ''
while True:
    Imprimir(' SISTEMA DE AJUDA PyHELP', '\033[30;43m')
    comando = str(input('Função ou Biblioteca: ')).lower()
    if comando == 'fim':
        Imprimir('ATÉ LOGO', '\033[30;41m')
        break
    Imprimir(f' Acessando o Manual do comando \'{comando}\'', '\033[30;44m')
    sleep(0.75)
    Ajuda(comando)


