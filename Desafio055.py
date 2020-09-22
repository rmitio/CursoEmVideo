#DESAFIO055 Faça um programa que leia o peso de cinco pessoas. No final, mostre qual  foi o maior e o menor peso lidos.

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa:  '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso


print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))

'''peso = []
for c in range(1, 6):
    p =float(input('Digite o peso da {}ª Pessoa: '.format(c)))
    peso.append(p)

p = sorted(peso)
print('Maior Peso: {} \nMenor Peso: {}'.format(p[4], p[0]))

'''
