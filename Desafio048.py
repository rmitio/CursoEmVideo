#DESAFIO048 Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontra no intervalo de 1 até 500.

s = 0
for c in range(0, 501):
    if c % 2 == 1 and c % 3 == 0:
        s += c
print(s)