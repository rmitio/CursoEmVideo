'''DESAFIO084 Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas Pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mias leves.'''

pessoas = list()
pessoa = list()
mai = men = cont = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()
    if cont == 0:
        mai = men = pessoas[0][1]
    else:
        if pessoas[cont][1] > mai:
            mai = pessoas[cont][1]
        if pessoas[cont][1] < men:
            men = pessoas[cont][1]
    cont += 1
    c = str(input('Deseja Continuar?[S/N]')).strip().upper()
    if c == 'N':
        break

#print(pessoas)
print(f'Foram cadastradas {cont} pessoas')
print(f'O maior foi {mai:.2f}kg. Peso de ', end='')
for i, v in enumerate(pessoas):
    if pessoas[i][1] == mai:
        print(f'{pessoas[i][0]} ', end='')
print()
print(f'O menor foi {men:.2f}kg. Peso de ', end='')
for i, v in enumerate(pessoas):
    if pessoas[i][1] == men:
        print(f'{pessoas[i][0]} ', end='')
print()
