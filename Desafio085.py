#DESAFIO085 Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares no final mostre os valores pares e ímpares em ordem crescente.

numeros = list()
impares = list()
pares = list()
for n in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
numeros.append(pares)
numeros.append(impares)

print(f'O números pares digitados foram {numeros[0]}')
print(f'O números impares digitados foram {numeros[1]}')