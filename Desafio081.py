'''
DESAFIO081 Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

numeros = list()
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    continuar = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Atenção Digite S para sim e N para não. Deseja Continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 not in numeros:
    print(f'O número 5 não faz parte da lista')
else:
    print(f'O valor 5 faz parte da lista')
