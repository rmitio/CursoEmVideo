#DESAFIO089 Crie um programa que leia nome e duas noterrário passa mostrar as nostas de cada aluno individualmente.

ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota, nota2], media])
    resp = str(iput('Quer Continuar? [S/N]'))
    if resp in 'Nn':
        break
print(ficha)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    opc = int(input('Mostrar notas de qual aluno? (999 iterrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')