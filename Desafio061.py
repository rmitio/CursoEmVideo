#DESAFIO061 Refaça o DESAFIO051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

'''termo = int(input('Digite o termo:'))
termo = int(input('Digite o termo:'))
razão = int(input('Digite a razão: '))
decimo = termo + (10 -1) * razão
for c in range(termo, decimo + razão, razão):
    print(c)
'''

termo = int(input('Digite o termo:'))
razão = int(input('Digite a razão: '))
decimo = termo + (10 -1) * razão
while termo != decimo+razão:
    termo += razão
    print(termo)