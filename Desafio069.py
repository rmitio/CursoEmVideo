'''DESAFIO069 Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No Final mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''

mais18 = h = mmenos20 = 0

while True:
    i = int(input('Digite a idade:'))
    s = str(input('Digite o sexo[M/F] ')).strip().upper()[0]
    while s not in 'MF':
        s = str(input('Digite o sexo[M/F] ')).strip().upper()[0]
    c = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    while c not in 'SN':
        c = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if i > 18:
        mais18 += 1
    if s == 'M':
        h += 1
    if s == 'F' and i < 20:
        mmenos20 += 1
    if c == 'N':
        break
print(f'{mais18} pessoas tem mais de 18 anos. Foram cadastrados {h} homens. E {mmenos20} mulheres com menos de 20 anos.')