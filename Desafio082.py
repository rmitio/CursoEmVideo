#DESAFIO082 Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas valores pares e os impares digitado respectivamente. Ao final, mostre o conteúdo das trê lista geradas.

numeros = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    continuar = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Atenção Digite S para sim e N para não. Deseja Continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

for num in range(0, len(numeros)):
    if numeros[num]%2 == 0:
        pares.append(numeros[num])
    else:
        impares.append(numeros[num])

print(numeros)
print(f'Impares: {impares}')
print(f'Pares: {pares}')