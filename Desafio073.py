'''DESAFIO073 Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois Mostre:
A) Apenas os 5 primeiros
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética.
D) Em que posição na table está o time da Chapecoense.'''

times = ('Flamengo',  'Santos', 'Palmeiras', 'Grêmio',
         'Athletico Paranaense', 'São Paulo',
         'Internacional', 'Corinthians', 'Fortaleza',
         'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético Mineiro',
         'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA',
         'Chapecoense', 'Avaí')

print(times)
print(f'Este são os 5 Primeiros times {times[:5]}')
print(f'Este são os 4 últimos colocados {times[-4:]}')
print(f'Estes são os times em ordem alfabetica: \n{sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense")+1}º posição')




















