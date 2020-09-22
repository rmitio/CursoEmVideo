#DESAFIO091 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esess resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencendor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
print('Valores Sorteados:')
jogo = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}
ranking = list()
for k, v in jogo.items():
    print(f'    O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos Jogadores: ')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)