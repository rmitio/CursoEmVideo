'''DESAFIO094 Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionário em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média.'''

pessoas = list()
pessoa = dict()
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo[M/F]:')).strip().upper()
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input('ERRO! Responda apenas [M/F]:')).strip().upper()
    pessoa['Idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    while continuar not in 'SsNn':
        continuar = str(input('ERRO! Respond apenas [S/N]')).strip().upper()
    if continuar == 'N':
        break
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma = 0
for i, v in enumerate(pessoas):
    soma += v["Idade"]
media = soma / len(pessoas)
print(f'{media}')
print(f'B) A média de idade é {media}')
print('C) As mulheres cadastradas foram', end=' ')
for k, v in enumerate(pessoas):
    if v['Sexo'] == 'F':
        print(v['Nome'], end=' ')
print()
print(f'D)Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['Idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v} ', end=';')
    print()

