#DESAFIO047 Crie um programa que mostre na tela todos os números pares  que estão no intervalo entre 1 e 50.

#for c in range(0, 51, 2):
#    print(c)

for c in range(1, 51):
    if c % 2 == 0:
        print('{}'.format(c), end=' ')