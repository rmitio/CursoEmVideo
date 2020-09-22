#DESAFIO051 Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
termo = int(input('Digite o termo:'))
razão = int(input('Digite a razão: '))
decimo = termo + (10 -1) * razão
for c in range(termo, decimo + razão, razão):
    print(c)

