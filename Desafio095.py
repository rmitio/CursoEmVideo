#DESAFIO095 Aprimore o DESAFIO093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador

aproveitamento = {}
aproveitamento['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {aproveitamento["Nome"]} jogou? '))
aproveitamento['gols'] = list()
print('-='*30)
total = 0
for p in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {p}? '))
    aproveitamento['gols'].append(gols)
    total += gols
aproveitamento['total'] = total
print('-='*30)
print(aproveitamento)
for k, v in aproveitamento.items():
    print(f'O Campo {k} tem o valor {v}')
print(f'O jogador {aproveitamento["Nome"]} jogou {partidas}')
#print(len(aproveitamento['gols']))
for i in range(0, len(aproveitamento['gols'])):
    print(f' => Na partida {i}, fez {aproveitamento["gols"][i]} gols.')
print(f'Foi um total de {aproveitamento["total"]} gols.')
