#DESAFIO078 Faça um programa que leia 4 valores numéricos e guarde-os em uma lista. No fina, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = list()
maior = menor = 0
pmenor = list()
pmaior = list()
for n in range(0, 5):
    num = numeros.append(int(input(f'Digite um valor para a Posição {n}: ')))

for p, c in enumerate(numeros):
    if p == 0:
        maior = menor = c
        pmaior.append(p)
        pmenor.append(p)
    elif c == menor:
        pmenor.append(p)
    elif c == maior:
        pmaior.append(p)
    elif c < menor:
        menor = c
        del pmenor[0]
        pmenor.append(p)
    elif c > maior:
        maior = c
        del pmaior[0]
        pmaior.append(p)

print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end=' ')
for ma in pmaior:
    print(f'{ma}..', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end=' ')
for me in pmenor:
    print(f'{me}..', end='')