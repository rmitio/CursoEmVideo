#DESAFIO0103 Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='', gols=0):
    if nome != '' and gols != 0:
        print(f'O Jogador {nome} fez {gols} no campeonato.')
    else:
        if nome == '' and gols == 0:
            print(f'O Jogador <desconhecido> fez 0 gol(s) no campeonato. (Dois vazios)')
        elif nome == '' and (gols != None or gols != ''):
            print(f'O Jogador <desconhecido> fez {gols} gol(s) no campeonato. (Nome Vazio, gol preenchido)')
        elif nome != '' and gols == 0:
            print(f'O Jogador {nome} fez 0 gols no campeonato. (Nome preenchido e gol vazio)')

nome = str(input('Nome do Jogador: '))
gols = input('Número de Gols: ')
ficha(nome, gols)
